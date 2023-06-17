import keyboard
import os

def tutor():
    os.system('cls')
    print("Lag switch")
    print("----------------------------------------")
    print("     Ctrl + E = Internet enabled")
    print("     Ctrl + Q = Internet disabled")
    print("----------------------------------------")
    print("by devix7")
    print(" ")

def disable_internet():
    tutor()
    print('Status:')
    print('Disabling internet now on Windows...')
    os.system('ipconfig/release > nul')
    print('Internet disabled.')

def enable_internet():
    tutor()
    print('Status:')
    print('Enabling internet now on Windows...')
    os.system('ipconfig/renew > nul')
    print('Internet enabled.')

tutor()

keyboard.add_hotkey('ctrl+q', disable_internet)
keyboard.add_hotkey('ctrl+e', enable_internet)

keyboard.wait('esc')
