#!/usr/bin/env python

import sys, os, FWCore.ParameterSet.Config as cms

from SUSYBSMAnalysis.Zprime2muAnalysis.Zprime2muAnalysis_cfg import process

# These modules define the basic selection cuts. For the monitoring
# sets below, we don't need to define a whole new module, since they
# just change one or two cuts -- see below.

import SUSYBSMAnalysis.Zprime2muAnalysis.OurSelectionDec2012_cff as OurSelectionDec2012
#print OurSelectionDec2012.loose_cut #FUNZIONA
from SUSYBSMAnalysis.Zprime2muAnalysis.OurSelectionDec2012_cff import loose_cut, trigger_match, tight_cut, allDimuons

from SUSYBSMAnalysis.Zprime2muAnalysis.hltTriggerMatch_cfi import trigger_paths
####process.goodDataFilter.TriggerResultsTag = cms.InputTag('TriggerResults', '', 'HLT')# was PAT
####process.goodDataFilter.HLTPaths = cms.vstring('HLT_Mu40_v*')#,trigger_paths#? was ['goodDataAll']

process.leptons.muon_track_for_momentum = cms.string('TunePNew')#default!
#process.leptons.muon_track_for_momentum = cms.string('Inner')

process.dimuonsNoVtxProb = process.dimuons.clone()
delattr(process.dimuonsNoVtxProb, 'vertex_chi2_max')

process.allDimuonsNoPt      = allDimuons.clone(loose_cut = loose_cut.replace('pt > 45 &&',''),
                                               )
process.allDimuonsNoIso      = allDimuons.clone(loose_cut = loose_cut.replace('isolationR03.sumPt / innerTrack.pt < 0.10 &&',''),
                                               )
process.dimuonsNoIso = process.dimuons.clone()
process.dimuonsNoIso.src = cms.InputTag("allDimuonsNoIso")

process.dimuonsNoPt = process.dimuons.clone()
process.dimuonsNoPt.src = cms.InputTag("allDimuonsNoPt")

# The histogramming module that will be cloned multiple times below
# for making histograms with different cut/dilepton combinations.
from SUSYBSMAnalysis.Zprime2muAnalysis.HistosFromPAT_cfi import HistosFromPAT
HistosFromPAT.leptonsFromDileptons = True
from SUSYBSMAnalysis.Zprime2muAnalysis.HistosVertexFromPAT_cfi import HistosVertexFromPAT
HistosVertexFromPAT.leptonsFromDileptons = True
from SUSYBSMAnalysis.Zprime2muAnalysis.ResolutionVertexUsingMC_cfi import ResolutionVertexUsingMC
ResolutionVertexUsingMC.leptonsFromDileptons = True
ResolutionVertexUsingMC.doQoverP = True


# Histos now just needs to know which leptons and dileptons to use.
process.load('SUSYBSMAnalysis.Zprime2muAnalysis.HistosFromPAT_cfi')
process.HistosFromPAT.leptonsFromDileptons = True
process.HistosFromPAT.dilepton_src = cms.InputTag("dimuonsNoVtxProb")
#alternativa
#process.histos = HistosFromPAT.clone(dilepton_src = cms.InputTag('dimuons'), lepton_src = cms.InputTag('leptons','muons'), leptonsFromDileptons = True)
process.load('SUSYBSMAnalysis.Zprime2muAnalysis.HistosVertexFromPAT_cfi')
process.HistosVertexFromPAT.leptonsFromDileptons = True
process.HistosVertexFromPAT.dilepton_src = cms.InputTag("dimuonsNoVtxProb")

process.load('SUSYBSMAnalysis.Zprime2muAnalysis.HardInteractionFilter_cfi')
process.HardInteractionFilterRes = process.HardInteractionFilter.clone(use_resonance_mass=True)

process.load('SUSYBSMAnalysis.Zprime2muAnalysis.ResolutionUsingMC_cfi')
process.ResolutionUsingMC.leptonsFromDileptons = True
process.ResolutionUsingMC.doQoverP = True
process.ResolutionUsingMC.dilepton_src = cms.InputTag("dimuonsNoVtxProb")

process.load('SUSYBSMAnalysis.Zprime2muAnalysis.ResolutionVertexUsingMC_cfi')
process.ResolutionVertexUsingMC.leptonsFromDileptons = True
process.ResolutionVertexUsingMC.doQoverP = True
process.ResolutionVertexUsingMC.dilepton_src = cms.InputTag("dimuonsNoVtxProb")

process.histosNoIso = HistosVertexFromPAT.clone(dilepton_src = cms.InputTag('dimuonsNoIso'), leptonsFromDileptons = True)
process.histosNoPt = HistosVertexFromPAT.clone(dilepton_src = cms.InputTag('dimuonsNoPt'), leptonsFromDileptons = True)

process.resNoIso = ResolutionVertexUsingMC.clone(dilepton_src = cms.InputTag('dimuonsNoIso'), leptonsFromDileptons = True, doQoverP = True)
process.resNoPt = ResolutionVertexUsingMC.clone(dilepton_src = cms.InputTag('dimuonsNoPt'), leptonsFromDileptons = True, doQoverP = True)

# cose di process def in Zprime2muAnalysis_cfg
process.source.fileNames =[
                           #'file:./pat.root'
                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_100_1_Hw6.root',
                           #'/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_10_1_r9E.root',
                           #'/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_11_1_bgC.root',
                           #'/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_12_1_GLd.root',
                           #'/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_13_1_U2Q.root',
                           ]
process.options.wantSummary = cms.untracked.bool(True)# false di default
process.MessageLogger.cerr.FwkReport.reportEvery = 1 # default 1000
process.maxEvents.input = 100
process.TFileService.fileName = cms.string('zp2mu-2.root')
# talk to output module ! questo crea un output che oltre ai contenuti della pattupla contiene anche le info dei processi di Zprime2muAnalysisSequence
#process.out = cms.OutputModule("PoolOutputModule",
#                               fileName = cms.untracked.string("zp2mu.root")
#                               )
##########
#Zprime2muAnalysis_cfg fa il load di Zprime2muAnalysis_cff dove e' definita la sequenza Zprime2muAnalysisSequence = cms.Sequence(muonPhotonMatch * leptons * allDimuons * dimuons)
# importando cose da MuonPhotonMatch_cff ed OurSelectionDec2012_cff
# da MuonPhotonMatch_cff viene questo filtro muonPhotonMatch
#da OurSelectionDec2012_cff vengono allDimuons ed dimuons.
# Zprime2muAnalysis_cff inoltre fa l'import HLTrigger.HLTfilters.hltHighLevel_cfi di clona in goodDataFilter il processo hltHighLevel_cfi.hltHighLevel
#che corrisponde a
#hltHighLevel = cms.EDFilter("HLTHighLevel",
#             TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
#             HLTPaths = cms.vstring(), # provide list of HLT paths (or patterns) you want
#             eventSetupPathsKey = cms.string(''), # not empty => use read paths from AlCaRecoTriggerBitsRcd via this key
#             andOr = cms.bool(True), # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true
#             throw = cms.bool(True) # throw exception on unknown path names
# con le seguenti modifiche:
#goodDataFilter.HLTPaths = ['goodDataAll'] # can set to just 'goodDataPrimaryVertexFilter', for example
#goodDataFilter.andOr = False # = AND


process.nEventsTotal = cms.EDProducer("EventCountProducer") #non so dove mette l'output
process.nEventsFiltered = cms.EDProducer("EventCountProducer")
#process.goodDataFilter
process.p = cms.Path(process.goodDataFilter*process.muonPhotonMatch * process.leptons * process.allDimuons * process.dimuonsNoVtxProb * process.HistosVertexFromPAT)
#process.p = cms.Path(process.goodDataFilter*process.muonPhotonMatch * process.leptons * process.allDimuons * process.dimuons * process.HistosFromPAT)
#process.p *=process.histos
# A list of analyzers or output modules to be run after all paths have been run.
#process.outpath = cms.EndPath(process.out)

process.pnoVtx  = cms.Path(process.HardInteractionFilterRes * process.goodDataFilter*process.muonPhotonMatch * process.leptons * process.allDimuons * process.dimuonsNoVtxProb * process.HistosFromPAT * process.ResolutionVertexUsingMC)

process.pnoIso  = cms.Path(process.HardInteractionFilterRes * process.goodDataFilter*process.muonPhotonMatch * process.leptons * process.allDimuonsNoIso * process.dimuonsNoIso * process.histosNoIso * process.resNoIso)
process.pnoPt  = cms.Path(process.HardInteractionFilterRes * process.goodDataFilter*process.muonPhotonMatch * process.leptons * process.allDimuonsNoPt * process.dimuonsNoPt * process.histosNoPt * process.resNoPt)

f = file('outfile_noVtx', 'w')
f.write(process.dumpPython())
f.close()

###### per sottomettere con crab
#def ntuplify(process, fill_gen_info=False):
#    process.SimpleNtupler = cms.EDAnalyzer('SimpleNtupler',
#                                           dimu_src = cms.InputTag('SimpleMuonsAllSigns'),
#                                           beamspot_src = cms.InputTag('offlineBeamSpot'),
#                                           vertices_src = cms.InputTag('offlinePrimaryVertices'),
#                                           )
#    if fill_gen_info:
#        from SUSYBSMAnalysis.Zprime2muAnalysis.HardInteraction_cff import hardInteraction
#                                                   process.SimpleNtupler.hardInteraction = hardInteraction
#                                               
#    process.pathSimple *= process.SimpleNtupler
#
#def for_mc(process, hlt_process_name, fill_gen_info):
#    ntuplify(process, fill_gen_info)
#    #switch_hlt_process_name(process, hlt_process_name) # this must be done last (i.e. after anything that might have an InputTag for something HLT-related)

if __name__ == '__main__' and 'submit' in sys.argv:
    crab_cfg = '''
[CRAB]
jobtype = cmssw
scheduler = remoteGlidein
use_server = 0
[CMSSW]
datasetpath = %(ana_dataset)s
#dbs_url = https://cmsdbsprod.cern.ch:8443/cms_dbs_ph_analysis_02_writer/servlet/DBSServlet
dbs_url=phys03
pset = histos_noVtxIsoPtCut_crab.py
get_edm_output = 1
job_control
use_dbs3=1
[USER]
ui_working_dir = crab/crab_ana_datamc_%(name)s
return_data = 1
'''
    just_testing = 'testing' in sys.argv
    if 'no_mc' not in sys.argv:
        # Set crab_cfg for MC.
        crab_cfg = crab_cfg.replace('job_control','''
total_number_of_events = -1
events_per_job = 50000
    ''')
        
        from SUSYBSMAnalysis.Zprime2muAnalysis.MCSamples import *
        samples = [zpsi5000, dy200, dy120]
        for sample in reversed(samples):
            print sample.name
            new_py = open('histos_noVtxIsoPtCut.py').read()
            #sample.fill_gen_info = sample.name in ['BHOzpsi5000']
            #new_py += "\nfor_mc(process, hlt_process_name='%(hlt_process_name)s', fill_gen_info=%(fill_gen_info)s)\n" % sample
            
            open('histos_noVtxIsoPtCut_crab.py', 'wt').write(new_py)
            open('crab.cfg', 'wt').write(crab_cfg % sample)
            if not just_testing:
                os.system('crab -create -submit all')
            if not just_testing:
                os.system('rm crab.cfg histos_crab.py histos_crab.pyc')


