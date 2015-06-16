#!/usr/bin/env python

import sys, os, FWCore.ParameterSet.Config as cms
from SUSYBSMAnalysis.Zprime2muAnalysis.Zprime2muAnalysis_cfg import process
from SUSYBSMAnalysis.Zprime2muAnalysis.OurSelectionDec2012_cff import loose_cut, trigger_match, tight_cut, allDimuons
from SUSYBSMAnalysis.Zprime2muAnalysis.HistosFromPAT_cfi import HistosFromPAT
HistosFromPAT.leptonsFromDileptons = True
process.load('SUSYBSMAnalysis.Zprime2muAnalysis.HistosFromPAT_cfi')
process.load('SUSYBSMAnalysis.Zprime2muAnalysis.ResolutionUsingMC_cfi')
process.load('SUSYBSMAnalysis.Zprime2muAnalysis.HardInteractionFilter_cfi')
process.HardInteractionFilterRes = process.HardInteractionFilter.clone(use_resonance_mass=True)

process.source.fileNames =[
                           'file:./pat.root'
                           ]
process.options.wantSummary = cms.untracked.bool(True)# false di default
process.MessageLogger.cerr.FwkReport.reportEvery = 1 # default 1000
process.maxEvents.input = -1
process.TFileService.fileName = cms.string('zp2mu-2.root')

cuts = [
        ('GlobTrack','isGlobalMuon && isTrackerMuon'),
        ('Pt',       'pt > 45'),
        ('DB',       'abs(dB) < 0.2'),
        ('Iso',      'isolationR03.sumPt / innerTrack.pt < 0.10'),
        ('TkLayers', 'globalTrack.hitPattern.trackerLayersWithMeasurement > 5'),
        ('PxHits',   'globalTrack.hitPattern.numberOfValidPixelHits >= 1'),
        ('MuHits',   'globalTrack.hitPattern.numberOfValidMuonHits > 0'),
        ('MuMatch',  'numberOfMatchedStations > 1'),
        ]

########################## OFF #######################################
process.allDimuonsOff      = allDimuons.clone(
    loose_cut = loose_cut.replace(loose_cut, ''),
    tight_cut = tight_cut.replace(trigger_match, '')
)
process.dimuonsOff= process.dimuons.clone()
process.dimuonsOff.src = cms.InputTag("allDimuonsOff")
delattr(process.dimuonsOff, 'dpt_over_pt_max')
delattr(process.dimuonsOff, 'back_to_back_cos_angle_min')
delattr(process.dimuonsOff, 'vertex_chi2_max')

process.HistosFromPATOff= process.HistosFromPAT.clone()
process.HistosFromPATOff.leptonsFromDileptons = True
process.HistosFromPATOff.dilepton_src = cms.InputTag("dimuonsOff")

process.ResolutionUsingMCOff= process.ResolutionUsingMC.clone()
process.ResolutionUsingMCOff.leptonsFromDileptons = True
process.ResolutionUsingMCOff.doQoverP = True
process.ResolutionUsingMCOff.dilepton_src = cms.InputTag("dimuonsOff")

#process.Off = cms.Path(process.HardInteractionFilterRes* process.goodDataFilter*process.muonPhotonMatch * process.leptons * process.allDimuonsOff * process.dimuonsOff * process.HistosFromPATOff * process.ResolutionUsingMCOff)
process.Off = cms.Path(process.goodDataFilter * process.muonPhotonMatch * process.leptons * process.allDimuonsOff * process.dimuonsOff * process.HistosFromPATOff * process.ResolutionUsingMCOff)


########################## Step1 #######################################
process.allDimuonsStep1      = allDimuons.clone(
    loose_cut = loose_cut.replace(loose_cut, 'isGlobalMuon && isTrackerMuon &&'\
                                  'pt > 45'),
    tight_cut = tight_cut.replace(trigger_match, '')
                                              )
process.dimuonsStep1= process.dimuons.clone()
process.dimuonsStep1.src = cms.InputTag("allDimuonsStep1")
delattr(process.dimuonsStep1, 'dpt_over_pt_max')
delattr(process.dimuonsStep1, 'back_to_back_cos_angle_min')
delattr(process.dimuonsStep1, 'vertex_chi2_max')

process.HistosFromPATStep1= process.HistosFromPAT.clone()
process.HistosFromPATStep1.leptonsFromDileptons = True
process.HistosFromPATStep1.dilepton_src = cms.InputTag("dimuonsStep1")

process.ResolutionUsingMCStep1= process.ResolutionUsingMC.clone()
process.ResolutionUsingMCStep1.leptonsFromDileptons = True
process.ResolutionUsingMCStep1.doQoverP = True
process.ResolutionUsingMCStep1.dilepton_src = cms.InputTag("dimuonsStep1")

process.Step1 = cms.Path(process.goodDataFilter * process.muonPhotonMatch * process.leptons * process.allDimuonsStep1 * process.dimuonsStep1 * process.HistosFromPATStep1 * process.ResolutionUsingMCStep1)

########################## Step2 #######################################
process.allDimuonsStep2      = allDimuons.clone(
                                                loose_cut = loose_cut.replace(loose_cut, 'isGlobalMuon && isTrackerMuon &&'\
                                                                              'pt > 45 &&'\
                                                                              'abs(dB) < 0.2'),
                                                tight_cut = tight_cut.replace(trigger_match, '')
                                                )
process.dimuonsStep2= process.dimuons.clone()
process.dimuonsStep2.src = cms.InputTag("allDimuonsStep2")
delattr(process.dimuonsStep2, 'dpt_over_pt_max')
delattr(process.dimuonsStep2, 'back_to_back_cos_angle_min')
delattr(process.dimuonsStep2, 'vertex_chi2_max')

process.HistosFromPATStep2= process.HistosFromPAT.clone()
process.HistosFromPATStep2.leptonsFromDileptons = True
process.HistosFromPATStep2.dilepton_src = cms.InputTag("dimuonsStep2")

process.ResolutionUsingMCStep2= process.ResolutionUsingMC.clone()
process.ResolutionUsingMCStep2.leptonsFromDileptons = True
process.ResolutionUsingMCStep2.doQoverP = True
process.ResolutionUsingMCStep2.dilepton_src = cms.InputTag("dimuonsStep2")

process.Step2 = cms.Path(process.goodDataFilter * process.muonPhotonMatch * process.leptons * process.allDimuonsStep2 * process.dimuonsStep2 * process.HistosFromPATStep2 * process.ResolutionUsingMCStep2)

########################## Step3 #######################################
process.allDimuonsStep3      = allDimuons.clone(
                                                loose_cut = loose_cut.replace(loose_cut, 'isGlobalMuon && isTrackerMuon &&'\
                                                                              'pt > 45 &&'\
                                                                              'abs(dB) < 0.2 &&'\
                                                                              'isolationR03.sumPt / innerTrack.pt < 0.10'),
                                                tight_cut = tight_cut.replace(trigger_match, '')
                                                )
process.dimuonsStep3= process.dimuons.clone()
process.dimuonsStep3.src = cms.InputTag("allDimuonsStep3")
delattr(process.dimuonsStep3, 'dpt_over_pt_max')
delattr(process.dimuonsStep3, 'back_to_back_cos_angle_min')
delattr(process.dimuonsStep3, 'vertex_chi2_max')

process.HistosFromPATStep3= process.HistosFromPAT.clone()
process.HistosFromPATStep3.leptonsFromDileptons = True
process.HistosFromPATStep3.dilepton_src = cms.InputTag("dimuonsStep3")

process.ResolutionUsingMCStep3= process.ResolutionUsingMC.clone()
process.ResolutionUsingMCStep3.leptonsFromDileptons = True
process.ResolutionUsingMCStep3.doQoverP = True
process.ResolutionUsingMCStep3.dilepton_src = cms.InputTag("dimuonsStep3")

process.Step3 = cms.Path(process.goodDataFilter * process.muonPhotonMatch * process.leptons * process.allDimuonsStep3 * process.dimuonsStep3 * process.HistosFromPATStep3 * process.ResolutionUsingMCStep3)

########################## Step4 #######################################
process.allDimuonsStep4      = allDimuons.clone(
                                                loose_cut = loose_cut.replace(loose_cut, 'isGlobalMuon && isTrackerMuon &&'\
                                                                              'pt > 45 &&'\
                                                                              'abs(dB) < 0.2 &&'\
                                                                              'isolationR03.sumPt / innerTrack.pt < 0.10 &&'\
                                                                              'globalTrack.hitPattern.trackerLayersWithMeasurement > 5'),
                                                tight_cut = tight_cut.replace(trigger_match, '')
                                                )
process.dimuonsStep4= process.dimuons.clone()
process.dimuonsStep4.src = cms.InputTag("allDimuonsStep4")
delattr(process.dimuonsStep4, 'dpt_over_pt_max')
delattr(process.dimuonsStep4, 'back_to_back_cos_angle_min')
delattr(process.dimuonsStep4, 'vertex_chi2_max')

process.HistosFromPATStep4= process.HistosFromPAT.clone()
process.HistosFromPATStep4.leptonsFromDileptons = True
process.HistosFromPATStep4.dilepton_src = cms.InputTag("dimuonsStep4")

process.ResolutionUsingMCStep4= process.ResolutionUsingMC.clone()
process.ResolutionUsingMCStep4.leptonsFromDileptons = True
process.ResolutionUsingMCStep4.doQoverP = True
process.ResolutionUsingMCStep4.dilepton_src = cms.InputTag("dimuonsStep4")

process.Step4 = cms.Path(process.goodDataFilter * process.muonPhotonMatch * process.leptons * process.allDimuonsStep4 * process.dimuonsStep4 * process.HistosFromPATStep4 * process.ResolutionUsingMCStep4)

########################## Step5 #######################################
process.allDimuonsStep5      = allDimuons.clone(
                                                loose_cut = loose_cut.replace(loose_cut, 'isGlobalMuon && isTrackerMuon &&'\
                                                                              'pt > 45 &&'\
                                                                              'abs(dB) < 0.2 &&'\
                                                                              'isolationR03.sumPt / innerTrack.pt < 0.10 &&'\
                                                                              'globalTrack.hitPattern.trackerLayersWithMeasurement > 5 &&'\
                                                                              'globalTrack.hitPattern.numberOfValidPixelHits >= 1'),
                                                tight_cut = tight_cut.replace(trigger_match, '')
                                                )
process.dimuonsStep5= process.dimuons.clone()
process.dimuonsStep5.src = cms.InputTag("allDimuonsStep5")
delattr(process.dimuonsStep5, 'dpt_over_pt_max')
delattr(process.dimuonsStep5, 'back_to_back_cos_angle_min')
delattr(process.dimuonsStep5, 'vertex_chi2_max')

process.HistosFromPATStep5= process.HistosFromPAT.clone()
process.HistosFromPATStep5.leptonsFromDileptons = True
process.HistosFromPATStep5.dilepton_src = cms.InputTag("dimuonsStep5")

process.ResolutionUsingMCStep5= process.ResolutionUsingMC.clone()
process.ResolutionUsingMCStep5.leptonsFromDileptons = True
process.ResolutionUsingMCStep5.doQoverP = True
process.ResolutionUsingMCStep5.dilepton_src = cms.InputTag("dimuonsStep5")

process.Step5 = cms.Path(process.goodDataFilter * process.muonPhotonMatch * process.leptons * process.allDimuonsStep5 * process.dimuonsStep5 * process.HistosFromPATStep5 * process.ResolutionUsingMCStep5)

########################## Step6 #######################################
process.allDimuonsStep6      = allDimuons.clone(
                                                loose_cut = loose_cut.replace(loose_cut, 'isGlobalMuon && isTrackerMuon &&'\
                                                                              'pt > 45 &&'\
                                                                              'abs(dB) < 0.2 &&'\
                                                                              'isolationR03.sumPt / innerTrack.pt < 0.10 &&'\
                                                                              'globalTrack.hitPattern.trackerLayersWithMeasurement > 5 &&'\
                                                                              'globalTrack.hitPattern.numberOfValidPixelHits >= 1 &&'\
                                                                              'globalTrack.hitPattern.numberOfValidMuonHits > 0'),
                                                tight_cut = tight_cut.replace(trigger_match, '')
                                                )
process.dimuonsStep6= process.dimuons.clone()
process.dimuonsStep6.src = cms.InputTag("allDimuonsStep6")
delattr(process.dimuonsStep6, 'dpt_over_pt_max')
delattr(process.dimuonsStep6, 'back_to_back_cos_angle_min')
delattr(process.dimuonsStep6, 'vertex_chi2_max')

process.HistosFromPATStep6= process.HistosFromPAT.clone()
process.HistosFromPATStep6.leptonsFromDileptons = True
process.HistosFromPATStep6.dilepton_src = cms.InputTag("dimuonsStep6")

process.ResolutionUsingMCStep6= process.ResolutionUsingMC.clone()
process.ResolutionUsingMCStep6.leptonsFromDileptons = True
process.ResolutionUsingMCStep6.doQoverP = True
process.ResolutionUsingMCStep6.dilepton_src = cms.InputTag("dimuonsStep6")

process.Step6 = cms.Path(process.goodDataFilter * process.muonPhotonMatch * process.leptons * process.allDimuonsStep6 * process.dimuonsStep6 * process.HistosFromPATStep6 * process.ResolutionUsingMCStep6)

########################## Step7 #######################################
process.allDimuonsStep7      = allDimuons.clone(
                                                loose_cut = loose_cut.replace(loose_cut, 'isGlobalMuon && isTrackerMuon &&'\
                                                                              'pt > 45 &&'\
                                                                              'abs(dB) < 0.2 &&'\
                                                                              'isolationR03.sumPt / innerTrack.pt < 0.10 &&'\
                                                                              'globalTrack.hitPattern.trackerLayersWithMeasurement > 5 &&'\
                                                                              'globalTrack.hitPattern.numberOfValidPixelHits >= 1 &&'\
                                                                              'globalTrack.hitPattern.numberOfValidMuonHits > 0 &&'\
                                                                              'numberOfMatchedStations > 1'),
                                                tight_cut = tight_cut.replace(trigger_match, '')
                                                )
process.dimuonsStep7= process.dimuons.clone()
process.dimuonsStep7.src = cms.InputTag("allDimuonsStep7")
delattr(process.dimuonsStep7, 'dpt_over_pt_max')
delattr(process.dimuonsStep7, 'back_to_back_cos_angle_min')
delattr(process.dimuonsStep7, 'vertex_chi2_max')

process.HistosFromPATStep7= process.HistosFromPAT.clone()
process.HistosFromPATStep7.leptonsFromDileptons = True
process.HistosFromPATStep7.dilepton_src = cms.InputTag("dimuonsStep7")

process.ResolutionUsingMCStep7= process.ResolutionUsingMC.clone()
process.ResolutionUsingMCStep7.leptonsFromDileptons = True
process.ResolutionUsingMCStep7.doQoverP = True
process.ResolutionUsingMCStep7.dilepton_src = cms.InputTag("dimuonsStep7")

process.Step7 = cms.Path(process.goodDataFilter * process.muonPhotonMatch * process.leptons * process.allDimuonsStep7 * process.dimuonsStep7 * process.HistosFromPATStep7 * process.ResolutionUsingMCStep7)

########################## Tight #######################################
process.allDimuonsTight      = allDimuons.clone(
                                                loose_cut = loose_cut.replace(loose_cut, 'isGlobalMuon && isTrackerMuon &&'\
                                                                              'pt > 45 &&'\
                                                                              'abs(dB) < 0.2 &&'\
                                                                              'isolationR03.sumPt / innerTrack.pt < 0.10 &&'\
                                                                              'globalTrack.hitPattern.trackerLayersWithMeasurement > 5 &&'\
                                                                              'globalTrack.hitPattern.numberOfValidPixelHits >= 1 &&'\
                                                                              'globalTrack.hitPattern.numberOfValidMuonHits > 0 &&'\
                                                                              'numberOfMatchedStations > 1')
                                                #tight_cut = tight_cut.replace(trigger_match, '')
                                                )
process.dimuonsTight= process.dimuons.clone()
process.dimuonsTight.src = cms.InputTag("allDimuonsTight")
delattr(process.dimuonsTight, 'dpt_over_pt_max')
delattr(process.dimuonsTight, 'back_to_back_cos_angle_min')
delattr(process.dimuonsTight, 'vertex_chi2_max')

process.HistosFromPATTight= process.HistosFromPAT.clone()
process.HistosFromPATTight.leptonsFromDileptons = True
process.HistosFromPATTight.dilepton_src = cms.InputTag("dimuonsTight")

process.ResolutionUsingMCTight= process.ResolutionUsingMC.clone()
process.ResolutionUsingMCTight.leptonsFromDileptons = True
process.ResolutionUsingMCTight.doQoverP = True
process.ResolutionUsingMCTight.dilepton_src = cms.InputTag("dimuonsTight")

process.Tight = cms.Path(process.goodDataFilter * process.muonPhotonMatch * process.leptons * process.allDimuonsTight* process.dimuonsTight * process.HistosFromPATTight * process.ResolutionUsingMCTight)

########################## TightVtx #######################################
process.allDimuonsTightVtx      = allDimuons.clone(
                                                loose_cut = loose_cut.replace(loose_cut, 'isGlobalMuon && isTrackerMuon &&'\
                                                                              'pt > 45 &&'\
                                                                              'abs(dB) < 0.2 &&'\
                                                                              'isolationR03.sumPt / innerTrack.pt < 0.10 &&'\
                                                                              'globalTrack.hitPattern.trackerLayersWithMeasurement > 5 &&'\
                                                                              'globalTrack.hitPattern.numberOfValidPixelHits >= 1 &&'\
                                                                              'globalTrack.hitPattern.numberOfValidMuonHits > 0 &&'\
                                                                              'numberOfMatchedStations > 1')
                                                #tight_cut = tight_cut.replace(trigger_match, '')
                                                )
process.dimuonsTightVtx= process.dimuons.clone()
process.dimuonsTightVtx.src = cms.InputTag("allDimuonsTightVtx")
delattr(process.dimuonsTightVtx, 'dpt_over_pt_max')
delattr(process.dimuonsTightVtx, 'back_to_back_cos_angle_min')
#delattr(process.dimuonsTightVtx, 'vertex_chi2_max')

process.HistosFromPATTightVtx= process.HistosFromPAT.clone()
process.HistosFromPATTightVtx.leptonsFromDileptons = True
process.HistosFromPATTightVtx.dilepton_src = cms.InputTag("dimuonsTightVtx")

process.ResolutionUsingMCTightVtx= process.ResolutionUsingMC.clone()
process.ResolutionUsingMCTightVtx.leptonsFromDileptons = True
process.ResolutionUsingMCTightVtx.doQoverP = True
process.ResolutionUsingMCTightVtx.dilepton_src = cms.InputTag("dimuonsTightVtx")

process.TightVtx = cms.Path(process.goodDataFilter * process.muonPhotonMatch * process.leptons * process.allDimuonsTightVtx* process.dimuonsTightVtx * process.HistosFromPATTightVtx * process.ResolutionUsingMCTightVtx)

########################## TightSpt #######################################
process.allDimuonsTightSpt      = allDimuons.clone(
                                                   loose_cut = loose_cut.replace(loose_cut, 'isGlobalMuon && isTrackerMuon &&'\
                                                                                 'pt > 45 &&'\
                                                                                 'abs(dB) < 0.2 &&'\
                                                                                 'isolationR03.sumPt / innerTrack.pt < 0.10 &&'\
                                                                                 'globalTrack.hitPattern.trackerLayersWithMeasurement > 5 &&'\
                                                                                 'globalTrack.hitPattern.numberOfValidPixelHits >= 1 &&'\
                                                                                 'globalTrack.hitPattern.numberOfValidMuonHits > 0 &&'\
                                                                                 'numberOfMatchedStations > 1')
                                                   #tight_cut = tight_cut.replace(trigger_match, '')
                                                   )
process.dimuonsTightSpt= process.dimuons.clone()
process.dimuonsTightSpt.src = cms.InputTag("allDimuonsTightSpt")
#delattr(process.dimuonsTightSpt, 'dpt_over_pt_max')
delattr(process.dimuonsTightSpt, 'back_to_back_cos_angle_min')
#delattr(process.dimuonsTightSpt, 'vertex_chi2_max')

process.HistosFromPATTightSpt= process.HistosFromPAT.clone()
process.HistosFromPATTightSpt.leptonsFromDileptons = True
process.HistosFromPATTightSpt.dilepton_src = cms.InputTag("dimuonsTightSpt")

process.ResolutionUsingMCTightSpt= process.ResolutionUsingMC.clone()
process.ResolutionUsingMCTightSpt.leptonsFromDileptons = True
process.ResolutionUsingMCTightSpt.doQoverP = True
process.ResolutionUsingMCTightSpt.dilepton_src = cms.InputTag("dimuonsTightSpt")

process.TightSpt = cms.Path(process.goodDataFilter * process.muonPhotonMatch * process.leptons * process.allDimuonsTightSpt* process.dimuonsTightSpt * process.HistosFromPATTightSpt * process.ResolutionUsingMCTightSpt)

########################## TightBk #######################################
process.allDimuonsTightBk      = allDimuons.clone(
                                                   loose_cut = loose_cut.replace(loose_cut, 'isGlobalMuon && isTrackerMuon &&'\
                                                                                 'pt > 45 &&'\
                                                                                 'abs(dB) < 0.2 &&'\
                                                                                 'isolationR03.sumPt / innerTrack.pt < 0.10 &&'\
                                                                                 'globalTrack.hitPattern.trackerLayersWithMeasurement > 5 &&'\
                                                                                 'globalTrack.hitPattern.numberOfValidPixelHits >= 1 &&'\
                                                                                 'globalTrack.hitPattern.numberOfValidMuonHits > 0 &&'\
                                                                                 'numberOfMatchedStations > 1')
                                                   #tight_cut = tight_cut.replace(trigger_match, '')
                                                   )
process.dimuonsTightBk= process.dimuons.clone()
process.dimuonsTightBk.src = cms.InputTag("allDimuonsTightBk")
#delattr(process.dimuonsTightBk, 'dpt_over_pt_max')
#delattr(process.dimuonsTightBk, 'back_to_back_cos_angle_min')
#delattr(process.dimuonsTightBk, 'vertex_chi2_max')

process.HistosFromPATTightBk= process.HistosFromPAT.clone()
process.HistosFromPATTightBk.leptonsFromDileptons = True
process.HistosFromPATTightBk.dilepton_src = cms.InputTag("dimuonsTightBk")

process.ResolutionUsingMCTightBk= process.ResolutionUsingMC.clone()
process.ResolutionUsingMCTightBk.leptonsFromDileptons = True
process.ResolutionUsingMCTightBk.doQoverP = True
process.ResolutionUsingMCTightBk.dilepton_src = cms.InputTag("dimuonsTightBk")

process.TightBk = cms.Path(process.goodDataFilter * process.muonPhotonMatch * process.leptons * process.allDimuonsTightBk* process.dimuonsTightBk * process.HistosFromPATTightBk * process.ResolutionUsingMCTightBk)

f = file('outfile_cutBycut', 'w')
f.write(process.dumpPython())
f.close()

