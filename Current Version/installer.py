import os, time as t
print('''
You are running the Proton Installer for Proton v1.1.3\n\nIt will install:\n- pyautogui\n- pydirectinput\n- playsound\n- keyboard\n\nPress x, then press enter to start the installer.\nTo exit, close the window.''')
while True:
    try:
        r = str(input("> "))
        if r == "x":
            print("\nThe installer will proceed."); t.sleep(0.1); break
    except:
        pass
os.system("pip install keyboard"); os.system("pip install pyautogui"); os.system("pip install pydirectinput"); os.system("pip install playsound==1.2.2") # otherwise you get an error about 'MCI'
print("\nThe Proton Installer has completed setup, you may now run Proton."); t.sleep(15); exit()
