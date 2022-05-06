#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 

Die main.py startet das Programm.
Zusätzlich implentiert und deklariert es alle Semaphoren

@author: lars
"""

###########################_Einbindung_import_#################################
###############################################################################
from pickletools import string1
import threading
import os
import subprocess
import time


##Einbindung der Modules
import sRam
import th_1
import th_2
import th_0


##############################_Variablen_######################################
###############################################################################



##############################_Semaphoren_#####################################
###############################################################################
##Erstellen der Semaphoren (Inhalt des Sema bei Start des Programms)
semaphor_sRam_Sema = threading.Semaphore(value = 1)    #Inhalt 1 für den Zugang aufs sRAm_Security (globals)

###############################_Main_##########################################
###############################################################################
if __name__ == "__main__":
    ##Systemsdaten abfragen
    system = sRam.System()
    system.plattform()

    schreiben_RamSec = sRam.RamSec()

    #--------------------------------------------------------------------------
    ##AnalyseDatei aus aus Vorlagen erzeugen
    data = int(input("Analysedatei aus Vorlage erzeugen? (Ja = 1 / Nein = 0): "))
    if data == 1:
        string0 = "Thread_0 Analysedaten_xlsx erzeugen!"
        f0 = threading.Thread(target = th_0.func_th_0_thread, args=(list,string0))
        f0.start()
        semaphor_sRam_Sema.acquire()    ##Dekrementiert -1
        schreiben_RamSec.funcClearData()
        schreiben_RamSec.funcDatei(data)
        semaphor_sRam_Sema.release()    ##Inkrementiert +1

    elif data == 0:
        print("keine Analysedatei erzeugen!")
    else:
        print("Falsche Eingabe")
        print("Es wird keine Analysedatei ausVorlage erzeugt!")

    time.sleep(2)

    #--------------------------------------------------------------------------
    ##Thread erzeugen
    string1 = "Thread_1 Analysedaten_xlsx startet!"
    f1 = threading.Thread(target = th_1.func_th_1_thread, args=(list,string1))
    string2 = "Thread_2 Analysedaten_xlsx startet!"
    f2 = threading.Thread(target = th_2.func_th_2_thread, args=(list,string2))

    time.sleep(2)

    #--------------------------------------------------------------------------
    ##Auswahl des Worksheet's
    print("")
    print("Befüllen der Exceldatei nur bei erzeugter Vorlage möglich!")
    print("Um zu Beenden != 1 - 6 eingeben!")
    ws = int(input("Bitte wählen Sie das WorkSheet aus (1 - 6): "))

    if ws > 0 and ws < 7:
        semaphor_sRam_Sema.acquire()    ##Dekrementiert -1
        schreiben_RamSec.funcClearWorksheet()
        schreiben_RamSec.funcWS(ws)
        semaphor_sRam_Sema.release()    ##Inkrementiert +1

        #--------------------------------------------------------------------------
        ##Thread's starten
        f1.start()
        f2.start()

        #--------------------------------------------------------------------------
        ##Freigabe an die Thread's
        time.sleep(1)
        semaphor_sRam_Sema.acquire()    ##Dekrementiert -1
        schreiben_RamSec.funcClear()
        schreiben_RamSec.funcSec(1,0,0)
        semaphor_sRam_Sema.release()    ##Inkrementiert +1
    
    else:
        print("Abbruch/ Falsche Eingabe / Programm wird beendet")


    time.sleep(3)
    print('Ende Main' + '-' * 60)
############################_Main_Ende_#######################################