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

###ps = plot_saver('plots/resfromdy_new')
c = ROOT.TCanvas( 'c', '')
#c.Divide(1,2)

f5tev = ROOT.TFile('./nminus1_histos/ana_nminus1_zpsi5000.root')
d5tev = f5tev.NoVtxProb
h5tev = d5tev.Get('DimuonMassVertexConstrained')
h5tev_chi = d5tev.Get('DimuonMassVtx_chi2')
f1tev_at8tev = ROOT.TFile('./nminus1_histos/ana_nminus1_zpsi1000_8tev.root')
d1tev_at8tev = f1tev_at8tev.NoVtxProb
h1tev_at8tev = d1tev_at8tev.Get('DimuonMassVertexConstrained')
h1tev_at8tev_chi = d1tev_at8tev.Get('DimuonMassVtx_chi2')
f1tev_at13tev = ROOT.TFile('./nminus1_histos/ana_nminus1_zpsi1000.root')
d1tev_at13tev = f1tev_at13tev.NoVtxProb
h1tev_at13tev = d1tev_at13tev.Get('DimuonMassVertexConstrained')
#h1tev_at13tev_chi = d1tev_at13tev.Get('DimuonMassVtx_chi2')
#h5tev = fit_gaussian(h5tev,None,True)
#h5tev = fit_gaussian(h5tev,None,True)
#c.cd(1)
h5tev.Scale(1/h5tev.Integral())
h1tev_at8tev.Scale(1/h1tev_at8tev.Integral())
h1tev_at13tev.Scale(1/h1tev_at13tev.Integral())
h5tev.Rebin(10)
h1tev_at8tev.Rebin(10)
h1tev_at13tev.Rebin(10)

h5tev.SetLineColor(6)
h5tev.SetLineWidth(2)
h1tev_at8tev.SetLineColor(1)
h1tev_at8tev.SetLineWidth(2)
h1tev_at13tev.SetLineColor(3)
h1tev_at13tev.SetLineWidth(2)

h1tev_at8tev.GetYaxis().SetRangeUser(0, 0.085)
h1tev_at13tev.GetYaxis().SetRangeUser(0, 0.085)
h5tev.GetYaxis().SetRangeUser(0, 0.085)
h5tev.GetXaxis().SetRangeUser(0, 6200)
h1tev_at8tev.GetXaxis().SetRangeUser(0, 6000)
h1tev_at13tev.GetXaxis().SetRangeUser(0, 6000)
h5tev.Draw("HISTO")
h1tev_at8tev.Draw("same histo")
h1tev_at13tev.Draw("same histo")
                  #h5tev.Fit('gaus', '','',-0.1,0.1)
####################

#c.cd(2)
h5tev_chi.Scale(1/h5tev_chi.Integral())
h1tev_at8tev_chi.Scale(1/h1tev_at8tev_chi.Integral())
h5tev_chi.SetLineColor(6)
h5tev_chi.SetLineWidth(2)
h1tev_at8tev_chi.SetLineColor(1)
h1tev_at8tev_chi.SetLineWidth(2)
h5tev_chi.GetXaxis().SetRangeUser(0, 12)
h1tev_at8tev_chi.GetXaxis().SetRangeUser(0, 12)
h1tev_at8tev_chi.GetYaxis().SetRangeUser(0, 0.3)
h5tev_chi.GetYaxis().SetRangeUser(0, 0.3)
#h5tev_chi.Draw("HISTO")
#h1tev_at8tev_chi.Draw("same histo")

# Legend:
leg = ROOT.TLegend( 0.7, 0.70, 0.9, 0.9 )
leg.SetFillColor(kWhite)
leg.SetLineColor(kWhite)
leg.AddEntry(h1tev_at8tev, " Z' 1TeV @ 8TeV", "L")
leg.AddEntry(h1tev_at13tev, " Z' 1TeV @ 13TeV (cmssw 701)", "L")
leg.AddEntry(h5tev, " Z' 5TeV @ 13TeV (phys14)", "L")
leg.Draw()

c.Print('superimposition_zprime.pdf')
#
#c2 = ROOT.TCanvas( 'c2', '')
#c2.Divide(3,2)
#
#ff5tev = ROOT.TFile('./crab/crab_ana_effres_nomasswin_new_dy5tev/res/zp2mu_histos_5tev.root')
#dd5tev = ff5tev.Resolutiontunepnew
#hh5tev = ROOT.TH1F(dd5tev.Get('DileptonMassReco'))
##h5tev = fit_gaussian(h5tev,None,True)
#c2.cd(1)
#hh5tev.Rebin(10)
#hh5tev.GetXaxis().SetRangeUser(0, 500)
#hh5tev.Draw("HISTO")
##h5tev.Fit('gaus', '','',-0.1,0.1)
#####################
#ff1tev_at8tev = ROOT.TFile('./crab/crab_ana_effres_nomasswin_new_dy1tev_at8tev/res/zp2mu_histos_1tev_at8tev.root')
#dd1tev_at8tev = ff1tev_at8tev.Resolutiontunepnew
#hh1tev_at8tev = ROOT.TH1F(dd1tev_at8tev.Get('DileptonMassReco'))
##h5tev = fit_gaussian(h5tev,None,True)
#c2.cd(2)
#hh1tev_at8tev.Rebin(50)
#hh1tev_at8tev.GetXaxis().SetRangeUser(0, 4000)
#hh1tev_at8tev.Draw("HISTO")
##h1tev_at8tev.Fit('gaus', '','',-0.1,0.1)
#####################
#ff800 = ROOT.TFile('./crab/crab_ana_effres_nomasswin_new_dy800/res/zp2mu_histos_800.root')
#dd800 = ff800.Resolutiontunepnew
#hh800 = ROOT.TH1F(dd800.Get('DileptonMassReco'))
##h5tev = fit_gaussian(h5tev,None,True)
#c2.cd(3)
#hh800.Rebin(20)
#hh800.GetXaxis().SetRangeUser(0, 2500)
#hh800.Draw("HISTO")
##h800.Fit('gaus', '','',-0.1,0.1)
######################
#ff1tev_at8tev0 = ROOT.TFile('./crab/crab_ana_effres_nomasswin_new_dy1tev_at8tev0/res/zp2mu_histos_1tev_at8tev0.root')
#dd1tev_at8tev0 = ff1tev_at8tev0.Resolutiontunepnew
#hh1tev_at8tev0 = ROOT.TH1F(dd1tev_at8tev0.Get('DileptonMassReco'))
##h5tev = fit_gaussian(h5tev,None,True)
#c2.cd(4)
#hh1tev_at8tev0.Rebin(50)
#hh1tev_at8tev0.GetXaxis().SetRangeUser(0, 8000)
#hh1tev_at8tev0.Draw("HISTO")
##h1tev_at8tev0.Fit('gaus', '','',-0.1,0.1)
######################
##ff3000 = ROOT.TFile('./crab/crab_ana_effres_nomasswin_new_dy3000/res/zp2mu_histos_3000.root')
##dd3000 = ff3000.Resolutiontunepnew
##hh3000 = dd3000.Get('DileptonMassReco')
###hh3000 = fit_gaussian(h5tev,None,True)
##c2.cd(5)
##hh3000.Draw("HISTO")
###h3000.Fit('gaus', '','',-0.1,0.1)
######################
#ff4500 = ROOT.TFile('./crab/crab_ana_effres_nomasswin_new_dy4500/res/zp2mu_histos_4500.root')
#dd4500 = ff4500.Resolutiontunepnew
#hh4500 = ROOT.TH1F(dd4500.Get('DileptonMassReco'))
##h5tev = fit_gaussian(h5tev,None,True)
#c2.cd(5)
#hh4500.Rebin(50)
##hh4500.GetXaxis().SetRangeUser(0, 8000)
#hh4500.Draw("HISTO")
##h4500.Fit('gaus', '','',-0.1,0.1)
######################
#
#c2.Print('mass_reco.pdf')
#
#c3 = ROOT.TCanvas( 'c3', '')
#c3.Divide(3,2)
#
#ff5tev_gen = ROOT.TFile('./crab/crab_ana_effres_nomasswin_new_dy5tev/res/zp2mu_histos_5tev.root')
#dd5tev_gen = ff5tev_gen.Resolutiontunepnew
#hh5tev_gen = ROOT.TH1F(dd5tev_gen.Get('DileptonMassGen'))
##h5tev = fit_gaussian(h5tev,None,True)
#c3.cd(1)
#hh5tev_gen.Rebin(10)
#hh5tev_gen.GetXaxis().SetRangeUser(0, 500)
#hh5tev_gen.Draw("HISTO")
##h5tev.Fit('gaus', '','',-0.1,0.1)
#####################
#ff1tev_at8tev_gen = ROOT.TFile('./crab/crab_ana_effres_nomasswin_new_dy1tev_at8tev/res/zp2mu_histos_1tev_at8tev.root')
#dd1tev_at8tev_gen = ff1tev_at8tev_gen.Resolutiontunepnew
#hh1tev_at8tev_gen = ROOT.TH1F(dd1tev_at8tev_gen.Get('DileptonMassGen'))
##h5tev = fit_gaussian(h5tev,None,True)
#c3.cd(2)
#hh1tev_at8tev_gen.Rebin(50)
#hh1tev_at8tev_gen.GetXaxis().SetRangeUser(0, 4000)
#hh1tev_at8tev_gen.Draw("HISTO")
##h1tev_at8tev.Fit('gaus', '','',-0.1,0.1)
#####################
#ff800_gen = ROOT.TFile('./crab/crab_ana_effres_nomasswin_new_dy800/res/zp2mu_histos_800.root')
#dd800_gen = ff800_gen.Resolutiontunepnew
#hh800_gen = ROOT.TH1F(dd800_gen.Get('DileptonMassGen'))
##h5tev = fit_gaussian(h5tev,None,True)
#c3.cd(3)
#hh800_gen.Rebin(20)
#hh800_gen.GetXaxis().SetRangeUser(0, 2500)
#hh800_gen.Draw("HISTO")
##h800.Fit('gaus', '','',-0.1,0.1)
######################
#ff1tev_at8tev0_gen = ROOT.TFile('./crab/crab_ana_effres_nomasswin_new_dy1tev_at8tev0/res/zp2mu_histos_1tev_at8tev0.root')
#dd1tev_at8tev0_gen = ff1tev_at8tev0_gen.Resolutiontunepnew
#hh1tev_at8tev0_gen = ROOT.TH1F(dd1tev_at8tev0_gen.Get('DileptonMassGen'))
##h5tev = fit_gaussian(h5tev,None,True)
#c3.cd(4)
#hh1tev_at8tev0_gen.Rebin(50)
#hh1tev_at8tev0_gen.GetXaxis().SetRangeUser(0, 8000)
#hh1tev_at8tev0_gen.Draw("HISTO")
##h1tev_at8tev0.Fit('gaus', '','',-0.1,0.1)
######################
##ff3000 = ROOT.TFile('./crab/crab_ana_effres_nomasswin_new_dy3000/res/zp2mu_histos_3000.root')
##dd3000 = ff3000.Resolutiontunepnew
##hh3000 = dd3000.Get('DileptonMassReco')
###hh3000 = fit_gaussian(h5tev,None,True)
##c2.cd(5)
##hh3000.Draw("HISTO")
###h3000.Fit('gaus', '','',-0.1,0.1)
######################
#ff4500_gen = ROOT.TFile('./crab/crab_ana_effres_nomasswin_new_dy4500/res/zp2mu_histos_4500.root')
#dd4500_gen = ff4500_gen.Resolutiontunepnew
#hh4500_gen = ROOT.TH1F(dd4500_gen.Get('DileptonMassGen'))
##h5tev = fit_gaussian(h5tev,None,True)
#c3.cd(5)
#hh4500_gen.Rebin(50)
##hh4500.GetXaxis().SetRangeUser(0, 8000)
#hh4500_gen.Draw("HISTO")
##h4500.Fit('gaus', '','',-0.1,0.1)
######################
#
#c3.Print('mass_gen.pdf')

#c_res = ROOT.TCanvas( 'c_res', '')
#c_res.cd()
#n= 5
#
#x = array( 'f', [140, 250.0, 1580.0, 3640.0, 6030.0])
#y = array( 'f', [0.0154,0.02,0.0432,0.0535,0.07])
#ex = array( 'f', [0.0,0.0,0.0,0.0,0.0])
#ey = array( 'f', [0.00023,0.00024,0.0005,0.0008,0.00178])
##
#gr = ROOT.TGraphErrors(n,x,y,ex,ey);
#gr.SetLineStyle(0)
#gr.SetLineColor(1)
#gr.SetLineWidth(2)
#gr.SetMarkerColor(1)
#gr.SetMarkerStyle(20)
#gr.SetMarkerSize(0.875)
#gr.GetYaxis().SetRangeUser(0.01,0.1)
#gr.Draw("AP")
##line = ROOT.TF1("line", '[0]/(ROOT.pow(x+[1],[2]))')
#line = ROOT.TF1('line', '[0]/pow(x+[1],[2])',0.,8000.)
#line.SetParameter(0, 4.64567e-03)
#line.SetParameter(1, -1.75397e+02)
#line.SetParameter(2, -3.02480e-01)
##line.SetParameters(4.64567e-03,-1.75397e+02,-3.02480e-01)
#line.SetLineColor(2)
##gr.Fit(line, 'R')
##c_res.Update()
##line.Draw()
#
##fn1 = ROOT.TF1("fn1",FittingFunc1,220,5050.0,3);
##fn1.SetParameters(4.64567e-03,-1.75397e+02,-3.02480e-01);
##fn1.SetLineColor(2);
##gr.Fit("fn1","R");
#c_res.Print('resVSmass.pdf')


