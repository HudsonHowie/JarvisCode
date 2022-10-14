#V1-9/15/22
#Created By Hudson Howie
#-Created Comms
#-Created Controls GUI
#-Created Admin Page
#-Created Admin Min/Max Alteraations
#-Created Points Commands
#-Created Nod and Count Demos

#V2
#Created By Hudson Howie
#-Finished Lockouts and added Home Alterations
#-Introduces session save and load previous sessions

#V3
#Created by Hudson Howie
#-Introduced Programs Page
#-Introduced code Navigation Infrastructure

from tkinter import *
import numpy as np
import array
import serial
import time
from JarvArrays import *
from JarvConfig import *

    
#array= np.array([])
SystemPointsArray = np.array([[400,370,515,556,556,550,500,440,225,225,100,400,475,100,100,250,250,250,100,250,336,100,100],
                              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],])

#PointsArray = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             #               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            #               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           #                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          #                  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         #                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        #                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
       #                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
      #                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     #                       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    #                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   #                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
  #                          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 #                           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
#                         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
 


# BtnArray = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
FuncArray = np.array([0,0,0])
MotorList = [
    'LS',
    'LX',
    'LY',
    'LB']
def defcomms():
    global comms
    comms = serial.Serial(port='COM3', baudrate=9600, timeout=5)
def relax(Mtr):
    Mtr(0)

def SaveArray():
    f = open('JarvArrays.py', 'w')
    f.write('import numpy as np' + '\n')
    f.write('PointsArray = np.array([')
    for i in range(15):
        f.write('[' 
        + str(PointsArray[i,0]) + ',' + str(PointsArray[i,1]) + ','
        + str(PointsArray[i,2]) + ',' + str(PointsArray[i,3]) + ','
        + str(PointsArray[i,4]) + ',' + str(PointsArray[i,5]) + ','
        + str(PointsArray[i,6]) + ',' + str(PointsArray[i,7]) + ','
        + str(PointsArray[i,8]) + ',' + str(PointsArray[i,9]) + ','
        + str(PointsArray[i,10]) + ',' + str(PointsArray[i,11]) + ','
        + str(PointsArray[i,12]) + ',' + str(PointsArray[i,13]) + ','
        + str(PointsArray[i,14]) + ',' + str(PointsArray[i,15]) + ','
        + str(PointsArray[i,16]) + ',' + str(PointsArray[i,17]) + ','
        + str(PointsArray[i,18]) + ',' + str(PointsArray[i,19]) + ','
        + str(PointsArray[i,20]) + ',' + str(PointsArray[i,21]) + ','
        + str(PointsArray[i,22]) + ']' +',' + '\n')
    f.write('])' + '\n')
    print(PointsArray)
    f.close()
def SaveConfig():
    f = open('JarvConfig.py', 'w')
    f.write('import numpy as np' + '\n')
    f.write('BtnArray = np.array(['
            + str(BtnArray[0]) + ','
            + str(BtnArray[1]) + ','
             + str(BtnArray[2]) + ','
             + str(BtnArray[3]) + ','
             + str(BtnArray[4]) + ','
             + str(BtnArray[5]) + ','
             + str(BtnArray[6]) + ','
             + str(BtnArray[7]) + ','
             + str(BtnArray[8]) + ','
             + str(BtnArray[9]) + ','
             + str(BtnArray[10]) + ','
             + str(BtnArray[11]) + ','
             + str(BtnArray[12]) + ','
             + str(BtnArray[13]) + ','
             + str(BtnArray[14]) + ','
             + str(BtnArray[15]) + ','
             + str(BtnArray[16]) + ','
             + str(BtnArray[17]) + ','
             + str(BtnArray[18]) + ','
             + str(BtnArray[19]) + ','
             + str(BtnArray[20]) + ','
             + str(BtnArray[21]) + ','
            + str(BtnArray[22]) + '])' + '\n')
    f.write('LSMin = ' + str(LSMin) + '\n')
    f.write('LXMin = ' + str(LXMin) + '\n')
    f.write('LYMin = ' + str(LYMin) + '\n')
    f.write('LBMin = ' + str(LBMin) + '\n')
    f.write('LWMin = ' + str(LWMin) + '\n')
    f.write('LTMin = ' + str(LTMin) + '\n')
    f.write('LIMin = ' + str(LIMin) + '\n')
    f.write('LMMin = ' + str(LMMin) + '\n')
    f.write('LRMin = ' + str(LRMin) + '\n')
    f.write('LPMin = ' + str(LPMin) + '\n')
    f.write('RSMin = ' + str(RSMin) + '\n')
    f.write('RXMin = ' + str(RXMin) + '\n')
    f.write('RYMin = ' + str(RYMin) + '\n')
    f.write('RBMin = ' + str(RBMin) + '\n')
    f.write('RWMin = ' + str(RWMin) + '\n')
    f.write('RTMin = ' + str(RTMin) + '\n')
    f.write('RIMin = ' + str(RIMin) + '\n')
    f.write('RMMin = ' + str(RMMin) + '\n')
    f.write('RRMin = ' + str(RRMin) + '\n')
    f.write('RPMin = ' + str(RPMin) + '\n')
    f.write('HPMin = ' + str(HPMin) + '\n')
    f.write('HTMin = ' + str(HTMin) + '\n')
    f.write('JMin = ' + str(JMin) + '\n')
    
    f.write('LSMax = ' + str(LSMax) + '\n')
    f.write('LXMax = ' + str(LXMax) + '\n')
    f.write('LYMax = ' + str(LYMax) + '\n')
    f.write('LBMax = ' + str(LBMax) + '\n')
    f.write('LWMax = ' + str(LWMax) + '\n')
    f.write('LTMax = ' + str(LTMax) + '\n')
    f.write('LIMax = ' + str(LIMax) + '\n')
    f.write('LMMax = ' + str(LMMax) + '\n')
    f.write('LRMax = ' + str(LRMax) + '\n')
    f.write('LPMax = ' + str(LPMax) + '\n')
    f.write('RSMax = ' + str(RSMax) + '\n')
    f.write('RXMax = ' + str(RXMax) + '\n')
    f.write('RYMax = ' + str(RYMax) + '\n')
    f.write('RBMax = ' + str(RBMax) + '\n')
    f.write('RWMax = ' + str(RWMax) + '\n')
    f.write('RTMax = ' + str(RTMax) + '\n')
    f.write('RIMax = ' + str(RIMax) + '\n')
    f.write('RMMax = ' + str(RMMax) + '\n')
    f.write('RRMax = ' + str(RRMax) + '\n')
    f.write('RPMax = ' + str(RPMax) + '\n')
    f.write('HPMax = ' + str(HPMax) + '\n')
    f.write('HTMax = ' + str(HTMax) + '\n')
    f.write('JMax = ' + str(JMax) + '\n')
    
    f.write('LSHome = ' + str(LSHome) + '\n')
    f.write('LXHome = ' + str(LXHome) + '\n')
    f.write('LYHome = ' + str(LYHome) + '\n')
    f.write('LBHome = ' + str(LBHome) + '\n')
    f.write('LWHome = ' + str(LWHome) + '\n')
    f.write('LTHome = ' + str(LTHome) + '\n')
    f.write('LIHome = ' + str(LIHome) + '\n')
    f.write('LMHome = ' + str(LMHome) + '\n')
    f.write('LRHome = ' + str(LRHome) + '\n')
    f.write('LPHome = ' + str(LPHome) + '\n')
    f.write('RSHome = ' + str(RSHome) + '\n')
    f.write('RXHome = ' + str(RXHome) + '\n')
    f.write('RYHome = ' + str(RYHome) + '\n')
    f.write('RBHome = ' + str(RBHome) + '\n')
    f.write('RWHome = ' + str(RWHome) + '\n')
    f.write('RTHome = ' + str(RTHome) + '\n')
    f.write('RIHome = ' + str(RIHome) + '\n')
    f.write('RMHome = ' + str(RMHome) + '\n')
    f.write('RRHome = ' + str(RRHome) + '\n')
    f.write('RPHome = ' + str(RPHome) + '\n')
    f.write('HPHome = ' + str(HPHome) + '\n')
    f.write('HTHome = ' + str(HTHome) + '\n')
    f.write('JHome = ' + str(JHome) + '\n')
    f.close

def Homepage():
#============================================================SYSTEM RELATED FUNCTIONS============================================
    def DisableBtn(var):
        var.config(state = DISABLED)
            
    def EnableBtn(var):
        var.config(state = NORMAL)
            
    def GoHome():
        LSSlide.set(LSHome)
        print('Homing')
        
    def GoToPoint(pos):
        print('Going to point ' + str(pos))
        LSMove(PointsArray[pos - 1, 0])
        LXMove(PointsArray[pos - 1, 1])
        LYMove(PointsArray[pos - 1, 2])
        LBMove(PointsArray[pos - 1, 3])
        LWMove(PointsArray[pos - 1, 4])
        LTMove(PointsArray[pos - 1, 5])
        LIMove(PointsArray[pos - 1, 6])
        LMMove(PointsArray[pos - 1, 7])
        LRMove(PointsArray[pos - 1, 8])
        LPMove(PointsArray[pos - 1, 9])
        RSMove(PointsArray[pos - 1, 10])
        RXMove(PointsArray[pos - 1, 11])
        RYMove(PointsArray[pos - 1, 12])
        RBMove(PointsArray[pos - 1, 13])
        RWMove(PointsArray[pos - 1, 14])
        RTMove(PointsArray[pos - 1, 15])
        RIMove(PointsArray[pos - 1, 16])
        RMMove(PointsArray[pos - 1, 17])
        RRMove(PointsArray[pos - 1, 18])
        RPMove(PointsArray[pos - 1, 19])
        HPMove(PointsArray[pos - 1, 20])
        HTMove(PointsArray[pos - 1, 21])
        JMove(PointsArray[pos - 1, 22])
        
#=================================================================MOVEMENT SEND FUNCTIONS============================================
    def write_read(dada):
        comms.write(bytes(dada, 'utf-8'))
        comms.write(bytes('\n', 'utf-8'))
        #print(str(comms.readline()))
    def LSMove(amt):
        print('LS Move Sent')
        print(amt)
        DataPac = amt
        write_read(str(DataPac))
        
    def LXMove(amt):
        print('LX Move Sent')
        print(amt)
        DataPac = amt + 10000
        write_read(str(DataPac))
        
    def LYMove(amt):
        print('LY Move Sent')
        print(amt)
        DataPac = amt + 20000
        write_read(str(DataPac))
        
    def LBMove(amt):
        print('LB Move Sent')
        print(amt)
        DataPac = amt + 30000
        write_read(str(DataPac))
    
    
    def LWMove(amt):
        print('LW Move Sent')
        print(amt)
        DataPac = amt + 40000
        write_read(str(DataPac))
        
    def LTMove(amt):
        print('LT Move Sent')
        print(amt)
        DataPac = amt + 50000
        write_read(str(DataPac))
        
    def LIMove(amt):
        print('LI Move Sent')
        print(amt)
        DataPac = amt + 60000
        write_read(str(DataPac))
        
    def LMMove(amt):
        print('LM Move Sent')
        print(amt)
        DataPac = amt + 70000
        write_read(str(DataPac))
        
    def LRMove(amt):
        print('LR Move Sent')
        print(amt)
        DataPac = amt + 80000
        write_read(str(DataPac))
        
    def LPMove(amt):
        print('LP Move Sent')
        print(amt)
        DataPac = amt + 90000
        write_read(str(DataPac))
        
    def RSMove(amt):
        print('RS Move Sent')
        print(amt)
        DataPac = amt + 100000
        write_read(str(DataPac))
        
    def RXMove(amt):
        print('RX Move Sent')
        print(amt)
        DataPac = amt + 110000
        write_read(str(DataPac))
        
    def RYMove(amt):
        print('RY Move Sent')
        print(amt)
        DataPac = amt + 120000
        write_read(str(DataPac))
        
    def RBMove(amt):
        print('RB Move Sent')
        print(amt)
        DataPac = amt + 130000
        write_read(str(DataPac))
        
    def RWMove(amt):
        print('RW Move Sent')
        print(amt)
        DataPac = amt + 140000
        write_read(str(DataPac))
            
    def RTMove(amt):
        print('RT Move Sent')
        print(amt)
        DataPac = amt + 150000
        write_read(str(DataPac))
        
    def RIMove(amt):
        print('RI Move Sent')
        print(amt)
        DataPac = amt + 160000
        write_read(str(DataPac))
        
    def RMMove(amt):
        print('RM Move Sent')
        print(amt)
        DataPac = amt + 170000
        write_read(str(DataPac))
        
    def RRMove(amt):
        print('RR Move Sent')
        print(amt)
        DataPac = amt + 180000
        write_read(str(DataPac))
        
    def RPMove(amt):
        print('RP Move Sent')
        print(amt)
        DataPac = amt + 190000
        write_read(str(DataPac))
        
    def HTMove(amt):
        print('HT Move Sent')
        print(amt)
        DataPac = amt + 210000
        write_read(str(DataPac))
        
    def HPMove(amt):
        print('HP Move Sent')
        print(amt)
        DataPac = amt + 200000
        write_read(str(DataPac))
        
    def JMove(amt):
        print('J Move Sent')
        print(amt)
        DataPac = amt + 220000
        write_read(str(DataPac))
    def Speakers(amt):
        print('Speaker Sent')
        print(amt)
        DataPac = amt + 230000
        write_read(str(DataPac))

#=====================================================CREATE PAGES==========================================================        
    def ControlsPage():
        def EncodePoint(numb):
            global PointsArray
            PointsArray[numb - 1]= [LSSlide.get(),LXSlide.get(),LYSlide.get(),LBSlide.get(),
                                    LWSlide.get(),LTSlide.get(),LISlide.get(),LMSlide.get(),
                                    LRSlide.get(),LPSlide.get(),RSSlide.get(),RXSlide.get(),
                                    RYSlide.get(),RBSlide.get(),RWSlide.get(),RTSlide.get(),
                                    RISlide.get(),RMSlide.get(),RRSlide.get(),RPSlide.get(),
                                    HPSlide.get(),HTSlide.get(),JSlide.get()]
            print('Updated points array at row: ' + str(numb))
            print(PointsArray)
            
            
            
        def DeletePoint(pos):
            global PointsArray
            PointsArray[(pos -  1)] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            print('updated points array at:' + str(pos))
            print(PointsArray)

        def RecoverBtns():
            if (BtnArray[0] == 1):
                DisableBtn(LSAccept)
            if (BtnArray[0] == 0):
                EnableBtn(LSAccept)
            if (BtnArray[1] == 1):
                DisableBtn(LYAccept)
            if (BtnArray[1] == 0):
                EnableBtn(LYAccept)
            if (BtnArray[2] == 1):
                DisableBtn(LXAccept)
            if (BtnArray[2] == 0):
                EnableBtn(LXAccept)
            if (BtnArray[3] == 1):
                DisableBtn(LBAccept)
            if (BtnArray[3] == 0):
                EnableBtn(LBAccept)
            if (BtnArray[4] == 1):
                DisableBtn(LWAccept)
            if (BtnArray[4] == 0):
                EnableBtn(LWAccept)
            if (BtnArray[5] == 1):
                DisableBtn(LTAccept)
            if (BtnArray[5] == 0):
                EnableBtn(LTAccept)
            if (BtnArray[6] == 1):
                DisableBtn(LIAccept)
            if (BtnArray[6] == 0):
                EnableBtn(LIAccept)
            if (BtnArray[7] == 1):
                DisableBtn(LMAccept)
            if (BtnArray[7] == 0):
                EnableBtn(LMAccept)
            if (BtnArray[8] == 1):
                DisableBtn(LRAccept)
            if (BtnArray[8] == 0):
                EnableBtn(LRAccept)
            if (BtnArray[9] == 1):
                DisableBtn(LPAccept)
            if (BtnArray[9] == 0):
                EnableBtn(LPAccept)
            if (BtnArray[10] == 1):
                DisableBtn(RSAccept)
            if (BtnArray[10] == 0):
                EnableBtn(RSAccept)
            if (BtnArray[11] == 1):
                DisableBtn(RYAccept)
            if (BtnArray[11] == 0):
                EnableBtn(RYAccept)
            if (BtnArray[12] == 1):
                DisableBtn(RXAccept)
            if (BtnArray[12] == 0):
                EnableBtn(RXAccept)
            if (BtnArray[13] == 1):
                DisableBtn(RBAccept)
            if (BtnArray[13] == 0):
                EnableBtn(RBAccept)
            if (BtnArray[14] == 1):
                DisableBtn(RWAccept)
            if (BtnArray[14] == 0):
                EnableBtn(RWAccept)
            if (BtnArray[15] == 1):
                DisableBtn(RTAccept)
            if (BtnArray[15] == 0):
                EnableBtn(RTAccept)
            if (BtnArray[16] == 1):
                DisableBtn(RIAccept)
            if (BtnArray[16] == 0):
                EnableBtn(RIAccept)
            if (BtnArray[17] == 1):
                DisableBtn(RMAccept)
            if (BtnArray[17] == 0):
                EnableBtn(RMAccept)
            if (BtnArray[18] == 1):
                DisableBtn(RRAccept)
            if (BtnArray[18] == 0):
                EnableBtn(RRAccept)
            if (BtnArray[19] == 1):
                DisableBtn(RPAccept)
            if (BtnArray[19] == 0):
                EnableBtn(RPAccept)
            if (BtnArray[20] == 1):
                DisableBtn(HPAccept)
            if (BtnArray[20] == 0):
                EnableBtn(HPAccept)
            if (BtnArray[21] == 1):
                DisableBtn(HTAccept)
            if (BtnArray[21] == 0):
                EnableBtn(HTAccept)
            if (BtnArray[22] == 1):
                DisableBtn(JAccept)
            if (BtnArray[22] == 0):
                EnableBtn(JAccept)
                
                
            if (PointsArray[0,0] == 0):
                EnableBtn(TeachBtn1)
                DisableBtn(ClearBtn1)
                DisableBtn(GoBtn1)
                print('Recovered 1:1')
            if (PointsArray[0,0] != 0):
                EnableBtn(GoBtn1)
                EnableBtn(ClearBtn1)
                DisableBtn(TeachBtn1)
                print('Recovered 1:2')
                
            if (PointsArray[1,0] == 0):
                EnableBtn(TeachBtn2)
                DisableBtn(ClearBtn2)
                DisableBtn(GoBtn2)
                print('Recovered 2:1')
            if (PointsArray[1,0] != 0):
                EnableBtn(GoBtn2)
                EnableBtn(ClearBtn2)
                DisableBtn(TeachBtn2)
                print('Recovered 2:2')
                
            if (PointsArray[2,0] == 0):
                EnableBtn(TeachBtn3)
                DisableBtn(ClearBtn3)
                DisableBtn(GoBtn3)
                print('Recovered 3:1')
            if (PointsArray[2,0] != 0):
                EnableBtn(GoBtn3)
                EnableBtn(ClearBtn3)
                DisableBtn(TeachBtn3)
                print('Recovered 3:2')
                
            if (PointsArray[3,0] == 0):
                EnableBtn(TeachBtn4)
                DisableBtn(ClearBtn4)
                DisableBtn(GoBtn4)
                print('Recovered 4:1')
            if (PointsArray[3,0] != 0):
                EnableBtn(GoBtn4)
                EnableBtn(ClearBtn4)
                DisableBtn(TeachBtn4)
                print('Recovered 4:2')
                
            if (PointsArray[4,0] == 0):
                EnableBtn(TeachBtn5)
                DisableBtn(ClearBtn5)
                DisableBtn(GoBtn5)
                print('Recovered 5:1')
            if (PointsArray[4,0] != 0):
                EnableBtn(GoBtn5)
                EnableBtn(ClearBtn5)
                DisableBtn(TeachBtn5)
                print('Recovered 5:2')
                
            if (PointsArray[5,0] == 0):
                EnableBtn(TeachBtn6)
                DisableBtn(ClearBtn6)
                DisableBtn(GoBtn6)
                print('Recovered 6:1')
            if (PointsArray[5,0] != 0):
                EnableBtn(GoBtn6)
                EnableBtn(ClearBtn6)
                DisableBtn(TeachBtn6)
                print('Recovered 6:2')
                
            if (PointsArray[6,0] == 0):
                EnableBtn(TeachBtn7)
                DisableBtn(ClearBtn7)
                DisableBtn(GoBtn7)
                print('Recovered 7:1')
            if (PointsArray[6,0] != 0):
                EnableBtn(GoBtn7)
                EnableBtn(ClearBtn7)
                DisableBtn(TeachBtn7)
                print('Recovered 7:2')
                
            if (PointsArray[7,0] == 0):
                EnableBtn(TeachBtn8)
                DisableBtn(ClearBtn8)
                DisableBtn(GoBtn8)
                print('Recovered 8:1')
            if (PointsArray[7,0] != 0):
                EnableBtn(GoBtn8)
                EnableBtn(ClearBtn8)
                DisableBtn(TeachBtn8)
                print('Recovered 8:2')
                
            if (PointsArray[8,0] == 0):
                EnableBtn(TeachBtn9)
                DisableBtn(ClearBtn9)
                DisableBtn(GoBtn9)
                print('Recovered 9:1')
            if (PointsArray[8,0] != 0):
                EnableBtn(GoBtn9)
                EnableBtn(ClearBtn9)
                DisableBtn(TeachBtn9)
                print('Recovered 9:2')
                
            if (PointsArray[9,0] == 0):
                EnableBtn(TeachBtn10)
                DisableBtn(ClearBtn10)
                DisableBtn(GoBtn10)
                print('Recovered 10:1')
            if (PointsArray[9,0] != 0):
                EnableBtn(GoBtn10)
                EnableBtn(ClearBtn10)
                DisableBtn(TeachBtn10)
                print('Recovered 10:2')
                
            if (PointsArray[10,0] == 0):
                EnableBtn(TeachBtn11)
                DisableBtn(ClearBtn11)
                DisableBtn(GoBtn11)
                print('Recovered 11:1')
            if (PointsArray[10,0] != 0):
                EnableBtn(GoBtn11)
                EnableBtn(ClearBtn11)
                DisableBtn(TeachBtn11)
                print('Recovered 11:2')
                
            if (PointsArray[11,0] == 0):
                EnableBtn(TeachBtn12)
                DisableBtn(ClearBtn12)
                DisableBtn(GoBtn12)
                print('Recovered 12:1')
            if (PointsArray[11,0] != 0):
                EnableBtn(GoBtn12)
                EnableBtn(ClearBtn12)
                DisableBtn(TeachBtn12)
                print('Recovered 12:2')
                
            if (PointsArray[12,0] == 0):
                EnableBtn(TeachBtn13)
                DisableBtn(ClearBtn13)
                DisableBtn(GoBtn13)
                print('Recovered 13:1')
            if (PointsArray[12,0] != 0):
                EnableBtn(GoBtn13)
                EnableBtn(ClearBtn13)
                DisableBtn(TeachBtn13)
                print('Recovered 13:2')
                
            if (PointsArray[13,0] == 0):
                EnableBtn(TeachBtn14)
                DisableBtn(ClearBtn14)
                DisableBtn(GoBtn14)
                print('Recovered 14:1')
            if (PointsArray[13,0] != 0):
                EnableBtn(GoBtn14)
                EnableBtn(ClearBtn14)
                DisableBtn(TeachBtn14)
                print('Recovered 14:2')
                
            if (PointsArray[14,0] == 0):
                EnableBtn(TeachBtn15)
                DisableBtn(ClearBtn15)
                DisableBtn(GoBtn15)
                print('Recovered 15:1')
            if (PointsArray[14,0] != 0):
                EnableBtn(GoBtn15)
                EnableBtn(ClearBtn15)
                DisableBtn(TeachBtn15)
                print('Recovered 15:2')
                
            
 
        print('opening Controls page')
        HomepageWin.destroy()
        ControlsPageWin=Tk() 
        ControlsPageWin.title('Jarvis Controller') 
        ControlsPageWin.geometry('1400x900')
        ControlsPageWin.configure(bg='#26343E')
        BackBtn=Button(ControlsPageWin, text="Back", width=4,height=2,command=lambda: [ControlsPageWin.destroy(), Homepage()])
        BackBtn.place(x=1300,y=800)
#====================================================Point Controls=====================================================
        GoBtn1 = Button(ControlsPageWin, text='Pose 1', state = DISABLED, command=lambda:[GoToPoint(1)])
        GoBtn1.place(x=1200,y=(0))
        ClearBtn1 = Button(ControlsPageWin, text='Clear', state= DISABLED,
        command=lambda: [print('deleted'), DeletePoint(1), EnableBtn(TeachBtn1), DisableBtn(GoBtn1),DisableBtn(ClearBtn1)], bg='red')
        ClearBtn1.place(x=1130, y=(0))
        TeachBtn1 =  Button(ControlsPageWin, text='Teach',
        command= lambda:[EncodePoint(1), DisableBtn(TeachBtn1), EnableBtn(GoBtn1), EnableBtn(ClearBtn1)])
        TeachBtn1.place(x=1275, y = (0))
        
        GoBtn2 = Button(ControlsPageWin, text='Pose 2', state = DISABLED, command=lambda:[GoToPoint(2)])
        GoBtn2.place(x=1200,y=(50))
        ClearBtn2 = Button(ControlsPageWin, text='Clear', state= DISABLED,
        command=lambda: [print('deleted'), DeletePoint(2), EnableBtn(TeachBtn2), DisableBtn(GoBtn2),DisableBtn(ClearBtn2)], bg='red')
        ClearBtn2.place(x=1130, y=(50))
        TeachBtn2 =  Button(ControlsPageWin, text='Teach',
        command= lambda:[EncodePoint(2), DisableBtn(TeachBtn2), EnableBtn(GoBtn2), EnableBtn(ClearBtn2)])
        TeachBtn2.place(x=1275, y = (50))

        GoBtn3 = Button(ControlsPageWin, text='Pose 3', state = DISABLED, command=lambda:[GoToPoint(3)])
        GoBtn3.place(x=1200,y=(100))
        ClearBtn3 = Button(ControlsPageWin, text='Clear', state= DISABLED,
        command=lambda: [print('deleted'), DeletePoint(3), EnableBtn(TeachBtn3), DisableBtn(GoBtn3),DisableBtn(ClearBtn3)], bg='red')
        ClearBtn3.place(x=1130, y=(100))
        TeachBtn3 =  Button(ControlsPageWin, text='Teach',
        command= lambda:[EncodePoint(3), DisableBtn(TeachBtn3), EnableBtn(GoBtn3), EnableBtn(ClearBtn3)])
        TeachBtn3.place(x=1275, y = (100))
        
        GoBtn4 = Button(ControlsPageWin, text='Pose 4', state = DISABLED, command=lambda:[GoToPoint(4)])
        GoBtn4.place(x=1200,y=(150))
        ClearBtn4 = Button(ControlsPageWin, text='Clear', state= DISABLED,
        command=lambda: [print('deleted'), DeletePoint(4), EnableBtn(TeachBtn4), DisableBtn(GoBtn4),DisableBtn(ClearBtn4)], bg='red')
        ClearBtn4.place(x=1130, y=(150))
        TeachBtn4 =  Button(ControlsPageWin, text='Teach',
        command= lambda:[EncodePoint(4), DisableBtn(TeachBtn4), EnableBtn(GoBtn4), EnableBtn(ClearBtn4)])
        TeachBtn4.place(x=1275, y = (150))
        
        GoBtn5 = Button(ControlsPageWin, text='Pose 5', state = DISABLED, command=lambda:[GoToPoint(5)])
        GoBtn5.place(x=1200,y=(200))
        ClearBtn5 = Button(ControlsPageWin, text='Clear', state= DISABLED,
        command=lambda: [print('deleted'), DeletePoint(5), EnableBtn(TeachBtn5), DisableBtn(GoBtn5),DisableBtn(ClearBtn5)], bg='red')
        ClearBtn5.place(x=1130, y=(200))
        TeachBtn5 =  Button(ControlsPageWin, text='Teach',
        command= lambda:[EncodePoint(5), DisableBtn(TeachBtn5), EnableBtn(GoBtn5), EnableBtn(ClearBtn5)])
        TeachBtn5.place(x=1275, y = (200))
        
        GoBtn6 = Button(ControlsPageWin, text='Pose 6', state = DISABLED, command=lambda:[GoToPoint(6)])
        GoBtn6.place(x=1200,y=(250))
        ClearBtn6 = Button(ControlsPageWin, text='Clear', state= DISABLED,
        command=lambda: [print('deleted'), DeletePoint(6), EnableBtn(TeachBtn6), DisableBtn(GoBtn6),DisableBtn(ClearBtn6)], bg='red')
        ClearBtn6.place(x=1130, y=(250))
        TeachBtn6 =  Button(ControlsPageWin, text='Teach',
        command= lambda:[EncodePoint(6), DisableBtn(TeachBtn6), EnableBtn(GoBtn6), EnableBtn(ClearBtn6)])
        TeachBtn6.place(x=1275, y = (250))
        
        GoBtn7 = Button(ControlsPageWin, text='Pose 7', state = DISABLED, command=lambda:[GoToPoint(7)])
        GoBtn7.place(x=1200,y=(300))
        ClearBtn7 = Button(ControlsPageWin, text='Clear', state= DISABLED,
        command=lambda: [print('deleted'), DeletePoint(7), EnableBtn(TeachBtn7), DisableBtn(GoBtn7),DisableBtn(ClearBtn7)], bg='red')
        ClearBtn7.place(x=1130, y=(300))
        TeachBtn7 =  Button(ControlsPageWin, text='Teach',
        command= lambda:[EncodePoint(7), DisableBtn(TeachBtn7), EnableBtn(GoBtn7), EnableBtn(ClearBtn7)])
        TeachBtn7.place(x=1275, y = (300))
        
        GoBtn8 = Button(ControlsPageWin, text='Pose 8', state = DISABLED, command=lambda:[GoToPoint(8)])
        GoBtn8.place(x=1200,y=(350))
        ClearBtn8 = Button(ControlsPageWin, text='Clear', state= DISABLED,
        command=lambda: [print('deleted'), DeletePoint(8), EnableBtn(TeachBtn8), DisableBtn(GoBtn8),DisableBtn(ClearBtn8)], bg='red')
        ClearBtn8.place(x=1130, y=(350))
        TeachBtn8 =  Button(ControlsPageWin, text='Teach',
        command= lambda:[EncodePoint(8), DisableBtn(TeachBtn8), EnableBtn(GoBtn8), EnableBtn(ClearBtn8)])
        TeachBtn8.place(x=1275, y = (350))
        
        GoBtn9 = Button(ControlsPageWin, text='Pose 9', state = DISABLED, command=lambda:[GoToPoint(9)])
        GoBtn9.place(x=1200,y=(400))
        ClearBtn9 = Button(ControlsPageWin, text='Clear', state= DISABLED,
        command=lambda: [print('deleted'), DeletePoint(9), EnableBtn(TeachBtn9), DisableBtn(GoBtn9),DisableBtn(ClearBtn9)], bg='red')
        ClearBtn9.place(x=1130, y=(400))
        TeachBtn9 =  Button(ControlsPageWin, text='Teach',
        command= lambda:[EncodePoint(9), DisableBtn(TeachBtn9), EnableBtn(GoBtn9), EnableBtn(ClearBtn9)])
        TeachBtn9.place(x=1275, y = (400))
        
        GoBtn10 = Button(ControlsPageWin, text='Pose 10', state = DISABLED, command=lambda:[GoToPoint(10)])
        GoBtn10.place(x=1200,y=(450))
        ClearBtn10 = Button(ControlsPageWin, text='Clear', state= DISABLED,
        command=lambda: [print('deleted'), DeletePoint(10), EnableBtn(TeachBtn10), DisableBtn(GoBtn10),DisableBtn(ClearBtn10)], bg='red')
        ClearBtn10.place(x=1130, y=(450))
        TeachBtn10 =  Button(ControlsPageWin, text='Teach',
        command= lambda:[EncodePoint(10), DisableBtn(TeachBtn10), EnableBtn(GoBtn10), EnableBtn(ClearBtn10)])
        TeachBtn10.place(x=1275, y = (450))
        
        GoBtn11 = Button(ControlsPageWin, text='Pose 11', state = DISABLED, command=lambda:[GoToPoint(11)])
        GoBtn11.place(x=1200,y=(500))
        ClearBtn11 = Button(ControlsPageWin, text='Clear', state= DISABLED,
        command=lambda: [print('deleted'), DeletePoint(11), EnableBtn(TeachBtn11), DisableBtn(GoBtn11),DisableBtn(ClearBtn11)], bg='red')
        ClearBtn11.place(x=1130, y=(500))
        TeachBtn11 =  Button(ControlsPageWin, text='Teach',
        command= lambda:[EncodePoint(11), DisableBtn(TeachBtn11), EnableBtn(GoBtn11), EnableBtn(ClearBtn11)])
        TeachBtn11.place(x=1275, y = (500))
        
        
        GoBtn12 = Button(ControlsPageWin, text='Pose 12', state = DISABLED, command=lambda:[GoToPoint(12)])
        GoBtn12.place(x=1200,y=(550))
        ClearBtn12 = Button(ControlsPageWin, text='Clear', state= DISABLED,
        command=lambda: [print('deleted'), DeletePoint(12), EnableBtn(TeachBtn12), DisableBtn(GoBtn12),DisableBtn(ClearBtn12)], bg='red')
        ClearBtn12.place(x=1130, y=(550))
        TeachBtn12 =  Button(ControlsPageWin, text='Teach',
        command= lambda:[EncodePoint(12), DisableBtn(TeachBtn12), EnableBtn(GoBtn12), EnableBtn(ClearBtn12)])
        TeachBtn12.place(x=1275, y = (550))
        
        GoBtn13 = Button(ControlsPageWin, text='Pose 13', state = DISABLED, command=lambda:[GoToPoint(13)])
        GoBtn13.place(x=1200,y=(600))
        ClearBtn13 = Button(ControlsPageWin, text='Clear', state= DISABLED,
        command=lambda: [print('deleted'), DeletePoint(13), EnableBtn(TeachBtn13), DisableBtn(GoBtn13),DisableBtn(ClearBtn13)], bg='red')
        ClearBtn13.place(x=1130, y=(600))
        TeachBtn13 =  Button(ControlsPageWin, text='Teach',
        command= lambda:[EncodePoint(13), DisableBtn(TeachBtn13), EnableBtn(GoBtn13), EnableBtn(ClearBtn13)])
        TeachBtn13.place(x=1275, y = (600))
        
        GoBtn14 = Button(ControlsPageWin, text='Pose 14', state = DISABLED, command=lambda:[GoToPoint(14)])
        GoBtn14.place(x=1200,y=(650))
        ClearBtn14 = Button(ControlsPageWin, text='Clear', state= DISABLED,
        command=lambda: [print('deleted'), DeletePoint(14), EnableBtn(TeachBtn14), DisableBtn(GoBtn14),DisableBtn(ClearBtn14)], bg='red')
        ClearBtn14.place(x=1130, y=(650))
        TeachBtn14 =  Button(ControlsPageWin, text='Teach',
        command= lambda:[EncodePoint(14), DisableBtn(TeachBtn14), EnableBtn(GoBtn14), EnableBtn(ClearBtn14)])
        TeachBtn14.place(x=1275, y = (650))
        
        GoBtn15 = Button(ControlsPageWin, text='Pose 15', state = DISABLED, command=lambda:[GoToPoint(15)])
        GoBtn15.place(x=1200,y=(700))
        ClearBtn15 = Button(ControlsPageWin, text='Clear', state= DISABLED,
        command=lambda: [print('deleted'), DeletePoint(15), EnableBtn(TeachBtn15), DisableBtn(GoBtn15),DisableBtn(ClearBtn15)], bg='red')
        ClearBtn15.place(x=1130, y=(700))
        TeachBtn15 =  Button(ControlsPageWin, text='Teach',
        command= lambda:[EncodePoint(15), DisableBtn(TeachBtn15), EnableBtn(GoBtn15), EnableBtn(ClearBtn15)])
        TeachBtn15.place(x=1275, y = (700))
        
#=====================================================Movement Commands=================================================
        LSSlide=Scale(ControlsPageWin, fg='white', bg='#26343E', label='LS control', width=20, length= 300, from_ = LSMin, to = LSMax, orient= HORIZONTAL)
        LSSlide.grid(row=0, column=2)
        LSSlide.set(LSHome)
        LSAccept=Button(text='Go',bg='lime', width=7, height=3, command=lambda: [ LSMove(LSSlide.get() + 0)])
        LSAccept.grid(row=0, column=3)
        
        LYSlide=Scale(ControlsPageWin, fg='white', bg='#26343E', label='LY control', width=20, length= 300,  from_ = LYMin, to = LYMax, orient= HORIZONTAL)
        LYSlide.grid(row=1, column=2)
        LYSlide.set(LYHome)
        LYAccept=Button(text='Go',bg='lime', width=7, height=3, command=lambda: [LYMove(LYSlide.get())])
        LYAccept.grid(row=1, column=3)
        
        LXSlide=Scale(ControlsPageWin, fg='white', bg='#26343E', label='LX Control', width=20, length= 300,  from_ = LXMin, to = LXMax, orient= HORIZONTAL)
        LXSlide.grid(row=2, column=2)
        LXSlide.set(LXHome)
        LXAccept=Button(text='Go',bg='lime', width=7, height=3, command=lambda: [LXMove(LXSlide.get())])
        LXAccept.grid(row=2, column=3)

        LBSlide=Scale(ControlsPageWin, fg='white', bg='#26343E', label='LB Control', width=20, length= 300,  from_ = LBMin, to = LBMax, orient= HORIZONTAL)
        LBSlide.grid(row=3, column=2)
        LBSlide.set(LBHome)
        LBAccept=Button(text='Go',bg='lime', width=7, height=3,command=lambda: [LBMove(LBSlide.get())])
        LBAccept.grid(row=3, column=3)
    

        LWSlide=Scale(ControlsPageWin, fg='white', bg='#26343E', label='LW Control', width=20, length= 300,  from_ = LWMin, to = LWMax, orient= HORIZONTAL)
        LWSlide.grid(row=4, column=2)
        LWSlide.set(LWHome)
        LWAccept=Button(text='Go',bg='lime', width=7, height=3,command=lambda: [LWMove(LWSlide.get())])
        LWAccept.grid(row=4, column=3)
        

        LTSlide=Scale(ControlsPageWin, fg='white', bg='#26343E', label='LT Control', width=20, length= 300,  from_ = LTMin, to = LTMax, orient= HORIZONTAL)
        LTSlide.grid(row=5, column=2)
        LTSlide.set(LTHome)
        LTAccept=Button(text='Go',bg='lime', width=7, height=3,command=lambda: [LTMove(LTSlide.get())])
        LTAccept.grid(row=5, column=3)
        

        LISlide=Scale(ControlsPageWin, fg='white', bg='#26343E',label='LI Control', width=20, length= 300,  from_ = LIMin, to = LIMax, orient= HORIZONTAL)
        LISlide.grid(row=6, column=2)
        LISlide.set(LIHome)
        LIAccept=Button(text='Go',bg='lime', width=7, height=3,command=lambda: [LIMove(LISlide.get())])
        LIAccept.grid(row=6, column=3)
        

        LMSlide=Scale(ControlsPageWin, fg='white', bg='#26343E', label='LM Control', width=20, length= 300, from_ = LMMin, to = LMMax, orient= HORIZONTAL)
        LMSlide.grid(row=7, column=2)
        LMSlide.set(LMHome)
        LMAccept=Button(text='Go',bg='lime', width=7, height=3,command=lambda: [LMMove(LMSlide.get())])
        LMAccept.grid(row=7, column=3)
        

        LRSlide=Scale(ControlsPageWin,fg='white', bg='#26343E', label='LR Control', width=20, length= 300, from_ = LRMin, to = LRMax, orient= HORIZONTAL)
        LRSlide.grid(row=8, column=2)
        LRSlide.set(LRHome)
        LRAccept=Button(text='Go',bg='lime', width=7, height=3,command=lambda: [LRMove(LRSlide.get())])
        LRAccept.grid(row=8, column=3)
        

        LPSlide=Scale(ControlsPageWin, fg='white', bg='#26343E', label='LP Control', width=20, length= 300, from_ = LPMin, to = LPMax, orient= HORIZONTAL)
        LPSlide.grid(row=9, column=2)
        LPSlide.set(LPHome)
        LPAccept=Button(text='Go', bg='lime', width=7, height=3,command=lambda: [LPMove(LPSlide.get())])
        LPAccept.grid(row=9, column=3)
        
        
        RSSlide=Scale(ControlsPageWin, fg='white', bg='#26343E', label='RS Control', width=20, length= 300,  from_ = RSMin, to = RSMax, orient= HORIZONTAL)
        RSSlide.grid(row=0, column=5)
        RSSlide.set(RSHome)
        RSAccept=Button(text='Go', bg='lime', width=7, height=3, command=lambda: [ RSMove(RSSlide.get())])
        RSAccept.grid(row=0, column=6)
        

        RYSlide=Scale(ControlsPageWin, fg='white', bg='#26343E', label='RY Control', width=20, length= 300, from_ = RYMin, to = RYMax, orient= HORIZONTAL)
        RYSlide.grid(row=1, column=5)
        RYSlide.set(RYHome)
        RYAccept=Button(text='Go', bg='lime', width=7, height=3, command=lambda: [RYMove(RYSlide.get())])
        RYAccept.grid(row=1, column=6)
        
    
        RXSlide=Scale(ControlsPageWin, fg='white', bg='#26343E', label='RX Control', width=20, length= 300, from_ = RXMin, to = RXMax, orient= HORIZONTAL)
        RXSlide.grid(row=2, column=5)
        RXSlide.set(RXHome)
        RXAccept=Button(text='Go', bg='lime', width=7, height=3, command=lambda: [RXMove(RXSlide.get())])
        RXAccept.grid(row=2, column=6)
    

        RBSlide=Scale(ControlsPageWin, fg='white', bg='#26343E', label='RB Control', width=20, length= 300, from_ = RBMin, to = RBMax, orient= HORIZONTAL)
        RBSlide.grid(row=3, column=5)
        RBSlide.set(RBHome)
        RBAccept=Button(text='Go', bg='lime', width=7, height=3, command=lambda: [RBMove(RBSlide.get())])
        RBAccept.grid(row=3, column=6)
    

        RWSlide=Scale(ControlsPageWin, fg='white', bg='#26343E', label='RW Control', width=20, length= 300, from_ = RWMin, to = RWMax, orient= HORIZONTAL)
        RWSlide.grid(row=4, column=5)
        RWSlide.set(RWHome)
        RWAccept=Button(text='Go', bg='lime', width=7, height=3, command=lambda: [RWMove(RWSlide.get())])
        RWAccept.grid(row=4, column=6)
        

        RTSlide=Scale(ControlsPageWin, fg='white', bg='#26343E', label='RT Control', width=20, length= 300, from_ = RTMin, to = RTMax, orient= HORIZONTAL)
        RTSlide.grid(row=5, column=5)
        RTSlide.set(RTHome)
        RTAccept=Button(text='Go', bg='lime', width=7, height=3, command=lambda: [RTMove(RTSlide.get())])
        RTAccept.grid(row=5, column=6)
        

        RISlide=Scale(ControlsPageWin, fg='white', bg='#26343E', label='RI Control', width=20, length= 300, from_ = RIMin, to = RIMax, orient= HORIZONTAL)
        RISlide.grid(row=6, column=5)
        RISlide.set(RWHome)
        RIAccept=Button(text='Go', bg='lime', width=7, height=3, command=lambda: [RIMove(RISlide.get())])
        RIAccept.grid(row=6, column=6)
        

        RMSlide=Scale(ControlsPageWin, fg='white', bg='#26343E', label='RM Control', width=20, length= 300, from_ = RMMin, to = RMMax, orient= HORIZONTAL)
        RMSlide.grid(row=7, column=5)
        RMSlide.set(RMHome)
        RMAccept=Button(text='Go', bg='lime', width=7, height=3, command=lambda: [RMMove(RMSlide.get())])
        RMAccept.grid(row=7, column=6)
    

        RRSlide=Scale(ControlsPageWin, fg='white', bg='#26343E', label='RR Control', width=20, length= 300, from_ = RRMin, to = RRMax, orient= HORIZONTAL)
        RRSlide.grid(row=8, column=5)
        RRSlide.set(RRHome)
        RRAccept=Button(text='Go', bg='lime', width=7, height=3, command=lambda: [RRMove(RRSlide.get())])
        RRAccept.grid(row=8, column=6)
        

        RPSlide=Scale(ControlsPageWin, fg='white', bg='#26343E', label='RP Control', width=20, length= 300, from_ = RPMin, to = RPMax, orient= HORIZONTAL)
        RPSlide.grid(row=9, column=5)
        RPSlide.set(RPHome)
        RPAccept=Button(text='Go', bg='lime', width=7, height=3, command=lambda: [RPMove(RPSlide.get())])
        RPAccept.grid(row=9, column=6)
    
        HPSlide=Scale(ControlsPageWin, fg='white', bg='#26343E', label='HP Control', width=20, length= 300, from_ = HPMin, to = HPMax, orient= HORIZONTAL)
        HPSlide.grid(row=0, column=7)
        HPSlide.set(HPHome)
        HPAccept=Button(text='Go', bg='lime', width=7, height=3, command=lambda: [HPMove(HPSlide.get())])
        HPAccept.grid(row=0, column=8)
        
        HTSlide=Scale(ControlsPageWin, fg='white', bg='#26343E', label='HT Control', width=20, length= 300, from_ = HTMin, to = HTMax, orient= HORIZONTAL)
        HTSlide.grid(row=1, column=7)
        HTSlide.set(HTHome)
        HTAccept=Button(text='Go', bg='lime', width=7, height=3, command=lambda: [HTMove(HTSlide.get())])
        HTAccept.grid(row=1, column=8)
        
        JSlide=Scale(ControlsPageWin, fg='white', bg='#26343E', label='J Control', width=20, length= 300, from_ = JMin, to = JMax, orient= HORIZONTAL)
        JSlide.grid(row=2, column=7)
        JSlide.set(JHome)
        JAccept=Button(text='Go', bg='lime', width=7, height=3, command=lambda: [JMove(JSlide.get())])
        JAccept.grid(row=2, column=8)
        
        SPSlide=Scale(ControlsPageWin, fg='white', bg='#26343E', label='SP Control', width=20, length= 300, from_ = 0, to = 1000, orient= HORIZONTAL)
        SPSlide.grid(row=3, column=7)
        SPSlide.set(JHome)
        SPAccept=Button(text='Go', bg='lime', width=7, height=3, command=lambda: [Speakers(SPSlide.get())])
        SPAccept.grid(row=3, column=8)
        
        
        
        #Label(ControlsPageWin, text='Commands:', font=("Helvetica", 24), fg='White', bg='#26343E').grid(row=3,column=7)
        
        ResetHomebtn = Button(ControlsPageWin, text='Reset to Home', bg='lime', width=37, height=3, command=lambda:[GoHome()])
        ResetHomebtn.grid(row=4, column=7)
        Label(ControlsPageWin, text='Text to Speach', bg='#26343E', fg='White').place(x=840, y=375)
        TalkEntry = Entry(ControlsPageWin, width=35)
        TalkEntry.grid(row=5, column=7)
        TalkBtn = Button(ControlsPageWin, text='Talk', bg='lime', width=5, height=1)
        TalkBtn.grid(row=5,column=8)
        
        SaveBtn = Button(ControlsPageWin, text='save', bg='lime', command=lambda:[SaveArray()])
        SaveBtn.place(x=1250, y=750)
        RecoverBtns()
#====================================================Programs Page===========================================================
    def ProgramPage():
        print('opening Program page')
        HomepageWin.destroy()
        ProgramPageWin=Tk() 
        ProgramPageWin.title('Jarvis Controller') 
        ProgramPageWin.geometry('1500x1000')
        ProgramPageWin.configure(bg='#26343E')
        global Min
        global Max
        Min = 0
        Max = 0
        Home = 0
        def Add(Var1, Var2, Var3):
            global FuncArray
            AddArray = np.array([Var1, Var2, Var3])
            FuncArray = np.vstack([AddArray])
            print(FuncArray)
        def AddFunc(Func):
            if (Func == 'Move'):
                if (str(MoveVar.get()) == 'LS'):
                    print('LS')
                    Min = LSMin
                    Max = LSMax
                    MoveSlider = Scale(ProgramPageWin, orient=HORIZONTAL, from_ = Min, to=Max)
                    MoveSlider.grid(row=0,column=2)
                    MoveSlider.set(LSHome)
                    AddBtn = Button(ProgramPageWin, text='Add', command=lambda:[Add('Move','LS',str(MoveSlider.get()))])
                    AddBtn.grid(row=0, column=3)
                    print(Min)
                    print(Max)
                if (str(MoveVar.get()) == 'LX'):
                    print('LX')
                    Min = LXMin
                    Max = LXMax
                    MoveSlider = Scale(ProgramPageWin, orient=HORIZONTAL, from_ = Min, to=Max)
                    MoveSlider.grid(row=0,column=2)
                    MoveSlider.set(LXHome)
                    print(Min)
                    print(Max)
                    
        MoveBtn = Button(ProgramPageWin, text='Move(Motor,Amt)', command=lambda:[AddFunc('Move')])
        MoveBtn.grid(row=0,column=0)
        MoveVar=StringVar()
        MoveDropDown = OptionMenu(ProgramPageWin, MoveVar, "LS", "LX", "LY", "LB","LW","LT",)
        MoveDropDown.grid(row=0, column=1)

        
        
        
        BackBtn=Button(ProgramPageWin,text="Back", width=4,height=2,command=lambda: [ProgramPageWin.destroy(), Homepage()])
        BackBtn.place(x=1400,y=900)
        
        
#==================================================Points Page========================================================
    def PointsPage():
        print('opening Points page')
        HomepageWin.destroy()
        PointsPageWin=Tk() 
        PointsPageWin.title('Jarvis Controller') 
        PointsPageWin.geometry('1500x1000')
        PointsPageWin.configure(bg='#26343E')
        BackBtn=Button(PointsPageWin,text="Back", width=4,height=2,command=lambda: [PointsPageWin.destroy(), Homepage()])
        BackBtn.place(x=1400,y=900)
        
        Label(PointsPageWin, text='Point 1', bg='#26343E',fg='white').grid(row=0,column=0)
        Label(PointsPageWin, text=PointsArray[0], bg='#26343E',fg='white',font=("Helvetica", 8)).grid(row=0,column=1)
        
        Label(PointsPageWin, text='Point 2', bg='#26343E',fg='white').grid(row=1,column=0)
        Label(PointsPageWin, text=PointsArray[1], bg='#26343E',fg='white',font=("Helvetica", 8)).grid(row=1,column=1)
        
        Label(PointsPageWin, text='Point 3', bg='#26343E',fg='white').grid(row=2,column=0)
        Label(PointsPageWin, text=PointsArray[2], bg='#26343E',fg='white',font=("Helvetica", 8)).grid(row=2,column=1)
        
        Label(PointsPageWin, text='Point 4', bg='#26343E',fg='white').grid(row=3,column=0)
        Label(PointsPageWin, text=PointsArray[3], bg='#26343E',fg='white',font=("Helvetica", 8)).grid(row=3,column=1)
        
        Label(PointsPageWin, text='Point 5', bg='#26343E',fg='white').grid(row=4,column=0)
        Label(PointsPageWin, text=PointsArray[4], bg='#26343E',fg='white',font=("Helvetica", 8)).grid(row=4,column=1)
        
        Label(PointsPageWin, text='Point 6', bg='#26343E',fg='white').grid(row=5,column=0)
        Label(PointsPageWin, text=PointsArray[5], bg='#26343E',fg='white',font=("Helvetica", 8)).grid(row=5,column=1)
        
        Label(PointsPageWin, text='Point 7', bg='#26343E',fg='white').grid(row=6,column=0)
        Label(PointsPageWin, text=PointsArray[6], bg='#26343E',fg='white',font=("Helvetica", 8)).grid(row=6,column=1)
        
        Label(PointsPageWin, text='Point 8', bg='#26343E',fg='white').grid(row=7,column=0)
        Label(PointsPageWin, text=PointsArray[7], bg='#26343E',fg='white',font=("Helvetica", 8)).grid(row=7,column=1)
        
        Label(PointsPageWin, text='Point 9', bg='#26343E',fg='white').grid(row=8,column=0)
        Label(PointsPageWin, text=PointsArray[8], bg='#26343E',fg='white',font=("Helvetica", 8)).grid(row=8,column=1)
        
        Label(PointsPageWin, text='Point 10', bg='#26343E',fg='white').grid(row=9,column=0)
        Label(PointsPageWin, text=PointsArray[9], bg='#26343E',fg='white',font=("Helvetica", 8)).grid(row=9,column=1)
        
        Label(PointsPageWin, text='Point 11', bg='#26343E',fg='white').grid(row=10,column=0)
        Label(PointsPageWin, text=PointsArray[10], bg='#26343E',fg='white',font=("Helvetica", 8)).grid(row=10,column=1)
        
        Label(PointsPageWin, text='Point 12', bg='#26343E',fg='white').grid(row=11,column=0)
        Label(PointsPageWin, text=PointsArray[11], bg='#26343E',fg='white',font=("Helvetica", 8)).grid(row=11,column=1)
        
        Label(PointsPageWin, text='Point 13', bg='#26343E',fg='white').grid(row=12,column=0)
        Label(PointsPageWin, text=PointsArray[12], bg='#26343E',fg='white',font=("Helvetica", 8)).grid(row=12,column=1)
        
        Label(PointsPageWin, text='Point 14', bg='#26343E',fg='white').grid(row=13,column=0)
        Label(PointsPageWin, text=PointsArray[13], bg='#26343E',fg='white',font=("Helvetica", 8)).grid(row=13,column=1)
        
        Label(PointsPageWin, text='Point 15', bg='#26343E',fg='white').grid(row=14,column=0)
        Label(PointsPageWin, text=PointsArray[14], bg='#26343E',fg='white',font=("Helvetica", 8)).grid(row=14,column=1)
        
        Label(PointsPageWin, text='Point 15', bg='#26343E',fg='white').grid(row=14,column=0)
        Label(PointsPageWin, text=PointsArray[14], bg='#26343E',fg='white',font=("Helvetica", 8)).grid(row=14,column=1)
        
        Label(PointsPageWin, text='System Point C1', bg='#26343E',fg='white').grid(row=0,column=2)
        Label(PointsPageWin, text=SystemPointsArray[0], bg='#26343E',fg='white',font=("Helvetica", 8)).grid(row=0,column=3)
        
        Label(PointsPageWin, text='System Point C2', bg='#26343E',fg='white').grid(row=1,column=2)
        Label(PointsPageWin, text=SystemPointsArray[1], bg='#26343E',fg='white',font=("Helvetica", 8)).grid(row=1,column=3)
        
        Label(PointsPageWin, text='System Point C3', bg='#26343E',fg='white').grid(row=2,column=2)
        Label(PointsPageWin, text=SystemPointsArray[2], bg='#26343E',fg='white',font=("Helvetica", 8)).grid(row=2,column=3)
        
        Label(PointsPageWin, text='System Point C4', bg='#26343E',fg='white').grid(row=3,column=2)
        Label(PointsPageWin, text=SystemPointsArray[3], bg='#26343E',fg='white',font=("Helvetica", 8)).grid(row=3,column=3)

        Label(PointsPageWin, text='System Point C5', bg='#26343E',fg='white').grid(row=4,column=2)
        Label(PointsPageWin, text=SystemPointsArray[4], bg='#26343E',fg='white',font=("Helvetica", 8)).grid(row=4,column=3)
        
        Label(PointsPageWin, text='System Point C6', bg='#26343E',fg='white').grid(row=5,column=2)
        Label(PointsPageWin, text=SystemPointsArray[5], bg='#26343E',fg='white',font=("Helvetica", 8)).grid(row=5,column=3)
        
        Label(PointsPageWin, text='System Point C7', bg='#26343E',fg='white').grid(row=6,column=2)
        Label(PointsPageWin, text=SystemPointsArray[6], bg='#26343E',fg='white',font=("Helvetica", 8)).grid(row=6,column=3)
        
        Label(PointsPageWin, text='System Point C8', bg='#26343E',fg='white').grid(row=7,column=2)
        Label(PointsPageWin, text=SystemPointsArray[7], bg='#26343E',fg='white',font=("Helvetica", 8)).grid(row=7,column=3)

        
    def AdminPage():
        print('opening Admin page')
        HomepageWin.destroy()
        AdminPageWin=Tk() 
        AdminPageWin.title('Jarvis Controller') 
        AdminPageWin.geometry('1500x1000')
        AdminPageWin.configure(bg='#26343E')
        BackBtn=Button(AdminPageWin,text="Back",command=lambda: [AdminPageWin.destroy(), Homepage()])
        BackBtn.place(x=690,y=500)
        Label(AdminPageWin, text='Admin Password').grid(row=0)
        PasswordEntry=Entry(AdminPageWin)
        PasswordEntry.grid(row=0, column=1)
        AcceptBtn=Button(AdminPageWin,text="Accept",command=lambda: [print( PasswordEntry.get()), LoginCheck()])
        AcceptBtn.place(x=740,y=500)
        def LoginCheck():
            if (PasswordEntry.get() == 'InMoov'):
                print('access granted')
                AdminConfig()
            else:
                print('access denied')
        def AdminConfig():
            print('config page opened')
            AdminPageWin.destroy()
            AdminConfigPageWin=Tk() 
            AdminConfigPageWin.title('Jarvis Controller') 
            AdminConfigPageWin.geometry('1500x1000')
            AdminConfigPageWin.configure(bg='#26343E')
            BackBtn=Button(AdminConfigPageWin,text="Back", width=4,height=2,command=lambda: [AdminConfigPageWin.destroy(), Homepage()])
            BackBtn.place(x=1400,y=900)
            SaveBtn = Button(AdminConfigPageWin, text='Save Config', height=2, command=lambda:[reassign(),SaveConfig()])
            SaveBtn.place(x=1300, y=900)

            def reassign():
                global LSMin
                global LXMin
                global LYMin
                global LBMin
                global LWMin
                global LTMin
                global LIMin
                global LMMin
                global LRMin
                global LPMin
                global RSMin
                global RXMin
                global RYMin
                global RBMin
                global RWMin
                global RTMin
                global RIMin
                global RMMin
                global RRMin
                global RPMin
                global HPMin
                global HTMin
                global JMin
                global LSMax
                global LXMax
                global LYMax
                global LBMax
                global LWMax
                global LTMax
                global LIMax
                global LMMax
                global LRMax
                global LPMax
                global RSMax
                global RXMax
                global RYMax
                global RBMax
                global RWMax
                global RTMax
                global RIMax
                global RMMax
                global RRMax
                global RPMax
                global HPMax
                global HTMax
                global JMax
                global LSHome
                global LXHome
                global LYHome
                global LBHome
                global LWHome
                global LTHome
                global LIHome
                global LMHome
                global LRHome
                global LPHome
                global RSHome
                global RXHome
                global RYHome
                global RBHome
                global RWHome
                global RTHome
                global RIHome
                global RMHome
                global RRHome
                global RPHome
                global HPHome
                global HTHome
                global JHome
                LSMin = LSMinEntry.get()
                LXMin = LXMinEntry.get()
                LYMin = LYMinEntry.get()
                LBMin = LBMinEntry.get()
                LWMin = LWMinEntry.get()
                LTMin = LTMinEntry.get()
                LIMin = LIMinEntry.get()
                LMMin = LMMinEntry.get()
                LRMin = LRMinEntry.get()
                LPMin = LPMinEntry.get()
                RSMin = RSMinEntry.get()
                RXMin = RXMinEntry.get()
                RYMin = RYMinEntry.get()
                RBMin = RBMinEntry.get()
                RWMin = RWMinEntry.get()
                RTMin = RTMinEntry.get()
                RIMin = RIMinEntry.get()
                RMMin = RMMinEntry.get()
                RRMin = RRMinEntry.get()
                RPMin = RPMinEntry.get()
                HPMin = HPMinEntry.get()
                HTMin = HTMinEntry.get()
                JMin = JMinEntry.get()
            
                LSMax = LSMaxEntry.get()
                LXMax = LXMaxEntry.get()
                LYMax = LYMaxEntry.get()
                LBMax = LBMaxEntry.get()
                LWMax = LWMaxEntry.get()
                LTMax = LTMaxEntry.get()
                LIMax = LIMaxEntry.get()
                LMMax = LMMaxEntry.get()
                LRMax = LRMaxEntry.get()
                LPMax = LPMaxEntry.get()
                RSMax = RSMaxEntry.get()
                RXMax = RXMaxEntry.get()
                RYMax = RYMaxEntry.get()
                RBMax = RBMaxEntry.get()
                RWMax = RWMaxEntry.get()
                RTMax = RTMaxEntry.get()
                RIMax = RIMaxEntry.get()
                RMMax = RMMaxEntry.get()
                RRMax = RRMaxEntry.get()
                RPMax = RPMaxEntry.get()
                HPMax = HPMaxEntry.get()
                HTMax = HTMaxEntry.get()
                JMax = JMaxEntry.get()
                
                LSHome = LSHomeEntry.get()
                LXHome = LXHomeEntry.get()
                LYHome = LYHomeEntry.get()
                LBHome = LBHomeEntry.get()
                LWHome = LWHomeEntry.get()
                LTHome = LTHomeEntry.get()
                LIHome = LIHomeEntry.get()
                LMHome = LMHomeEntry.get()
                LRHome = LRHomeEntry.get()
                LPHome = LPHomeEntry.get()
                RSHome = RSHomeEntry.get()
                RXHome = RXHomeEntry.get()
                RYHome = RYHomeEntry.get()
                RBHome = RBHomeEntry.get()
                RWHome = RWHomeEntry.get()
                RTHome = RTHomeEntry.get()
                RIHome = RIHomeEntry.get()
                RMHome = RMHomeEntry.get()
                RRHome = RRHomeEntry.get()
                RPHome = RPHomeEntry.get()
                HPHome = HPHomeEntry.get()
                HTHome = HTHomeEntry.get()
                JHome = JHomeEntry.get()
        
                
                
            def Lockout(var):
                if (BtnArray[var] == 0):
                    BtnArray[var] = 1
                    print('locked')
                    
                else:
                    BtnArray[var] = 0
                    print('unlocked')
                
            def ColorChange():
                if (BtnArray[0] == 1):
                    LSLockout.config(bg ='red')
                if (BtnArray[0] == 0):
                    LSLockout.config(bg = 'green')
                if (BtnArray[1] == 1):
                    LXLockout.config(bg ='red')
                if (BtnArray[1] == 0):
                    LXLockout.config(bg = 'green')
                if (BtnArray[2] == 1):
                    LYLockout.config(bg ='red')
                if (BtnArray[2] == 0):
                    LYLockout.config(bg = 'green')
                if (BtnArray[3] == 1):
                    LBLockout.config(bg ='red')
                if (BtnArray[3] == 0):
                    LBLockout.config(bg = 'green')
                if (BtnArray[4] == 1):
                    LWLockout.config(bg ='red')
                if (BtnArray[4] == 0):
                    LWLockout.config(bg = 'green')
                if (BtnArray[5] == 1):
                    LTLockout.config(bg ='red')
                if (BtnArray[5] == 0):
                    LTLockout.config(bg = 'green')
                if (BtnArray[6] == 1):
                    LILockout.config(bg ='red')
                if (BtnArray[6] == 0):
                    LILockout.config(bg = 'green')
                if (BtnArray[7] == 1):
                    LMLockout.config(bg ='red')
                if (BtnArray[7] == 0):
                    LMLockout.config(bg = 'green')
                if (BtnArray[8] == 1):
                    LRLockout.config(bg ='red')
                if (BtnArray[8] == 0):
                    LRLockout.config(bg = 'green')
                if (BtnArray[9] == 1):
                    LPLockout.config(bg ='red')
                if (BtnArray[9] == 0):
                    LPLockout.config(bg = 'green')
                if (BtnArray[10] == 1):
                    RSLockout.config(bg ='red')
                if (BtnArray[10] == 0):
                    RSLockout.config(bg = 'green')
                if (BtnArray[11] == 1):
                    RXLockout.config(bg ='red')
                if (BtnArray[11] == 0):
                    RXLockout.config(bg = 'green')
                if (BtnArray[12] == 1):
                    RYLockout.config(bg ='red')
                if (BtnArray[12] == 0):
                    RYLockout.config(bg = 'green')
                if (BtnArray[13] == 1):
                    RBLockout.config(bg ='red')
                if (BtnArray[13] == 0):
                    RBLockout.config(bg = 'green')
                if (BtnArray[14] == 1):
                    RWLockout.config(bg ='red')
                if (BtnArray[14] == 0):
                    RWLockout.config(bg = 'green')
                if (BtnArray[15] == 1):
                    RTLockout.config(bg ='red')
                if (BtnArray[15] == 0):
                    RTLockout.config(bg = 'green')
                if (BtnArray[16] == 1):
                    RILockout.config(bg ='red')
                if (BtnArray[16] == 0):
                    RILockout.config(bg = 'green')
                if (BtnArray[17] == 1):
                    RMLockout.config(bg ='red')
                if (BtnArray[17] == 0):
                    RMLockout.config(bg = 'green')
                if (BtnArray[18] == 1):
                    RRLockout.config(bg ='red')
                if (BtnArray[18] == 0):
                    RRLockout.config(bg = 'green')
                if (BtnArray[19] == 1):
                    RPLockout.config(bg ='red')
                if (BtnArray[19] == 0):
                    RPLockout.config(bg = 'green')
                if (BtnArray[20] == 1):
                    HPLockout.config(bg ='red')
                if (BtnArray[20] == 0):
                    HPLockout.config(bg = 'green')
                if (BtnArray[21] == 1):
                    HTLockout.config(bg ='red')
                if (BtnArray[21] == 0):
                    HTLockout.config(bg = 'green')
                if (BtnArray[22] == 1):
                    JLockout.config(bg ='red')
                if (BtnArray[22] == 0):
                    JLockout.config(bg = 'green')

                
            Label(AdminConfigPageWin,bg='yellow', text='Warning: Changing admin config variables may result in damage to the robot.').place(x=0,y=0)
            Label(AdminConfigPageWin, bg='yellow',text='').grid(row=0,column=0)
            
            Label(AdminConfigPageWin, text='Minimums').grid(row=1,column=1)
            Label(AdminConfigPageWin, text='Maximums').grid(row=1,column=2)
            Label(AdminConfigPageWin, text='Home Values').grid(row=1,column=3)
            Label(AdminConfigPageWin, text='Maintnence Lockouts').grid(row=1,column=4)

            
            Label(AdminConfigPageWin,bg='#26343E', text='Left Shoulder  ').grid(row=2, column=0)
            LSMinEntry=Entry(AdminConfigPageWin)
            LSMinEntry.grid(row=2, column=1)
            LSMaxEntry=Entry(AdminConfigPageWin)
            LSMaxEntry.grid(row=2, column=2)
            LSHomeEntry=Entry(AdminConfigPageWin)
            LSHomeEntry.grid(row=2, column=3)
            LSLockout = Button(AdminConfigPageWin, text='Lockout', command=lambda:[print('locked LS'),Lockout(0), ColorChange()])
            LSLockout.grid(row=2, column=4)
            
            Label(AdminConfigPageWin,bg='#26343E', text='Left X-Arm ').grid(row=3, column=0)
            LXMinEntry=Entry(AdminConfigPageWin)
            LXMinEntry.grid(row=3, column=1)
            LXMaxEntry=Entry(AdminConfigPageWin)
            LXMaxEntry.grid(row=3, column=2)
            LXHomeEntry=Entry(AdminConfigPageWin)
            LXHomeEntry.grid(row=3, column=3)
            LXLockout = Button(AdminConfigPageWin, text='Lockout', command=lambda:[print('locked LX'),Lockout(1), ColorChange()])
            LXLockout.grid(row=3, column=4)
    
            Label(AdminConfigPageWin,bg='#26343E', text='Left Y-Arm ').grid(row=4, column=0)
            LYMinEntry=Entry(AdminConfigPageWin)
            LYMinEntry.grid(row=4, column=1)
            LYMaxEntry=Entry(AdminConfigPageWin)
            LYMaxEntry.grid(row=4, column=2)
            LYHomeEntry=Entry(AdminConfigPageWin)
            LYHomeEntry.grid(row=4, column=3)
            LYLockout = Button(AdminConfigPageWin, text='Lockout', command=lambda:[print('locked LY'),Lockout(2), ColorChange()])
            LYLockout.grid(row=4, column=4)
            
            Label(AdminConfigPageWin,bg='#26343E', text='Left Bicep ').grid(row=5, column=0)
            LBMinEntry=Entry(AdminConfigPageWin)
            LBMinEntry.grid(row=5, column=1)
            LBMaxEntry=Entry(AdminConfigPageWin)
            LBMaxEntry.grid(row=5, column=2)
            LBHomeEntry=Entry(AdminConfigPageWin)
            LBHomeEntry.grid(row=5, column=3)
            LBLockout = Button(AdminConfigPageWin, text='Lockout', command=lambda:[print('locked LB'),Lockout(3), ColorChange()])
            LBLockout.grid(row=5, column=4)
            
            Label(AdminConfigPageWin,bg='#26343E', text='Left Wrist ').grid(row=6, column=0)
            LWMinEntry=Entry(AdminConfigPageWin)
            LWMinEntry.grid(row=6, column=1)
            LWMaxEntry=Entry(AdminConfigPageWin)
            LWMaxEntry.grid(row=6, column=2)
            LWHomeEntry=Entry(AdminConfigPageWin)
            LWHomeEntry.grid(row=6, column=3)
            LWLockout = Button(AdminConfigPageWin, text='Lockout', command=lambda:[print('locked LW'),Lockout(4), ColorChange()])
            LWLockout.grid(row=6, column=4)
            
            Label(AdminConfigPageWin,bg='#26343E', text='Left Thumb ').grid(row=7, column=0)
            LTMinEntry=Entry(AdminConfigPageWin)
            LTMinEntry.grid(row=7, column=1)
            LTMaxEntry=Entry(AdminConfigPageWin)
            LTMaxEntry.grid(row=7, column=2)
            LTHomeEntry=Entry(AdminConfigPageWin)
            LTHomeEntry.grid(row=7, column=3)
            LTLockout = Button(AdminConfigPageWin, text='Lockout', command=lambda:[print('locked LT'),Lockout(5), ColorChange()])
            LTLockout.grid(row=7, column=4)
            
            Label(AdminConfigPageWin,bg='#26343E', text='Left Index ').grid(row=8, column=0)
            LIMinEntry=Entry(AdminConfigPageWin)
            LIMinEntry.grid(row=8, column=1)
            LIMaxEntry=Entry(AdminConfigPageWin)
            LIMaxEntry.grid(row=8, column=2)
            LIHomeEntry=Entry(AdminConfigPageWin)
            LIHomeEntry.grid(row=8, column=3)
            LILockout = Button(AdminConfigPageWin, text='Lockout', command=lambda:[print('locked LI'),Lockout(6), ColorChange()])
            LILockout.grid(row=8, column=4)
            
            Label(AdminConfigPageWin,bg='#26343E', text='Left Middle ').grid(row=9, column=0)
            LMMinEntry=Entry(AdminConfigPageWin)
            LMMinEntry.grid(row=9, column=1)
            LMMaxEntry=Entry(AdminConfigPageWin)
            LMMaxEntry.grid(row=9, column=2)
            LMHomeEntry=Entry(AdminConfigPageWin)
            LMHomeEntry.grid(row=9, column=3)
            LMLockout = Button(AdminConfigPageWin, text='Lockout', command=lambda:[print('locked LM'),Lockout(7), ColorChange()])
            LMLockout.grid(row=9, column=4)
            
            Label(AdminConfigPageWin,bg='#26343E', text='Left Ring ').grid(row=10, column=0)
            LRMinEntry=Entry(AdminConfigPageWin)
            LRMinEntry.grid(row=10, column=1)
            LRMaxEntry=Entry(AdminConfigPageWin)
            LRMaxEntry.grid(row=10, column=2)
            LRHomeEntry=Entry(AdminConfigPageWin)
            LRHomeEntry.grid(row=10, column=3)
            LRLockout = Button(AdminConfigPageWin, text='Lockout', command=lambda:[print('locked LR'),Lockout(8), ColorChange()])
            LRLockout.grid(row=10, column=4)
            
            Label(AdminConfigPageWin,bg='#26343E', text='Left Pinky ').grid(row=11, column=0)
            LPMinEntry=Entry(AdminConfigPageWin)
            LPMinEntry.grid(row=11, column=1)
            LPMaxEntry=Entry(AdminConfigPageWin)
            LPMaxEntry.grid(row=11, column=2)
            LPHomeEntry=Entry(AdminConfigPageWin)
            LPHomeEntry.grid(row=11, column=3)
            LPLockout = Button(AdminConfigPageWin, text='Lockout', command=lambda:[print('locked LP'),Lockout(9), ColorChange()])
            LPLockout.grid(row=11, column=4)
            
            Label(AdminConfigPageWin,bg='#26343E', text='Right Shoulder ').grid(row=12, column=0)
            RSMinEntry=Entry(AdminConfigPageWin)
            RSMinEntry.grid(row=12, column=1)
            RSMaxEntry=Entry(AdminConfigPageWin)
            RSMaxEntry.grid(row=12, column=2)
            RSHomeEntry=Entry(AdminConfigPageWin)
            RSHomeEntry.grid(row=12, column=3)
            RSLockout = Button(AdminConfigPageWin, text='Lockout', command=lambda:[print('locked RS'),Lockout(10), ColorChange()])
            RSLockout.grid(row=12, column=4)
            
            Label(AdminConfigPageWin,bg='#26343E', text='Right X-Arm ').grid(row=13, column=0)
            RXMinEntry=Entry(AdminConfigPageWin)
            RXMinEntry.grid(row=13, column=1)
            RXMaxEntry=Entry(AdminConfigPageWin)
            RXMaxEntry.grid(row=13, column=2)
            RXHomeEntry=Entry(AdminConfigPageWin)
            RXHomeEntry.grid(row=13, column=3)
            RXLockout = Button(AdminConfigPageWin, text='Lockout', command=lambda:[print('locked RX'),Lockout(11), ColorChange()])
            RXLockout.grid(row=13, column=4)

            Label(AdminConfigPageWin,bg='#26343E', text='Right Y-Arm ').grid(row=14, column=0)
            RYMinEntry=Entry(AdminConfigPageWin)
            RYMinEntry.grid(row=14, column=1)
            RYMaxEntry=Entry(AdminConfigPageWin)
            RYMaxEntry.grid(row=14, column=2)
            RYHomeEntry=Entry(AdminConfigPageWin)
            RYHomeEntry.grid(row=14, column=3)
            RYLockout = Button(AdminConfigPageWin, text='Lockout', command=lambda:[print('locked RY'),Lockout(12), ColorChange()])
            RYLockout.grid(row=14, column=4)
            
            Label(AdminConfigPageWin,bg='#26343E', text='Right Bicep ').grid(row=15, column=0)
            RBMinEntry=Entry(AdminConfigPageWin)
            RBMinEntry.grid(row=15, column=1)
            RBMaxEntry=Entry(AdminConfigPageWin)
            RBMaxEntry.grid(row=15, column=2)
            RBHomeEntry=Entry(AdminConfigPageWin)
            RBHomeEntry.grid(row=15, column=3)
            RBLockout = Button(AdminConfigPageWin, text='Lockout', command=lambda:[print('locked RB'),Lockout(13), ColorChange()])
            RBLockout.grid(row=15, column=4)
            
            Label(AdminConfigPageWin,bg='#26343E', text='Right Wrist ').grid(row=16, column=0)
            RWMinEntry=Entry(AdminConfigPageWin)
            RWMinEntry.grid(row=16, column=1)
            RWMaxEntry=Entry(AdminConfigPageWin)
            RWMaxEntry.grid(row=16, column=2)
            RWHomeEntry=Entry(AdminConfigPageWin)
            RWHomeEntry.grid(row=16, column=3)
            RWLockout = Button(AdminConfigPageWin, text='Lockout', command=lambda:[print('locked RW'),Lockout(14), ColorChange()])
            RWLockout.grid(row=16, column=4)
            
            Label(AdminConfigPageWin,bg='#26343E', text='Right Thumb ').grid(row=17, column=0)
            RTMinEntry=Entry(AdminConfigPageWin)
            RTMinEntry.grid(row=17, column=1)
            RTMaxEntry=Entry(AdminConfigPageWin)
            RTMaxEntry.grid(row=17, column=2)
            RTHomeEntry=Entry(AdminConfigPageWin)
            RTHomeEntry.grid(row=17, column=3)
            RTLockout = Button(AdminConfigPageWin, text='Lockout', command=lambda:[print('locked RT'),Lockout(15), ColorChange()])
            RTLockout.grid(row=17, column=4)
            
            Label(AdminConfigPageWin,bg='#26343E', text='Right Index ').grid(row=18, column=0)
            RIMinEntry=Entry(AdminConfigPageWin)
            RIMinEntry.grid(row=18, column=1)
            RIMaxEntry=Entry(AdminConfigPageWin)
            RIMaxEntry.grid(row=18, column=2)
            RIHomeEntry=Entry(AdminConfigPageWin)
            RIHomeEntry.grid(row=18, column=3)
            RILockout = Button(AdminConfigPageWin, text='Lockout', command=lambda:[print('locked RI'),Lockout(16), ColorChange()])
            RILockout.grid(row=18, column=4)
            
            Label(AdminConfigPageWin,bg='#26343E', text='Right Middle ').grid(row=19, column=0)
            RMMinEntry=Entry(AdminConfigPageWin)
            RMMinEntry.grid(row=19, column=1)
            RMMaxEntry=Entry(AdminConfigPageWin)
            RMMaxEntry.grid(row=19, column=2)
            RMHomeEntry=Entry(AdminConfigPageWin)
            RMHomeEntry.grid(row=19, column=3)
            RMLockout = Button(AdminConfigPageWin, text='Lockout', command=lambda:[print('locked RM'),Lockout(17), ColorChange()])
            RMLockout.grid(row=19, column=4)
            
            Label(AdminConfigPageWin,bg='#26343E', text='Right Ring ').grid(row=20, column=0)
            RRMinEntry=Entry(AdminConfigPageWin)
            RRMinEntry.grid(row=20, column=1)
            RRMaxEntry=Entry(AdminConfigPageWin)
            RRMaxEntry.grid(row=20, column=2)
            RRHomeEntry=Entry(AdminConfigPageWin)
            RRHomeEntry.grid(row=20, column=3)
            RRLockout = Button(AdminConfigPageWin, text='Lockout', command=lambda:[print('locked RR'),Lockout(18), ColorChange()])
            RRLockout.grid(row=20, column=4)
            
            Label(AdminConfigPageWin,bg='#26343E', text='Right Pinky ').grid(row=21, column=0)
            RPMinEntry=Entry(AdminConfigPageWin)
            RPMinEntry.grid(row=21, column=1)
            RPMaxEntry=Entry(AdminConfigPageWin)
            RPMaxEntry.grid(row=21, column=2)
            RPHomeEntry=Entry(AdminConfigPageWin)
            RPHomeEntry.grid(row=21, column=3)
            RPLockout = Button(AdminConfigPageWin, text='Lockout', command=lambda:[print('locked RP'),Lockout(19), ColorChange()])
            RPLockout.grid(row=21, column=4)
            
            Label(AdminConfigPageWin,bg='#26343E', text='Head Pan ').grid(row=22, column=0)
            HPMinEntry=Entry(AdminConfigPageWin)
            HPMinEntry.grid(row=22, column=1)
            HPMaxEntry=Entry(AdminConfigPageWin)
            HPMaxEntry.grid(row=22, column=2)
            HPHomeEntry=Entry(AdminConfigPageWin)
            HPHomeEntry.grid(row=22, column=3)
            HPLockout = Button(AdminConfigPageWin, text='Lockout', command=lambda:[print('locked HP'),Lockout(20), ColorChange()])
            HPLockout.grid(row=22, column=4)
            
            Label(AdminConfigPageWin,bg='#26343E', text='Head Tilt ').grid(row=23, column=0)
            HTMinEntry=Entry(AdminConfigPageWin)
            HTMinEntry.grid(row=23, column=1)
            HTMaxEntry=Entry(AdminConfigPageWin)
            HTMaxEntry.grid(row=23, column=2)
            HTHomeEntry=Entry(AdminConfigPageWin)
            HTHomeEntry.grid(row=23, column=3)
            HTLockout = Button(AdminConfigPageWin, text='Lockout', command=lambda:[print('locked HT'),Lockout(21), ColorChange()])
            HTLockout.grid(row=23, column=4)
            
            Label(AdminConfigPageWin,bg='#26343E', text='Jaw ').grid(row=24, column=0)
            JMinEntry=Entry(AdminConfigPageWin)
            JMinEntry.grid(row=24, column=1)
            JMaxEntry=Entry(AdminConfigPageWin)
            JMaxEntry.grid(row=24, column=2)
            JHomeEntry=Entry(AdminConfigPageWin)
            JHomeEntry.grid(row=24, column=3)
            JLockout = Button(AdminConfigPageWin, text='Lockout', command=lambda:[print('locked J'),Lockout(22), ColorChange()])
            JLockout.grid(row=24, column=4)
            
            def assignhome():
                LSMinEntry.insert(LSMin, str(LSMin))
                LYMinEntry.insert(LYMin, str(LYMin))
                LXMinEntry.insert(LXMin, str(LXMin))
                LBMinEntry.insert(LBMin, str(LBMin))
                LWMinEntry.insert(LWMin, str(LWMin))
                LTMinEntry.insert(LTMin, str(LTMin))
                LIMinEntry.insert(LIMin, str(LIMin))
                LMMinEntry.insert(LMMin, str(LMMin))
                LRMinEntry.insert(LRMin, str(LRMin))
                LPMinEntry.insert(LPMin, str(LPMin))
                RSMinEntry.insert(RSMin, str(RSMin))
                RYMinEntry.insert(RYMin, str(RYMin))
                RXMinEntry.insert(RXMin, str(RXMin))
                RBMinEntry.insert(RBMin, str(RBMin))
                RWMinEntry.insert(RWMin, str(RWMin))
                RTMinEntry.insert(RTMin, str(RTMin))
                RIMinEntry.insert(RIMin, str(RIMin))
                RMMinEntry.insert(RMMin, str(RMMin))
                RRMinEntry.insert(RRMin, str(RRMin))
                RPMinEntry.insert(RPMin, str(RPMin))
                HPMinEntry.insert(HPMin, str(HPMin))
                HTMinEntry.insert(HTMin, str(HTMin))
                JMinEntry.insert(JMin, str(JMin))
                LSMaxEntry.insert(LSMax, str(LSMax))
                LYMaxEntry.insert(LYMax, str(LYMax))
                LXMaxEntry.insert(LXMax, str(LXMax))
                LBMaxEntry.insert(LBMax, str(LBMax))
                LWMaxEntry.insert(LWMax, str(LWMax))
                LTMaxEntry.insert(LTMax, str(LTMax))
                LIMaxEntry.insert(LIMax, str(LIMax))
                LMMaxEntry.insert(LMMax, str(LMMax))
                LRMaxEntry.insert(LRMax, str(LRMax))
                LPMaxEntry.insert(LPMax, str(LPMax))
                RSMaxEntry.insert(RSMax, str(RSMax))
                RYMaxEntry.insert(RYMax, str(RYMax))
                RXMaxEntry.insert(RXMax, str(RXMax))
                RBMaxEntry.insert(RBMax, str(RBMax))
                RWMaxEntry.insert(RWMax, str(RWMax))
                RTMaxEntry.insert(RTMax, str(RTMax))
                RIMaxEntry.insert(RIMax, str(RIMax))
                RMMaxEntry.insert(RMMax, str(RMMax))
                RRMaxEntry.insert(RRMax, str(RRMax))
                RPMaxEntry.insert(RPMax, str(RPMax))
                HTMaxEntry.insert(HTMax, str(HTMax))
                HPMaxEntry.insert(HPMax, str(HPMax))
                JMaxEntry.insert(JMax, str(JMax))
                LSHomeEntry.insert(LSHome, str(LSHome))
                LYHomeEntry.insert(LYHome, str(LYHome))
                LXHomeEntry.insert(LXHome, str(LXHome))
                LBHomeEntry.insert(LBHome, str(LBHome))
                LWHomeEntry.insert(LWHome, str(LWHome))
                LTHomeEntry.insert(LTHome, str(LTHome))
                LIHomeEntry.insert(LIHome, str(LIHome))
                LMHomeEntry.insert(LMHome, str(LMHome))
                LRHomeEntry.insert(LRHome, str(LRHome))
                LPHomeEntry.insert(LPHome, str(LPHome))
                RSHomeEntry.insert(RSHome, str(RSHome))
                RYHomeEntry.insert(RYHome, str(RYHome))
                RXHomeEntry.insert(RXHome, str(RXHome))
                RBHomeEntry.insert(RBHome, str(RBHome))
                RWHomeEntry.insert(RWHome, str(RWHome))
                RTHomeEntry.insert(RTHome, str(RTHome))
                RIHomeEntry.insert(RIHome, str(RIHome))
                RMHomeEntry.insert(RMHome, str(RMHome))
                RRHomeEntry.insert(RRHome, str(RRHome))
                RPHomeEntry.insert(RPHome, str(RPHome))
                HTHomeEntry.insert(HTHome, str(HTHome))
                HPHomeEntry.insert(HPHome, str(HPHome))
                JHomeEntry.insert(JHome, str(JHome))
                
            assignhome()
            ColorChange()
                

    print('opening Home page')
    HomepageWin=Tk()
    HomepageWin.title('Jarvis Controller')
    HomepageWin.geometry('1400x900')
    HomepageWin.configure(bg='#26343E')
    label = Label(text='Welcome to the Jarvis Controller', font=("Helvetica", 24),bg='#949FA0')
    label.pack()
    label = Label(HomepageWin,text='Demos',font=("Helvetica", 24), width=10,bg='#949FA0')
    label.place(x=1190,y=0)
    def Count():
        LTMove(500)
        LIMove(500)
        LMMove(440)
        LRMove(225)
        LPMove(225)
        RTMove(RTMax)
        RIMove(RIMin)
        RMMove(RMMax)
        RRMove(RRMax)
        RPMove(RPMax)
        time.sleep(.5)
        LIMove(275)
        time.sleep(.5)
        LMMove(300)
        time.sleep(.5)
        LRMove(375)
        time.sleep(.5)
        LPMove(400)
        time.sleep(.5)
        LTMove(300)
        time.sleep(.5)
        RIMove(RIMax)
        time.sleep(.5)
        RMMove(RMMin)
        time.sleep(.5)
        RRMove(RRMin)
        time.sleep(.5)
        RPMove(RPMin)
        time.sleep(.5)
        RTMove(RTMin)
        print('done')
        
        
    def RockOut():
        LTMove(300)
        LIMove(275)
        LPMove(225)
        LMMove(440)
        LRMove(225)
        LBMove(LBMax)
        time.sleep(.1)
        LXMove(500)
        time.sleep(.1)
        HTMove(300)
        time.sleep(.15)
        HTMove(150)
        time.sleep(.15)
        HTMove(300)
        time.sleep(.15)
        HTMove(150)
        time.sleep(.15)
        HTMove(300)
        print('done')
        
    def Nod():
        HTMove(300)
        time.sleep(.15)
        HTMove(150)
        time.sleep(.15)
        HTMove(300)
        time.sleep(.15)
        HTMove(150)
        time.sleep(.15)
        HTMove(300)
        print('done')
        
    def Music():
        for i in range(700):
            Speakers(i)
            time.sleep(.01)
        time.sleep(.2)
        Speakers(1)
        Speakers(1)
    CountBtn = Button(HomepageWin, text='Count', width=10, font=("Helvetica", 18),bg='#949FA0', command=lambda:[Count(), print('counting')])
    CountBtn.place(x=1200, y=75)
    
    DanceBtn = Button(HomepageWin, text='Music?', width=10,font=("Helvetica", 18),bg='#949FA0', command=lambda:[Music(),print('dancing')])
    DanceBtn.place(x=1200, y=150)
    
    NodBtn = Button(HomepageWin, text='Nod', width=10,font=("Helvetica", 18),bg='#949FA0', command=lambda:[Nod(), print('noding')])
    NodBtn.place(x=1200, y=225)
          
    ControlBtn=Button(HomepageWin,text="Controls", font=("Helvetica", 18),bg='#949FA0', width=20,height=2,command=lambda: [ControlsPage()])
    ControlBtn.place(x=0,y=100)

    ProgramBtn=Button(HomepageWin,text="Program",font=("Helvetica", 18),bg='#949FA0', width=20,height=2,command=ProgramPage)
    ProgramBtn.place(x=0,y=200)

    PointsBtn=Button(HomepageWin,text="Points",font=("Helvetica", 18),bg='#949FA0', width=20,height=2,command=PointsPage)
    PointsBtn.place(x=0,y=300)

    AdminBtn=Button(HomepageWin,text="Admin",font=("Helvetica", 18),bg='#949FA0', width=20,height=2,command=AdminPage)
    AdminBtn.place(x=0,y=400)
    
    ConnectBtn = Button(HomepageWin,text='Connect',font=("Helvetica", 18),bg='#949FA0', width=20,height=2,command=lambda:[defcomms()])
    ConnectBtn.place(x=0,y=500)
        
    HomepageWin.mainloop()
Homepage()
