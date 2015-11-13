#!/bin/bash
cd /afs/cern.ch/work/l/lpernie/ECALpro/gitHubCalib/WD/CMSSW_7_4_12_patch4/src/CalibCode/submit/AfterCalibTools/WorkOnIC
eval `scramv1 runtime -sh`
python DoTxtFromTh2.py root://eoscms//eos/cms/store/group/dpg_ecal/alca_ecalcalib/lpernie/ALL_2015D_Multifit_7412p4_74X_dataRun2_Prompt_v2_GoldORSilverJson_03/iter_7/2015D_calibMap.root calibMap_EB 2015D_IC True
