#!/usr/bin/env python

# (py resfromdy.py >! plots/out.resfromdy) && tlp plots/*resfromdy

import os
import ROOT
import math
from array import array
from ROOT import *
#from SUSYBSMAnalysis.Zprime2muAnalysis.roottools import *
#set_zp2mu_style()
#ROOT.gStyle.SetOptFit(1111)
gStyle.SetOptStat("")

ROOT.gStyle.SetPadTopMargin(0.02)
ROOT.gStyle.SetPadRightMargin(0.02)
###################################################################
def projectAndFit(Histo2D, postFix = "none"):
    nx    = Histo2D.GetNbinsX()
    print nx
    htmp= Histo2D.ProfileX()
    print htmp.GetNbinsX()
    x1    = htmp.GetBinLowEdge(1)
    bw    = htmp.GetBinWidth(nx)
    x2    = htmp.GetBinLowEdge(nx)+bw
    h2 = ROOT.TH1D((postFix + "Sigma"),(postFix + "Sigma"),nx, x1, x2)
    for i in xrange(1, Histo2D.GetNbinsX()+1):
        proj = Histo2D.ProjectionY("proj_%.d" %i,i,i)
        if proj.GetEntries() != 0:
            print "%.d orario" %i
            func = TF1("func_%.d" %i,"gaus", -0.13, 0.13)
            proj.Fit("func_%.d" %i, 'R')
            h2.SetBinContent(i,func.GetParameter(2))
            h2.SetBinError(i,func.GetParError(2))
    return h2
#                std::stringstream ss;
#                ss<<postFix.c_str()<<i;
#                std::string pf = ss.str();
#                
#                //if(found1 != string::npos || found2 != string::npos || found3 != string::npos) temp = extractSigmaBis(proj1,pf.c_str());
#                temp = extractSigma(proj1,pf.c_str());
#                
#                h2->SetBinContent(i,temp.sigma);
#                h2->SetBinError(i,temp.DeltaSigma);
#        
#        }
#        
#        vec.push_back(h1);
#        vec.push_back(h2);
#    return vec;
###################################################################
f1tev_at8tev = ROOT.TFile('./files/zp2mu_dy1500_8TM.root')
d1tev_at8tev = f1tev_at8tev.ResolutionVertexUsingMC
h1tev_at8tev_PtBB = d1tev_at8tev.Get('LeptonPt_BarrelBarrel')
h1tev_at8tev_PtEE = d1tev_at8tev.Get('LeptonPt_EndcapEndcap')
h1tev_at8tev_PtEB = d1tev_at8tev.Get('LeptonPt_EndcapBarrel')

h1tev_at8tev_PtResBB = d1tev_at8tev.Get('LeptonPtRes_BarrelBarrel')
h1tev_at8tev_PtResEE = d1tev_at8tev.Get('LeptonPtRes_EndcapEndcap')
h1tev_at8tev_PtResEB = d1tev_at8tev.Get('LeptonPtRes_EndcapBarrel')

h1tev_at8tev_PtPullBB = d1tev_at8tev.Get('LeptonPtPull_BarrelBarrel')
h1tev_at8tev_PtPullEE = d1tev_at8tev.Get('LeptonPtPull_EndcapEndcap')
h1tev_at8tev_PtPullEB = d1tev_at8tev.Get('LeptonPtPull_EndcapBarrel')

h1tev_at8tev_MresBB = d1tev_at8tev.Get('DileptonMassRes_BarrelBarrel')
h1tev_at8tev_MresEE = d1tev_at8tev.Get('DileptonMassRes_EndcapEndcap')
h1tev_at8tev_MresEB = d1tev_at8tev.Get('DileptonMassRes_EndcapBarrel')

h1tev_at8tev_PtResVStrkprob = d1tev_at8tev.Get('LeptonPtResVSMuonPtProb')


###################################################################
f1tev_at13tev = ROOT.TFile('./files/zp2mu_dy1500_13TM.root')
d1tev_at13tev = f1tev_at13tev.ResolutionVertexUsingMC
h1tev_at13tev_PtBB = d1tev_at13tev.Get('LeptonPt_BarrelBarrel')
h1tev_at13tev_PtEE = d1tev_at13tev.Get('LeptonPt_EndcapEndcap')
h1tev_at13tev_PtEB = d1tev_at13tev.Get('LeptonPt_EndcapBarrel')

h1tev_at13tev_PtResBB = d1tev_at13tev.Get('LeptonPtRes_BarrelBarrel')
h1tev_at13tev_PtResEE = d1tev_at13tev.Get('LeptonPtRes_EndcapEndcap')
h1tev_at13tev_PtResEB = d1tev_at13tev.Get('LeptonPtRes_EndcapBarrel')

h1tev_at13tev_PtPullBB = d1tev_at13tev.Get('LeptonPtPull_BarrelBarrel')
h1tev_at13tev_PtPullEE = d1tev_at13tev.Get('LeptonPtPull_EndcapEndcap')
h1tev_at13tev_PtPullEB = d1tev_at13tev.Get('LeptonPtPull_EndcapBarrel')

h1tev_at13tev_MresBB = d1tev_at13tev.Get('DileptonMassRes_BarrelBarrel')
h1tev_at13tev_MresEE = d1tev_at13tev.Get('DileptonMassRes_EndcapEndcap')
h1tev_at13tev_MresEB = d1tev_at13tev.Get('DileptonMassRes_EndcapBarrel')

h1tev_at13tev_MresEB = d1tev_at13tev.Get('DileptonMassRes_EndcapBarrel')

h1tev_at13tev_PtResVStrkprob = d1tev_at13tev.Get('LeptonPtResVSMuonPtProb')

###############
nGen_8tev=99992.
nGen_13tev=13206.
print "nGen_8tev", nGen_8tev
print "nGen_13tev", nGen_13tev
###############

c_PtresVSprob = ROOT.TCanvas( 'c_PtresVSprob', '')
h1tev_at13tev_PtResVStrkprob.Rebin2D(50,1)
h1tev_at8tev_PtResVStrkprob.Rebin2D(50,1)
hprof_at13tev_PtRes= h1tev_at13tev_PtResVStrkprob.ProfileX()
hprof_at8tev_PtRes= h1tev_at8tev_PtResVStrkprob.ProfileX()
hPtResVStrkprob_13tev=projectAndFit(h1tev_at13tev_PtResVStrkprob,'PtResVStrkprob_13tev')
hPtResVStrkprob_8tev=projectAndFit(h1tev_at8tev_PtResVStrkprob, 'PtResVStrkprob_8tev')
hPtResVStrkprob_13tev.SetLineColor(2)
hPtResVStrkprob_13tev.SetLineWidth(2)
hPtResVStrkprob_8tev.SetLineColor(1)
hPtResVStrkprob_8tev.SetLineWidth(2)
hPtResVStrkprob_13tev.SetMaximum(0.2)
hPtResVStrkprob_13tev.SetMinimum(0.0)
hPtResVStrkprob_13tev.Draw()
hPtResVStrkprob_8tev.Draw('same')
c_PtresVSprob.Print('ABSDYTMRES_PtresVSprob.pdf')

c_Pt = ROOT.TCanvas( 'c_Pt', '')
pad1 = TPad( 'pad1', '', 0.03, 0.50, 0.48, 0.95)
pad2 = TPad( 'pad2', '', 0.50, 0.50, 0.98, 0.95)
pad3 = TPad( 'pad3', '', 0.03, 0.02, 0.48, 0.48)
pad4 = TPad( 'pad4', '', 0.50, 0.02, 0.98, 0.48)
pad1.Draw()
pad2.Draw()
pad3.Draw()
pad4.Draw()
pad1.cd()
#pad1.SetLogy()
h1tev_at8tev_PtBB.Scale(1/nGen_8tev)
h1tev_at13tev_PtBB.Scale(1/nGen_13tev)
h1tev_at8tev_PtBB.Rebin(20)
h1tev_at13tev_PtBB.Rebin(20)
h1tev_at8tev_PtBB.SetLineColor(1)
h1tev_at8tev_PtBB.SetLineWidth(2)
h1tev_at13tev_PtBB.SetLineColor(2)
h1tev_at13tev_PtBB.SetLineWidth(2)
h1tev_at8tev_PtBB.Draw("histo")
h1tev_at13tev_PtBB.Draw("same histo")
pad2.cd()
h1tev_at8tev_PtEE.Scale(1/nGen_8tev)
h1tev_at13tev_PtEE.Scale(1/nGen_13tev)
h1tev_at8tev_PtEE.Rebin(20)
h1tev_at13tev_PtEE.Rebin(20)
h1tev_at8tev_PtEE.SetLineColor(1)
h1tev_at8tev_PtEE.SetLineWidth(2)
h1tev_at13tev_PtEE.SetLineColor(2)
h1tev_at13tev_PtEE.SetLineWidth(2)
h1tev_at8tev_PtEE.Draw("histo")
h1tev_at13tev_PtEE.Draw("same histo")
pad3.cd()
h1tev_at8tev_PtEB.Scale(1/nGen_8tev)
h1tev_at13tev_PtEB.Scale(1/nGen_13tev)
h1tev_at8tev_PtEB.Rebin(20)
h1tev_at13tev_PtEB.Rebin(20)
h1tev_at8tev_PtEB.SetLineColor(1)
h1tev_at8tev_PtEB.SetLineWidth(2)
h1tev_at13tev_PtEB.SetLineColor(2)
h1tev_at13tev_PtEB.SetLineWidth(2)
h1tev_at13tev_PtEB.Draw("histo")
h1tev_at8tev_PtEB.Draw("same histo")
c_Pt.Print('ABSDYTMRESsuperimposition_Pt.pdf')

par=[0,0]
parPull=[0,0,0,0]
print "PTRES"
c_PtRes = ROOT.TCanvas( 'c_PtRes', '')
pad1 = TPad( 'pad1', '', 0.03, 0.50, 0.48, 0.95)
pad2 = TPad( 'pad2', '', 0.50, 0.50, 0.98, 0.95)
pad3 = TPad( 'pad3', '', 0.03, 0.02, 0.48, 0.48)
pad4 = TPad( 'pad4', '', 0.50, 0.02, 0.98, 0.48)
pad1.Draw()
pad2.Draw()
pad3.Draw()
pad4.Draw()
pad1.cd()
#pad1.SetLogy()
h1tev_at8tev_PtResBB.Scale(1/nGen_8tev)
h1tev_at13tev_PtResBB.Scale(1/nGen_13tev)
h1tev_at8tev_PtResBB.SetLineColor(1)
h1tev_at8tev_PtResBB.SetLineWidth(2)
h1tev_at13tev_PtResBB.SetLineColor(2)
h1tev_at13tev_PtResBB.SetLineWidth(2)
PtResBB_8 = TF1("PtResBB_8","gaus", -0.13, 0.13)
PtResBB_13 = TF1("PtResBB_13","gaus", -0.13, 0.13)
h1tev_at13tev_PtResBB.Fit('PtResBB_13', 'R')
h1tev_at8tev_PtResBB.Fit('PtResBB_8', 'R')
h1tev_at8tev_PtResBB.Draw("histo")
h1tev_at13tev_PtResBB.Draw("same histo")
PtResBB_8.SetLineColor(4)
PtResBB_13.SetLineColor(4)
PtResBB_8.SetLineWidth(1)
PtResBB_13.SetLineWidth(1)
PtResBB_8.Draw("same")
PtResBB_13.Draw("same")
par[0]=float(PtResBB_8.GetParameter(2))
par[1]=float(PtResBB_13.GetParameter(2))
tPtResBB = ROOT.TLatex(0.15, 0.8, '#splitline{8TeV: #sigma=%.3f }{#color[2]{13TeV: #sigma=%.3f} }' %tuple(par) )
tPtResBB.SetNDC()
tPtResBB.Draw()

pad2.cd()
h1tev_at8tev_PtResEE.Scale(1/nGen_8tev)
h1tev_at13tev_PtResEE.Scale(1/nGen_13tev)
h1tev_at8tev_PtResEE.SetLineColor(1)
h1tev_at8tev_PtResEE.SetLineWidth(2)
h1tev_at13tev_PtResEE.SetLineColor(2)
h1tev_at13tev_PtResEE.SetLineWidth(2)
PtResEE_8 = TF1("PtResEE_8","gaus", -0.13, 0.13)
PtResEE_13 = TF1("PtResEE_13","gaus", -0.13, 0.13)
h1tev_at13tev_PtResEE.Fit('PtResEE_13', 'R')
h1tev_at8tev_PtResEE.Fit('PtResEE_8', 'R')
h1tev_at13tev_PtResEE.Draw("histo")
h1tev_at8tev_PtResEE.Draw("same histo")
PtResEE_8.SetLineColor(4)
PtResEE_13.SetLineColor(4)
PtResEE_8.SetLineWidth(1)
PtResEE_13.SetLineWidth(1)
PtResEE_8.Draw("same")
PtResEE_13.Draw("same")
par[0]=float(PtResEE_8.GetParameter(2))
par[1]=float(PtResEE_13.GetParameter(2))
tPtResEE = ROOT.TLatex(0.15, 0.8, '#splitline{8TeV: #sigma=%.3f }{#color[2]{13TeV: #sigma=%.3f} }' %tuple(par) )
tPtResEE.SetNDC()
tPtResEE.Draw()

pad3.cd()
h1tev_at8tev_PtResEB.Scale(1/nGen_8tev)
h1tev_at13tev_PtResEB.Scale(1/nGen_13tev)
h1tev_at8tev_PtResEB.SetLineColor(1)
h1tev_at8tev_PtResEB.SetLineWidth(2)
h1tev_at13tev_PtResEB.SetLineColor(2)
h1tev_at13tev_PtResEB.SetLineWidth(2)
PtResEB_8 = TF1("PtResEB_8","gaus", -0.13, 0.13)
PtResEB_13 = TF1("PtResEB_13","gaus", -0.13, 0.13)
h1tev_at13tev_PtResEB.Fit('PtResEB_13', 'R')
h1tev_at8tev_PtResEB.Fit('PtResEB_8', 'R')
h1tev_at13tev_PtResEB.Draw("histo")
h1tev_at8tev_PtResEB.Draw("same histo")
PtResEB_8.SetLineColor(4)
PtResEB_13.SetLineColor(4)
PtResEB_8.SetLineWidth(1)
PtResEB_13.SetLineWidth(1)
PtResEB_8.Draw("same")
PtResEB_13.Draw("same")
par[0]=float(PtResEB_8.GetParameter(2))
par[1]=float(PtResEB_13.GetParameter(2))
tPtResEB = ROOT.TLatex(0.15, 0.8, '#splitline{8TeV: #sigma=%.3f }{#color[2]{13TeV: #sigma=%.3f} }' %tuple(par) )
tPtResEB.SetNDC()
tPtResEB.Draw()

c_PtRes.Print('ABSDYTMRESsuperimposition_PtRes.pdf')
print "PULL"
c_Pt = ROOT.TCanvas( 'c_PtPull', '')
pad1 = TPad( 'pad1', '', 0.03, 0.50, 0.48, 0.95)
pad2 = TPad( 'pad2', '', 0.50, 0.50, 0.98, 0.95)
pad3 = TPad( 'pad3', '', 0.03, 0.02, 0.48, 0.48)
pad4 = TPad( 'pad4', '', 0.50, 0.02, 0.98, 0.48)
pad1.Draw()
pad2.Draw()
pad3.Draw()
pad4.Draw()
pad1.cd()
#pad1.SetLogy()
h1tev_at8tev_PtPullBB.Scale(1/nGen_8tev)
h1tev_at13tev_PtPullBB.Scale(1/nGen_13tev)
h1tev_at8tev_PtPullBB.SetLineColor(1)
h1tev_at8tev_PtPullBB.SetLineWidth(2)
h1tev_at13tev_PtPullBB.SetLineColor(2)
h1tev_at13tev_PtPullBB.SetLineWidth(2)
PtPullBB_8 = TF1("PtPullBB_8","gaus", -2, 2)
PtPullBB_13 = TF1("PtPullBB_13","gaus", -2, 2)
h1tev_at13tev_PtPullBB.Fit('PtPullBB_13', 'R')
h1tev_at8tev_PtPullBB.Fit('PtPullBB_8', 'R')
h1tev_at8tev_PtPullBB.Draw("histo")
h1tev_at13tev_PtPullBB.Draw("same histo")
PtPullBB_8.SetLineColor(4)
PtPullBB_13.SetLineColor(4)
PtPullBB_8.SetLineWidth(1)
PtPullBB_13.SetLineWidth(1)
PtPullBB_8.Draw("same")
PtPullBB_13.Draw("same")
parPull[0]=float(h1tev_at8tev_PtPullBB.GetRMS())
parPull[1]=float(h1tev_at13tev_PtPullBB.GetRMS())
parPull[2]=float(PtPullBB_8.GetParameter(2))
parPull[3]=float(PtPullBB_13.GetParameter(2))
tPtPullBB = ROOT.TLatex(0.15, 0.8, '#splitline{#splitline{8TeV: RMS=%.2f }{#color[2]{13TeV: RMS=%.2f}}}{#splitline{8TeV: #sigma=%.2f }{#color[2]{13TeV: #sigma=%.2f}} }' %tuple(parPull) )
tPtPullBB.SetNDC()
tPtPullBB.Draw()
pad2.cd()
h1tev_at8tev_PtPullEE.Scale(1/nGen_8tev)
h1tev_at13tev_PtPullEE.Scale(1/nGen_13tev)
#h1tev_at8tev_PtPullEE.Rebin(20)
#h1tev_at13tev_PtPullEE.Rebin(20)
h1tev_at8tev_PtPullEE.SetLineColor(1)
h1tev_at8tev_PtPullEE.SetLineWidth(2)
h1tev_at13tev_PtPullEE.SetLineColor(2)
h1tev_at13tev_PtPullEE.SetLineWidth(2)
PtPullEE_8 = TF1("PtPullEE_8","gaus", -2, 2)
PtPullEE_13 = TF1("PtPullEE_13","gaus", -2, 2)
h1tev_at13tev_PtPullEE.Fit('PtPullEE_13', 'R')
h1tev_at8tev_PtPullEE.Fit('PtPullEE_8', 'R')
h1tev_at13tev_PtPullEE.Draw("histo")
h1tev_at8tev_PtPullEE.Draw("same histo")
PtPullEE_8.SetLineColor(4)
PtPullEE_13.SetLineColor(4)
PtPullEE_8.SetLineWidth(1)
PtPullEE_13.SetLineWidth(1)
PtPullEE_8.Draw("same")
PtPullEE_13.Draw("same")
parPull[0]=float(h1tev_at8tev_PtPullEE.GetRMS())
parPull[1]=float(h1tev_at13tev_PtPullEE.GetRMS())
parPull[2]=float(PtPullEE_8.GetParameter(2))
parPull[3]=float(PtPullEE_13.GetParameter(2))
tPtPullEE = ROOT.TLatex(0.15, 0.8, '#splitline{#splitline{8TeV: RMS=%.2f }{#color[2]{13TeV: RMS=%.2f}}}{#splitline{8TeV: #sigma=%.2f }{#color[2]{13TeV: #sigma=%.2f}} }' %tuple(parPull) )
tPtPullEE.SetNDC()
tPtPullEE.Draw()
pad3.cd()
h1tev_at8tev_PtPullEB.Scale(1/nGen_8tev)
h1tev_at13tev_PtPullEB.Scale(1/nGen_13tev)
#h1tev_at8tev_PtPullEB.Rebin(20)
#h1tev_at13tev_PtPullEB.Rebin(20)
h1tev_at8tev_PtPullEB.SetLineColor(1)
h1tev_at8tev_PtPullEB.SetLineWidth(2)
h1tev_at13tev_PtPullEB.SetLineColor(2)
h1tev_at13tev_PtPullEB.SetLineWidth(2)
PtPullEB_8 = TF1("PtPullEB_8","gaus", -2, 2)
PtPullEB_13 = TF1("PtPullEB_13","gaus", -2, 2)
h1tev_at13tev_PtPullEB.Fit('PtPullEB_13', 'R')
h1tev_at8tev_PtPullEB.Fit('PtPullEB_8', 'R')
h1tev_at13tev_PtPullEB.Draw("histo")
h1tev_at8tev_PtPullEB.Draw("same histo")
PtPullEB_8.SetLineColor(4)
PtPullEB_13.SetLineColor(4)
PtPullEB_8.SetLineWidth(1)
PtPullEB_13.SetLineWidth(1)
PtPullEB_8.Draw("same")
PtPullEB_13.Draw("same")
parPull[0]=float(h1tev_at8tev_PtPullEB.GetRMS())
parPull[1]=float(h1tev_at13tev_PtPullEB.GetRMS())
parPull[2]=float(PtPullEB_8.GetParameter(2))
parPull[3]=float(PtPullEB_13.GetParameter(2))
tPtPullEB = ROOT.TLatex(0.15, 0.8, '#splitline{#splitline{8TeV: RMS=%.2f }{#color[2]{13TeV: RMS=%.2f}}}{#splitline{8TeV: #sigma=%.2f }{#color[2]{13TeV: #sigma=%.2f}} }' %tuple(parPull) )
tPtPullEB.SetNDC()
tPtPullEB.Draw()
c_PtPull.Print('ABSDYTMRESsuperimposition_PtPull.pdf')
print "MRES"
c_mRes = ROOT.TCanvas( 'c_mRes', '')
pad1 = TPad( 'pad1', '', 0.03, 0.50, 0.48, 0.95)
pad2 = TPad( 'pad2', '', 0.50, 0.50, 0.98, 0.95)
pad3 = TPad( 'pad3', '', 0.03, 0.02, 0.48, 0.48)
pad4 = TPad( 'pad4', '', 0.50, 0.02, 0.98, 0.48)
pad1.Draw()
pad2.Draw()
pad3.Draw()
pad4.Draw()
pad1.cd()
#pad1.SetLogy()
h1tev_at8tev_MresBB.Scale(1/nGen_8tev)
h1tev_at13tev_MresBB.Scale(1/nGen_13tev)
h1tev_at8tev_MresBB.SetLineColor(1)
h1tev_at8tev_MresBB.SetLineWidth(2)
h1tev_at13tev_MresBB.SetLineColor(2)
h1tev_at13tev_MresBB.SetLineWidth(2)
MresBB_8 = TF1("MresBB_8","gaus", -0.13, 0.13)
MresBB_13 = TF1("MresBB_13","gaus", -0.13, 0.13)
h1tev_at13tev_MresBB.Fit('MresBB_13', 'R')
h1tev_at8tev_MresBB.Fit('MresBB_8', 'R')
h1tev_at13tev_MresBB.Draw("histo")
h1tev_at8tev_MresBB.Draw("same histo")
MresBB_8.SetLineColor(4)
MresBB_13.SetLineColor(4)
MresBB_8.SetLineWidth(1)
MresBB_13.SetLineWidth(1)
MresBB_8.Draw("same")
MresBB_13.Draw("same")
par[0]=float(MresBB_8.GetParameter(2))
par[1]=float(MresBB_13.GetParameter(2))
tMresBB = ROOT.TLatex(0.15, 0.8, '#splitline{8TeV: #sigma=%.3f }{#color[2]{13TeV: #sigma=%.3f} }' %tuple(par) )
tMresBB.SetNDC()
tMresBB.Draw()
pad2.cd()
h1tev_at8tev_MresEE.Scale(1/nGen_8tev)
h1tev_at13tev_MresEE.Scale(1/nGen_13tev)
h1tev_at8tev_MresEE.SetLineColor(1)
h1tev_at8tev_MresEE.SetLineWidth(2)
h1tev_at13tev_MresEE.SetLineColor(2)
h1tev_at13tev_MresEE.SetLineWidth(2)
MresEE_8 = TF1("MresEE_8","gaus", -0.13, 0.13)
MresEE_13 = TF1("MresEE_13","gaus", -0.13, 0.13)
h1tev_at13tev_MresEE.Fit('MresEE_13', 'R')
h1tev_at8tev_MresEE.Fit('MresEE_8', 'R')
h1tev_at13tev_MresEE.Draw("histo")
h1tev_at8tev_MresEE.Draw("same histo")
MresEE_8.SetLineColor(4)
MresEE_13.SetLineColor(4)
MresEE_8.SetLineWidth(1)
MresEE_13.SetLineWidth(1)
MresEE_8.Draw("same")
MresEE_13.Draw("same")
par[0]=float(MresEE_8.GetParameter(2))
par[1]=float(MresEE_13.GetParameter(2))
tMresEE = ROOT.TLatex(0.15, 0.8, '#splitline{8TeV: #sigma=%.3f }{#color[2]{13TeV: #sigma=%.3f} }' %tuple(par) )
tMresEE.SetNDC()
tMresEE.Draw()
pad3.cd()
h1tev_at8tev_MresEB.Scale(1/nGen_8tev)
h1tev_at13tev_MresEB.Scale(1/nGen_13tev)
h1tev_at8tev_MresEB.SetLineColor(1)
h1tev_at8tev_MresEB.SetLineWidth(2)
h1tev_at13tev_MresEB.SetLineColor(2)
h1tev_at13tev_MresEB.SetLineWidth(2)
MresEB_8 = TF1("MresEB_8","gaus", -0.13, 0.13)
MresEB_13 = TF1("MresEB_13","gaus", -0.13, 0.13)
h1tev_at13tev_MresEB.Fit('MresEB_13', 'R')
h1tev_at8tev_MresEB.Fit('MresEB_8', 'R')
h1tev_at13tev_MresEB.Draw("histo")
h1tev_at8tev_MresEB.Draw("same histo")
MresEB_8.SetLineColor(4)
MresEB_13.SetLineColor(4)
MresEB_8.SetLineWidth(1)
MresEB_13.SetLineWidth(1)
MresEB_8.Draw("same")
MresEB_13.Draw("same")
par[0]=float(MresEB_8.GetParameter(2))
par[1]=float(MresEB_13.GetParameter(2))
tMresEB = ROOT.TLatex(0.15, 0.8, '#splitline{8TeV: #sigma=%.3f }{#color[2]{13TeV: #sigma=%.3f} }' %tuple(par) )
tMresEB.SetNDC()
tMresEB.Draw()
c_mRes.Print('ABSDYTMRESsuperimposition_MRes.pdf')