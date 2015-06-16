#!/usr/bin/env python

import os
from SUSYBSMAnalysis.Zprime2muAnalysis.roottools import ROOT

#path = 'data/Run2012MuonsOnly/ana_datamc_data.root'
path = 'mc/ana_datamc_dy200.root'
tmp_fn = 'micro_ntuple_vtx.temp.txt'
#branch_spec = 'run:lumi:event:vertex_m'dil_mass
#branch_spec = 'run:lumi:event'
branch_spec = 'run:lumi:event:lep_pt[0]:lep_pt[1]:dil_mass:vertex_m:vertex_chi2'
#branch_spec = 'run:lumi:event:dil_mass:lep_pt[0]:lep_pt[1]:lep_eta[0]:lep_eta[1]:triggerMatched:trigger_match_0:trigger_match_1:lep_tk_numberOfValidPixelHits[0]:lep_tk_numberOfValidPixelHits[1]:lep_glb_numberOfValidPixelHits[0]:lep_glb_numberOfValidPixelHits[1]:lep_triggerMatchEta[0]:lep_triggerMatchEta[1]'
#cut = 'event == 16279 || event == 62429'
cut = 'loose_2012_0 && loose_2012_1 && triggerMatched && cos_angle > -0.9998  && GoodData && OppSign && vertex_chi2 > 30'
#cut = 'vertex_chi2 > 30'

f = ROOT.TFile(path)
#d = f.HistosVertexFromPAT
t = f.SimpleNtupler.Get('t')
t.GetPlayer().SetScanRedirect(True)
t.GetPlayer().SetScanFileName(tmp_fn)
t.Scan(branch_spec, cut)
t.GetPlayer().SetScanRedirect(False)
f.Close()

lines = [line.split(' *')[1:] for line in open(tmp_fn).readlines() if ' * ' in line and 'Row' not in line]
lines = ['\t'.join(y.strip() for y in x) for x in lines]
open(tmp_fn, 'wt').write('\n'.join(lines))

#f = ROOT.TFile(path.replace('.root', '.microtuple.root'), 'CREATE')
#t = ROOT.TTree('t','')
#t.ReadFile(tmp_fn, branch_spec)
#f.Write()
#f.Close()

#os.remove(tmp_fn)
