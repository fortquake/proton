__version__ = str("1.2.4 release")
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
    for i in range(0,gaps): print("")
try:
    import keyboard as key, pyautogui as pyg, pydirectinput as pygi, random as ra, threading as trng, playsound as ps, linecache as lica
except:    
    print("er01 required modules not found\n\nPlease verify 'pyautogui', 'pydirectinput' and 'playsound' are installed.")
    lfwm("er01 modulesAbsent")
    run = False; wait(9); quit()

def NF(a,b):
    print(f"{a} - {b}")
def protonLogo():
    print('''
██████  ██████   ██████  ████████  ██████  ███    ██
██   ██ ██   ██ ██    ██    ██    ██    ██ ████   ██
██████  ██████  ██    ██    ██    ██    ██ ██ ██  ██
██      ██   ██ ██    ██    ██    ██    ██ ██  ██ ██
██      ██   ██  ██████     ██     ██████  ██   ████
Keypressing Utility
Version ''' + __version__)
def protonCredit():
    print('''\n\n
Twitter  @fortquake
Discord  Fort Quake#3107
Reddit   r/fortquake
Reddit   u/fortquake

Audio- https://www.freesoundslibrary.com

Modules
pyautogui\nkeyboard\ntkinter\nthreading\nrandom\ntime

Coded with Python 3.11 and Visual Studio Code
Released on GitHub
    ''')
def protonHelp():
    print('''\nHelp\n\nCommands''')
    kB0 = open('protonAssets/keybinds.txt','rt')
    print((kB0.read()))
    kB0.close()
    print('''\nQ: Modifing an existing command\nA: Edit the commands.txt document\n''')
def protonPatch():
    print('''\nPatch Notes
(for previous patch notes, see patchnotes.txt)\n
''' + __version__ + '''
Changed
Shorted code and improved text clarity
''')
def plsnd(tp="er"):
    try:
        if tp == "er":
            ps.playsound("protonAssets/sd2.mp3")
        else:
            ps.playsound("protonAssets/sd1.mp3")
    except:
        print("er08 playsound error")
        lfwm("er08 playsoundError")
global p
p, run, c = True, True, 0
ll = rl = fd = bd = lt = rt = jp = st = ch = ak = tp = cp = am = bs = bl = hs = isq = ae = False
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
    plsnd()
    print("er02 error accessing keybinds.txt")
    lfwm("er02 accessingKeybinds")
try:
    logf1 = open("protonAssets/logs.txt", "a")
    abc = ["", f"{str(t.time())} - eventLaunch, ver {__version__}"]
    logf1.writelines('\n'.join(abc))
    logf1.close()
except:
    plsnd()
    print("er03 error accessing logs.txt\nNo logs will be made.")
    lfwm("er03 accessingLogs\n")
    lgTr = False

postn = [14,15,16,17,18,19,20,21,22,23,24,25,31,32,33,34,35,36,37,38,39,40,41, 4,5,6,7,8,9,10,11,12, 43,44,45,46,47,48,49, 24,25,26,27,28,29,30] 
#list of line numbers, client keybinds (0-20), game keybinds (21-29), chatspam (30-36), additional modules (37-43)
for j in (kBr):
    try:
        if j[1] == chr(32):
            if c == postn[0]: ll1 = j[0] #left click
            elif c == postn[1]: rl1 = j[0] #no idea
            elif c == postn[2]: rl1 = j[0] #right click
            elif c == postn[3]: rh1 = j[0] #hold right click
            elif c == postn[4]: fd1 = j[0] #forward
            elif c == postn[5]: bd1 = j[0] #backward
            elif c == postn[6]: lt1 = j[0] #left
            elif c == postn[7]: rt1 = j[0] #right
            elif c == postn[8]: jp1 = j[0] #jump
            elif c == postn[9]: st1 = j[0] #idk
            elif c == postn[10]: ch1 = j[0]
            elif c == postn[11]: ak1 = j[0]
            elif c == postn[12]: af1 = j[0]
            elif c == postn[13]: cs1 = j[0]
            elif c == postn[14]: ct1 = j[0]
            elif c == postn[15]: hp1 = j[0]
            elif c == postn[16]: co1 = j[0]
            elif c == postn[17]: at1 = j[0]
            elif c == postn[18]: at2 = j[0]
            elif c == postn[19]: at3 = j[0]
            elif c == postn[20]: at4 = j[0]
            elif c == postn[21]: at5 = j[0]
            elif c == postn[22]: at6 = j[0]
            elif c == postn[23]: fd2 = j[0]
            elif c == postn[24]: bd2 = j[0]
            elif c == postn[25]: lt2 = j[0]
            elif c == postn[26]: rt2 = j[0]
            elif c == postn[27]: jp2 = j[0]
            elif c == postn[28]: st2 = j[0]
            elif c == postn[29]: ch2 = j[0]
            elif c == postn[30]: ca1 = j[0]
            elif c == postn[31]: db1 = j[0]
            elif c == postn[39]: tp1 = j[0] #tp aura
            elif c == postn[40]: cp1 = j[0] #crystal spam
            elif c == postn[41]: am1 = j[0] #autotravel
            elif c == postn[42]: bs1 = j[0] #bow spam
            elif c == postn[43]: bl1 = j[0] #bow far
            elif c == postn[44]: is1 = j[0] #hotbar scroll
            elif c == postn[45]: ae1 = j[0] #auto ezz (no function)
            elif c == 1:
                if j[0] == 'y':
                    NF("GUI","On")
                    guiS = True
                elif j[0] == 'n':
                    NF("GUI","Off")
                    guiS = False
                elif j[0] == 'm':
                    cg = False
                    while cg == False:
                        try:
                            print("Do you wish to enable the GUI? y/n")
                            logggg = str(input()).lower()
                            space(1)
                            if logggg == 'y' or logggg == 'yes' or logggg == 'yeah':
                                NF("GUI","On")
                                guiS, cg = True, True
                            elif logggg == 'n' or logggg == 'no' or logggg == 'nah':
                                NF("GUI","Off")
                                guiS, cg = False, True
                        except:
                            pass
            elif c == 2:
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
                                lgTr, cg = True, True
                            elif loggg == 'n' or loggg == 'no' or loggg == 'nah':
                                NF("Logging","Off")
                                lgTr, cg = False, True
                        except:
                            pass
        elif j[0] == chr(115) and j[1] == chr(104): #shift
            if c == postn[0]: ll1 = 'shift'
            elif c == postn[1]: rl1 = 'shift'
            elif c == postn[2]: rl1 = 'shift'
            elif c == postn[3]: rh1 = 'shift'
            elif c == postn[4]: fd1 = 'shift'
            elif c == postn[5]: bd1 = 'shift'
            elif c == postn[6]: lt1 = 'shift'
            elif c == postn[7]: rt1 = 'shift'
            elif c == postn[8]: jp1 = 'shift'
            elif c == postn[9]: st1 = 'shift'
            elif c == postn[10]: ch1 = 'shift'
            elif c == postn[11]: ak1 = 'shift'
            elif c == postn[12]: af1 = 'shift'
            elif c == postn[13]: cs1 = 'shift'
            elif c == postn[14]: ct1 = 'shift'
            elif c == postn[15]: hp1 = 'shift'
            elif c == postn[16]: co1 = 'shift'
            elif c == postn[17]: at1 = 'shift'
            elif c == postn[18]: at2 = 'shift'
            elif c == postn[19]: at3 = 'shift'
            elif c == postn[20]: at4 = 'shift'
            elif c == postn[21]: at5 = 'shift'
            elif c == postn[22]: at6 = 'shift'
            elif c == postn[23]: fd2 = 'shift'
            elif c == postn[24]: bd2 = 'shift'
            elif c == postn[25]: lt2 = 'shift'
            elif c == postn[26]: rt2 = 'shift'
            elif c == postn[27]: jp2 = 'shift'
            elif c == postn[28]: st2 = 'shift'
            elif c == postn[29]: ch2 = 'shift'
            elif c == postn[30]: ca1 = 'shift'
            elif c == postn[31]: db1 = 'shift'
            elif c == postn[39]: tp1 = 'shift'
            elif c == postn[40]: cp1 = 'shift'
            elif c == postn[41]: am1 = 'shift'
            elif c == postn[42]: bs1 = 'shift'
            elif c == postn[43]: bl1 = 'shift'
            elif c == postn[44]: is1 = 'shift'
            elif c == postn[45]: ae1 = 'shift'
        elif j[0] == chr(115) and j[1] == chr(112): #space
            if c == postn[0]: ll1 = 'space'
            elif c == postn[1]: rl1 = 'space'
            elif c == postn[2]: rl1 = 'space'
            elif c == postn[3]: rh1 = 'space'
            elif c == postn[4]: fd1 = 'space'
            elif c == postn[5]: bd1 = 'space'
            elif c == postn[6]: lt1 = 'space'
            elif c == postn[7]: rt1 = 'space'
            elif c == postn[8]: jp1 = 'space'
            elif c == postn[9]: st1 = 'space'
            elif c == postn[10]: ch1 = 'space'
            elif c == postn[11]: ak1 = 'space'
            elif c == postn[12]: af1 = 'space'
            elif c == postn[13]: cs1 = 'space'
            elif c == postn[14]: ct1 = 'space'
            elif c == postn[15]: hp1 = 'space'
            elif c == postn[16]: co1 = 'space'
            elif c == postn[17]: at1 = 'space'
            elif c == postn[18]: at2 = 'space'
            elif c == postn[19]: at3 = 'space'
            elif c == postn[20]: at4 = 'space'
            elif c == postn[21]: at5 = 'space'
            elif c == postn[22]: at6 = 'space'
            elif c == postn[23]: fd2 = 'space'
            elif c == postn[24]: bd2 = 'space'
            elif c == postn[25]: lt2 = 'space'
            elif c == postn[26]: rt2 = 'space'
            elif c == postn[27]: jp2 = 'space'
            elif c == postn[28]: st2 = 'space'
            elif c == postn[29]: ch2 = 'space'
            elif c == postn[30]: ca1 = 'space'
            elif c == postn[31]: db1 = 'space'
            elif c == postn[39]: tp1 = 'space'
            elif c == postn[40]: cp1 = 'space'
            elif c == postn[41]: am1 = 'space'
            elif c == postn[42]: bs1 = 'space'
            elif c == postn[43]: bl1 = 'space'
            elif c == postn[44]: is1 = 'space'
            elif c == postn[45]: ae1 = 'space'
        elif j[0] == chr(99) and j[1] == chr(116): #ctrl
            if c == postn[0]: ll1 = 'ctrl'
            elif c == postn[1]: rl1 = 'ctrl'
            elif c == postn[2]: rl1 = 'ctrl'
            elif c == postn[3]: rh1 = 'ctrl'
            elif c == postn[4]: fd1 = 'ctrl'
            elif c == postn[5]: bd1 = 'ctrl'
            elif c == postn[6]: lt1 = 'ctrl'
            elif c == postn[7]: rt1 = 'ctrl'
            elif c == postn[8]: jp1 = 'ctrl'
            elif c == postn[9]: st1 = 'ctrl'
            elif c == postn[10]: ch1 = 'ctrl'
            elif c == postn[11]: ak1 = 'ctrl'
            elif c == postn[12]: af1 = 'ctrl'
            elif c == postn[13]: cs1 = 'ctrl'
            elif c == postn[14]: ct1 = 'ctrl'
            elif c == postn[15]: hp1 = 'ctrl'
            elif c == postn[16]: co1 = 'ctrl'
            elif c == postn[17]: at1 = 'ctrl'
            elif c == postn[18]: at2 = 'ctrl'
            elif c == postn[19]: at3 = 'ctrl'
            elif c == postn[20]: at4 = 'ctrl'
            elif c == postn[21]: at5 = 'ctrl'
            elif c == postn[22]: at6 = 'ctrl'
            elif c == postn[23]: fd2 = 'ctrl'
            elif c == postn[24]: bd2 = 'ctrl'
            elif c == postn[25]: lt2 = 'ctrl'
            elif c == postn[26]: rt2 = 'ctrl'
            elif c == postn[27]: jp2 = 'ctrl'
            elif c == postn[28]: st2 = 'ctrl'
            elif c == postn[29]: ch2 = 'ctrl'
            elif c == postn[30]: ca1 = 'ctrl'
            elif c == postn[31]: db1 = 'ctrl'
            elif c == postn[39]: tp1 = 'ctrl'
            elif c == postn[40]: cp1 = 'ctrl'
            elif c == postn[41]: am1 = 'ctrl'
            elif c == postn[42]: bs1 = 'ctrl'
            elif c == postn[43]: bl1 = 'ctrl'
            elif c == postn[44]: is1 = 'ctrl'
            elif c == postn[45]: ae1 = 'ctrl'
        elif j[0] == chr(97) and j[1] == chr(108): #alt
            if c == postn[0]: ll1 = 'alt'
            elif c == postn[1]: rl1 = 'alt'
            elif c == postn[2]: rl1 = 'alt'
            elif c == postn[3]: rh1 = 'alt'
            elif c == postn[4]: fd1 = 'alt'
            elif c == postn[5]: bd1 = 'alt'
            elif c == postn[6]: lt1 = 'alt'
            elif c == postn[7]: rt1 = 'alt'
            elif c == postn[8]: jp1 = 'alt'
            elif c == postn[9]: st1 = 'alt'
            elif c == postn[10]: ch1 = 'alt'
            elif c == postn[11]: ak1 = 'alt'
            elif c == postn[12]: af1 = 'alt'
            elif c == postn[13]: cs1 = 'alt'
            elif c == postn[14]: ct1 = 'alt'
            elif c == postn[15]: hp1 = 'alt'
            elif c == postn[16]: co1 = 'alt'
            elif c == postn[17]: at1 = 'alt'
            elif c == postn[18]: at2 = 'alt'
            elif c == postn[19]: at3 = 'alt'
            elif c == postn[20]: at4 = 'alt'
            elif c == postn[21]: at5 = 'alt'
            elif c == postn[22]: at6 = 'alt'
            elif c == postn[23]: fd2 = 'alt'
            elif c == postn[24]: bd2 = 'alt'
            elif c == postn[25]: lt2 = 'alt'
            elif c == postn[26]: rt2 = 'alt'
            elif c == postn[27]: jp2 = 'alt'
            elif c == postn[28]: st2 = 'alt'
            elif c == postn[29]: ch2 = 'alt'
            elif c == postn[30]: ca1 = 'alt'
            elif c == postn[31]: db1 = 'alt'
            elif c == postn[39]: tp1 = 'alt'
            elif c == postn[40]: cp1 = 'alt'
            elif c == postn[41]: am1 = 'alt'
            elif c == postn[42]: bs1 = 'alt'
            elif c == postn[43]: bl1 = 'alt'
            elif c == postn[44]: is1 = 'alt'
            elif c == postn[45]: ae1 = 'alt'
        elif j[0] == chr(116) and j[1] == chr(97): #tab
            if c == postn[0]: ll1 = 'tab'
            elif c == postn[1]: rl1 = 'tab'
            elif c == postn[2]: rl1 = 'tab'
            elif c == postn[3]: rh1 = 'tab'
            elif c == postn[4]: fd1 = 'tab'
            elif c == postn[5]: bd1 = 'tab'
            elif c == postn[6]: lt1 = 'tab'
            elif c == postn[7]: rt1 = 'tab'
            elif c == postn[8]: jp1 = 'tab'
            elif c == postn[9]: st1 = 'tab'
            elif c == postn[10]: ch1 = 'tab'
            elif c == postn[11]: ak1 = 'tab'
            elif c == postn[12]: af1 = 'tab'
            elif c == postn[13]: cs1 = 'tab'
            elif c == postn[14]: ct1 = 'tab'
            elif c == postn[15]: hp1 = 'tab'
            elif c == postn[16]: co1 = 'tab'
            elif c == postn[17]: at1 = 'tab'
            elif c == postn[18]: at2 = 'tab'
            elif c == postn[19]: at3 = 'tab'
            elif c == postn[20]: at4 = 'tab'
            elif c == postn[21]: at5 = 'tab'
            elif c == postn[22]: at6 = 'tab'
            elif c == postn[23]: fd2 = 'tab'
            elif c == postn[24]: bd2 = 'tab'
            elif c == postn[25]: lt2 = 'tab'
            elif c == postn[26]: rt2 = 'tab'
            elif c == postn[27]: jp2 = 'tab'
            elif c == postn[28]: st2 = 'tab'
            elif c == postn[29]: ch2 = 'tab'
            elif c == postn[30]: ca1 = 'tab'
            elif c == postn[31]: db1 = 'tab'
            elif c == postn[39]: tp1 = 'tab'
            elif c == postn[40]: cp1 = 'tab'
            elif c == postn[41]: am1 = 'tab'
            elif c == postn[42]: bs1 = 'tab'
            elif c == postn[43]: bl1 = 'tab'
            elif c == postn[44]: is1 = 'tab'
            elif c == postn[45]: ae1 = 'tab'
        elif j[0] == chr(117) and j[1] == chr(110): #unbound
            if c == postn[0]: ll1 = None
            elif c == postn[1]: rl1 = None
            elif c == postn[2]: rl1 = None
            elif c == postn[3]: rh1 = None
            elif c == postn[4]: fd1 = None
            elif c == postn[5]: bd1 = None
            elif c == postn[6]: lt1 = None
            elif c == postn[7]: rt1 = None
            elif c == postn[8]: jp1 = None
            elif c == postn[9]: st1 = None
            elif c == postn[10]: ch1 = None
            elif c == postn[11]: ak1 = None
            elif c == postn[12]: af1 = None
            elif c == postn[13]: cs1 = None
            elif c == postn[14]: ct1 = None
            elif c == postn[15]: hp1 = None
            elif c == postn[16]: co1 = None
            elif c == postn[17]: at1 = None
            elif c == postn[18]: at2 = None
            elif c == postn[19]: at3 = None
            elif c == postn[20]: at4 = None
            elif c == postn[21]: at5 = None
            elif c == postn[22]: at6 = None
            elif c == postn[23]: fd2 = None
            elif c == postn[24]: bd2 = None
            elif c == postn[25]: lt2 = None
            elif c == postn[26]: rt2 = None
            elif c == postn[27]: jp2 = None
            elif c == postn[28]: st2 = None
            elif c == postn[29]: ch2 = None
            elif c == postn[30]: ca1 = None
            elif c == postn[31]: db1 = None
            elif c == postn[39]: tp1 = None
            elif c == postn[40]: cp1 = None
            elif c == postn[41]: am1 = None
            elif c == postn[42]: bs1 = None
            elif c == postn[43]: bl1 = None
            elif c == postn[44]: is1 = None
            elif c == postn[45]: ae1 = None
        c += 1
    except: pass
try:
   chat1 = lica.getline("protonAssets\keybinds.txt", postn[32])
   chat2 = lica.getline("protonAssets\keybinds.txt", postn[33])
   chat3 = lica.getline("protonAssets\keybinds.txt", postn[34])
   chat4 = lica.getline("protonAssets\keybinds.txt", postn[35])
   chat5 = lica.getline("protonAssets\keybinds.txt", postn[36])
   chat6 = lica.getline("protonAssets\keybinds.txt", postn[37])
   chatEZ = lica.getline("protonAssets\keybinds.txt", postn[38])
except:
    plsnd()
    print("er06 error accessing text for chat spam")
    lfwm("er06 errorChatSpamGet")

lfwm("eventKeybindsAccessed")
logf2 = open('protonAssets/logs.txt', 'a')
abc = ["", f"{str(t.time())} - load1"]
logf2.writelines('\n'.join(abc))
logf2.close()
guiS = ezSta = False
protonLogo()
lfwm("load2")
isPc1 = isPc2 = thPc1 = thPc2 = 1

if guiS == False:
    print(f"\n\nPress '{hp1}' for a list of commands")
    space(10)
    def disablr():
        global ll, rl, fd, bd, lt, rt, jp, st, ch, ak, tp, cp, am, bs, bl, isq, ae
        ll = rl = fd = bd = lt = rt = jp = st = ch = tp = cp = am = bs = bl = isq = ae = False
        for i in range (1,7):
            exec(f"sta{i} = False")
    def isP1():
        global isPc1
        if isPc1 == 1:
            global ll, rl, fd, bd, lt, rt, jp, st, ch, ak, tp, cp, am, bs, bl, isq, ae
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
                    plsnd("nt")
                    ajc1 = 5
            if jC1 == True:
                if ajc1 == 1:
                    jC1 = False
                else:
                    ajc1 -= 1
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
                    plsnd("nt")
                    ajc2 = 5
            elif jC2 == False:
                if ajc2 == 1:
                    jC2 = False
                else:
                    ajc2 -= 1
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
                    plsnd("nt")
                    ajc3 = 5
            elif jC3 == True:
                if ajc3 == 1:
                    jC3 = False
                else:
                    ajc3 -= 1
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
                    plsnd("nt")
                    ajc4 = 5
            elif jC4 == True:
                if ajc4 == 1:
                    jC4 = False
                else:
                    ajc4 -= 1
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
                    plsnd("nt")
                    ajc5 = 5
            elif jC5 == True:
                if ajc5 == 1:
                    jC5 = False
                else:
                    ajc5 -= 1
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
                    plsnd("nt")
                    ajc6 = 5
            elif jC6 == True:
                if ajc6 == 1:
                    jC6 = False
                else:
                    ajc6 -= 1
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
                    plsnd("nt")
                    ajc7 = 5
            elif jC7 == True:
                if ajc7 == 1:
                    jC7 = False
                else:
                    ajc7 -= 1
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
                    plsnd("nt")
                    ajc8 = 5
            elif jC8 == True:
                if ajc8 == 1:
                    jC8 = False
                else:
                    ajc8 -= 1
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
                    plsnd("nt")
                    ajc9 = 5
            elif jC9 == True:
                if ajc9 == 1:
                    jC9 = False
                else:
                    ajc9 -= 1
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
                    plsnd("nt")
                    ajc0 = 5
            elif jC0 == True:
                if ajc0 == 1:
                    jC0 = False
                else:
                    ajc0 -= 1
            elif key.is_pressed(af1):
                plsnd("nt")
                disablr()
                key.release("shift")
                NF("All","Off")
                lfwm("modALoff")
        except:
            plsnd()
            print("er04 click check error")
            lfwm("er04 clickCheck")
    def isP2():
        global isPc2
        if isPc2 == 1:
            global sta1, sta2, sta3, sta4, sta5, sta6
            global jC1, jC2, jC3, jC4, jC5, jC6, jC7, jC8, jC9, jC0, jC10, jC11, jC12, jC13, jC14, jC15
            global ajc0, ajc1, ajc2, ajc3, ajc4, ajc5, ajc6, ajc7, ajc8, ajc9, ajc10, ajc11, ajc12, ajc13, ajc14, ajc15
            isPc2 = 2
        try:
            if key.is_pressed(cs1):
                lfwm("eventCredits")
                plsnd("nt")
                wait(0.1)
                protonLogo()
                protonCredit()
                wait(0.1)
            elif key.is_pressed(hp1):
                lfwm("eventHelp")
                plsnd("nt")
                protonLogo()
                protonHelp()
            elif key.is_pressed(co1):
                lfwm("eventPatch")
                plsnd("nt")
                protonLogo()
                protonPatch()
            if key.is_pressed(ct1):
                lfwm("eventClose")
                plsnd("nt")
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
                    plsnd("nt")
                    ajc10 = 5
            elif jC10 == True:
                if ajc10 == 1:
                    jC10 = False
                else:
                    ajc10 -= 1
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
                    plsnd("nt")
                    ajc11 = 5
            elif jC11 == True:
                if ajc11 == 1:
                    jC11 = False
                else:
                    ajc11 -= 1
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
                    plsnd("nt")
                    ajc12 = 5
            elif jC12 == True:
                if ajc12 == 1:
                    jC12 = False
                else:
                    ajc12 -= 1
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
                    plsnd("nt")
                    ajc13 = 5
            elif jC13 == True:
                if ajc13 == 1:
                    jC13 = False
                else:
                    ajc13 -= 1
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
                    plsnd("nt")
                    ajc14 = 5
            elif jC14 == True:
                if ajc14 == 1:
                    jC10 = False
                else:
                    ajc14 -= 1
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
                    plsnd("nt")
                    ajc15 = 5
            elif jC15 == True:
                if ajc15 == 1:
                    jC15 = False
                else:
                    ajc15 -= 1
            if jC16 == False:
                if key.is_pressed(is1):
                    if hs == False:
                        hs = True
                        NF("Hotbar Scroll","On")
                        lfwm("modHSon")
                    elif hs == True:
                        hs = False
                        NF("Hotbar Scroll","Off")
                        lfwm("modHSoff")
                    jC16 = True
                    plsnd("nt")
                    ajc16 = 5
            elif jC16 == True:
                if ajc16 == 1:
                    jC16 = False
                else:
                    ajc16 -= 1
            if jC17 == False:
                if key.is_pressed(bl1):
                    if bl == False:
                        bl = True
                        NF("Bow Shoot","On")
                        lfwm("modBTon")
                    elif bl == True:
                        bl = False
                        NF("Bow Shoot","Off")
                        lfwm("modBToff")
                    jC17 = True
                    plsnd("nt")
                    ajc17 = 5
            elif jC17 == True:
                if ajc17 == 1:
                    jC17 = False
                else:
                    ajc17 -= 1
            if jC18 == False:
                if key.is_pressed(bs1):
                    if bs == False:
                        bs = True
                        NF("Bow Spam","On")
                        lfwm("modBSon")
                    elif bs == True:
                        bs = False
                        NF("Bow Spam","Off")
                        lfwm("modBSoff")
                    jC18 = True
                    plsnd("nt")
                    ajc18 = 5
            elif jC18 == True:
                if ajc18 == 1:
                    jC18 = False
                else:
                    ajc18 -= 1
            if jC19 == False:
                if key.is_pressed(ae1):
                    if ezSta == False:
                        disablr()
                        ezSta = True
                        NF("Auto Ezzz","On")
                        lfwm("modATOEZon")
                    elif ezSta == True:
                        ezSta = False
                        NF("Auto Ezzz","Off")
                        lfwm("modATOEZoff")
                    jC19 = True
                    plsnd("nt")
                    ajc19 = 5
            elif jC19 == True:
                if ajc19 == 1:
                    jC19 = False
                else:
                    ajc19 -= 1
        except:
            plsnd()
            print("er04 click check error")
            lfwm("er04 clickCheck")
    def thP1():
        global thPc1
        if thPc1 == 1:
            global ll, rl, fd, bd, lt, rt, jp, st, ch, ak, tp, cp, am, bs, bl, isq, ae
            thPc1 = 2
        try:
            r = ra.randint(2600,3500)
            r = r / 100000
            wait(r)
            if ll == True:
                pygi.click()
            if rl == True:
                pygi.rightClick()
            if fd == True:
                pygi.keyDown(fd2)
            elif fd == False:
                pygi.keyUp(fd2)
            if bd == True:
                pygi.keyDown(bd2)
            elif bd == False:
                pygi.keyUp(bd2)
            if lt == True:
                pygi.keyDown(lt2)
            elif lt == False:
                pygi.keyUp(lt2)
            if rt == True:
                pygi.keyDown(rt2)
            elif rt == False:
                pygi.keyUp(rt2)
            if jp == True:
                pygi.press(jp2)
            if st == True:
                pygi.keyDown(st2)
            elif st == False:
                pygi.keyUp(st2)
            if ch == True:
                pygi.keyDown(ch2)
            elif ch == False:
                pygi.keyUp(ch2)
            if hs == True:
                pyg.scroll(r.randint(1,9))
            if bs == True:
                pygi.mouseDown(button='right')
                t.sleep(0.1)
                pygi.mouseUp(button='right')
            if bl == True:
                pygi.mouseDown(button='right')
                t.sleep(1.3)
                pygi.mouseUp(button='right')
            if ak == True:
                r = ra.randint(10,4999)
                r = r/10000
                wait(r)
                r = ra.randint(1,6)
                if r == 1:
                    pygi.press(fd2)
                elif r == 2:
                    pygi.press(bd2)
                elif r == 3:
                    pygi.press(lt2)
                elif r == 4:
                    pygi.press(rt2)
                elif r == 5:
                    pygi.press(jp2)
                elif r == 6:
                    pyg.click()
        except:
            plsnd()
            print("er05 keyboard click simulation error")
            lfwm("er05 clickSim")
    def thP2():
        global thPc2
        if thPc2 == 1:
            global sta1, sta2, sta3, sta4, sta5, sta6, stb1, stb2, stb3, stb4, stb5, ae, ezSta
            global jC1, jC2, jC3, jC4, jC5, jC6, jC7, jC8, jC9, jC0, jC10, jC11, jC12, jC13, jC14, jC15
            global ajc0, ajc1, ajc2, ajc3, ajc4, ajc5, ajc6, ajc7, ajc8, ajc9, ajc10, ajc11, ajc12, ajc13, ajc14, ajc15
            thPc2 = 2
        try:
            if sta1 == True:
                if stb1 == 1:
                    pygi.press(ca1)
                pygi.write(chat1)
                pygi.press("enter")
                stb1 += 1
            elif sta1 == False:
                stb1 = 1
            if sta2 == True:
                if stb2 == 1:
                    pygi.press(ca1)
                pygi.write(chat2)
                pygi.press("enter")
                stb2 += 1
            elif sta2 == False:
                stb2 = 1
            if sta3 == True:
                if stb3 == 1:
                    pygi.press(ca1)
                pygi.write(chat3)
                pygi.press("enter")
                stb3 += 1
            elif sta3 == False:
                stb3 = 1
            if sta4 == True:
                if stb4 == 1:
                    pygi.press(ca1)
                pygi.write(chat4)
                pygi.press("enter")
                stb4 += 1
            elif sta4 == False:
                stb4 = 1
            if sta5 == True:
                if stb5 == 1:
                    pygi.press(ca1)
                pygi.write(chat5)
                pygi.press("enter")
                stb5 += 1
            elif sta5 == False:
                stb5 = 1
            if sta6 == True:
                if stb6 == 1:
                    pygi.press(ca1)
                pygi.write(chat6)
                pygi.press("enter")
                stb6 += 1
            elif sta6 == False:
                stb6 = 1
            if ezSta == True:
                if False == True: #replace with check for kill message
                    pygi.press(ca1)
                    pygi.write(chatEZ)
                    pygi.press("enter")
                    pygi.press("esc")
                stb7 += 1
            elif sta6 == False:
                stb7 = 1
        except:
            plsnd()
            print("er05 keyboard click simulation error")
            lfwm("er05 clickSim")
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
            plsnd()
            print("er07 threading error")
            lfwm("er07 threading")
kB.close()
