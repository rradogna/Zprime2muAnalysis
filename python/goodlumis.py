import copy
from FWCore.PythonUtilities.LumiList import LumiList

def for_cmssw(ll):
    return ll.getCMSSWString().split(',')

last_rereco_run = 163869
last_prompt_run = 165542
assert last_prompt_run > last_rereco_run

DCSOnly_ll           = LumiList('/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions11/7TeV/DCSOnly/json_DCSONLY.txt')
DCSOnlyForNewRuns_ll = LumiList('/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions11/7TeV/DCSOnly/json_DCSONLY.txt')
DCSOnlyForNewRuns_ll.removeRuns(xrange(160404, last_prompt_run+1))

Prompt_ll          = LumiList('/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions11/7TeV/Prompt/Cert_160404-%i_7TeV_PromptReco_Collisions11_JSON.txt'          % last_prompt_run)
PromptMuonsOnly_ll = LumiList('/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions11/7TeV/Prompt/Cert_160404-%i_7TeV_PromptReco_Collisions11_JSON_MuonPhys.txt' % last_prompt_run)

May10_ll          = LumiList('/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions11/7TeV/Reprocessing/Cert_160404-%i_7TeV_May10ReReco_Collisions11_JSON.txt'          % last_rereco_run)
May10MuonsOnly_ll = LumiList('/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions11/7TeV/Reprocessing/Cert_160404-%i_7TeV_May10ReReco_Collisions11_JSON_MuonPhys.txt' % last_rereco_run)

def combine(may10_ll, prompt_ll, dcsonly_ll=None):
    prompt_ll = copy.deepcopy(prompt_ll)
    prompt_ll.removeRuns(xrange(160404, last_rereco_run+1))
    ll = may10_ll | prompt_ll
    if dcsonly_ll is not None:
        dcsonly_ll = copy.deepcopy(dcsonly_ll)
        dcsonly_ll.removeRuns(xrange(160404, last_prompt_run+1))
        ll = ll | dcsonly_ll
    return ll

Run2011A_ll          = combine(May10_ll,          Prompt_ll)
Run2011AMuonsOnly_ll = combine(May10MuonsOnly_ll, PromptMuonsOnly_ll)

Run2011APlusDCSOnly_ll          = combine(May10_ll,          Prompt_ll,          DCSOnly_ll)
Run2011APlusDCSOnlyMuonsOnly_ll = combine(May10MuonsOnly_ll, PromptMuonsOnly_ll, DCSOnly_ll)

Run2010_ll          = LumiList('/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions10/7TeV/Reprocessing/Cert_136033-149442_7TeV_Apr21ReReco_Collisions10_JSON.txt')
Run2010MuonsOnly_ll = LumiList('/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions10/7TeV/Reprocessing/Cert_136033-149442_7TeV_Apr21ReReco_Collisions10_JSON_MuonPhys.txt')

for x in ['DCSOnly', 'DCSOnlyForNewRuns', 'Prompt', 'PromptMuonsOnly', 'May10', 'May10MuonsOnly', 'Run2011A', 'Run2011AMuonsOnly', 'Run2011APlusDCSOnly', 'Run2011APlusDCSOnlyMuonsOnly', 'Run2010', 'Run2010MuonsOnly']:
    exec '%s = for_cmssw(%s_ll)' % (x,x)

if __name__ == '__main__':
    import sys
    if 'WriteGoodLumiJSONs' in sys.argv:
        for name in ['DCSOnly_ll', 'DCSOnlyForNewRuns_ll', 'Prompt_ll', 'PromptMuonsOnly_ll', 'May10', 'May10MuonsOnly', 'Run2011A_ll', 'Run2011AMuonsOnly_ll']:
            obj = eval(name)
            obj.writeJSON('zp2mu_goodlumis_%s.json' % name.replace('_ll', ''))
