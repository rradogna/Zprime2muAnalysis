#!/usr/bin/env python

import sys, os, FWCore.ParameterSet.Config as cms
from SUSYBSMAnalysis.Zprime2muAnalysis.Zprime2muAnalysis_cff import switch_hlt_process_name
from SUSYBSMAnalysis.Zprime2muAnalysis.Zprime2muAnalysis_cfg import process

#process.source.fileNames =['file:./pat2.root']
#process.source.fileNames =['/store/relval/CMSSW_7_1_0/RelValZMM_13/GEN-SIM-RECO/POSTLS171_V15-v1/00000/6650F961-99FB-E311-BA90-0025905A48BC.root']
#process.source.fileNames=['/store/relval/CMSSW_7_1_0_pre4_AK4/RelValProdTTbar/AODSIM/START71_V1-v2/00000/7A3637AA-28B5-E311-BC25-003048678B94.root']
process.maxEvents.input = -1

readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
process.source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_100_1_Bc7.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_101_1_YfK.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_10_1_e78.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_11_1_OzT.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_12_1_1qr.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_13_1_6EI.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_14_1_NFJ.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_15_1_yMJ.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_16_1_A8S.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_17_1_tnH.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_18_1_2f0.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_19_1_Psv.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_1_1_Zes.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_20_1_BRX.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_21_1_HJ6.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_22_1_ACy.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_23_1_RTy.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_24_1_0nC.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_25_1_QEJ.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_26_1_OJ0.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_27_1_dzA.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_28_1_ksz.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_29_1_EBN.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_2_1_xnL.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_30_1_F2R.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_31_1_Enx.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_32_1_UX3.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_33_1_QFH.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_34_1_rdI.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_35_1_XDg.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_36_1_CFV.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_37_1_ZOv.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_38_1_Z8K.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_39_1_hJJ.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_3_1_AF0.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_40_1_PrV.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_41_1_ZnE.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_42_1_OOd.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_43_1_6CX.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_44_1_nuS.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_45_1_vKA.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_46_1_u5F.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_47_1_ea8.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_48_1_15G.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_49_1_0rh.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_4_1_cc6.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_50_1_4Hl.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_51_1_kZX.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_52_1_ze6.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_53_1_ahT.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_54_1_WDv.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_55_1_z30.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_56_1_ypb.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_57_1_WCA.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_58_1_HW5.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_59_1_lKH.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_5_1_eNV.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_60_1_Twn.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_61_1_ChM.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_62_1_v1v.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_63_1_V5h.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_64_1_FhK.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_65_1_Bwc.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_66_1_mdg.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_67_1_UWx.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_68_1_Ze3.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_69_1_lay.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_6_1_s7E.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_70_1_Hvo.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_71_1_ZHF.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_72_1_g9r.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_73_1_8nb.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_74_1_7UH.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_75_1_lhC.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_76_1_qvV.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_77_1_7cn.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_78_1_GTz.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_79_1_Sik.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_7_1_pJc.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_80_1_CV0.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_81_1_nHL.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_82_1_Y5i.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_83_1_YQL.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_84_1_whW.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_85_1_ZG4.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_86_1_y0w.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_87_1_KMp.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_88_1_cEL.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_89_1_Hil.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_8_1_ODG.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_90_1_rDv.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_91_1_6Ii.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_92_1_M2j.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_93_1_J2J.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_94_1_mAI.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_95_1_aoc.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_96_1_oiz.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_97_1_dEF.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_98_1_a6K.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_99_1_sVv.root',
       '/store/user/rradogna/ZprimeToMuMu_M-1000_Tune4C_13TeV-pythia8/datamc_zpsi1000/5ae2dc0ad5519e42240ad5a71eb54bed/pat_9_1_RsK.root' ] );


secFiles.extend( [
               ] )

from SUSYBSMAnalysis.Zprime2muAnalysis.hltTriggerMatch_cfi import trigger_match, prescaled_trigger_match, trigger_paths, prescaled_trigger_paths, overall_prescale, offline_pt_threshold, prescaled_offline_pt_threshold

# Since the prescaled trigger comes with different prescales in
# different runs/lumis, this filter prescales it to a common factor to
# make things simpler.
process.load('SUSYBSMAnalysis.Zprime2muAnalysis.PrescaleToCommon_cff')
process.PrescaleToCommon.trigger_paths = prescaled_trigger_paths
process.PrescaleToCommon.overall_prescale = overall_prescale

# The histogramming module that will be cloned multiple times below
# for making histograms with different cut/dilepton combinations.
from SUSYBSMAnalysis.Zprime2muAnalysis.HistosFromPAT_cfi import HistosFromPAT
HistosFromPAT.leptonsFromDileptons = True

# These modules define the basic selection cuts. For the monitoring
# sets below, we don't need to define a whole new module, since they
# just change one or two cuts -- see below.
#import SUSYBSMAnalysis.Zprime2muAnalysis.VBTFSelection_cff as VBTFSelection
#import SUSYBSMAnalysis.Zprime2muAnalysis.OurSelectionOld_cff as OurSelectionOld
#import SUSYBSMAnalysis.Zprime2muAnalysis.OurSelection2011EPS_cff as OurSelection2011EPS
import SUSYBSMAnalysis.Zprime2muAnalysis.OurSelectionNew_cff as OurSelectionNew
import SUSYBSMAnalysis.Zprime2muAnalysis.OurSelectionDec2012_cff as OurSelectionDec2012

# CandCombiner includes charge-conjugate decays with no way to turn it
# off. To get e.g. mu+mu+ separate from mu-mu-, cut on the sum of the
# pdgIds (= -26 for mu+mu+).
dils = [
    ('MuonsPlusMuonsMinus',          '%(leptons_name)s:muons@+ %(leptons_name)s:muons@-',         'daughter(0).pdgId() + daughter(1).pdgId() == 0'),
    ('MuonsPlusMuonsPlus',           '%(leptons_name)s:muons@+ %(leptons_name)s:muons@+',         'daughter(0).pdgId() + daughter(1).pdgId() == -26'),
    ('MuonsMinusMuonsMinus',         '%(leptons_name)s:muons@- %(leptons_name)s:muons@-',         'daughter(0).pdgId() + daughter(1).pdgId() == 26'),
    ('MuonsSameSign',                '%(leptons_name)s:muons@- %(leptons_name)s:muons@-',         ''),
    ('MuonsAllSigns',                '%(leptons_name)s:muons@- %(leptons_name)s:muons@-',         ''),
    ('MuonsPlusElectronsMinus',      '%(leptons_name)s:muons@+ %(leptons_name)s:electrons@-',     'daughter(0).pdgId() + daughter(1).pdgId() == -2'),
    ('MuonsMinusElectronsPlus',      '%(leptons_name)s:muons@- %(leptons_name)s:electrons@+',     'daughter(0).pdgId() + daughter(1).pdgId() == 2'),
    ('MuonsPlusElectronsPlus',       '%(leptons_name)s:muons@+ %(leptons_name)s:electrons@+',     'daughter(0).pdgId() + daughter(1).pdgId() == -24'),
    ('MuonsMinusElectronsMinus',     '%(leptons_name)s:muons@- %(leptons_name)s:electrons@-',     'daughter(0).pdgId() + daughter(1).pdgId() == 24'),
    ('MuonsElectronsOppSign',        '%(leptons_name)s:muons@+ %(leptons_name)s:electrons@-',     ''),
    ('MuonsElectronsSameSign',       '%(leptons_name)s:muons@+ %(leptons_name)s:electrons@+',     ''),
    ('MuonsElectronsAllSigns',       '%(leptons_name)s:muons@+ %(leptons_name)s:electrons@+',     ''),
    ]

# Define sets of cuts for which to make plots. If using a selection
# that doesn't have a trigger match, need to re-add a hltHighLevel
# filter somewhere below.
cuts = {
#    'VBTF'     : VBTFSelection,
#    'OurOld'   : OurSelectionOld,
#    'OurEPS'   : OurSelection2011EPS,
    #'OurNew'   : OurSelectionNew,
    'Our2012'  : OurSelectionDec2012,
    #'OurNoIso' : OurSelectionDec2012,
    #'EmuVeto'  : OurSelectionDec2012,
    #'Simple'   : OurSelectionDec2012, # The selection cuts in the module listed here are ignored below.
#    'VBTFMuPrescaled' : VBTFSelection,
    #'OurMuPrescaledNew'  : OurSelectionNew,
    #'OurMuPrescaled2012' : OurSelectionDec2012
    }

# Loop over all the cut sets defined and make the lepton, allDilepton
# (combinatorics only), and dilepton (apply cuts) modules for them.
for cut_name, Selection in cuts.iteritems():
    # Keep track of modules to put in the path for this set of cuts.
    path_list = []

    # Clone the LeptonProducer to make leptons with the set of cuts
    # we're doing here flagged.  I.e., muon_cuts in LeptonProducer
    # just marks each muon with a userInt "cutFor" that is 0 if it
    # passes the cuts, and non-0 otherwise; it does not actually drop
    # any of the muons. The cutFor flag actually gets ignored by the
    # LooseTightPairSelector in use for all the cuts above, at
    # present.
    leptons_name = cut_name + 'Leptons'
    if cut_name == 'Simple':
        muon_cuts = ''
    elif 'MuPrescaled' in cut_name:
        muon_cuts = Selection.loose_cut.replace('pt > %s' % offline_pt_threshold, 'pt > %s' % prescaled_offline_pt_threshold)
    else:
        muon_cuts = Selection.loose_cut
    leptons = process.leptons.clone(muon_cuts = muon_cuts)
    if cut_name == 'EmuVeto':
        leptons.electron_muon_veto_dR = 0.1
    # Keep using old TuneP for past selections
    if 'Dec2012' not in Selection.__file__:
        leptons.muon_track_for_momentum = cms.string('TuneP')
    setattr(process, leptons_name, leptons)
    path_list.append(leptons)

    # Make all the combinations of dileptons we defined above.
    for dil_name, dil_decay, dil_cut in dils:
        # For the EmuVeto path, we only care about e-mu events.
        if cut_name == 'EmuVeto' and 'Electron' not in dil_name:
            continue

        # For the MuPrescaled paths, we don't care about e-mu events.
        if 'MuPrescaled' in cut_name and 'Electron' in dil_name:
            continue

        # Unique names for the modules: allname for the allDileptons,
        # and name for dileptons.
        name = cut_name + dil_name
        allname = 'all' + name

        alldil = Selection.allDimuons.clone(decay = dil_decay % locals(), cut = dil_cut)
        if 'AllSigns' in dil_name:
            alldil.checkCharge = cms.bool(False)
        dil = Selection.dimuons.clone(src = cms.InputTag(allname))

        # Implement the differences to the selections; currently, as
        # in Zprime2muCombiner, the cuts in loose_cut and
        # tight_cut are the ones actually used to drop leptons, and
        # not the ones passed into the LeptonProducer to set cutFor above.
        if cut_name == 'Simple':
            alldil.electron_cut_mask = cms.uint32(0)
            alldil.loose_cut = 'isGlobalMuon && pt > 20.'
            alldil.tight_cut = ''
            dil.max_candidates = 100
            dil.do_remove_overlap = False
            delattr(dil, 'back_to_back_cos_angle_min')
            delattr(dil, 'vertex_chi2_max')
            delattr(dil, 'dpt_over_pt_max')
        elif cut_name == 'OurNoIso':
            alldil.loose_cut = alldil.loose_cut.value().replace(' && isolationR03.sumPt / innerTrack.pt < 0.10', '')
        elif 'MuPrescaled' in cut_name:
            alldil.loose_cut = alldil.loose_cut.value().replace('pt > %s' % offline_pt_threshold, 'pt > %s' % prescaled_offline_pt_threshold)
            assert alldil.tight_cut == trigger_match
            alldil.tight_cut = prescaled_trigger_match

        # Histos now just needs to know which leptons and dileptons to use.
        histos = HistosFromPAT.clone(lepton_src = cms.InputTag(leptons_name, 'muons'), dilepton_src = cms.InputTag(name))

        # Add all these modules to the process and the path list.
        setattr(process, allname, alldil)
        setattr(process, name, dil)
        setattr(process, name + 'Histos', histos)
        path_list.append(alldil * dil * histos)

    # Finally, make the path for this set of cuts.
    pathname = 'path' + cut_name
    pobj = process.muonPhotonMatch * reduce(lambda x,y: x*y, path_list)
    if 'VBTF' not in cut_name and cut_name != 'Simple':
        pobj = process.goodDataFilter * pobj
    if 'MuPrescaled' in cut_name:
        pobj = process.PrescaleToCommon * pobj
    path = cms.Path(pobj)
    setattr(process, pathname, path)

def ntuplify(process, fill_gen_info=False):
    process.SimpleNtupler = cms.EDAnalyzer('SimpleNtupler',
                                           dimu_src = cms.InputTag('SimpleMuonsAllSigns'),
                                           beamspot_src = cms.InputTag('offlineBeamSpot'),
                                           vertices_src = cms.InputTag('offlinePrimaryVertices'),
                                           )
    process.SimpleNtuplerEmu = process.SimpleNtupler.clone(dimu_src = cms.InputTag('SimpleMuonsElectronsAllSigns'))

    if fill_gen_info:
        from SUSYBSMAnalysis.Zprime2muAnalysis.HardInteraction_cff import hardInteraction
        process.SimpleNtupler.hardInteraction = hardInteraction

    process.pathSimple *= process.SimpleNtupler * process.SimpleNtuplerEmu

def printify(process):
    process.MessageLogger.categories.append('PrintEvent')

    process.load('HLTrigger.HLTcore.triggerSummaryAnalyzerAOD_cfi')
    process.triggerSummaryAnalyzerAOD.inputTag = cms.InputTag('hltTriggerSummaryAOD','','HLT')
    process.pathSimple *= process.triggerSummaryAnalyzerAOD

    process.PrintOriginalMuons = cms.EDAnalyzer('PrintEvent', muon_src = cms.InputTag('cleanPatMuonsTriggerMatch'), trigger_results_src = cms.InputTag('TriggerResults','','HLT'))
    process.pathSimple *= process.PrintOriginalMuons

    pe = process.PrintEventSimple = cms.EDAnalyzer('PrintEvent', dilepton_src = cms.InputTag('SimpleMuonsPlusMuonsMinus'))
    process.pathSimple *= process.PrintEventSimple

    #- 2011-2012 selection (Nlayers > 8)
    #process.PrintEventOurNew = pe.clone(dilepton_src = cms.InputTag('OurNewMuonsPlusMuonsMinus'))
    #process.PrintEventOurNewSS = pe.clone(dilepton_src = cms.InputTag('OurNewMuonsSameSign'))
    #process.PrintEventOurNewEmu = pe.clone(dilepton_src = cms.InputTag('OurNewMuonsElectronsOppSign'))
    #process.pathOurNew *= process.PrintEventOurNew * process.PrintEventOurNewSS * process.PrintEventOurNewEmu

    #- December 2012 selection (Nlayers > 5, re-tuned TuneP, dpT/pT < 0.3)
    process.PrintEventOur2012    = pe.clone(dilepton_src = cms.InputTag('Our2012MuonsPlusMuonsMinus'))
    process.PrintEventOur2012SS  = pe.clone(dilepton_src = cms.InputTag('Our2012MuonsSameSign'))
    process.PrintEventOur2012Emu = pe.clone(dilepton_src = cms.InputTag('Our2012MuonsElectronsOppSign'))
    process.pathOur2012 *= process.PrintEventOur2012 * process.PrintEventOur2012SS * process.PrintEventOur2012Emu

def check_prescale(process, trigger_paths, hlt_process_name='HLT'):
    process.load('SUSYBSMAnalysis.Zprime2muAnalysis.CheckPrescale_cfi')
    process.CheckPrescale.trigger_paths = cms.vstring(*trigger_paths)
    process.pCheckPrescale = cms.Path(process.CheckPrescale)

def for_data(process):
    process.GlobalTag.globaltag = 'GR_P_V42_AN2::All'
    ntuplify(process)
    check_prescale(process, trigger_paths)

def for_mc(process, hlt_process_name, fill_gen_info):
    ntuplify(process, fill_gen_info)
    switch_hlt_process_name(process, hlt_process_name) # this must be done last (i.e. after anything that might have an InputTag for something HLT-related)

def get_dataset(run):
    #JMTBAD common with dataset_details in submit below, make a DataSamples.py?
    run = int(run)
    if 190450 <= run <= 191284:
        return '/SingleMu/tucker-datamc_SingleMuRun2012A_Prompt_190450_191284_20120418134612-57b19813ab8f2ab142c4566dc6738156/USER'
    else:
        raise ValueError('dunno how to do run %i' % run)

if 'int_data' in sys.argv:
    for_data(process)
    printify(process)
    
if 'int_mc' in sys.argv:
    for_mc(process, 'HLT', False)
    printify(process)
    
if 'gogo' in sys.argv:
    for_data(process)
    printify(process)
    
    n = sys.argv.index('gogo')
    run, lumi, event = sys.argv[n+1], sys.argv[n+2], sys.argv[n+3]
    print run, lumi, event
    run = int(run)
    lumi = int(lumi)
    event = int(event)
    filename = [x for x in sys.argv if x.endswith('.root')]
    if filename:
        filename = filename[0]
    else:
        dataset = get_dataset(run)
        print dataset
        output = os.popen('dbs search --url https://cmsdbsprod.cern.ch:8443/cms_dbs_ph_analysis_02_writer/servlet/DBSServlet --query="find file where dataset=%s and run=%s and lumi=%s"' % (dataset, run, lumi)).read()
        print repr(output)
        filename = [x for x in output.split('\n') if x.endswith('.root')][0]
    print filename
    process.source.fileNames = [filename]
    from SUSYBSMAnalysis.Zprime2muAnalysis.cmsswtools import set_events_to_process
    set_events_to_process(process, [(run, event)])

if __name__ == '__main__' and 'submit' in sys.argv:
    crab_cfg = '''
[CRAB]
jobtype = cmssw
scheduler = condor

[CMSSW]
datasetpath = %(ana_dataset)s
dbs_url = https://cmsdbsprod.cern.ch:8443/cms_dbs_ph_analysis_02_writer/servlet/DBSServlet
pset = histos_crab.py
get_edm_output = 1
job_control

[USER]
ui_working_dir = crab/crab_ana_datamc_%(name)s
return_data = 1
'''

    just_testing = 'testing' in sys.argv
        
    # Run on data.
    if 'no_data' not in sys.argv:
        from SUSYBSMAnalysis.Zprime2muAnalysis.goodlumis import *

        dataset_details = [
            ('SingleMuRun2012A_13Jul2012_190450_193751', '/SingleMu/slava-datamc_SingleMuRun2012A-13Jul2012_190450_193751_20121011073628-426a2d966f78bce6bde85f3ed41c07ba/USER'),
            ('SingleMuRun2012A_06Aug2012_190782_190949', '/SingleMu/slava-datamc_SingleMuRun2012A-recover-06Aug2012_190782_190949_20121011120430-426a2d966f78bce6bde85f3ed41c07ba/USER'),
            ('SingleMuRun2012B_13Jul2012_193752_196531', '/SingleMu/slava-datamc_SingleMuRun2012B-13Jul2012_193752_196531_20121012044921-426a2d966f78bce6bde85f3ed41c07ba/USER'),
            ('SingleMuRun2012C_24Aug2012_197556_198913', '/SingleMu/slava-datamc_SingleMuRun2012C-24Aug2012_197556_198913_20121012113325-426a2d966f78bce6bde85f3ed41c07ba/USER'),
            ('SingleMuRun2012C_Prompt_198934_203772',    '/SingleMu/slava-datamc_SingleMuRun2012C-Prompt_198934_203772_20121015023300-8627c6a48d2426dec4aa557620a039a0/USER'),
            ('SingleMuRun2012D_Prompt_203773_204563',    '/SingleMu/slava-datamc_SingleMuRun2012D-Prompt_203773_204563_20121016104501-8627c6a48d2426dec4aa557620a039a0/USER'),
            ('SingleMuRun2012D_Prompt_204564_206087',    '/SingleMu/slava-datamc_SingleMuRun2012D-Prompt_204564_206087_20121029121943-8627c6a48d2426dec4aa557620a039a0/USER'),
            ('SingleMuRun2012D_Prompt_206066_206066',    '/SingleMu/slava-datamc_SingleMuRun2012D-Prompt_206066_206066_20130115083834-5fce88899b8479b9df01fc5ef8a1e921/USER'),
            ('SingleMuRun2012D-Prompt_206088_206539',    '/SingleMu/slava-datamc_SingleMuRun2012D-Prompt_206088_206539_20121112085341-8627c6a48d2426dec4aa557620a039a0/USER'),
            ('SingleMuRun2012D-Prompt_206540_207900',    '/SingleMu/slava-datamc_SingleMuRun2012D-Prompt_206540_207900_20121203042806-8627c6a48d2426dec4aa557620a039a0/USER'),
            ('SingleMuRun2012D-Prompt_207901_208380',    '/SingleMu/slava-datamc_SingleMuRun2012D-Prompt_207901_208380_20121212090713-5fce88899b8479b9df01fc5ef8a1e921/USER'),
            ('SingleMuRun2012D-Prompt_208381_208700',    '/SingleMu/slava-datamc_SingleMuRun2012D-Prompt_208381_208700_20121217043712-5fce88899b8479b9df01fc5ef8a1e921/USER'),
#            ('SingleMuRun2012C-11Dec2012_201191_201191', '/SingleMu/slava-datamc_SingleMuRun2012C-EcalRecover_11Dec2012_201191_201191_20130115101201-5fce88899b8479b9df01fc5ef8a1e921/USER'),
            ]

        lumi_lists = [
#            'DCSOnly',
#            'Run2012PlusDCSOnlyMuonsOnly',
            'Run2012MuonsOnly',
            'Run2012',
            ]

        jobs = []
        for lumi_name in lumi_lists:
            ll = eval(lumi_name + '_ll') if lumi_name != 'NoLumiMask' else None
            for dd in dataset_details:
                jobs.append(dd + (lumi_name, ll))
                
        for dataset_name, ana_dataset, lumi_name, lumi_list in jobs:
            json_fn = 'tmp.json'
            lumi_list.writeJSON(json_fn)
            lumi_mask = 'lumi_mask = %s' % json_fn

            name = '%s_%s' % (lumi_name, dataset_name)
            print name

            new_py = open('histos.py').read()
            new_py += "\nfor_data(process)\n"
            open('histos_crab.py', 'wt').write(new_py)

            new_crab_cfg = crab_cfg % locals()

            job_control = '''
total_number_of_lumis = -1
lumis_per_job = 500
%(lumi_mask)s''' % locals()

            new_crab_cfg = new_crab_cfg.replace('job_control', job_control)
            open('crab.cfg', 'wt').write(new_crab_cfg)

            if not just_testing:
                os.system('crab -create -submit all')
            else:
                cmd = 'diff histos.py histos_crab.py | less'
                print cmd
                os.system(cmd)
                cmd = 'less crab.cfg'
                print cmd
                os.system(cmd)

        if not just_testing:
            os.system('rm crab.cfg histos_crab.py histos_crab.pyc tmp.json')

    if 'no_mc' not in sys.argv:
        # Set crab_cfg for MC.
        crab_cfg = crab_cfg.replace('job_control','''
total_number_of_events = -1
events_per_job = 100000
    ''')

        from SUSYBSMAnalysis.Zprime2muAnalysis.MCSamples import samples

        combine_dy_samples = len([x for x in samples if x.name in ['zmumu', 'dy120_c1', 'dy200_c1', 'dy500_c1', 'dy800_c1', 'dy1000_c1', 'dy1500_c1', 'dy2000_c1']]) > 0
        print 'combine_dy_samples:', combine_dy_samples

        for sample in reversed(samples):
            print sample.name

            new_py = open('histos.py').read()
            sample.fill_gen_info = sample.name in ['zmumu', 'dy120_c1', 'dy200_c1', 'dy500_c1', 'dy800_c1', 'dy1000_c1', 'dy1500_c1', 'dy2000_c1', 'zssm1000']
            new_py += "\nfor_mc(process, hlt_process_name='%(hlt_process_name)s', fill_gen_info=%(fill_gen_info)s)\n" % sample

            if combine_dy_samples and (sample.name == 'zmumu' or 'dy' in sample.name):
                mass_limits = {
                    'zmumu'    : (  20,    120),
                    'dy120_c1' : ( 120,    200),
                    'dy200_c1' : ( 200,    500),
                    'dy500_c1' : ( 500,    800),
                    'dy800_c1' : ( 800,   1000),
                    'dy1000_c1': (1000,   1500),
                    'dy1500_c1': (1500,   2000),
                    'dy2000_c1': (2000, 100000),
                    }
                lo,hi = mass_limits[sample.name]
                from SUSYBSMAnalysis.Zprime2muAnalysis.DYGenMassFilter_cfi import dy_gen_mass_cut
                new_cut = dy_gen_mass_cut % locals()

                new_py += '''
process.load('SUSYBSMAnalysis.Zprime2muAnalysis.DYGenMassFilter_cfi')

process.DYGenMassFilter.cut = "%(new_cut)s"
for pn,p in process.paths.items():
    setattr(process, pn, cms.Path(process.DYGenMassFilter*p._seq))
''' % locals()

            open('histos_crab.py', 'wt').write(new_py)

            open('crab.cfg', 'wt').write(crab_cfg % sample)
            if not just_testing:
                os.system('crab -create -submit all')
            else:
                cmd = 'diff histos.py histos_crab.py | less'
                print cmd
                os.system(cmd)
                cmd = 'less crab.cfg'
                print cmd
                os.system(cmd)

        if not just_testing:
            os.system('rm crab.cfg histos_crab.py histos_crab.pyc')
