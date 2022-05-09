#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 

@author: lars
"""

###########################_Einbindung_import_#################################
###############################################################################
import time
import datetime

import socket
import platform
import os
import subprocess
import threading
#import xlsxwriter
#import xlwt
import csv
import openpyxl

##Einbindung der Module
import sRam
import main

###########################_Funktionen_########################################
###############################################################################


################################_THREAD_#######################################

def func_th_0_thread(list,string):
    print(string)
    beginn = True

    lesen_RamSec0 = sRam.RamSec()
    path0 = sRam.Path()
   
    time.sleep(2)
    ##Endlosschleife (verlassen nur durch Abrechen)
    while beginn == True:
        ######################################################################################
        ## Aus Vorlagenordner Excel-Datei öffnen und separat abspeichern
        #     
        main.semaphor_sRam_Sema.acquire()    ##Dekrementiert -1
        if lesen_RamSec0.start_datei[0] == 1:
            main.semaphor_sRam_Sema.release()    ##Inkrementiert +1
            print("Thread_0 Analysedaten_xlsx erzeugen und speichern!" + '-' * 60)
            try:
                print("Excel-Datei-Vorlage oeffnen" + '-' * 60)
                file = path0.vorlagePath
                #file = 'Vorlagen\Rolling_Analyse_RLZ_Gesamt.xlsx'
                fileXLSX = openpyxl.load_workbook(file)

            except Exception as erzeugen:
                print("Erzeugen der Exceldatei!" + '-' * 60)
                print(erzeugen)
                beginn = False
                break

            ######################################################################################
            ## Auswertung speichern        
            try:
                ##Excel-Datei speichern
                fileXLSX.save(path0.ablagePath)
                #fileXLSX.save('Result_Gesamt_Analyse_RLZ.xlsx')
                print("Excel-Datei erzeugt/gespeichert" + '-' * 60)
                
                time.sleep(1)
                beginn == False
                break

            except Exception as speichern:
                print("Speichern der Excel fehlgeschlagen!" + '-' * 60)
                print(speichern)
                beginn = False
                break
        main.semaphor_sRam_Sema.release()    ##Inkrementiert +1        

        if lesen_RamSec0.beenden[0] == 1:
            time.sleep(2)
            beginn = False
            break
            #sys.exit()

        # else:
        #     ##Start kann nicht durchgeführt werden
        #     print("Thread_0")
        #     if lesen_RamSec0.beenden[0] == 1:
        #         beginn = False
        #         break
        #         #sys.exit()

    print("Thread_0 Analysedaten_xlsx erzeugen/speichern beendet!" + '-' * 60)