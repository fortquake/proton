version = str("1.0.2 release")
lgTr = True
import time as t
def lfwm(lfwt):
    if lgTr == True:
        logf2 = open('proton_assets/logs.txt', 'a')
        xyz = f"{str(t.time())} - {lfwt}"
        abc = ["", xyz]
        logf2.writelines('\n'.join(abc))
        logf2.close()
def wait(timeWait):
    t.sleep(timeWait)
wait(0.02)
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
    print("Modules loaded.")
except:
    run = False
    print("error_011 required modules not found")
    lfwm("error_011_modules_absent")
    space(1)
    print("Please verify 'pyautogui', 'playsound' and 'tkinter' are installed.")
    wait(9)
    quit()
try:
    def NF(a,b):
        print(f"{a} - {b}")
    def protonLogo():
        space(1)
        print('''
######  ######  ######  #######  ######  #    #
#    #  #    #  #    #     #     #    #  ##   #
#    #  #    #  #    #     #     #    #  # #  #
######  ######  #    #     #     #    #  #  # #
#       #  #    #    #     #     #    #  #   ##
#       #   #   ######     #     ######  #    #
Minecraft Hack Client
Version ''' + version + ''', no known bugs
        ''')
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
        kB0 = open('proton_assets/keybinds.txt','rt')
        tCo = kB0.read()
        print(tCo)
        kB0.close()
        print('''
Modifing an existing command

Edit the commands.txt document
    ''')
    def protonPatch():
        print('''
Patch Notes
(for previous patch notes, see patchnotes.txt)

''' + version + '''
Fixed
Fixed an error with the playsound library (ensure you have 1.2.2 installed)
Changed
Cleared log.txt file
    ''')
    def error1():
        tkinter.messagebox.showerror('Proton', 'Requested feature not available in this version.')
    def er():
        ps.playsound("proton_assets/sd3.mp3")
    def nt():
        nt1n = ra.randint(0,6174)
        if nt1n == 22:
            try:
                ps.playsound("proton_assets/sd2.mp3")
            except:
                ps.playsound("proton_assets/sd1.mp3")
        else:
            ps.playsound("proton_assets/sd1.mp3")
except:
    run = False
    print("error_001 problem defining variables")
    lfwm("error_001_variable_define")
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
sta1 = False
sta2 = False
sta3 = False
sta4 = False
sta5 = False
sta6 = False
stb1 = 1
stb2 = 1
stb3 = 1
stb4 = 1
stb5 = 1
stb6 = 1
jC1 = False
jC2 = False
jC3 = False
jC4 = False
jC5 = False
jC6 = False
jC7 = False
jC8 = False
jC9 = False
jC0 = False
jC10 = False
jC11 = False
jC12 = False
jC13 = False
jC14 = False
jC15 = False
ajc1 = 3
ajc2 = 3
ajc3 = 3
ajc4 = 3
ajc5 = 3
ajc6 = 3
ajc7 = 3
ajc8 = 3
ajc9 = 3
ajc0 = 3
ajc10 = 3
ajc11 = 3
ajc12 = 3
ajc13 = 3
ajc14 = 3
ajc15 = 3
lgTr = False
try:
    kB = open("proton_assets/keybinds.txt", "r")
    kBr = kB.readlines()
except:
    run = False
    er()
    print("error_002 error accessing keybinds.txt")
    lfwm("error_002_accessing_keybinds")
try:
    logf1 = open("proton_assets/logs.txt", "a")
    xyz = f"{str(t.time())} - event_launch, ver {version}"
    abc = ["", xyz]
    logf1.writelines('\n'.join(abc))
    logf1.close()
except:
    er()
    print("error_003 error accessing logs.txt")
    lfwm("error_003_accessing_logs")
    space(1)
    print("No logs will be made.")
    lgTr = False
for j in (kBr):
    try:
        if j[1] == chr(32):
            if c == 1:
                ll1 = j[0]
            elif c == 2:
                rl1 = j[0]
            elif c == 3:
                fd1 = j[0]
            elif c == 4:
                bd1 = j[0]
            elif c == 5:
                lt1 = j[0]
            elif c == 6:
                rt1 = j[0]
            elif c == 7:
                jp1 = j[0]
            elif c == 8:
                st1 = j[0]
            elif c == 9:
                ch1 = j[0]
            elif c == 10:
                ak1 = j[0]
            elif c == 11:
                af1 = j[0]
            elif c == 12:
                cs1 = j[0]
            elif c == 13:
                ct1 = j[0]
            elif c == 14:
                hp1 = j[0]
            elif c == 15:
                co1 = j[0]
            elif c == 16:
                at1 = j[0]
            elif c == 17:
                at2 = j[0]
            elif c == 18:
                at3 = j[0]
            elif c == 19:
                at4 = j[0]
            elif c == 20:
                at5 = j[0]
            elif c == 21:
                at6 = j[0]
            elif c == 23:
                fd2 = j[0]
            elif c == 24:
                bd2 = j[0]
            elif c == 25:
                lt2 = j[0]
            elif c == 26:
                rt2 = j[0]
            elif c == 27:
                jp2 = j[0]
            elif c == 28:
                st2 = j[0]
            elif c == 29:
                ch2 = j[0]
            elif c == 30:
                ca1 = j[0]
            elif c == 31:
                db1 = j[0]
            elif c == 33:
                xx2 = j[0]
                if j[0] == 'y':
                    space(1)
                    NF("GUI","On")
                    guiS = True
                elif j[0] == 'n':
                    space(1)
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
            if c == 1:
                ll1 = 'shift'
            elif c == 2:
                rl1 = 'shift'
            elif c == 3:
                fd1 = 'shift'
            elif c == 4:
                bd1 = 'shift'
            elif c == 5:
                lt1 = 'shift'
            elif c == 6:
                rt1 = 'shift'
            elif c == 7:
                jp1 = 'shift'
            elif c == 8:
                st1 = 'shift'
            elif c == 9:
                ch1 = 'shift'
            elif c == 10:
                ak1 = 'shift'
            elif c == 11:
                af1 = 'shift'
            elif c == 12:
                cs1 = 'shift'
            elif c == 13:
                ct1 = 'shift'
            elif c == 14:
                hp1 = 'shift'
            elif c == 15:
                co1 = 'shift'
            elif c == 16:
                at1 = 'shift'
            elif c == 17:
                at2 = 'shift'
            elif c == 18:
                at3 = 'shift'
            elif c == 19:
                at4 = 'shift'
            elif c == 20:
                at5 = 'shift'
            elif c == 21:
                at6 = 'shift'
            elif c == 23:
                fd2 = 'shift'
            elif c == 24:
                bd2 = 'shift'
            elif c == 25:
                lt2 = 'shift'
            elif c == 26:
                rt2 = 'shift'
            elif c == 27:
                jp2 = 'shift'
            elif c == 28:
                st2 = 'shift'
            elif c == 29:
                ch2 = 'shift'
            elif c == 30:
                ca1 = 'shift'
            elif c == 31:
                db1 = 'shift'
        elif j[0] == chr(115) and j[1] == chr(112):
            if c == 1:
                ll1 = 'space'
            elif c == 2:
                rl1 = 'space'
            elif c == 3:
                fd1 = 'space'
            elif c == 4:
                bd1 = 'space'
            elif c == 5:
                lt1 = 'space'
            elif c == 6:
                rt1 = 'space'
            elif c == 7:
                jp1 = 'space'
            elif c == 8:
                st1 = 'space'
            elif c == 9:
                ch1 = 'space'
            elif c == 10:
                ak1 = 'space'
            elif c == 11:
                af1 = 'space'
            elif c == 12:
                cs1 = 'space'
            elif c == 13:
                ct1 = 'space'
            elif c == 14:
                hp1 = 'space'
            elif c == 15:
                co1 = 'space'
            elif c == 16:
                at1 = 'space'
            elif c == 17:
                at2 = 'space'
            elif c == 18:
                at3 = 'space'
            elif c == 19:
                at4 = 'space'
            elif c == 20:
                at5 = 'space'
            elif c == 21:
                at6 = 'space'
            elif c == 23:
                fd2 = 'space'
            elif c == 24:
                bd2 = 'space'
            elif c == 25:
                lt2 = 'space'
            elif c == 26:
                rt2 = 'space'
            elif c == 27:
                jp2 = 'space'
            elif c == 28:
                st2 = 'space'
            elif c == 29:
                ch2 = 'space'
            elif c == 30:
                ca1 = 'space'
            elif c == 31:
                db1 = 'space'                
        elif j[0] == chr(99) and j[1] == chr(116):
            if c == 1:
                ll1 = 'ctrl'
            elif c == 2:
                rl1 = 'ctrl'
            elif c == 3:
                fd1 = 'ctrl'
            elif c == 4:
                bd1 = 'ctrl'
            elif c == 5:
                lt1 = 'ctrl'
            elif c == 6:
                rt1 = 'ctrl'
            elif c == 7:
                jp1 = 'ctrl'
            elif c == 8:
                st1 = 'ctrl'
            elif c == 9:
                ch1 = 'ctrl'
            elif c == 10:
                ak1 = 'ctrl'
            elif c == 11:
                af1 = 'ctrl'
            elif c == 12:
                cs1 = 'ctrl'
            elif c == 13:
                ct1 = 'ctrl'
            elif c == 14:
                hp1 = 'ctrl'
            elif c == 15:
                co1 = 'ctrl'
            elif c == 16:
                at1 = 'ctrl'
            elif c == 17:
                at2 = 'ctrl'
            elif c == 18:
                at3 = 'ctrl'
            elif c == 19:
                at4 = 'ctrl'
            elif c == 20:
                at5 = 'ctrl'
            elif c == 21:
                at6 = 'ctrl'
            elif c == 23:
                fd2 = 'ctrl'
            elif c == 24:
                bd2 = 'ctrl'
            elif c == 25:
                lt2 = 'ctrl'
            elif c == 26:
                rt2 = 'ctrl'
            elif c == 27:
                jp2 = 'ctrl'
            elif c == 28:
                st2 = 'ctrl'
            elif c == 29:
                ch2 = 'ctrl'
            elif c == 30:
                ca1 = 'ctrl'
            elif c == 31:
                db1 = 'ctrl'
        c += 1
    except:
        pass
try:
   chat1 = lica.getline("proton_assets\keybinds.txt", 37)
   chat2 = lica.getline("proton_assets\keybinds.txt", 38)
   chat3 = lica.getline("proton_assets\keybinds.txt", 39)
   chat4 = lica.getline("proton_assets\keybinds.txt", 40)
   chat5 = lica.getline("proton_assets\keybinds.txt", 41)
   chat6 = lica.getline("proton_assets\keybinds.txt", 42)
except:
    er()
    print("error_013 error accessing text for chat spam")
    lfwm("error_013_error_chat_spam_get")
try:
    lfwm("event_keybinds_accessed")
    logf2 = open('proton_assets/logs.txt', 'a')
    xyz = f"{str(t.time())} - load_1"
    abc = ["", xyz]
    logf2.writelines('\n'.join(abc))
    logf2.close()
    wait(0.075)
    guiS = False
    print("Program loaded.")
    wait(0.01)
    space(2)
    protonLogo()
    altf4 = False
except:
    er()
    print("error_004 gui activation error")
    lfwm("error_004_gui_activation")
lfwm("load_2")
if guiS == False:
    space(3)
    print(f"Press '{hp1}' for a list of commands")
    space(9)
    def isP():
        try:
            global ll
            global rl
            global fd
            global bd
            global lt
            global rt
            global jp
            global st
            global ch
            global ak
            global sta1
            global sta2
            global sta3
            global sta4
            global sta5
            global sta6
            global jC1
            global jC2
            global jC3
            global jC4
            global jC5
            global jC6
            global jC7
            global jC8
            global jC9
            global jC0
            global jC10
            global jC11
            global jC12
            global jC13
            global jC14
            global jC15
            global ajc1
            global ajc2
            global ajc3
            global ajc4
            global ajc5
            global ajc6
            global ajc7
            global ajc8
            global ajc9
            global ajc0
            global ajc10
            global ajc11
            global ajc12
            global ajc13
            global ajc14
            global ajc15
            global chat1
            global chat2
            global chat3
            global chat4
            global chat5
            global chat6
            if jC1 == True:
                if key.is_pressed(ll1):
                    if ll == False:
                        ll = True
                        NF("Left Click","On")
                        lfwm("mod_lc_on")
                    elif ll == True:
                        ll = False
                        NF("Left Click","Off")
                        lfwm("mod_lc_off")
                    jC1 = False
                    nt()
                    ajc1 = 5
            if jC1 == False:
                if ajc1 == 1:
                    jC1 = True
                else:
                    ajc1 = ajc1 - 1
            if jC2 == True:
                if key.is_pressed(rl1):
                    if rl == False:
                        rl = True
                        NF("Right Click","On")
                        lfwm("mod_rc_on")
                    elif rl == True:
                        rl = False
                        NF("Right Click","Off")
                        lfwm("mod_rc_off")
                    jC2 = True
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
                        lfwm("mod_fd_on")
                    elif fd == True:
                        fd = False
                        NF("Forward","Off")
                        lfwm("mod_fd_off")
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
                        lfwm("mod_bd_on")
                    elif bd == True:
                        bd = False
                        NF("Backward","Off")
                        lfwm("mod_bd_off")
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
                        lfwm("mod_lt_on")
                    elif lt == True:
                        lt = False
                        NF("Left","Off")
                        lfwm("mod_lt_off")
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
                        lfwm("mod_rt_on")
                    elif rt == True:
                        rt = False
                        NF("Right","Off")
                        lfwm("mod_rt_off")
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
                        lfwm("mod_jp_on")
                    elif jp == True:
                        jp = False
                        NF("Jump","Off")
                        lfwm("mod_jp_off")
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
                        lfwm("mod_sp_on")
                    elif st == True:
                        st = False
                        NF("Sprint","Off")
                        lfwm("mod_sp_off")
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
                        lfwm("mod_ch_on")
                    elif ch == True:
                        ch = False
                        NF("Crouch","Off")
                        lfwm("mod_ch_off")
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
                        ll = False
                        rl = False
                        fd = False
                        bd = False
                        lt = False
                        rt = False
                        jp = False
                        st = False
                        ch = False
                        sta1 = False
                        sta2 = False
                        sta3 = False
                        sta4 = False
                        sta5 = False
                        sta6 = False
                        ak = True
                        NF("Anti AFK","On")
                        lfwm("mod_ak_on")
                    elif ak == True:
                        ak = False
                        NF("Anti AFK","Off")
                        lfwm("mod_ak_off")
                    jC0 = True
                    nt()
                    ajc0 = 5
            elif jC0 == True:
                if ajc0 == 1:
                    jC0 = False
                else:
                    ajc0 = ajc0 - 1
            if key.is_pressed(af1):
                nt()
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
                sta1 = False
                sta2 = False
                sta3 = False
                sta4 = False
                sta5 = False
                sta6 = False
                key.release("shift")
                NF("All","Off")
                lfwm("mod_al_off")
            elif key.is_pressed(cs1):
                lfwm("event_credits")
                nt()
                wait(0.1)
                protonLogo()
                protonCredit()
                wait(0.1)
            elif key.is_pressed(hp1):
                lfwm("event_help")
                nt()
                protonLogo()
                protonHelp()
            elif key.is_pressed(co1):
                lfwm("event_patch")
                nt()
                protonLogo()
                protonPatch()
            if key.is_pressed(ct1):
                lfwm("event_close")
                nt()
                wait(0.1)
                NF("Program","Closed")
                kB.close()
                logf1.close()
                exit()
            if jC10 == False:
                if key.is_pressed(at1):
                    if sta1 == False:
                        sta1 = True
                        NF("Chat Spam 1","On")
                        lfwm("mod_chsp1_on")
                    elif sta1 == True:
                        sta1 = False
                        NF("Chat Spam 1","Off")
                        lfwm("mod_chsp1_off")
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
                        sta2 = True
                        NF("Chat Spam 2","On")
                        lfwm("mod_chsp2_on")
                    elif sta2 == True:
                        sta2 = False
                        NF("Chat Spam 2","Off")
                        lfwm("mod_chsp2_off")
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
                        sta3 = True
                        NF("Chat Spam 3","On")
                        lfwm("mod_chsp3_on")
                    elif sta3 == True:
                        sta3 = False
                        NF("Chat Spam 3","Off")
                        lfwm("mod_chsp3_off")
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
                        sta4 = True
                        NF("Chat Spam 4","On")
                        lfwm("mod_chsp4_on")
                    elif sta4 == True:
                        sta4 = False
                        NF("Chat Spam 4","Off")
                        lfwm("mod_chsp4_off")
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
                        sta5 = True
                        NF("Chat Spam 5","On")
                        lfwm("mod_chsp5_on")
                    elif sta5 == True:
                        sta5 = False
                        NF("Chat Spam 5","Off")
                        lfwm("mod_chsp5_off")
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
                        sta6 = True
                        NF("Chat Spam 6","On")
                        lfwm("mod_chsp6_on")
                    elif sta6 == True:
                        sta6 = False
                        NF("Chat Spam 6","Off")
                        lfwm("mod_chsp6_off")
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
            print("error_005 click check error")
            lfwm("error_005_click_check")
    def thP():
        global stb1
        global stb2
        global stb3
        global stb4
        global stb5
        try:
            r = ra.randint(2600,3500)
            r = r / 100000
            wait(r)
            if ll == True:
                pyguia.click()
            if rl == True:
                pyguia.click(button='right')
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
            print("error_006 keyboard click simulation error")
            lfwm("error_006_click_sim")
    lfwm("event_threading")
    while run == True:
        try:
            isP1 = trng.Thread(target = isP)#args=
            thP1 = trng.Thread(target = thP)
            isP1.start()
            thP1.start()
            isP1.join()
            thP1.join()
        except:
            er()
            print("error_007 threading error")
            lfwm("error_007_threading")
if altf4 == True:
    print("dasfdasf")
    kB.close()
    quit()
try:
    lfwm("event_gui_initiated")
    win = Tk()
    win.title("Proton")
    win.geometry("600x378")
    leftC = BooleanVar(win, True)
    rightC = BooleanVar(win, True)
    proT = Label(win, text = "Proton Hack Client")
    proT.grid(column = 0, row = 0)
    proT1 = Label(win, text = "The GUI currently has no functionality")
    proT1.grid(column = 0, row = 1)
except:
    er()
    print("error_008 tkinter window creation error")
    lfwm("error_008_tkinter_win_creation")
try:
    def clicked(leftC):
        if leftC == False:
            proT.configure(text = "Button was clicked!")
            return True
        elif leftC == True:
            proT.configure(text = "Already pressed")
            return False
    def gthb():
        lfwm("event_link_github")
        webR.open("https://www.github.com/fortquake", new = 2, autoraise = True)
    def twtr():
        lfwm("event_link_twitter")
        webR.open("https://www.twitter.com/fortquake", new = 2, autoraise = True)
    def yutb():
        lfwm("event_link_youtube")
        webR.open("https://www.youtube.com/channel/UCQYx5is7XMUkjaVaRef9hEA", new = 2, autoraise = True)
    def opnPA():
        try:
            os.startfile("patchnotes.txt")
            lfwm("event_patchnotes_accessed")
        except:
            tkinter.messagebox.showerror("File Integrity Error", "patchnotes.txt was not found")
            lfwm("event_patchnotes_access_failed")
    def gtPg():
        lfwm("event_link_proton")
        webR.open("https://www.github.com/fortquake/proton/")
    def abtP():
        lfwm("event_link_proton_legal")
        webR.open("https://www.github.com/fortquake/proton/wiki/Proton-")
    def legP():
        lfwm("event_link_about_proton")
        webR.open("https://www.github.com/fortquake/proton/wiki/Proton-Legal")   
except:
    er()
    print("error_009 gui click condition error")
    lfwm("error_009_tkinter_click_condition")
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
    print("error_010 menu & button creation error")
    lfwm("error_010_tkinter_gui")
win.mainloop()
