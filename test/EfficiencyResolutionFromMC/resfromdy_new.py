#!/usr/bin/env python

# (py resfromdy.py >! plots/out.resfromdy) && tlp plots/*resfromdy

import os
import ROOT
import math
from array import array
#from SUSYBSMAnalysis.Zprime2muAnalysis.roottools import *
#set_zp2mu_style()
#ROOT.gStyle.SetOptFit(1111)
ROOT.gStyle.SetPadTopMargin(0.02)
ROOT.gStyle.SetPadRightMargin(0.02)

###ps = plot_saver('plots/resfromdy_new')
c = ROOT.TCanvas( 'c', '')
c.Divide(3,2)

f120 = ROOT.TFile('./crab/crab_ana_effres_nomasswin_new_dy120/res/zp2mu_histos_120.root')
d120 = f120.Resolutiontunepnew
h120 = d120.Get('DileptonMassRes')
#h120 = fit_gaussian(h120,None,True)
c.cd(1)
h120.Draw("HISTO")
h120.Fit('gaus', '','',-0.1,0.1)
####################
f200 = ROOT.TFile('./crab/crab_ana_effres_nomasswin_new_dy200/res/zp2mu_histos_200.root')
d200 = f200.Resolutiontunepnew
h200 = d200.Get('DileptonMassRes')
#h120 = fit_gaussian(h120,None,True)
c.cd(2)
h200.Draw("HISTO")
h200.Fit('gaus', '','',-0.1,0.1)
####################
f800 = ROOT.TFile('./crab/crab_ana_effres_nomasswin_new_dy800/res/zp2mu_histos_800.root')
d800 = f800.Resolutiontunepnew
h800 = d800.Get('DileptonMassRes')
#h120 = fit_gaussian(h120,None,True)
c.cd(3)
h800.Draw("HISTO")
h800.Fit('gaus', '','',-0.1,0.1)
#####################
f2000 = ROOT.TFile('./crab/crab_ana_effres_nomasswin_new_dy2000/res/zp2mu_histos_2000.root')
d2000 = f2000.Resolutiontunepnew
h2000 = d2000.Get('DileptonMassRes')
#h120 = fit_gaussian(h120,None,True)
c.cd(4)
h2000.Draw("HISTO")
h2000.Fit('gaus', '','',-0.1,0.1)
#####################
#f3000 = ROOT.TFile('./crab/crab_ana_effres_nomasswin_dy3000/res/zp2mu_histos_3000.root')
#d3000 = f3000.Resolutiontunepnew
#h3000 = d3000.Get('DileptonMassRes')
#h120 = fit_gaussian(h120,None,True)
#c.cd(5)
#h3000.Draw("HISTO")
#h3000.Fit('gaus', '','',-0.1,0.1)
#####################
f4500 = ROOT.TFile('./crab/crab_ana_effres_nomasswin_new_dy4500/res/zp2mu_histos_4500.root')
d4500 = f4500.Resolutiontunepnew
h4500 = d4500.Get('DileptonMassRes')
#h120 = fit_gaussian(h120,None,True)
c.cd(5)
h4500.Draw("HISTO")
h4500.Fit('gaus', '','',-0.1,0.1)
#####################

c.Print('res.pdf')
#
#c2 = ROOT.TCanvas( 'c2', '')
#c2.Divide(3,2)
#
#ff120 = ROOT.TFile('./crab/crab_ana_effres_nomasswin_new_dy120/res/zp2mu_histos_120.root')
#dd120 = ff120.Resolutiontunepnew
#hh120 = ROOT.TH1F(dd120.Get('DileptonMassReco'))
##h120 = fit_gaussian(h120,None,True)
#c2.cd(1)
#hh120.Rebin(10)
#hh120.GetXaxis().SetRangeUser(0, 500)
#hh120.Draw("HISTO")
##h120.Fit('gaus', '','',-0.1,0.1)
#####################
#ff200 = ROOT.TFile('./crab/crab_ana_effres_nomasswin_new_dy200/res/zp2mu_histos_200.root')
#dd200 = ff200.Resolutiontunepnew
#hh200 = ROOT.TH1F(dd200.Get('DileptonMassReco'))
##h120 = fit_gaussian(h120,None,True)
#c2.cd(2)
#hh200.Rebin(50)
#hh200.GetXaxis().SetRangeUser(0, 4000)
#hh200.Draw("HISTO")
##h200.Fit('gaus', '','',-0.1,0.1)
#####################
#ff800 = ROOT.TFile('./crab/crab_ana_effres_nomasswin_new_dy800/res/zp2mu_histos_800.root')
#dd800 = ff800.Resolutiontunepnew
#hh800 = ROOT.TH1F(dd800.Get('DileptonMassReco'))
##h120 = fit_gaussian(h120,None,True)
#c2.cd(3)
#hh800.Rebin(20)
#hh800.GetXaxis().SetRangeUser(0, 2500)
#hh800.Draw("HISTO")
##h800.Fit('gaus', '','',-0.1,0.1)
######################
#ff2000 = ROOT.TFile('./crab/crab_ana_effres_nomasswin_new_dy2000/res/zp2mu_histos_2000.root')
#dd2000 = ff2000.Resolutiontunepnew
#hh2000 = ROOT.TH1F(dd2000.Get('DileptonMassReco'))
##h120 = fit_gaussian(h120,None,True)
#c2.cd(4)
#hh2000.Rebin(50)
#hh2000.GetXaxis().SetRangeUser(0, 8000)
#hh2000.Draw("HISTO")
##h2000.Fit('gaus', '','',-0.1,0.1)
######################
##ff3000 = ROOT.TFile('./crab/crab_ana_effres_nomasswin_new_dy3000/res/zp2mu_histos_3000.root')
##dd3000 = ff3000.Resolutiontunepnew
##hh3000 = dd3000.Get('DileptonMassReco')
###hh3000 = fit_gaussian(h120,None,True)
##c2.cd(5)
##hh3000.Draw("HISTO")
###h3000.Fit('gaus', '','',-0.1,0.1)
######################
#ff4500 = ROOT.TFile('./crab/crab_ana_effres_nomasswin_new_dy4500/res/zp2mu_histos_4500.root')
#dd4500 = ff4500.Resolutiontunepnew
#hh4500 = ROOT.TH1F(dd4500.Get('DileptonMassReco'))
##h120 = fit_gaussian(h120,None,True)
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
#ff120_gen = ROOT.TFile('./crab/crab_ana_effres_nomasswin_new_dy120/res/zp2mu_histos_120.root')
#dd120_gen = ff120_gen.Resolutiontunepnew
#hh120_gen = ROOT.TH1F(dd120_gen.Get('DileptonMassGen'))
##h120 = fit_gaussian(h120,None,True)
#c3.cd(1)
#hh120_gen.Rebin(10)
#hh120_gen.GetXaxis().SetRangeUser(0, 500)
#hh120_gen.Draw("HISTO")
##h120.Fit('gaus', '','',-0.1,0.1)
#####################
#ff200_gen = ROOT.TFile('./crab/crab_ana_effres_nomasswin_new_dy200/res/zp2mu_histos_200.root')
#dd200_gen = ff200_gen.Resolutiontunepnew
#hh200_gen = ROOT.TH1F(dd200_gen.Get('DileptonMassGen'))
##h120 = fit_gaussian(h120,None,True)
#c3.cd(2)
#hh200_gen.Rebin(50)
#hh200_gen.GetXaxis().SetRangeUser(0, 4000)
#hh200_gen.Draw("HISTO")
##h200.Fit('gaus', '','',-0.1,0.1)
#####################
#ff800_gen = ROOT.TFile('./crab/crab_ana_effres_nomasswin_new_dy800/res/zp2mu_histos_800.root')
#dd800_gen = ff800_gen.Resolutiontunepnew
#hh800_gen = ROOT.TH1F(dd800_gen.Get('DileptonMassGen'))
##h120 = fit_gaussian(h120,None,True)
#c3.cd(3)
#hh800_gen.Rebin(20)
#hh800_gen.GetXaxis().SetRangeUser(0, 2500)
#hh800_gen.Draw("HISTO")
##h800.Fit('gaus', '','',-0.1,0.1)
######################
#ff2000_gen = ROOT.TFile('./crab/crab_ana_effres_nomasswin_new_dy2000/res/zp2mu_histos_2000.root')
#dd2000_gen = ff2000_gen.Resolutiontunepnew
#hh2000_gen = ROOT.TH1F(dd2000_gen.Get('DileptonMassGen'))
##h120 = fit_gaussian(h120,None,True)
#c3.cd(4)
#hh2000_gen.Rebin(50)
#hh2000_gen.GetXaxis().SetRangeUser(0, 8000)
#hh2000_gen.Draw("HISTO")
##h2000.Fit('gaus', '','',-0.1,0.1)
######################
##ff3000 = ROOT.TFile('./crab/crab_ana_effres_nomasswin_new_dy3000/res/zp2mu_histos_3000.root')
##dd3000 = ff3000.Resolutiontunepnew
##hh3000 = dd3000.Get('DileptonMassReco')
###hh3000 = fit_gaussian(h120,None,True)
##c2.cd(5)
##hh3000.Draw("HISTO")
###h3000.Fit('gaus', '','',-0.1,0.1)
######################
#ff4500_gen = ROOT.TFile('./crab/crab_ana_effres_nomasswin_new_dy4500/res/zp2mu_histos_4500.root')
#dd4500_gen = ff4500_gen.Resolutiontunepnew
#hh4500_gen = ROOT.TH1F(dd4500_gen.Get('DileptonMassGen'))
##h120 = fit_gaussian(h120,None,True)
#c3.cd(5)
#hh4500_gen.Rebin(50)
##hh4500.GetXaxis().SetRangeUser(0, 8000)
#hh4500_gen.Draw("HISTO")
##h4500.Fit('gaus', '','',-0.1,0.1)
######################
#
#c3.Print('mass_gen.pdf')

c_res = ROOT.TCanvas( 'c_res', '')
c_res.cd()
n= 5

x = array( 'f', [140, 250.0, 1580.0, 3640.0, 6030.0])
y = array( 'f', [0.0154,0.02,0.0432,0.0535,0.07])
ex = array( 'f', [0.0,0.0,0.0,0.0,0.0])
ey = array( 'f', [0.00023,0.00024,0.0005,0.0008,0.00178])
#
gr = ROOT.TGraphErrors(n,x,y,ex,ey);
gr.SetLineStyle(0)
gr.SetLineColor(1)
gr.SetLineWidth(2)
gr.SetMarkerColor(1)
gr.SetMarkerStyle(20)
gr.SetMarkerSize(0.875)
gr.GetYaxis().SetRangeUser(0.01,0.1)
gr.Draw("AP")
#line = ROOT.TF1("line", '[0]/(ROOT.pow(x+[1],[2]))')
line = ROOT.TF1('line', '[0]/pow(x+[1],[2])',0.,8000.)
line.SetParameter(0, 4.64567e-03)
line.SetParameter(1, -1.75397e+02)
line.SetParameter(2, -3.02480e-01)
#line.SetParameters(4.64567e-03,-1.75397e+02,-3.02480e-01)
line.SetLineColor(2)
#gr.Fit(line, 'R')
#c_res.Update()
#line.Draw()

#fn1 = ROOT.TF1("fn1",FittingFunc1,220,5050.0,3);
#fn1.SetParameters(4.64567e-03,-1.75397e+02,-3.02480e-01);
#fn1.SetLineColor(2);
#gr.Fit("fn1","R");
c_res.Print('resVSmass.pdf')


