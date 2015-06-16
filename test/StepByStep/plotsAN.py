#!/usr/bin/env python

# (py resfromdy.py >! plots/out.resfromdy) && tlp plots/*resfromdy

import os
import ROOT
import math
from array import array
from ROOT import *
#from SUSYBSMAnalysis.Zprime2muAnalysis.roottools import *
#set_zp2mu_style()
#ROOT.gStyle.SetOptFit(11)
#gStyle.SetOptStat("eMRuo")
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
            func = TF1("func_%.d" %i,"gaus", -0.1, 0.1)
            proj.Fit("func_%.d" %i, 'R')
            h2.SetBinContent(i,func.GetParameter(2))
            h2.SetBinError(i,func.GetParError(2))
    return h2

def projectAndMean(Histo2D, postFix = "none"):
    nx    = Histo2D.GetNbinsX()
    print nx
    htmp= Histo2D.ProfileX()
    print htmp.GetNbinsX()
    x1    = htmp.GetBinLowEdge(1)
    bw    = htmp.GetBinWidth(nx)
    x2    = htmp.GetBinLowEdge(nx)+bw
    h2 = ROOT.TH1D((postFix + "Mean"),(postFix + "Mean"),nx, x1, x2)
    for i in xrange(1, Histo2D.GetNbinsX()+1):
        proj = Histo2D.ProjectionY("proj_%.d" %i,i,i)
        if proj.GetEntries() != 0:
            print "%.d orario" %i
            h2.SetBinContent(i,proj.GetMean())
            h2.SetBinError(i,proj.GetMeanError())
    return h2

def projectAndFitCumulative_m(Histo2D, postFix = "none"):
    nx    = Histo2D.GetNbinsX()
    print nx
    htmp= Histo2D.ProfileX()
    print htmp.GetNbinsX()
    x1    = htmp.GetBinLowEdge(1)
    bw    = htmp.GetBinWidth(nx)
    x2    = htmp.GetBinLowEdge(nx)+bw
    h2 = ROOT.TH1D((postFix + "Sigma"),(postFix + "Sigma"),nx, x1, x2)
    for i in xrange(1, Histo2D.GetNbinsX()+1):
        proj = Histo2D.ProjectionY("proj_%.d" %i,1,i)
        if proj.GetEntries() != 0:
            print "%.d cumulativo < cut" %i
            func = TF1("func_%.d" %i,"gaus", -0.1, 0.1)
            proj.Fit("func_%.d" %i, 'R')
            h2.SetBinContent(i,func.GetParameter(2))
            h2.SetBinError(i,func.GetParError(2))
    return h2

def projectAndFitCumulative_M(Histo2D, postFix = "none"):
    nx    = Histo2D.GetNbinsX()
    print nx
    htmp= Histo2D.ProfileX()
    print htmp.GetNbinsX()
    x1    = htmp.GetBinLowEdge(1)
    bw    = htmp.GetBinWidth(nx)
    x2    = htmp.GetBinLowEdge(nx)+bw
    h2 = ROOT.TH1D((postFix + "Sigma"),(postFix + "Sigma"),nx, x1, x2)
    for i in xrange(1, Histo2D.GetNbinsX()+1):
        proj = Histo2D.ProjectionY("proj_%.d" %i,i,nx+1)
        if proj.GetEntries() != 0:
            print "%.d cumulativo < cut" %i
            func = TF1("func_%.d" %i,"gaus", -0.1, 0.1)
            proj.Fit("func_%.d" %i, 'R')
            h2.SetBinContent(i,func.GetParameter(2))
            h2.SetBinError(i,func.GetParError(2))
    return h2

def projectAndMeanCumulative_M(Histo2D, postFix = "none"):
    nx    = Histo2D.GetNbinsX()
    print nx
    htmp= Histo2D.ProfileX()
    print htmp.GetNbinsX()
    x1    = htmp.GetBinLowEdge(1)
    bw    = htmp.GetBinWidth(nx)
    x2    = htmp.GetBinLowEdge(nx)+bw
    h2 = ROOT.TH1D((postFix + "Mean"),(postFix + "Mean"),nx, x1, x2)
    for i in xrange(1, Histo2D.GetNbinsX()+1):
        proj = Histo2D.ProjectionY("proj_%.d" %i,i,nx+1)
        if proj.GetEntries() != 0:
            print "%.d cumulativo < cut" %i
            h2.SetBinContent(i,proj.GetMean())
            h2.SetBinError(i,proj.GetMeanError())
    return h2

def projectAndRMSCumulative_M(Histo2D, postFix = "none"):
    nx    = Histo2D.GetNbinsX()
    print nx
    htmp= Histo2D.ProfileX()
    print htmp.GetNbinsX()
    x1    = htmp.GetBinLowEdge(1)
    bw    = htmp.GetBinWidth(nx)
    x2    = htmp.GetBinLowEdge(nx)+bw
    h2 = ROOT.TH1D((postFix + "RMS"),(postFix + "RMS"),nx, x1, x2)
    for i in xrange(1, Histo2D.GetNbinsX()+1):
        proj = Histo2D.ProjectionY("proj_%.d" %i,i,nx+1)
        if proj.GetEntries() != 0:
            print "%.d cumulativo > cut" %i
            h2.SetBinContent(i,proj.GetRMS())
            h2.SetBinError(i,proj.GetRMSError())
    return h2

def projectAndRMSCumulative_m(Histo2D, postFix = "none"):
    nx    = Histo2D.GetNbinsX()
    print nx
    htmp= Histo2D.ProfileX()
    print htmp.GetNbinsX()
    x1    = htmp.GetBinLowEdge(1)
    bw    = htmp.GetBinWidth(nx)
    x2    = htmp.GetBinLowEdge(nx)+bw
    h2 = ROOT.TH1D((postFix + "RMS"),(postFix + "RMS"),nx, x1, x2)
    for i in xrange(1, Histo2D.GetNbinsX()+1):
        proj = Histo2D.ProjectionY("proj_%.d" %i,0,i)
        if proj.GetEntries() != 0:
            print "%.d cumulativo < cut" %i
            h2.SetBinContent(i,proj.GetRMS())
            h2.SetBinError(i,proj.GetRMSError())
    return h2

def PaintOverflow(h, opt=''):
    #This function paint the histogram h with an extra bin for overflows
    name  = h.GetName()
    print name
    title = h.GetTitle()
    nx    = h.GetNbinsX()+1
    x1    = h.GetBinLowEdge(1)
    bw    = h.GetBinWidth(nx)
    x2    = h.GetBinLowEdge(nx)+bw
    print nx, x1, bw, x2
    htmp  = ROOT.TH1F(name, title, nx, x1, x2)
    for i in xrange(1, nx+1):
        htmp.Fill(htmp.GetBinCenter(i), h.GetBinContent(i))
    #print h.GetBinContent(i)
    htmp.Fill(x1-1, h.GetBinContent(0))
    htmp.SetEntries(h.GetEntries())
    return htmp

def Eff(h, opt=''):
    #This function paint the histogram h with an extra bin for overflows
    name  = h.GetName()
    print name
    title = h.GetTitle()
    nx    = h.GetNbinsX()
    x1    = h.GetBinLowEdge(1)
    bw    = h.GetBinWidth(nx)
    x2    = h.GetBinLowEdge(nx)+bw
    print nx, x1, bw, x2
    htmp_n  = ROOT.TH1F(name + "_num", title, nx+1, x1, x2+bw)
    htmp_d  = ROOT.TH1F(name + "_den", title, nx+1, x1, x2+bw)
    print htmp_n.GetName(), htmp_d.GetName(), htmp_n.GetNbinsX(), htmp_n.GetBinLowEdge(1), htmp_n.GetBinWidth(htmp_n.GetNbinsX())
    for i in xrange(1, nx+2):
        print "bin ", i, " chi< ",i*bw, "bin content: ", int(h.Integral(0,i)), "total: ",int(h.Integral(0,nx+1)), "eff: ", h.Integral(0,i)/h.Integral(0,nx+1)
        for n in xrange(1, int(h.Integral(0,i))+1):
            htmp_n.Fill(i*bw-bw)
        print htmp_n.GetBinContent(i)
        for d in xrange(1, int(h.Integral(0,nx+1))+1):
            htmp_d.Fill(i*bw-bw)
        print htmp_d.GetBinContent(i)
        
    htmp_n.Sumw2()
    htmp_d.Sumw2()
    if(ROOT.TEfficiency.CheckConsistency(htmp_n,htmp_d)):
        htmp = ROOT.TEfficiency(htmp_n,htmp_d)
    #print h.GetBinContent(i)
    return htmp
####################################################################
f1tev_at8tev = ROOT.TFile('/afs/cern.ch/work/r/rradogna/ZPrime/CMSSW_7_2_0/src/SUSYBSMAnalysis/Zprime2muAnalysis/test/StepByStep/files/zp2mu_dy1500_8.root')
d1tev_at8tev = f1tev_at8tev.ResolutionVertexUsingMC

###################################################################
#f1tev_at13tev = ROOT.TFile('./files/zp2mu_dy1500_13.root')
f1tev_at13tev = ROOT.TFile('/afs/cern.ch/work/r/rradogna/ZPrime/CMSSW_7_2_0/src/SUSYBSMAnalysis/Zprime2muAnalysis/test/StepByStep/crab/crab_ana_datamc_dy200/res/zp2mu_dy1500_13.root')
d1tev_at13tev = f1tev_at13tev.ResolutionVertexUsingMC

#f120_at13tev = ROOT.TFile('./files/zp2mu_dy120_13.root')
f120_at13tev = ROOT.TFile('/afs/cern.ch/work/r/rradogna/ZPrime/CMSSW_7_2_0/src/SUSYBSMAnalysis/Zprime2muAnalysis/test/StepByStep/crab/crab_ana_datamc_dy120/res/zp2mu_dy120_13.root')
d120_at13tev = f120_at13tev.ResolutionVertexUsingMC

#h1tev_at13tev_MassResVStrkprob = d1tev_at13tev.Get('DileptonMassResVSMuonPtProb')
h1tev_at13tev_MassResVStrkprob = d1tev_at13tev.Get('DileptonMassResVSMinMuonPtProb')
h120_at13tev_MassResVStrkprob = d120_at13tev.Get('DileptonMassResVSMinMuonPtProb')

#vtxChi2VSMuonPtProb = d1tev_at13tev.Get('vtxChi2VSMuonPtProb')
vtxChi2VSMuonPtProb = d1tev_at13tev.Get('vtxChi2VSMinMuonPtProb')

h1tev_at13tev_InvPtResVStrkprob = d1tev_at13tev.Get('LeptonInvPtResVSMuonPtProb')
                           
h1tev_at13tev_LeptonGenDxy2VSvtxChi2 = d1tev_at13tev.Get('LeptonGenDxy2VSvtxChi2')
h1tev_at13tev_LeptonGenDz2VSvtxChi2 = d1tev_at13tev.Get('LeptonGenDz2VSvtxChi2')

###############
nGen_8tev=99992.
nGen_13tev=13206.
print "nGen_8tev", nGen_8tev
print "nGen_13tev", nGen_13tev
###############

par=[0,0]
parPull=[0,0,0,0]

#c_MresVSprob = ROOT.TCanvas( 'c_MresVSprob', '')
#c_MresVSprob.SetGridy()
#h1tev_at13tev_MassResVStrkprob.Rebin2D(100,1)
#hMResVStrkprob_13tev=projectAndFit(h1tev_at13tev_MassResVStrkprob,'MResVStrkprob_13tev')
#hMResVStrkprob_13tev.SetLineColor(1)
#hMResVStrkprob_13tev.SetMarkerColor(2)
#hMResVStrkprob_13tev.SetMarkerStyle(22)
##hMResVStrkprob_13tev.SetLineWidth(2)
#hMResVStrkprob_13tev.SetMaximum(0.05)
#hMResVStrkprob_13tev.SetMinimum(0.02)
#hMResVStrkprob_13tev.GetXaxis().SetTitle("min track_{#mu} prob.")
#hMResVStrkprob_13tev.GetYaxis().SetTitle("relative mass resolution")
#hMResVStrkprob_13tev.GetYaxis().SetTitleOffset(1.5);
#hMResVStrkprob_13tev.Draw()
#c_MresVSprob.Print('ABSDYRES_MresVSprob_min.pdf')

c_chiVSprob = ROOT.TCanvas( 'c_chiVSprob', '')
c_chiVSprob.SetGridy()
vtxChi2VSMuonPtProb.Rebin2D(100,1)
hchiVStrkprob_13tev=projectAndMean(vtxChi2VSMuonPtProb,'chiVStrkprob_13tev')
hchiVStrkprob_13tev.SetLineColor(1)
hchiVStrkprob_13tev.SetMarkerColor(1)
hchiVStrkprob_13tev.SetFillColor(2)
hchiVStrkprob_13tev.SetFillStyle(3002)
hchiVStrkprob_13tev.SetMarkerStyle(22)
hchiVStrkprob_13tev.SetMaximum(2.0)
hchiVStrkprob_13tev.SetMinimum(0.0)
hchiVStrkprob_13tev.SetTitle(" ")
hchiVStrkprob_13tev.GetXaxis().SetTitle("min #mu_{track} prob.")
hchiVStrkprob_13tev.GetYaxis().SetTitle("vertex <#chi^{2}/dof>")
hchiVStrkprob_13tev.GetYaxis().SetTitleOffset(1.5);
hchiVStrkprob_13tev.Draw("E2")
hchiVStrkprob_13tev.Draw("same")

leg = ROOT.TLegend( 0.55, 0.15, 0.9, 0.4 )
leg.SetFillColor(kWhite)
#leg.SetLineColor(kWhite)
leg.SetTextSize(0.03)
leg.AddEntry(hchiVStrkprob_13tev, " DY 1.5TeV @ 13TeV", "Fep")
leg.Draw('same')

c_chiVSprob.Print('AN_ABSDYRES_chiVSprob_min.pdf')

#####################
h1tev_at13tev_MassResVSvtxChi2 = d1tev_at13tev.Get('DileptonMassVtxResVSvtxChi2')
h1tev_at8tev_MassResVSvtxChi2 = d1tev_at8tev.Get('DileptonMassResVSvtxChi2')
h120_at13tev_MassResVSvtxChi2 = d120_at13tev.Get('DileptonMassVtxResVSvtxChi2')
h1tev_at13tev_MassResVSvtxChi2.Rebin2D(10,1)
h1tev_at8tev_MassResVSvtxChi2.Rebin2D(10,1)
h120_at13tev_MassResVSvtxChi2.Rebin2D(10,1)

c_chi = ROOT.TCanvas( 'c_chi', '')
c_chi.SetLogy()

h1tev_at13tev_Chi2= h1tev_at13tev_MassResVSvtxChi2.ProjectionX("h1tev_at13tev_Chi2",0,101)
h1tev_at8tev_Chi2= h1tev_at8tev_MassResVSvtxChi2.ProjectionX("h1tev_at8tev_Chi2",0,101)
h1tev_at8tev_Chi2_overf = PaintOverflow(h1tev_at8tev_Chi2)
h1tev_at13tev_Chi2_overf = PaintOverflow(h1tev_at13tev_Chi2)
h1tev_at8tev_Chi2_overf.Scale(1/nGen_8tev)
h1tev_at13tev_Chi2_overf.Scale(1/nGen_13tev)
h1tev_at13tev_Chi2_overf.SetTitle(" ")
h1tev_at13tev_Chi2_overf.SetLineColor(2)
h1tev_at13tev_Chi2_overf.SetLineWidth(2)
h1tev_at8tev_Chi2_overf.SetLineColor(1)
h1tev_at8tev_Chi2_overf.SetLineWidth(2)
h1tev_at8tev_Chi2_overf.Draw()
h1tev_at13tev_Chi2_overf.Draw('same')

leg = ROOT.TLegend( 0.55, 0.75, 0.9, 0.9 )
leg.SetFillColor(kWhite)
#leg.SetLineColor(kWhite)
#leg.SetTextSize(0.03)
leg.AddEntry(h1tev_at8tev_Chi2_overf, " DY 1.5TeV @ 8TeV", "L")
leg.AddEntry(h1tev_at13tev_Chi2_overf, " DY 1.5TeV @ 13TeV", "L")
leg.Draw('same')

c_chi.Print('AN_ABSDYRES_chi.pdf')

#c_chiCut = ROOT.TCanvas( 'c_chiCut', '')
#c_chiCut.SetGridy()
#heff_13=Eff(h1tev_at13tev_Chi2)
#heff_8=Eff(h1tev_at8tev_Chi2)
#heff_13.SetLineColor(2)
#heff_13.SetLineWidth(2)
#heff_8.SetLineColor(1)
#heff_8.SetLineWidth(2)
##heff_13.GetXaxis().SetTitle("#chi^{2}/dof #mu #mu vtx cut value")
##heff_13.GetYaxis().SetTitle("#chi^{2}/dof #mu #mu vtx cut N-1 efficiency")
#heff_13.SetTitle(" ; #chi^{2}/dof #mu#mu vtx cut value ; #chi^{2}/dof #mu#mu vtx cut N-1 efficiency");
#heff_13.Draw()
#heff_8.Draw('same')
#c_chiCut.Update()
#heff_13.GetPaintedGraph().GetYaxis().SetTitleOffset(1.5);
#
#leg = ROOT.TLegend( 0.55, 0.55, 0.9, 0.7 )
#leg.SetFillColor(kWhite)
#leg.SetLineColor(kBlack)
#leg.SetTextSize(0.03)
#leg.AddEntry(heff_8, " DY 1.5TeV @ 8TeV", "Lep")
#leg.AddEntry(heff_13, " DY 1.5TeV @ 13TeV", "Lep")
#leg.Draw('same')
#
#
#c_chiCut.Print('AN_ABSDYRES_chiCut.pdf')

c_MresVSchi = ROOT.TCanvas( 'c_MresVSchi', '')
c_MresVSchi.SetGridy()
hMResVSvtxChi2_13tevMRMS=projectAndRMSCumulative_M(h1tev_at13tev_MassResVSvtxChi2,'MResVSvtxChi2_13tevMRMS')
hMResVSvtxChi2_8tevMRMS=projectAndRMSCumulative_M(h120_at13tev_MassResVSvtxChi2, 'MResVSvtxChi2_8tevMRMS')
#hMResVSvtxChi2_13tevMRMS.SetLineColor(2)
#hMResVSvtxChi2_13tevMRMS.SetLineWidth(2)
#hMResVSvtxChi2_8tevMRMS.SetLineColor(4)
#hMResVSvtxChi2_8tevMRMS.SetLineWidth(2)
hMResVSvtxChi2_8tevMRMS.SetLineColor(1)
hMResVSvtxChi2_8tevMRMS.SetMarkerColor(1)
hMResVSvtxChi2_8tevMRMS.SetFillColor(4)
hMResVSvtxChi2_8tevMRMS.SetFillStyle(3013)
hMResVSvtxChi2_8tevMRMS.SetMarkerStyle(23)

hMResVSvtxChi2_13tevMRMS.SetLineColor(1)
hMResVSvtxChi2_13tevMRMS.SetMarkerColor(1)
hMResVSvtxChi2_13tevMRMS.SetFillColor(2)
hMResVSvtxChi2_13tevMRMS.SetFillStyle(3002)
hMResVSvtxChi2_13tevMRMS.SetMarkerStyle(22)
#hchiVStrkprob_13tev.SetMaximum(2.0)
#hchiVStrkprob_13tev.SetMinimum(0.0)

hMResVSvtxChi2_13tevMRMS.GetXaxis().SetRangeUser(0,25)
hMResVSvtxChi2_8tevMRMS.GetXaxis().SetRangeUser(0,25)
hMResVSvtxChi2_13tevMRMS.GetXaxis().SetTitle("#chi^{2}/dof #mu#mu vtx cut value")
hMResVSvtxChi2_13tevMRMS.GetYaxis().SetTitle("Relative Mass Resolution RMS (#chi^{2}/dof #mu#mu vtx >cut)")
hMResVSvtxChi2_13tevMRMS.SetTitle(" ")
hMResVSvtxChi2_13tevMRMS.GetYaxis().SetTitleOffset(1.5)
hMResVSvtxChi2_13tevMRMS.SetMinimum(0.0)
hMResVSvtxChi2_13tevMRMS.Draw("E2")
hMResVSvtxChi2_13tevMRMS.Draw("same")
hMResVSvtxChi2_8tevMRMS.Draw('same E2')
hMResVSvtxChi2_8tevMRMS.Draw("same")

leg = ROOT.TLegend( 0.75, 0.15, 0.9, 0.4 )
leg.SetFillColor(kWhite)
#leg.SetLineColor(kWhite)
leg.SetTextSize(0.03)
leg.AddEntry(hMResVSvtxChi2_8tevMRMS, " DY 120 GeV", "fep")
leg.AddEntry(hMResVSvtxChi2_13tevMRMS, " DY 1.5 TeV", "fep")
leg.Draw('same')

c_MresVSchi.Print('AN_ABSDYRES_MresRMSVSchi_M.pdf')
####################################################
c_MresVSchi = ROOT.TCanvas( 'c_MresVSchi', '')
c_MresVSchi.SetGridy()
hMResVSvtxChi2_13tevMRMS=projectAndRMSCumulative_m(h1tev_at13tev_MassResVSvtxChi2,'MResVSvtxChi2_13tevMRMS')
hMResVSvtxChi2_8tevMRMS=projectAndRMSCumulative_m(h120_at13tev_MassResVSvtxChi2, 'MResVSvtxChi2_8tevMRMS')
#hMResVSvtxChi2_13tevMRMS.SetLineColor(2)
#hMResVSvtxChi2_13tevMRMS.SetLineWidth(2)
#hMResVSvtxChi2_8tevMRMS.SetLineColor(4)
#hMResVSvtxChi2_8tevMRMS.SetLineWidth(2)
hMResVSvtxChi2_8tevMRMS.SetLineColor(1)
hMResVSvtxChi2_8tevMRMS.SetMarkerColor(1)
hMResVSvtxChi2_8tevMRMS.SetFillColor(4)
hMResVSvtxChi2_8tevMRMS.SetFillStyle(3013)
hMResVSvtxChi2_8tevMRMS.SetMarkerStyle(23)

hMResVSvtxChi2_13tevMRMS.SetLineColor(1)
hMResVSvtxChi2_13tevMRMS.SetMarkerColor(1)
hMResVSvtxChi2_13tevMRMS.SetFillColor(2)
hMResVSvtxChi2_13tevMRMS.SetFillStyle(3002)
hMResVSvtxChi2_13tevMRMS.SetMarkerStyle(22)
#hchiVStrkprob_13tev.SetMaximum(2.0)
#hchiVStrkprob_13tev.SetMinimum(0.0)

hMResVSvtxChi2_13tevMRMS.GetXaxis().SetRangeUser(0,25)
hMResVSvtxChi2_8tevMRMS.GetXaxis().SetRangeUser(0,25)
hMResVSvtxChi2_13tevMRMS.GetXaxis().SetTitle("#chi^{2}/dof #mu#mu vtx cut value")
hMResVSvtxChi2_13tevMRMS.GetYaxis().SetTitle("Relative Mass Resolution RMS (#chi^{2}/dof #mu#mu vtx <cut)")
hMResVSvtxChi2_13tevMRMS.SetTitle(" ")
hMResVSvtxChi2_13tevMRMS.GetYaxis().SetTitleOffset(1.5)
hMResVSvtxChi2_13tevMRMS.SetMinimum(0.0)
hMResVSvtxChi2_13tevMRMS.Draw("E2")
hMResVSvtxChi2_13tevMRMS.Draw("same")
hMResVSvtxChi2_8tevMRMS.Draw('same E2')
hMResVSvtxChi2_8tevMRMS.Draw("same")

leg = ROOT.TLegend( 0.75, 0.15, 0.9, 0.4 )
leg.SetFillColor(kWhite)
#leg.SetLineColor(kWhite)
leg.SetTextSize(0.03)
leg.AddEntry(hMResVSvtxChi2_8tevMRMS, " DY 120 GeV", "fep")
leg.AddEntry(hMResVSvtxChi2_13tevMRMS, " DY 1.5 TeV", "fep")
leg.Draw('same')

c_MresVSchi.Print('AN_ABSDYRES_MresRMSVSchi_m.pdf')



###########################
c_MresVSchi = ROOT.TCanvas( 'c_MresVSchi', '')
c_MresVSchi.SetGridy()
hMResVSvtxChi2_13tevMRMS=projectAndFitCumulative_M(h1tev_at13tev_MassResVSvtxChi2,'MResVSvtxChi2_13tevMRMS')
hMResVSvtxChi2_8tevMRMS=projectAndFitCumulative_M(h120_at13tev_MassResVSvtxChi2, 'MResVSvtxChi2_8tevMRMS')
#hMResVSvtxChi2_13tevMRMS.SetLineColor(2)
#hMResVSvtxChi2_13tevMRMS.SetLineWidth(2)
#hMResVSvtxChi2_8tevMRMS.SetLineColor(4)
#hMResVSvtxChi2_8tevMRMS.SetLineWidth(2)
hMResVSvtxChi2_8tevMRMS.SetLineColor(1)
hMResVSvtxChi2_8tevMRMS.SetMarkerColor(1)
hMResVSvtxChi2_8tevMRMS.SetFillColor(4)
hMResVSvtxChi2_8tevMRMS.SetFillStyle(3013)
hMResVSvtxChi2_8tevMRMS.SetMarkerStyle(23)

hMResVSvtxChi2_13tevMRMS.SetLineColor(1)
hMResVSvtxChi2_13tevMRMS.SetMarkerColor(1)
hMResVSvtxChi2_13tevMRMS.SetFillColor(2)
hMResVSvtxChi2_13tevMRMS.SetFillStyle(3002)
hMResVSvtxChi2_13tevMRMS.SetMarkerStyle(22)
#hchiVStrkprob_13tev.SetMaximum(2.0)
#hchiVStrkprob_13tev.SetMinimum(0.0)

hMResVSvtxChi2_13tevMRMS.GetXaxis().SetRangeUser(0,25)
hMResVSvtxChi2_8tevMRMS.GetXaxis().SetRangeUser(0,25)
hMResVSvtxChi2_13tevMRMS.GetXaxis().SetTitle("#chi^{2}/dof #mu#mu vtx cut value")
hMResVSvtxChi2_13tevMRMS.GetYaxis().SetTitle("Relative Mass Resolution (#chi^{2}/dof #mu#mu vtx >cut)")
hMResVSvtxChi2_13tevMRMS.SetTitle(" ")
hMResVSvtxChi2_13tevMRMS.GetYaxis().SetTitleOffset(1.5)
hMResVSvtxChi2_13tevMRMS.SetMinimum(-0.05)
hMResVSvtxChi2_13tevMRMS.Draw("E2")
hMResVSvtxChi2_13tevMRMS.Draw("same")
hMResVSvtxChi2_8tevMRMS.Draw('same E2')
hMResVSvtxChi2_8tevMRMS.Draw("same")

leg = ROOT.TLegend( 0.65, 0.75, 0.8, 0.9 )
leg.SetFillColor(kWhite)
#leg.SetLineColor(kWhite)
leg.SetTextSize(0.03)
leg.AddEntry(hMResVSvtxChi2_8tevMRMS, " DY 120 GeV", "fep")
leg.AddEntry(hMResVSvtxChi2_13tevMRMS, " DY 1.5 TeV", "fep")
leg.Draw('same')

c_MresVSchi.Print('AN_ABSDYRES_MresSigmaVSchi_M.pdf')
####################################################
c_MresVSchi = ROOT.TCanvas( 'c_MresVSchi', '')
c_MresVSchi.SetGridy()
hMResVSvtxChi2_13tevMRMS=projectAndFitCumulative_m(h1tev_at13tev_MassResVSvtxChi2,'MResVSvtxChi2_13tevMRMS')
hMResVSvtxChi2_8tevMRMS=projectAndFitCumulative_m(h120_at13tev_MassResVSvtxChi2, 'MResVSvtxChi2_8tevMRMS')
#hMResVSvtxChi2_13tevMRMS.SetLineColor(2)
#hMResVSvtxChi2_13tevMRMS.SetLineWidth(2)
#hMResVSvtxChi2_8tevMRMS.SetLineColor(4)
#hMResVSvtxChi2_8tevMRMS.SetLineWidth(2)
hMResVSvtxChi2_8tevMRMS.SetLineColor(1)
hMResVSvtxChi2_8tevMRMS.SetMarkerColor(1)
hMResVSvtxChi2_8tevMRMS.SetFillColor(4)
hMResVSvtxChi2_8tevMRMS.SetFillStyle(3013)
hMResVSvtxChi2_8tevMRMS.SetMarkerStyle(23)

hMResVSvtxChi2_13tevMRMS.SetLineColor(1)
hMResVSvtxChi2_13tevMRMS.SetMarkerColor(1)
hMResVSvtxChi2_13tevMRMS.SetFillColor(2)
hMResVSvtxChi2_13tevMRMS.SetFillStyle(3002)
hMResVSvtxChi2_13tevMRMS.SetMarkerStyle(22)
#hchiVStrkprob_13tev.SetMaximum(2.0)
#hchiVStrkprob_13tev.SetMinimum(0.0)

hMResVSvtxChi2_13tevMRMS.GetXaxis().SetRangeUser(0,25)
hMResVSvtxChi2_8tevMRMS.GetXaxis().SetRangeUser(0,25)
hMResVSvtxChi2_13tevMRMS.GetXaxis().SetTitle("#chi^{2}/dof #mu#mu vtx cut value")
hMResVSvtxChi2_13tevMRMS.GetYaxis().SetTitle("Relative Mass Resolution (#chi^{2}/dof #mu#mu vtx <cut)")
hMResVSvtxChi2_13tevMRMS.SetTitle(" ")
hMResVSvtxChi2_13tevMRMS.GetYaxis().SetTitleOffset(1.5)
hMResVSvtxChi2_13tevMRMS.SetMinimum(0)
hMResVSvtxChi2_13tevMRMS.Draw("E2")
hMResVSvtxChi2_13tevMRMS.Draw("same")
hMResVSvtxChi2_8tevMRMS.Draw('same E2')
hMResVSvtxChi2_8tevMRMS.Draw("same")

leg = ROOT.TLegend( 0.65, 0.75, 0.8, 0.9 )
leg.SetFillColor(kWhite)
#leg.SetLineColor(kWhite)
leg.SetTextSize(0.03)
leg.AddEntry(hMResVSvtxChi2_8tevMRMS, " DY 120 GeV", "fep")
leg.AddEntry(hMResVSvtxChi2_13tevMRMS, " DY 1.5 TeV", "fep")
leg.Draw('same')

c_MresVSchi.Print('AN_ABSDYRES_MresSigmaVSchi_m.pdf')


#######################################################

###########################
c_MresVSchi = ROOT.TCanvas( 'c_MresVSchi', '')
c_MresVSchi.SetGridy()
hMResVSvtxChi2_13tevMRMS=projectAndFitCumulative_M(h1tev_at13tev_MassResVSvtxChi2,'MResVSvtxChi2_13tevMRMS')
hMResVSvtxChi2_8tevMRMS=projectAndFitCumulative_M(h120_at13tev_MassResVSvtxChi2, 'MResVSvtxChi2_8tevMRMS')
#hMResVSvtxChi2_13tevMRMS.SetLineColor(2)
#hMResVSvtxChi2_13tevMRMS.SetLineWidth(2)
#hMResVSvtxChi2_8tevMRMS.SetLineColor(4)
#hMResVSvtxChi2_8tevMRMS.SetLineWidth(2)
hMResVSvtxChi2_8tevMRMS.SetLineColor(1)
hMResVSvtxChi2_8tevMRMS.SetMarkerColor(1)
hMResVSvtxChi2_8tevMRMS.SetFillColor(4)
hMResVSvtxChi2_8tevMRMS.SetFillStyle(3013)
hMResVSvtxChi2_8tevMRMS.SetMarkerStyle(23)

hMResVSvtxChi2_13tevMRMS.SetLineColor(1)
hMResVSvtxChi2_13tevMRMS.SetMarkerColor(1)
hMResVSvtxChi2_13tevMRMS.SetFillColor(2)
hMResVSvtxChi2_13tevMRMS.SetFillStyle(3002)
hMResVSvtxChi2_13tevMRMS.SetMarkerStyle(22)
#hchiVStrkprob_13tev.SetMaximum(2.0)
#hchiVStrkprob_13tev.SetMinimum(0.0)

hMResVSvtxChi2_13tevMRMS.GetXaxis().SetRangeUser(0,25)
hMResVSvtxChi2_8tevMRMS.GetXaxis().SetRangeUser(0,25)
hMResVSvtxChi2_13tevMRMS.GetXaxis().SetTitle("#chi^{2}/dof #mu#mu vtx cut value")
hMResVSvtxChi2_13tevMRMS.GetYaxis().SetTitle("Relative Mass Resolution (#chi^{2}/dof #mu#mu vtx >cut)")
hMResVSvtxChi2_13tevMRMS.SetTitle(" ")
hMResVSvtxChi2_13tevMRMS.GetYaxis().SetTitleOffset(1.5)
hMResVSvtxChi2_13tevMRMS.SetMinimum(-0.05)
hMResVSvtxChi2_13tevMRMS.Draw("E2")
hMResVSvtxChi2_13tevMRMS.Draw("same")
#hMResVSvtxChi2_8tevMRMS.Draw('same E2')
#hMResVSvtxChi2_8tevMRMS.Draw("same")

leg = ROOT.TLegend( 0.65, 0.75, 0.8, 0.9 )
leg.SetFillColor(kWhite)
#leg.SetLineColor(kWhite)
leg.SetTextSize(0.03)
#leg.AddEntry(hMResVSvtxChi2_8tevMRMS, " DY 120 GeV", "fep")
leg.AddEntry(hMResVSvtxChi2_13tevMRMS, " DY 1.5 TeV", "fep")
leg.Draw('same')

c_MresVSchi.Print('AN_ABSDYRES_MresSigmaVSchi_M1500.pdf')
####################################################
c_MresVSchi = ROOT.TCanvas( 'c_MresVSchi', '')
c_MresVSchi.SetGridy()
hMResVSvtxChi2_13tevMRMS=projectAndFitCumulative_m(h1tev_at13tev_MassResVSvtxChi2,'MResVSvtxChi2_13tevMRMS')
hMResVSvtxChi2_8tevMRMS=projectAndFitCumulative_m(h120_at13tev_MassResVSvtxChi2, 'MResVSvtxChi2_8tevMRMS')
#hMResVSvtxChi2_13tevMRMS.SetLineColor(2)
#hMResVSvtxChi2_13tevMRMS.SetLineWidth(2)
#hMResVSvtxChi2_8tevMRMS.SetLineColor(4)
#hMResVSvtxChi2_8tevMRMS.SetLineWidth(2)
hMResVSvtxChi2_8tevMRMS.SetLineColor(1)
hMResVSvtxChi2_8tevMRMS.SetMarkerColor(1)
hMResVSvtxChi2_8tevMRMS.SetFillColor(4)
hMResVSvtxChi2_8tevMRMS.SetFillStyle(3013)
hMResVSvtxChi2_8tevMRMS.SetMarkerStyle(23)

hMResVSvtxChi2_13tevMRMS.SetLineColor(1)
hMResVSvtxChi2_13tevMRMS.SetMarkerColor(1)
hMResVSvtxChi2_13tevMRMS.SetFillColor(2)
hMResVSvtxChi2_13tevMRMS.SetFillStyle(3002)
hMResVSvtxChi2_13tevMRMS.SetMarkerStyle(22)
#hchiVStrkprob_13tev.SetMaximum(2.0)
#hchiVStrkprob_13tev.SetMinimum(0.0)

hMResVSvtxChi2_13tevMRMS.GetXaxis().SetRangeUser(0,25)
hMResVSvtxChi2_8tevMRMS.GetXaxis().SetRangeUser(0,25)
hMResVSvtxChi2_13tevMRMS.GetXaxis().SetTitle("#chi^{2}/dof #mu#mu vtx cut value")
hMResVSvtxChi2_13tevMRMS.GetYaxis().SetTitle("Relative Mass Resolution (#chi^{2}/dof #mu#mu vtx <cut)")
hMResVSvtxChi2_13tevMRMS.SetTitle(" ")
hMResVSvtxChi2_13tevMRMS.GetYaxis().SetTitleOffset(1.5)
hMResVSvtxChi2_13tevMRMS.SetMinimum(0.04)
hMResVSvtxChi2_13tevMRMS.SetMaximum(0.05)
hMResVSvtxChi2_13tevMRMS.Draw("E2")
hMResVSvtxChi2_13tevMRMS.Draw("same")
#hMResVSvtxChi2_8tevMRMS.Draw('same E2')
#hMResVSvtxChi2_8tevMRMS.Draw("same")

leg = ROOT.TLegend( 0.65, 0.75, 0.8, 0.9 )
leg.SetFillColor(kWhite)
#leg.SetLineColor(kWhite)
leg.SetTextSize(0.03)
#leg.AddEntry(hMResVSvtxChi2_8tevMRMS, " DY 120 GeV", "fep")
leg.AddEntry(hMResVSvtxChi2_13tevMRMS, " DY 1.5 TeV", "fep")
leg.Draw('same')

c_MresVSchi.Print('AN_ABSDYRES_MresSigmaVSchi_m1500.pdf')