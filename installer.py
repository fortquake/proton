# the specified version of playsound must be used otherwise you get an error about 'MCI'
import os, time as t
print('''You are running Proton Installer\n
It will install:\n- pyautogui\n- pydirectinput\n- playsound\n- keyboard\n
Press enter to start the installer.\nTo exit, close the window.''')
input("> "); print("\nThe installer will proceed.\n")
os.system("pip install keyboard"); os.system("py -m pip install pyautogui"); os.system("py -m pip install pydirectinput"); os.system("py -m pip install playsound==1.2.2")
print("Proton Installer has completed setup, you may now run Proton."); t.sleep(9); exit()