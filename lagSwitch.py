import keyboard
import os
from colorama import Fore, Style, init

init(autoreset=True)

def main_window():
    os.system('cls')
    print(f"{Fore.CYAN}Lag switch v1.5")
    print("----------------------------------------")
    print(f"{Fore.YELLOW}\tCtrl + E{Style.RESET_ALL} = Internet enabled")
    print(f"{Fore.YELLOW}\tCtrl + Q{Style.RESET_ALL} = Internet disabled")
    #print("\tShift + Esc = Close Lag switch")
    print("----------------------------------------")
    print(f"by {Fore.MAGENTA}devix7{Style.RESET_ALL}\n")

def disable_internet():
    main_window()
    print(Fore.RED + 'Status:')
    print('Disabling internet now on Windows...')
    os.system('ipconfig/release > nul')
    print('Internet disabled.')

def enable_internet():
    main_window()
    print(Fore.GREEN + 'Status:')
    print('Enabling internet now on Windows...')
    os.system('ipconfig/renew > nul')
    print('Internet enabled.')

main_window()

keyboard.add_hotkey('ctrl+q', disable_internet)
keyboard.add_hotkey('ctrl+e', enable_internet)
keyboard.wait("left shift+esc")
