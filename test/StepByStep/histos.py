#!/usr/bin/env python

import sys, os, FWCore.ParameterSet.Config as cms

from SUSYBSMAnalysis.Zprime2muAnalysis.Zprime2muAnalysis_cfg import process

# The histogramming module that will be cloned multiple times below
# for making histograms with different cut/dilepton combinations.
from SUSYBSMAnalysis.Zprime2muAnalysis.HistosFromPAT_cfi import HistosFromPAT
HistosFromPAT.leptonsFromDileptons = True

# Histos now just needs to know which leptons and dileptons to use.
process.load('SUSYBSMAnalysis.Zprime2muAnalysis.HistosFromPAT_cfi')
process.HistosFromPAT.leptonsFromDileptons = True
#alternativa
#process.histos = HistosFromPAT.clone(dilepton_src = cms.InputTag('dimuons'), lepton_src = cms.InputTag('leptons','muons'), leptonsFromDileptons = True)

# These modules define the basic selection cuts. For the monitoring
# sets below, we don't need to define a whole new module, since they
# just change one or two cuts -- see below.

import SUSYBSMAnalysis.Zprime2muAnalysis.OurSelectionDec2012_cff as OurSelectionDec2012
#print OurSelectionDec2012.loose_cut #FUNZIONA
from SUSYBSMAnalysis.Zprime2muAnalysis.hltTriggerMatch_cfi import trigger_paths
####process.goodDataFilter.TriggerResultsTag = cms.InputTag('TriggerResults', '', 'HLT')# was PAT
####process.goodDataFilter.HLTPaths = cms.vstring('HLT_Mu40_v*')#,trigger_paths#? was ['goodDataAll']

process.load('SUSYBSMAnalysis.Zprime2muAnalysis.SimpleAnalyzer_cfi') # vuoto per ora

# cose di process def in Zprime2muAnalysis_cfg
process.source.fileNames =[
                           'file:./pat.root'
                           #'/store/user/federica/PATTuple/DYJetsToEEMuMu_M-120To200_13TeV-madgraph/DY_M-120To200_Phys14_PU20BX25/150317_182312/0000/pat_1.root'
#                           #'/store/mc/Phys14DR/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/AODSIM/PU20bx25_tsg_PHYS14_25_V1-v1/00000/02BE6C0D-E46E-E411-89C3-003048F0E1B0.root'
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_100_1_Hw6.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_10_1_r9E.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_11_1_bgC.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_12_1_GLd.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_13_1_U2Q.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_14_1_0hG.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_15_1_vGZ.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_16_1_5jc.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_17_1_NVZ.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_18_1_t0s.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_19_1_5zC.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_1_1_G9p.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_20_1_p7N.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_21_1_rH5.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_22_1_NeA.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_23_1_dAY.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_24_1_jUN.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_25_1_DeM.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_26_1_kUx.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_27_1_Esw.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_28_1_VZ3.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_29_1_gfs.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_2_1_Y1d.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_30_1_3bb.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_31_1_mKL.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_32_1_kYc.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_33_1_wBJ.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_34_1_1aa.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_35_1_0XZ.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_36_1_qbG.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_37_1_rKh.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_38_1_xyD.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_39_1_9VD.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_3_1_rW7.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_40_1_zPe.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_41_1_Vep.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_42_1_uYW.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_43_1_OvU.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_44_1_H86.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_45_1_6aT.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_46_1_bI2.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_47_1_DEq.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_48_1_i4E.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_49_1_iow.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_4_1_cv0.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_50_1_OVd.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_51_2_spW.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_52_1_k4t.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_53_1_dMd.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_54_1_xKk.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_55_1_9g9.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_56_1_oCA.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_57_1_CgL.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_58_1_vCl.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_59_1_HXe.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_5_1_JaG.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_60_1_nk0.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_61_2_NMY.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_62_1_tSY.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_63_1_EQb.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_64_1_LV2.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_65_1_oyi.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_66_1_trE.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_67_1_W8P.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_68_1_5L8.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_69_1_FSa.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_6_1_01i.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_70_1_y4d.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_71_1_utZ.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_72_1_JGz.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_73_1_T4M.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_74_1_4YI.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_75_1_vLz.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_76_1_FrG.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_77_1_7ng.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_78_1_Egq.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_79_1_6aE.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_7_1_mbe.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_80_1_A5q.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_81_1_Kpd.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_82_1_yks.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_83_1_k2f.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_84_1_P1s.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_85_1_eCA.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_86_1_FlB.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_87_1_RC0.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_88_1_bm2.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_89_1_lbI.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_8_1_Ceo.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_90_1_zbp.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_91_1_SXw.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_92_1_OYk.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_93_1_vv3.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_94_1_bDc.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_95_1_klX.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_96_1_gFO.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_97_1_OID.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_98_1_CqE.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_99_1_133.root',
#                           '/store/user/rradogna/ZprimeToMuMu_M-5000_Tune4C_13TeV-pythia8/datamc_zpsi5000/a8881ceec144e0dfafbb7486d1b7f8e6/pat_9_1_N9I.root' 
                           
                           
                           ]
process.options.wantSummary = cms.untracked.bool(True)# false di default
process.MessageLogger.cerr.FwkReport.reportEvery = 1 # default 1000
process.maxEvents.input = -1
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
process.p = cms.Path(process.goodDataFilter*process.Zprime2muAnalysisSequence* process.HistosFromPAT)
#process.p *=process.histos
# A list of analyzers or output modules to be run after all paths have been run.
#process.outpath = cms.EndPath(process.out)
f = file('outfile', 'w')
f.write(process.dumpPython())
f.close()


