#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 

@author: lars
"""

###########################_Einbindung_import_#################################
###############################################################################
import time
import platform

##Einbindung der Module
#import main

###############################################################################
##################################_CLASS_######################################
##Systemklasse
class System():
    sys_vers = []
    python_vers = []

    def plattform(self):
        self.sys_vers.append(platform.platform())
        self.python_vers.append(platform.python_version())
        print(self.sys_vers[-1])
        print(self.python_vers[-1])
###############################################################################
##Befehlsklasse
class RamSec():
    start_datei = [0]
    start = [0]
    stop = [1]
    beenden = [0]
    worksheet = [0]

    def funcClearData(self):
        self.start_datei.clear()

    def funcClear(self):
        self.start.clear()
        self.stop.clear()
        self.beenden.clear()

    def funcClearWorksheet(self):
        self.worksheet.clear()

    def funcDatei(self, start_datei_content):
        self.start_datei.append(start_datei_content)

    def funcSec(self,   start_content, 
                        stop_content,
                        beenden_content):
        self.start.append(start_content)
        self.stop.append(stop_content)
        self.beenden.append(beenden_content)

    def funcWS(self, worksheet_content):
        self.worksheet.append(worksheet_content)
        
###############################################################################
class Zwischenspeicher():
    data_csv_i0 = [0]
    data_csv_i1 = [0]
    data_csv_i2 = [0]
    data_csv_i3 = [0]
    data_csv_i4 = [0]
    data_csv_i5 = [0]
    data_csv_i6 = [0]
    data_csv_i7 = [0]
    data_csv_i8 = [0]
    data_csv_i9 = [0]
    data_csv_i10 = [0]

    def funcClear(self):
        self.data_csv_i0.clear()
        self.data_csv_i1.clear()
        self.data_csv_i2.clear()
        self.data_csv_i3.clear()
        self.data_csv_i4.clear()
        self.data_csv_i5.clear()
        self.data_csv_i6.clear()
        self.data_csv_i7.clear()
        self.data_csv_i8.clear()
        self.data_csv_i9.clear()
        self.data_csv_i10.clear()

    def funcSpeicher0(self, data_csv_i0_content):
        self.data_csv_i0.append(data_csv_i0_content)

    def funcSpeicher1(self, data_csv_i1_content):
        self.data_csv_i1.append(data_csv_i1_content)

    def funcSpeicher2(self, data_csv_i2_content):
        self.data_csv_i2.append(data_csv_i2_content)

    def funcSpeicher3(self, data_csv_i3_content):
        self.data_csv_i3.append(data_csv_i3_content)

    def funcSpeicher4(self, data_csv_i4_content):
        self.data_csv_i4.append(data_csv_i4_content)

    def funcSpeicher5(self, data_csv_i5_content):
        self.data_csv_i5.append(data_csv_i5_content)

    def funcSpeicher6(self, data_csv_i6_content):
        self.data_csv_i6.append(data_csv_i6_content)

    def funcSpeicher7(self, data_csv_i7_content):
        self.data_csv_i7.append(data_csv_i7_content)

    def funcSpeicher8(self, data_csv_i8_content):
        self.data_csv_i8.append(data_csv_i8_content)

    def funcSpeicher9(self, data_csv_i9_content):
        self.data_csv_i9.append(data_csv_i9_content)

    def funcSpeicher10(self, data_csv_i10_content):
        self.data_csv_i10.append(data_csv_i10_content)
