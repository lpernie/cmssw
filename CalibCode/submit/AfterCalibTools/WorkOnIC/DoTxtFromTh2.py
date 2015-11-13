#!/usr/bin/env python
#python DoTxtFromTh2.py root://eoscms//eos/cms/store/group/dpg_ecal/alca_ecalcalib/lpernie/ALL_2015D_Multifit_7412p4_74X_dataRun2_Prompt_v2_GoldORSilverJson_03/iter_7/2015D_calibMap.root calibMap_EB 2015D_IC True

#from sys import argv
from math import fabs

import operator
import xml.dom.minidom

import subprocess, time, sys, os

from ROOT import gROOT, gStyle, gSystem, TCanvas, TH1F, TH2F, TFile
from PhysicsTools.PythonAnalysis import *
gSystem.Load("libFWCoreFWLite.so")
#AutoLibraryLoader.enable()

ROOT.gROOT.SetStyle("Plain")
ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetPalette(1)
ROOT.gStyle.SetOptFit(11111)

def usage():
    print "Usage: -----> python DoTxtFromTh2.py path_ROOT name_TH2 Output UseError"

def PrintTxt(fileTXT, EBIC, EBTree):
    EB_nIC = 0
    EB_Wrong = 0
    for iEta in range(1,EBIC.GetXaxis().GetNbins()+1):
        for iPhi in range(1,EBIC.GetYaxis().GetNbins()+1):
            if(iEta-86 != 0):
                EB_nIC += 1
                IC = EBIC.GetBinContent(iEta,iPhi)
                if(IC!=0 and IC!=1):
                    IC = format(IC, '.6f')
                    cond = "ieta_ == " + str(iEta-86) + " && iphi_ == " + str(iPhi)
                    h_tmp = TH1F("h_tmp","",1000,-1,1)
                    EBTree.Draw("fit_mean_err_>>h_tmp",cond,"goff")
                    Err = h_tmp.GetMean()
                    Err = format(Err, '.6f')
                    line = str(iEta-86) + " " + str(iPhi) + " 0 " + str(IC) + " " + str(Err) +  "\n"
                    fileTXT.write(line)
                    del h_tmp
                else:
                    EB_Wrong += 1
                    line = str(iEta-86) + " " + str(iPhi) + " 0 -1. 999. \n"
                    fileTXT.write(line)
    print "EB IC: " + str(EB_nIC) + " -> Not Calibrated are: " + str(EB_Wrong)
###START
print "START"
if (len(sys.argv) != 5):
    print "N arg. is: " + str(len(sys.argv))
    usage()
    sys.exit(1)
try:
    #Input
    path_ROOT = sys.argv[1]
    name_TH2  = sys.argv[2]
    Output    = sys.argv[3]
    UseError  = sys.argv[4]
    print "Reading file " +str(path_ROOT)
    print "Name TH2F is " +str(name_TH2)
    fileTXT = open(str(Output) + "/IC.txt",'w')
    fileTH2 = ROOT.TFile.Open(path_ROOT)
    EBIC    = fileTH2.Get(name_TH2)
except:
    print "ERROR: unknown options in argument %s" % sys.argv[1:]
    usage()
    sys.exit(1)
#Take Stat. error
TreeEBname = "calibEB"
EBTree = fileTH2.Get(TreeEBname)
#Do the trick
PrintTxt(fileTXT, EBIC, EBTree)

print 'Finish...'

#Final Writing
fileTXT.close()
