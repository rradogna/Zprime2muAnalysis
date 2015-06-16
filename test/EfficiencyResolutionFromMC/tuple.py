#!/usr/bin/env python

from SUSYBSMAnalysis.Zprime2muAnalysis.PATTuple_cfg import cms, process
from SUSYBSMAnalysis.Zprime2muAnalysis.PATTools import switchHLTProcessName, AODOnly, pruneMCLeptons

process.maxEvents.input = 50
process.GlobalTag.globaltag = 'PHYS14_25_V1::All'
#process.source.fileNames = ['/store/mc/Phys14DR/DYJetsToEEMuMu_M-9500_13TeV-madgraph/AODSIM/PU20bx25_PHYS14_25_V1-v2/00000/18C7C360-E076-E411-9E2F-E0CB4E19F9BC.root',]
process.source.fileNames = ['/store/mc/Phys14DR/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/AODSIM/PU20bx25_tsg_PHYS14_25_V1-v1/00000/02BE6C0D-E46E-E411-89C3-003048F0E1B0.root']
#process.p = cms.Path(process.patDefaultSequence)

pruneMCLeptons(process, use_sim=True)
AODOnly(process)

process.countPatMuons.minNumber = 0

process.out.outputCommands = [
    'drop *',
    'keep *_prunedMCLeptons_*_*',
    'keep *_offlineBeamSpot_*_*',
    'keep *_offlinePrimaryVertices_*_*',
    'keep *_addPileupInfo_*_*',
    'keep patMuons_cleanPatMuonsTriggerMatch__PAT',
    'keep L1GlobalTriggerObjectMaps_l1L1GtObjectMap_*_*',
    'keep L1GlobalTriggerReadoutRecord_gtDigis__RECO',
    'keep triggerTriggerEvent_hltTriggerSummaryAOD__HLT*',
    'keep triggerTriggerEvent_hltTriggerSummaryAOD__REDIGI*',
    'keep patElectrons_cleanPatElectrons__PAT',
    'keep patPhotons_cleanPatPhotons__PAT',
    'keep edmTriggerResults_TriggerResults__HLT*',
    'keep edmTriggerResults_TriggerResults__REDIGI*',
    'keep GenEventInfoProduct_generator__SIM',
    #'keep GenEventInfoProduct_generator__HLT',
    'keep edmTriggerResults_TriggerResults__PAT',
    'keep *_patTrigger_*_*', # keep these two for now, for Level-1 decisions
    'keep *_patTriggerEvent_*_*',
    ]

import sys, os
if __name__ == '__main__' and 'submit' in sys.argv:
    crab_cfg = '''
[CRAB]
jobtype = cmssw
scheduler = remoteGlidein
use_server = 0

[CMSSW]
datasetpath = %(dataset)s
pset = %(pset_fn)s
total_number_of_events = -1
events_per_job = %(events_per_job)s
get_edm_output = 1

use_dbs3=1

[USER]
ui_working_dir = crab/crab_effres_%(name)s
copy_data = 1
storage_element = T2_IT_Legnaro
check_user_remote_dir = 0
publish_data = 1
publish_data_name = effres_%(name)s
#dbs_url_for_publication = https://cmsdbsprod.cern.ch:8443/cms_dbs_ph_analysis_02_writer/servlet/DBSServlet
'''

    os.system('mkdir -p psets crab')
    
    just_testing = 'testing' in sys.argv
    
    samples = [
#        ('dy20',   '/DYToMuMu_M-20_CT10_TuneZ2star_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'),
        ('dy120',  '/DYJetsToEEMuMu_M-120To200_13TeV-madgraph/Phys14DR-PU20bx25_PHYS14_25_V1-v2/AODSIM'),
        ('dy200',  '/DYJetsToEEMuMu_M-200To400_13TeV-madgraph/Phys14DR-PU20bx25_PHYS14_25_V1-v1/AODSIM'),
#        ('dy500',  '/DYToMuMu_M-500_CT10_TuneZ2star_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'),
        ('dy800',  '/DYJetsToEEMuMu_M-400To800_13TeV-madgraph/Phys14DR-PU20bx25_PHYS14_25_V1-v1/AODSIM'),
#        ('dy1000', '/DYToMuMu_M-1000_CT10_TuneZ2star_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'),
        ('dy2000', '/DYJetsToEEMuMu_M-1400To2300_13TeV-madgraph/Phys14DR-PU20bx25_PHYS14_25_V1-v1/AODSIM'),
        ('dy3000', '/DYJetsToEEMuMu_M-2300To3500_13TeV-madgraph/Phys14DR-PU20bx25_PHYS14_25_V1-v2/AODSIM'),
        ('dy9500',  '/DYJetsToEEMuMu_M-9500_13TeV-madgraph/Phys14DR-PU20bx25_PHYS14_25_V1-v2/AODSIM'),
        ('dy5000',  '/DYJetsToEEMuMu_M-4500To6000_13TeV-madgraph/Phys14DR-PU20bx25_PHYS14_25_V1-v1/AODSIM'),
#        ('dy200_c1',  '/DYToMuMu_M-200_CT10_TuneZ2star_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7C1-v1/AODSIM'),
#        ('dy500_c1',  '/DYToMuMu_M-500_CT10_TuneZ2star_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7C1-v1/AODSIM'),
#        ('dy800_c1',  '/DYToMuMu_M-800_CT10_TuneZ2star_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7C1-v1/AODSIM'),
#        ('dy1000_c1', '/DYToMuMu_M-1000_CT10_TuneZ2star_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7C1-v1/AODSIM'),
#        ('dy1500_c1', '/DYToMuMu_M-1500_CT10_TuneZ2star_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7C1-v1/AODSIM'),
#        ('dy2000_c1', '/DYToMuMu_M-2000_CT10_TuneZ2star_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7C1-v1/AODSIM'),
#        ('dy120_c2',  '/DYToMuMu_M-120_CT10_TuneZ2star_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7C2-v1/AODSIM'),
#        ('dy200_c2',  '/DYToMuMu_M-200_CT10_TuneZ2star_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7C2-v1/AODSIM'),
#        ('dy500_c2',  '/DYToMuMu_M-500_CT10_TuneZ2star_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7C2-v1/AODSIM'),
#        ('dy800_c2',  '/DYToMuMu_M-800_CT10_TuneZ2star_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7C2-v1/AODSIM'),
#        ('dy1000_c2', '/DYToMuMu_M-1000_CT10_TuneZ2star_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7C2-v1/AODSIM'),
#        ('dy1500_c2', '/DYToMuMu_M-1500_CT10_TuneZ2star_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7C2-v1/AODSIM'),
#        ('dy2000_c2', '/DYToMuMu_M-2000_CT10_TuneZ2star_8TeV-powheg-pythia6/Summer12_DR53X-PU_S10_START53_V7C2-v1/AODSIM'),
#        ('zp750',  '/ZprimePSIToMuMu_M-750_TuneZ2star_8TeV-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'),
#        ('zp1000', '/ZprimePSIToMuMu_M-1000_TuneZ2star_8TeV-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'),
#        ('zp1250', '/ZprimePSIToMuMu_M-1250_TuneZ2star_8TeV-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'),
#        ('zp1500', '/ZprimePSIToMuMu_M-1500_TuneZ2star_8TeV-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'),
#        ('zp1750', '/ZprimePSIToMuMu_M-1750_TuneZ2star_8TeV-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'),
#        ('zp2000', '/ZprimePSIToMuMu_M-2000_TuneZ2star_8TeV-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'),
#        ('zp2250', '/ZprimePSIToMuMu_M-2250_TuneZ2star_8TeV-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'),
#        ('zp2500', '/ZprimePSIToMuMu_M-2500_TuneZ2star_8TeV-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'),
#        ('zp2750', '/ZprimePSIToMuMu_M-2750_TuneZ2star_8TeV-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'),
#        ('zp3000', '/ZprimePSIToMuMu_M-3000_TuneZ2star_8TeV-pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM'),
        ('zp5000',  '/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/Phys14DR-PU20bx25_tsg_PHYS14_25_V1-v1/AODSIM'),
#        ('zp1000_c1', '/ZprimePSIToMuMu_M-1000_TuneZ2star_8TeV-pythia6/Summer12_DR53X-PU_S10_START53_V7C1-v1/AODSIM'),
#        ('zp1250_c1', '/ZprimePSIToMuMu_M-1250_TuneZ2star_8TeV-pythia6/Summer12_DR53X-PU_S10_START53_V7C1-v1/AODSIM'),
#        ('zp1500_c1', '/ZprimePSIToMuMu_M-1500_TuneZ2star_8TeV-pythia6/Summer12_DR53X-PU_S10_START53_V7C1-v1/AODSIM'),
#        ('zp1750_c1', '/ZprimePSIToMuMu_M-1750_TuneZ2star_8TeV-pythia6/Summer12_DR53X-PU_S10_START53_V7C1-v1/AODSIM'),
#        ('zp2000_c1', '/ZprimePSIToMuMu_M-2000_TuneZ2star_8TeV-pythia6/Summer12_DR53X-PU_S10_START53_V7C1-v1/AODSIM'),
#        ('zp2250_c1', '/ZprimePSIToMuMu_M-2250_TuneZ2star_8TeV-pythia6/Summer12_DR53X-PU_S10_START53_V7C1-v1/AODSIM'),
#        ('zp2500_c1', '/ZprimePSIToMuMu_M-2500_TuneZ2star_8TeV-pythia6/Summer12_DR53X-PU_S10_START53_V7C1-v1/AODSIM'),
#        ('zp2750_c1', '/ZprimePSIToMuMu_M-2750_TuneZ2star_8TeV-pythia6/Summer12_DR53X-PU_S10_START53_V7C1-v1/AODSIM'),
#        ('zp3000_c1', '/ZprimePSIToMuMu_M-3000_TuneZ2star_8TeV-pythia6/Summer12_DR53X-PU_S10_START53_V7C1-v1/AODSIM'),
    ]

    for name, dataset in samples:
        print name
        events_per_job = 5000

        pset = open('tuple.py').read()
        #if name == 'dy20':
        #    pset += '\nswitchHLTProcessName(process, "REDIGI38X")\n'
        pset_fn = 'psets/tuple_effres_crab_%s.py' % name
        open(pset_fn, 'wt').write(pset)
        
        open('crab.cfg', 'wt').write(crab_cfg % locals())
        if not just_testing:
            os.system('crab -create -submit all')
            os.system('rm crab.cfg')
