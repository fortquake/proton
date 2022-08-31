import os, time as t
print('''You are running the Proton Installer for Proton v1.2.1\n
It will install:\n- pyautogui\n- pydirectinput\n- playsound\n- keyboard\n
Press enter (or type x, and then press enter) to start the installer.\nTo exit, close the window.''')
while True:
    if ((str(input("> "))) == "x") or ((str(input("> "))) == ""): print("\nThe installer will proceed.\n"); break
os.system("pip install keyboard"); os.system("pip install pyautogui"); os.system("pip install pydirectinput"); os.system("pip install playsound==1.2.2") # with playsound, otherwise you get an error about 'MCI'
print("The Proton Installer has completed setup, you may now run Proton."); t.sleep(9); exit()