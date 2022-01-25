import time as t
import os
def s(z):
    for i in range(z):
        print()
print("You are running the Proton Installer v1.1.1 for Proton v1.0.3")
print('''
It will install:
 pyautogui
 pydirectinput
 playsound
 keyboard
''')
r1 = False
print("Press x, then press enter to start the installer.")
while r1 == False:
    try:
        r = str(input())
        if r == "x":
            print("\nThe installer will proceed.\n")
            t.sleep(0.1); r1 = True
    except:
        pass
os.system("pip install pyautogui")
os.system("pip install playsound==1.2.2") #otherwise you get an error 'MCI'
os.system("pip install pydirectinput")
os.system("pip install keyboard")
print("The Proton Installer has completed setup, you may now run Proton.")
t.sleep(15)
exit()
