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
###################################################################
f1tev_at8tev = ROOT.TFile('./files/zp2mu_dy1500_8.root')
d1tev_at8tev = f1tev_at8tev.ResolutionVertexUsingMC


###################################################################
f1tev_at13tev = ROOT.TFile('./files/zp2mu_dy1500_13.root')
d1tev_at13tev = f1tev_at13tev.ResolutionVertexUsingMC

#h1tev_at13tev_MassResVStrkprob = d1tev_at13tev.Get('DileptonMassResVSMuonPtProb')
h1tev_at13tev_MassResVStrkprob = d1tev_at13tev.Get('DileptonMassResVSMinMuonPtProb')

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

c_MresVSprob = ROOT.TCanvas( 'c_MresVSprob', '')
c_MresVSprob.SetGridy()
h1tev_at13tev_MassResVStrkprob.Rebin2D(100,1)
hMResVStrkprob_13tev=projectAndFit(h1tev_at13tev_MassResVStrkprob,'MResVStrkprob_13tev')
hMResVStrkprob_13tev.SetLineColor(8)
hMResVStrkprob_13tev.SetLineWidth(2)
hMResVStrkprob_13tev.SetMaximum(0.05)
hMResVStrkprob_13tev.SetMinimum(0.02)
hMResVStrkprob_13tev.GetXaxis().SetTitle("min track_{#mu} prob.")
hMResVStrkprob_13tev.GetYaxis().SetTitle("relative mass resolution")
hMResVStrkprob_13tev.GetYaxis().SetTitleOffset(1.5);
hMResVStrkprob_13tev.Draw()
c_MresVSprob.Print('ABSDYRES_MresVSprob_min.pdf')
                           
c_chiVSprob = ROOT.TCanvas( 'c_chiVSprob', '')
c_chiVSprob.SetGridy()
vtxChi2VSMuonPtProb.Rebin2D(100,1)
hchiVStrkprob_13tev=projectAndMean(vtxChi2VSMuonPtProb,'chiVStrkprob_13tev')
hchiVStrkprob_13tev.SetLineColor(8)
hchiVStrkprob_13tev.SetLineWidth(2)
hchiVStrkprob_13tev.SetMaximum(2.0)
hchiVStrkprob_13tev.SetMinimum(0.0)
hchiVStrkprob_13tev.GetXaxis().SetTitle("min track_{#mu} prob.")
hchiVStrkprob_13tev.GetYaxis().SetTitle("<#chi^{2}/dof>")
hchiVStrkprob_13tev.GetYaxis().SetTitleOffset(1.5);
hchiVStrkprob_13tev.Draw()
c_chiVSprob.Print('ABSDYRES_chiVSprob_min.pdf')

c_InvPtresVSprob = ROOT.TCanvas( 'c_InvPtresVSprob', '')
c_InvPtresVSprob.SetGridy()
h1tev_at13tev_InvPtResVStrkprob.Rebin2D(100,1)
hInvPtResVStrkprob_13tev=projectAndFit(h1tev_at13tev_InvPtResVStrkprob,'InvPtResVStrkprob_13tev')
hInvPtResVStrkprob_13tev.SetLineColor(8)
hInvPtResVStrkprob_13tev.SetLineWidth(2)
hInvPtResVStrkprob_13tev.SetMaximum(0.07)
hInvPtResVStrkprob_13tev.SetMinimum(0.03)
hInvPtResVStrkprob_13tev.GetXaxis().SetTitle("min track_{#mu} prob.")
hInvPtResVStrkprob_13tev.GetYaxis().SetTitle("Inv. pt resolution")
hInvPtResVStrkprob_13tev.GetYaxis().SetTitleOffset(1.5);
hInvPtResVStrkprob_13tev.Draw()
c_InvPtresVSprob.Print('ABSDYRES_InvPtresVSprob.pdf')

c_genDxy = ROOT.TCanvas( 'c_genDxy', '')
c_genDxy.SetGridy()
h1tev_at13tev_LeptonGenDxy2VSvtxChi2.Rebin2D(5,1)
#h1tev_at13tev_LeptonGenDxy2VSvtxChi2.Draw("colz")
genDxy=h1tev_at13tev_LeptonGenDxy2VSvtxChi2.ProjectionY("genDxy",0,61)
genDxy.SetLineColor(8)
genDxy.SetLineWidth(2)
genDxy.GetXaxis().SetTitle("#Delta(vx_{#mu_gen1},vx_{#mu_gen2})^{2}+#Delta(vy_{#mu_gen1},vy_{#mu_gen2})^{2}")
genDxy.GetYaxis().SetTitle("N")
genDxy.GetYaxis().SetTitleOffset(1.5);
genDxy.Draw("histo")
c_genDxy.Print('ABSDYRES_genDxy.pdf')
#
c_genDz = ROOT.TCanvas( 'c_genDz', '')
c_genDz.SetGridy()
h1tev_at13tev_LeptonGenDz2VSvtxChi2.Rebin2D(5,1)
genDz=h1tev_at13tev_LeptonGenDz2VSvtxChi2.ProjectionY("genDz",0,61)
genDz.SetLineColor(8)
genDz.SetLineWidth(2)
genDz.GetXaxis().SetTitle("#Delta(vz_{#mu_gen1},vz_{#mu_gen2})^{2}")
genDz.GetYaxis().SetTitle("N")
genDz.GetYaxis().SetTitleOffset(1.5);
genDz.Draw("histo")
c_genDz.Print('ABSDYRES_genDz.pdf')
