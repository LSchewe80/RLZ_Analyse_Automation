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
import th_0
import th_1
import th_2
import th_3
import th_4
import th_5
import th_6
import th_7
import th_8
import th_9



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
    string3 = "Thread_3 Analysedaten_xlsx startet!"
    f3 = threading.Thread(target = th_3.func_th_3_thread, args=(list,string3))
    string4 = "Thread_4 Analysedaten_xlsx startet!"
    f4 = threading.Thread(target = th_4.func_th_4_thread, args=(list,string4))
    string5 = "Thread_5 Analysedaten_xlsx startet!"
    f5 = threading.Thread(target = th_5.func_th_5_thread, args=(list,string5))
    string6 = "Thread_6 Analysedaten_xlsx startet!"
    f6 = threading.Thread(target = th_6.func_th_6_thread, args=(list,string6))
    string7 = "Thread_7 Analysedaten_xlsx startet!"
    f7 = threading.Thread(target = th_7.func_th_7_thread, args=(list,string7))
    string8 = "Thread_8 Analysedaten_xlsx startet!"
    f8 = threading.Thread(target = th_8.func_th_8_thread, args=(list,string8))
    string9 = "Thread_9 Analysedaten_xlsx startet!"
    f9 = threading.Thread(target = th_9.func_th_9_thread, args=(list,string9))

    time.sleep(2)

    #--------------------------------------------------------------------------
    ##Auswahl des Worksheet's
    print("")
    print("Befüllen der Exceldatei nur bei erzeugter Vorlage möglich!")
    print("Um zu Beenden != 1 - 9 eingeben!")
    ws = int(input("Bitte wählen Sie das WorkSheet aus (1 - 9): "))

    if ws > 0 and ws < 10:
        semaphor_sRam_Sema.acquire()    ##Dekrementiert -1
        schreiben_RamSec.funcClearWorksheet()
        schreiben_RamSec.funcWS(ws)
        semaphor_sRam_Sema.release()    ##Inkrementiert +1

        #--------------------------------------------------------------------------
        ##Thread's starten
        if ws == 1:
            f1.start()
        elif ws == 2:
            f2.start()
        elif ws == 3:
            f3.start()
        elif ws == 4:
            f4.start()
        elif ws == 5:
            f5.start()
        elif ws == 6:
            f6.start()
        elif ws == 7:
            f7.start()
        elif ws == 8:
            f8.start()
        elif ws == 9:
            f9.start()
        else:
            print("Kein Woorksheet ausgewaehlt!")

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