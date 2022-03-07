version = str("1.1.2 release")
lgTr = True
import time as t
def lfwm(lfwt):
    if lgTr == True:
        logf2 = open('protonAssets/logs.txt', 'a')
        xyz = f"{str(t.time())} - {lfwt}"
        abc = ["", xyz]
        logf2.writelines('\n'.join(abc))
        logf2.close()
def wait(timeWait):
    t.sleep(timeWait)
def space(gaps):
    for i in range(0,gaps):
        print("")
try:
    import os
    import keyboard as key
    import pyautogui as pygui
    import pydirectinput as pyguia
    import random as ra
    import tkinter as tk
    from tkinter import *
    import tkinter.messagebox
    import threading as trng
    import webbrowser as webR
    import playsound as ps
    import linecache as lica
except:
    run = False
    print("error011 required modules not found")
    lfwm("error011 modulesAbsent")
    space(1)
    print("Please verify 'pyautogui', 'playsound' and 'tkinter' are installed.")
    wait(9)
    quit()
try:
    def NF(a,b):
        print(f"{a} - {b}")
    def protonLogo():
        space(1)
        print('''######  ######  ######  #######  ######  #    #
#    #  #    #  #    #     #     #    #  ##   #
#    #  #    #  #    #     #     #    #  # #  #
######  ######  #    #     #     #    #  #  # #
#       #  #    #    #     #     #    #  #   ##
#       #   #   ######     #     ######  #    #
Minecraft Hack Client
Version ''' + version + ''', no known bugs''')
    def protonCredit():
        space(2)
        print('''
Twitter  @fortquake
Discord  Fort Quake#3107
Reddit   r/fortquake

*Programming
Fort Quake

*Sound Effects
https://www.freesoundslibrary.com

*Modules
pyautogui
keyboard
tkinter
threading
random
time

Coded with Python 3.9
Published on GitHub

Thanks for choosing Proton
    ''')
    def protonHelp():
        print('''
Help

Commands
    ''')
        kB0 = open('protonAssets/keybinds.txt','rt')
        tCo = kB0.read()
        print(tCo)
        kB0.close()
        print('''
Modifing an existing command\n
Edit the commands.txt document
    ''')
    def protonPatch():
        print('''
Patch Notes
(for previous patch notes, see patchnotes.txt)

''' + version + '''
Changed
Merged statements onto one line (now under 1000 lines of code)
Changed some phrasing of text.
    ''')
    def error1():
        tkinter.messagebox.showerror('Proton', 'Requested feature not available in this version.')
    def er():
        ps.playsound("protonAssets/sd3.mp3")
    def nt():
        ps.playsound("protonAssets/sd1.mp3")
except:
    run = False
    print("error001 problem defining variables")
    lfwm("error001 variableDefine")
global p
wait(0.02)
p = True
run = True
c = 0
ll = False
rl = False
fd = False
bd = False
lt = False
rt = False
jp = False
st = False
ch = False
ak = False
for i in range (1,7):
    exec(f"sta{i} = False")
for i in range (1,7):
    exec(f"stb{i} = 1")
for i in range (0,16):
    exec(f"jC{i} = False")
for i in range (0,16):
    exec(f"ajc{i} = 3")
lgTr = False
try:
    kB = open("protonAssets/keybinds.txt", "r")
    kBr = kB.readlines()
except:
    run = False
    er()
    print("error002 error accessing keybinds.txt")
    lfwm("error002 accessingKeybinds")
try:
    logf1 = open("protonAssets/logs.txt", "a")
    abc = ["", f"{str(t.time())} - eventLaunch, ver {version}"]
    logf1.writelines('\n'.join(abc))
    logf1.close()
except:
    er()
    print("error003 error accessing logs.txt")
    lfwm("error003 accessingLogs\n")
    print("No logs will be made.")
    lgTr = False
for j in (kBr):
    try:
        if j[1] == chr(32):
            if c == 1: ll1 = j[0]
            elif c == 2: rl1 = j[0]
            elif c == 3: fd1 = j[0]
            elif c == 4: bd1 = j[0]
            elif c == 5: lt1 = j[0]
            elif c == 6: rt1 = j[0]
            elif c == 7: jp1 = j[0]
            elif c == 8: st1 = j[0]
            elif c == 9: ch1 = j[0]
            elif c == 10: ak1 = j[0]
            elif c == 11: af1 = j[0]
            elif c == 12: cs1 = j[0]
            elif c == 13: ct1 = j[0]
            elif c == 14: hp1 = j[0]
            elif c == 15: co1 = j[0]
            elif c == 16: at1 = j[0]
            elif c == 17: at2 = j[0]
            elif c == 18: at3 = j[0]
            elif c == 19: at4 = j[0]
            elif c == 20: at5 = j[0]
            elif c == 21: at6 = j[0]
            elif c == 23: fd2 = j[0]
            elif c == 24: bd2 = j[0]
            elif c == 25: lt2 = j[0]
            elif c == 26: rt2 = j[0]
            elif c == 27: jp2 = j[0]
            elif c == 28: st2 = j[0]
            elif c == 29: ch2 = j[0]
            elif c == 30: ca1 = j[0]
            elif c == 31: db1 = j[0]
            elif c == 33:
                xx2 = j[0]
                if j[0] == 'y':
                    NF("GUI","On")
                    guiS = True
                elif j[0] == 'n':
                    NF("GUI","Off")
                    guiS = False
                elif xx2 == 'm':
                    cg = False
                    while cg == False:
                        try:
                            print("Do you wish to enable the GUI? y/n")
                            logggg = str(input()).lower()
                            space(1)
                            if logggg == 'y' or logggg == 'yes' or logggg == 'yeah':
                                NF("GUI","On")
                                guiS = True
                                cg = True
                            elif logggg == 'n' or logggg == 'no' or logggg == 'nah':
                                NF("GUI","Off")
                                guiS = False
                                cg = True
                        except:
                            pass
            elif c == 34:
                zz2 = j[0]
                if j[0] == 'y':
                    NF("Logging","On")
                    lgTr = True
                elif j[0] == 'n':
                    NF("Logging","Off")
                    lgTr = False
                elif j[0] == 'm':
                    cg = False
                    while cg == False:
                        try:
                            print("Do you wish to enable logging? y/n")
                            loggg = str(input()).lower()
                            space(1)
                            if loggg == 'y' or loggg == 'yes' or loggg == 'yeah':
                                NF("Logging","On")
                                lgTr = True
                                cg = True
                            elif loggg == 'n' or loggg == 'no' or loggg == 'nah':
                                NF("Logging","Off")
                                lgTr = False
                                cg = True
                        except:
                            pass
        elif j[0] == chr(115) and j[1] == chr(104):
            if c == 1: ll1 = 'shift'
            elif c == 2: rl1 = 'shift'
            elif c == 3: fd1 = 'shift'
            elif c == 4: bd1 = 'shift'
            elif c == 5: lt1 = 'shift'
            elif c == 6: rt1 = 'shift'
            elif c == 7: jp1 = 'shift'
            elif c == 8: st1 = 'shift'
            elif c == 9: ch1 = 'shift'
            elif c == 10: ak1 = 'shift'
            elif c == 11: af1 = 'shift'
            elif c == 12: cs1 = 'shift'
            elif c == 13: ct1 = 'shift'
            elif c == 14: hp1 = 'shift'
            elif c == 15: co1 = 'shift'
            elif c == 16: at1 = 'shift'
            elif c == 17: at2 = 'shift'
            elif c == 18: at3 = 'shift'
            elif c == 19: at4 = 'shift'
            elif c == 20: at5 = 'shift'
            elif c == 21: at6 = 'shift'
            elif c == 23: fd2 = 'shift'
            elif c == 24: bd2 = 'shift'
            elif c == 25: lt2 = 'shift'
            elif c == 26: rt2 = 'shift'
            elif c == 27: jp2 = 'shift'
            elif c == 28: st2 = 'shift'
            elif c == 29: ch2 = 'shift'
            elif c == 30: ca1 = 'shift'
            elif c == 31: db1 = 'shift'
        elif j[0] == chr(115) and j[1] == chr(112):
            if c == 1: ll1 = 'space'
            elif c == 2: rl1 = 'space'
            elif c == 3: fd1 = 'space'
            elif c == 4: bd1 = 'space'
            elif c == 5: lt1 = 'space'
            elif c == 6: rt1 = 'space'
            elif c == 7: jp1 = 'space'
            elif c == 8: st1 = 'space'
            elif c == 9: ch1 = 'space'
            elif c == 10: ak1 = 'space'
            elif c == 11: af1 = 'space'
            elif c == 12: cs1 = 'space'
            elif c == 13: ct1 = 'space'
            elif c == 14: hp1 = 'space'
            elif c == 15: co1 = 'space'
            elif c == 16: at1 = 'space'
            elif c == 17: at2 = 'space'
            elif c == 18: at3 = 'space'
            elif c == 19: at4 = 'space'
            elif c == 20: at5 = 'space'
            elif c == 21: at6 = 'space'
            elif c == 23: fd2 = 'space'
            elif c == 24: bd2 = 'space'
            elif c == 25: lt2 = 'space'
            elif c == 26: rt2 = 'space'
            elif c == 27: jp2 = 'space'
            elif c == 28: st2 = 'space'
            elif c == 29: ch2 = 'space'
            elif c == 30: ca1 = 'space'
            elif c == 31: db1 = 'space'                
        elif j[0] == chr(99) and j[1] == chr(116):
            if c == 1: ll1 = 'ctrl'
            elif c == 2: rl1 = 'ctrl'
            elif c == 3: fd1 = 'ctrl'
            elif c == 4: bd1 = 'ctrl'
            elif c == 5: lt1 = 'ctrl'
            elif c == 6: rt1 = 'ctrl'
            elif c == 7: jp1 = 'ctrl'
            elif c == 8: st1 = 'ctrl'
            elif c == 9: ch1 = 'ctrl'
            elif c == 10: ak1 = 'ctrl'
            elif c == 11: af1 = 'ctrl'
            elif c == 12: cs1 = 'ctrl'
            elif c == 13: ct1 = 'ctrl'
            elif c == 14: hp1 = 'ctrl'
            elif c == 15: co1 = 'ctrl'
            elif c == 16: at1 = 'ctrl'
            elif c == 17: at2 = 'ctrl'
            elif c == 18: at3 = 'ctrl'
            elif c == 19: at4 = 'ctrl'
            elif c == 20: at5 = 'ctrl'
            elif c == 21: at6 = 'ctrl'
            elif c == 23: fd2 = 'ctrl'
            elif c == 24: bd2 = 'ctrl'
            elif c == 25: lt2 = 'ctrl'
            elif c == 26: rt2 = 'ctrl'
            elif c == 27: jp2 = 'ctrl'
            elif c == 28: st2 = 'ctrl'
            elif c == 29: ch2 = 'ctrl'
            elif c == 30: ca1 = 'ctrl'
            elif c == 31: db1 = 'ctrl'
        c += 1
    except: pass
try:
   chat1 = lica.getline("protonAssets\keybinds.txt", 37)
   chat2 = lica.getline("protonAssets\keybinds.txt", 38)
   chat3 = lica.getline("protonAssets\keybinds.txt", 39)
   chat4 = lica.getline("protonAssets\keybinds.txt", 40)
   chat5 = lica.getline("protonAssets\keybinds.txt", 41)
   chat6 = lica.getline("protonAssets\keybinds.txt", 42)
except:
    er()
    print("error013 error accessing text for chat spam")
    lfwm("error013 errorChatSpamGet")
try:
    lfwm("eventKeybindsAccessed")
    logf2 = open('protonAssets/logs.txt', 'a')
    abc = ["", f"{str(t.time())} - load1"]
    logf2.writelines('\n'.join(abc))
    logf2.close()
    guiS = False
    protonLogo()
    altf4 = False
except:
    er()
    print("error004 gui activation error")
    lfwm("error004 guiActivation")
lfwm("load2")
isPc1, isPc2 = 1, 1
thPc1, thPc2 = 1, 1

if guiS == False:
    space(2)
    print(f"Press '{hp1}' for a list of commands")
    space(10)
    def disablr():
        ll = False
        rl = False
        fd = False
        bd = False
        lt = False
        rt = False
        jp = False
        st = False
        ch = False
        for i in range (1,7):
            exec(f"sta{i} = False")
    def isP1():
        global isPc1
        if isPc1 == 1:
            global ll, rl, fd, bd, lt, rt, jp, st, ch, ak
            global sta1, sta2, sta3, sta4, sta5, sta6
            global jC1, jC2, jC3, jC4, jC5, jC6, jC7, jC8, jC9, jC0, jC10, jC11, jC12, jC13, jC14, jC15
            global ajc0, ajc1, ajc2, ajc3, ajc4, ajc5, ajc6, ajc7, ajc8, ajc9, ajc10, ajc11, ajc12, ajc13, ajc14, ajc15
            isPc1 = 2
        try:
            if jC1 == False:
                if key.is_pressed(ll1):
                    if ll == False:
                        ll = True
                        NF("Left Click","On")
                        lfwm("modLCon")
                    elif ll == True:
                        ll = False
                        NF("Left Click","Off")
                        lfwm("modLCoff")
                    jC1 = False
                    nt()
                    ajc1 = 5
            if jC1 == True:
                if ajc1 == 1:
                    jC1 = False
                else:
                    ajc1 = ajc1 - 1
            if jC2 == False:
                if key.is_pressed(rl1):
                    if rl == False:
                        rl = True
                        NF("Right Click","On")
                        lfwm("modRCon")
                    elif rl == True:
                        rl = False
                        NF("Right Click","Off")
                        lfwm("modRCoff")
                    jC2 = False
                    nt()
                    ajc2 = 5
            elif jC2 == False:
                if ajc2 == 1:
                    jC2 = False
                else:
                    ajc2 = ajc2 - 1
            if jC3 == False:
                if key.is_pressed(fd1):
                    if fd == False:
                        fd = True
                        NF("Forward","On")
                        lfwm("modFDon")
                    elif fd == True:
                        fd = False
                        NF("Forward","Off")
                        lfwm("modFDoff")
                    jC3 = True
                    nt()
                    ajc3 = 5
            elif jC3 == True:
                if ajc3 == 1:
                    jC3 = False
                else:
                    ajc3 = ajc3 - 1
            if jC4 == False:
                if key.is_pressed(bd1):
                    if bd == False:
                        bd = True
                        NF("Backward","On")
                        lfwm("modBDon")
                    elif bd == True:
                        bd = False
                        NF("Backward","Off")
                        lfwm("modBDoff")
                    jC4 = True
                    nt()
                    ajc4 = 5
            elif jC4 == True:
                if ajc4 == 1:
                    jC4 = False
                else:
                    ajc4 = ajc4 - 1
            if jC5 == False:
                if key.is_pressed(lt1):
                    if lt == False:
                        lt = True
                        NF("Left","On")
                        lfwm("modLTon")
                    elif lt == True:
                        lt = False
                        NF("Left","Off")
                        lfwm("modLToff")
                    jC5 = True
                    nt()
                    ajc5 = 5
            elif jC5 == True:
                if ajc5 == 1:
                    jC5 = False
                else:
                    ajc5 = ajc5 - 1
            if jC6 == False:
                if key.is_pressed(rt1):
                    if rt == False:
                        rt = True
                        NF("Right","On")
                        lfwm("modRTon")
                    elif rt == True:
                        rt = False
                        NF("Right","Off")
                        lfwm("modRToff")
                    jC6 = True
                    nt()
                    ajc6 = 5
            elif jC6 == True:
                if ajc6 == 1:
                    jC6 = False
                else:
                    ajc6 = ajc6 - 1
            if jC7 == False:
                if key.is_pressed(jp1):
                    if jp == False:
                        jp = True
                        NF("Jump","On")
                        lfwm("modJPon")
                    elif jp == True:
                        jp = False
                        NF("Jump","Off")
                        lfwm("modJPoff")
                    jC7 = True
                    nt()
                    ajc7 = 5
            elif jC7 == True:
                if ajc7 == 1:
                    jC7 = False
                else:
                    ajc7 = ajc7 - 1
            if jC8 == False:
                if key.is_pressed(st1):
                    if st == False:
                        st = True
                        NF("Sprint","On")
                        lfwm("modSPon")
                    elif st == True:
                        st = False
                        NF("Sprint","Off")
                        lfwm("modSPoff")
                    jC8 = True
                    nt()
                    ajc8 = 5
            elif jC8 == True:
                if ajc8 == 1:
                    jC8 = False
                else:
                    ajc8 = ajc8 - 1
            if jC9 == False:
                if key.is_pressed(ch1):
                    if ch == False:
                        ch = True
                        NF("Crouch","On")
                        lfwm("modCHon")
                    elif ch == True:
                        ch = False
                        NF("Crouch","Off")
                        lfwm("modCHoff")
                    jC9 = True
                    nt()
                    ajc9 = 5
            elif jC9 == True:
                if ajc9 == 1:
                    jC9 = False
                else:
                    ajc9 = ajc9 - 1
            if jC0 == False:
                if key.is_pressed(ak1):
                    if ak == False:
                        disablr()
                        ak = True
                        NF("Anti AFK","On")
                        lfwm("modAKon")
                    elif ak == True:
                        ak = False
                        NF("Anti AFK","Off")
                        lfwm("modAKoff")
                    jC0 = True
                    nt()
                    ajc0 = 5
            elif jC0 == True:
                if ajc0 == 1:
                    jC0 = False
                else:
                    ajc0 = ajc0 - 1
            elif key.is_pressed(af1):
                nt()
                disablr()
                key.release("shift")
                NF("All","Off")
                lfwm("modALoff")
        except:
            er()
            print("error005 click check error")
            lfwm("error005 clickCheck")
    def isP2():
        global isPc2
        if isPc2 == 1:
            global ll, rl, fd, bd, lt, rt, jp, st, ch, ak
            global sta1, sta2, sta3, sta4, sta5, sta6
            global jC1, jC2, jC3, jC4, jC5, jC6, jC7, jC8, jC9, jC0, jC10, jC11, jC12, jC13, jC14, jC15
            global ajc0, ajc1, ajc2, ajc3, ajc4, ajc5, ajc6, ajc7, ajc8, ajc9, ajc10, ajc11, ajc12, ajc13, ajc14, ajc15
            isPc2 = 2
        try:
            if key.is_pressed(cs1):
                lfwm("eventCredits")
                nt()
                wait(0.1)
                protonLogo()
                protonCredit()
                wait(0.1)
            elif key.is_pressed(hp1):
                lfwm("eventHelp")
                nt()
                protonLogo()
                protonHelp()
            elif key.is_pressed(co1):
                lfwm("eventPatch")
                nt()
                protonLogo()
                protonPatch()
            if key.is_pressed(ct1):
                lfwm("eventClose")
                nt()
                wait(0.1)
                NF("Program","Closed")
                kB.close()
                logf1.close()
                exit()
            if jC10 == False:
                if key.is_pressed(at1):
                    if sta1 == False:
                        disablr()
                        sta1 = True
                        NF("Chat Spam 1","On")
                        lfwm("modCHSP1on")
                    elif sta1 == True:
                        sta1 = False
                        NF("Chat Spam 1","Off")
                        lfwm("modCHSP1off")
                    jC10 = True
                    nt()
                    ajc10 = 5
            elif jC10 == True:
                if ajc10 == 1:
                    jC10 = False
                else:
                    ajc10 = ajc10 - 1
            if jC11 == False:
                if key.is_pressed(at2):
                    if sta2 == False:
                        disablr()
                        sta2 = True
                        NF("Chat Spam 2","On")
                        lfwm("modCHSP2on")
                    elif sta2 == True:
                        sta2 = False
                        NF("Chat Spam 2","Off")
                        lfwm("modCHSP2off")
                    jC11 = True
                    nt()
                    ajc11 = 5
            elif jC11 == True:
                if ajc11 == 1:
                    jC11 = False
                else:
                    ajc11 = ajc11 - 1
            if jC12 == False:
                if key.is_pressed(at3):
                    if sta3 == False:
                        disablr()
                        sta3 = True
                        NF("Chat Spam 3","On")
                        lfwm("modCHSP3on")
                    elif sta3 == True:
                        sta3 = False
                        NF("Chat Spam 3","Off")
                        lfwm("modCHSP3off")
                    jC12 = True
                    nt()
                    ajc12 = 5
            elif jC12 == True:
                if ajc12 == 1:
                    jC12 = False
                else:
                    ajc12 = ajc12 - 1
            if jC13 == False:
                if key.is_pressed(at4):
                    if sta4 == False:
                        disablr()
                        sta4 = True
                        NF("Chat Spam 4","On")
                        lfwm("modCHSP4on")
                    elif sta4 == True:
                        sta4 = False
                        NF("Chat Spam 4","Off")
                        lfwm("modCHSP4off")
                    jC13 = True
                    nt()
                    ajc13 = 5
            elif jC13 == True:
                if ajc13 == 1:
                    jC13 = False
                else:
                    ajc13 = ajc13 - 1
            if jC14 == False:
                if key.is_pressed(at5):
                    if sta5 == False:
                        disablr()
                        sta5 = True
                        NF("Chat Spam 5","On")
                        lfwm("modCHSP5on")
                    elif sta5 == True:
                        sta5 = False
                        NF("Chat Spam 5","Off")
                        lfwm("modCHSP5off")
                    jC14 = True
                    nt()
                    ajc14 = 5
            elif jC14 == True:
                if ajc14 == 1:
                    jC10 = False
                else:
                    ajc14 = ajc14 - 1
            wait(0.001)
            if jC15 == False:
                if key.is_pressed(at6):
                    if sta6 == False:
                        disablr()
                        sta6 = True
                        NF("Chat Spam 6","On")
                        lfwm("modCHSP6on")
                    elif sta6 == True:
                        sta6 = False
                        NF("Chat Spam 6","Off")
                        lfwm("modCHSP6off")
                    jC15 = True
                    nt()
                    ajc15 = 5
            elif jC15 == True:
                if ajc15 == 1:
                    jC15 = False
                else:
                    ajc15 = ajc15 - 1
        except:
            er()
            print("error005 click check error")
            lfwm("error005 clickCheck")
    def thP1():
        global thPc1
        if thPc1 == 1:
            global ll, rl, fd, bd, lt, rt, jp, st, ch, ak
            global sta1, sta2, sta3, sta4, sta5, sta6
            global jC1, jC2, jC3, jC4, jC5, jC6, jC7, jC8, jC9, jC0, jC10, jC11, jC12, jC13, jC14, jC15
            global ajc0, ajc1, ajc2, ajc3, ajc4, ajc5, ajc6, ajc7, ajc8, ajc9, ajc10, ajc11, ajc12, ajc13, ajc14, ajc15
            thPc1 = 2
        try:
            r = ra.randint(2600,3500)
            r = r / 100000
            wait(r)
            if ll == True:
                pyguia.click()
            if rl == True:
                pyguia.rightClick()
            if fd == True:
                pyguia.keyDown(fd2)
            elif fd == False:
                pyguia.keyUp(fd2)
            if bd == True:
                pyguia.keyDown(bd2)
            elif bd == False:
                pyguia.keyUp(bd2)
            if lt == True:
                pyguia.keyDown(lt2)
            elif lt == False:
                pyguia.keyUp(lt2)
            if rt == True:
                pyguia.keyDown(rt2)
            elif rt == False:
                pyguia.keyUp(rt2)
            if jp == True:
                pyguia.press(jp2)
            if st == True:
                pyguia.keyDown(st2)
            elif st == False:
                pyguia.keyUp(st2)
            if ch == True:
                pyguia.keyDown(ch2)
            elif ch == False:
                pyguia.keyUp(ch2)
            if ak == True:
                r = ra.randint(10,4999)
                r = r/10000
                wait(r)
                r = ra.randint(1,6)
                if r == 1:
                    pyguia.press(fd2)
                elif r == 2:
                    pyguia.press(bd2)
                elif r == 3:
                    pyguia.press(lt2)
                elif r == 4:
                    pyguia.press(rt2)
                elif r == 5:
                    pyguia.press(jp2)
                elif r == 6:
                    pygui.click()
        except:
            er()
            print("error006 keyboard click simulation error")
            lfwm("error006 clickSim")
    def thP2():
        global thPc2
        if thPc2 == 1:
            global ll, rl, fd, bd, lt, rt, jp, st, ch, ak
            global sta1, sta2, sta3, sta4, sta5, sta6
            global jC1, jC2, jC3, jC4, jC5, jC6, jC7, jC8, jC9, jC0, jC10, jC11, jC12, jC13, jC14, jC15
            global ajc0, ajc1, ajc2, ajc3, ajc4, ajc5, ajc6, ajc7, ajc8, ajc9, ajc10, ajc11, ajc12, ajc13, ajc14, ajc15
            global stb1, stb2, stb3, stb4, stb5
            thPc2 = 2
        try:
            if sta1 == True:
                if stb1 == 1:
                    pyguia.press(ca1)
                pyguia.write(chat1)
                pyguia.press("enter")
                stb1 += 1
            elif sta1 == False:
                stb1 = 1
            if sta2 == True:
                if stb2 == 1:
                    pyguia.press(ca1)
                pyguia.write(chat2)
                pyguia.press("enter")
                stb2 += 1
            elif sta2 == False:
                stb2 = 1
            if sta3 == True:
                if stb3 == 1:
                    pyguia.press(ca1)
                pyguia.write(chat3)
                pyguia.press("enter")
                stb3 += 1
            elif sta3 == False:
                stb3 = 1
            if sta4 == True:
                if stb4 == 1:
                    pyguia.press(ca1)
                pyguia.write(chat4)
                pyguia.press("enter")
                stb4 += 1
            elif sta4 == False:
                stb4 = 1
            if sta5 == True:
                if stb5 == 1:
                    pyguia.press(ca1)
                pyguia.write(chat5)
                pyguia.press("enter")
                stb5 += 1
            elif sta5 == False:
                stb5 = 1
            if sta6 == True:
                if stb6 == 1:
                    pyguia.press(ca1)
                pyguia.write(chat6)
                pyguia.press("enter")
                stb6 += 1
            elif sta6 == False:
                stb6 = 1
        except:
            er()
            print("error006 keyboard click simulation error")
            lfwm("error006 clickSim")
    lfwm("eventThreading")
    while run == True:
        try:
            isPr1 = trng.Thread(target = isP1); isPr2 = trng.Thread(target = isP2) #args=
            thPr1 = trng.Thread(target = thP1); thPr2 = trng.Thread(target = thP2)
            isPr1.start(); isPr2.start()
            thPr1.start(); thPr2.start()
            isPr1.join(); isPr2.join()
            thPr1.join(); thPr2.join()
        except:
            er()
            print("error007 threading error")
            lfwm("error007 threading")
if altf4 == True:
    kB.close()
    quit()
try:
    lfwm("eventGUIInitiated")
    win = Tk()
    win.title("Proton")
    win.geometry("600x400")
    leftC = BooleanVar(win, True)
    rightC = BooleanVar(win, True)
    proT = Label(win, text = "Proton Hack Client")
    proT.grid(column = 0, row = 0)
    proT1 = Label(win, text = "The GUI currently has no functionality")
    proT1.grid(column = 0, row = 1)
except:
    er()
    print("error008 tkinter window creation error")
    lfwm("error008 tkinterWinCreation")
try:
    def clicked(leftC):
        if leftC == False:
            proT.configure(text = "Button was clicked!")
            return True
        elif leftC == True:
            proT.configure(text = "Already pressed")
            return False
    def gthb():
        lfwm("eventLinkGithub")
        webR.open("https://www.github.com/fortquake", new = 2, autoraise = True)
    def twtr():
        lfwm("eventLinkTwitter")
        webR.open("https://www.twitter.com/fortquake", new = 2, autoraise = True)
    def yutb():
        lfwm("eventLinkYoutube")
        webR.open("https://www.youtube.com/channel/UCQYx5is7XMUkjaVaRef9hEA", new = 2, autoraise = True)
    def opnPA():
        try:
            os.startfile("patchnotes.txt")
            lfwm("eventPatchNotesAccessed")
        except:
            tkinter.messagebox.showerror("File Integrity Error", "patchnotes.txt was not found")
            lfwm("eventPatchNotesAccessFailed")
    def gtPg():
        lfwm("eventLinkProton")
        webR.open("https://www.github.com/fortquake/proton/")
    def abtP():
        lfwm("eventLinkProtonLegal")
        webR.open("https://www.github.com/fortquake/proton/wiki/Proton")
    def legP():
        lfwm("eventLinkAboutProton")
        webR.open("https://www.github.com/fortquake/proton/wiki/Proton-Legal")   
except:
    er()
    print("error009 gui click condition error")
    lfwm("error009 tkinterClickCondition")
nt()
try:
    btn = Button(win, text = "Test", command = clicked(leftC))
    btn.grid(column = 0, row = 3)
    menu = Menu(win)
    win.config(menu = menu)
    fileM = Menu(menu, tearoff = False)
    setSM = Menu(fileM, tearoff = 0)
    setSM.add_command(label = "Keyboard Shortcuts")
    setSM.add_command(label = "Themes")
    setSM.add_command(label = "Online Mode")
    setSM.add_command(label = "Time Zone")
    fileM.add_cascade(label = "Settings", menu = setSM)
    
    patSM = Menu(fileM, tearoff = 0)
    patSM.add_command(label = "Latest")
    patSM.add_command(label = "All", command = opnPA)
    fileM.add_cascade(label = "Patch Notes", menu = patSM)
    fileM.add_command(label = "Info", command = gtPg)
    fileM.add_separator()
    fileM.add_command(label = "Exit", command = win.destroy)
    menu.add_cascade(label = "File", menu = fileM, underline = 0)

    viewM = Menu(menu, tearoff = False)
    viewM.add_command(label = "Zoom")
    viewM.add_command(label = "CLI")
    menu.add_cascade(label = "View", menu = viewM)

    helpM = Menu(menu, tearoff = False)
    helpM.add_command(label = "About Proton", command = abtP)
    helpM.add_command(label = "Legal", command = legP)
    feeSM = Menu(helpM, tearoff = 0)
    feeSM.add_command(label = "Github", command = gthb)
    feeSM.add_command(label = "Twitter", command = twtr)
    feeSM.add_command(label = "YouTube", command = yutb)
    helpM.add_cascade(label = "Send Feedback", menu = feeSM)
    helpM.add_separator()
    helpM.add_command(label = "Help")
    menu.add_cascade(label = "Help", menu = helpM)
    tkinter.messagebox.showwarning("GUI Warning", "The GUI currently has no functionality")
except:
    er()
    print("error010 menu & button creation error")
    lfwm("error010 tkinterGUI")
win.mainloop()
