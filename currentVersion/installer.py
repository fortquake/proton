import time as t
import os
def s(z):
    for i in range(z):
        print()
print("You are running the Proton Installer v1.1.0 for Proton v2.5.0")
print('''
It will install:
pyautogui
pydirectinput
playsound
keyboard
''')
s(1)
r1 = False
print("Press x, then press enter to start the installer.")
while r1 == False:
    try:
        r = str(input())
        if r == "x":
            print("The installer will proceed.")
            s(1)
            t.sleep(0.1)
            r1 = True
    except:
        pass
t.sleep(0.1)
os.system("pip install pyautogui")
t.sleep(0.3)
os.system("pip install playsound==1.2.2") #otherwise you get an error 'MCI'
t.sleep(0.3)
os.system("pip install pydirectinput")
t.sleep(0.3)
os.system("pip install keyboard")
s(2)
print("The Proton Installer has completed setup, you may now run Proton.")
t.sleep(15)
exit()
