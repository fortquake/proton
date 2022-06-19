import os, time as t
print('''You are running the Proton Installer for Proton v1.1.5\n
It will install:\n- pyautogui\n- pydirectinput\n- playsound\n- keyboard\n\nPress x, then press enter to start the installer.\nTo exit, close the window.''')
while True:
    if (str(input("> "))) == "x": print("\nThe installer will proceed."); break
os.system("pip install keyboard"); os.system("pip install pyautogui"); os.system("pip install pydirectinput"); os.system("pip install playsound==1.2.2") # with playsound, otherwise you get an error about 'MCI'
print("\nThe Proton Installer has completed setup, you may now run Proton."); t.sleep(9); exit()