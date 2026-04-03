```python
import os
import platform
import subprocess
import re

# --- BRANDING ---
C = '\033[96m'
G = '\033[92m'
Y = '\033[93m'
R = '\033[91m'
W = '\033[0m'

def banner():
    print(f"""
{R}  ██████  ██▓███  ▓██   ██▓    ██░ ██  ▄▄▄       ██▀███   ██▒   █▓
 ▒██    ▒ ▓██░  ██▒▒██  ██▒    ▓██░ ██▒▒████▄    ▓██ ▒ ██▒▓██░   █▒
 ░ ▓██▄   ▓██░ ██▓▒ ▒██ ██░    ▒██▀▀██░▒██  ▀█▄  ▓██ ░▄█ ▒ ▓██  █▒░
   ▒   ██▒▒██▄█▓▒ ▒ ░ ▐██▓░    ░▓█ ░██ ░██▄▄▄▄██ ▒██▀▀█▄    ▒██ █░░ 
 ▒██████▒▒▒██▒ ░  ░ ░ ██▒▓░    ░▓█▒░██▓ ▓█   ▓██▒░██▓ ▒██▒   ▒▀█░   
 ▒ ▒▓▒ ▒ ░▒▓▒ ░ ░░  ██▒▒▒       ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒▓ ░▒▓░   ░ ▐░   
 ░ ░▒  ░ ░░▒ ░      ▓██ ░▒░      ▒ ░▒░ ░  ▒   ▒▒ ░  ░▒ ░ ▒░   ░ ░░   
 ░  ░  ░  ░░        ▒ ▓ ░░       ░  ░░ ░  ░   ▒     ░░   ░      ░░   
       ░            ░ ░          ░  ░  ░      ░  ░   ░           ░   
{W}{C}         >>> SPY-WIFI-HARVESTER | 123Tool Premium <<<
    """)

def harvest_windows():
    print(f"{Y}[*] Detecting Windows System... Harvesting Profiles...{W}")
    try:
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
        profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
        for i in profiles:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            try:
                print(f"{G}SSID: {i:<20} | Password: {results[0]}{W}")
            except IndexError:
                print(f"{G}SSID: {i:<20} | Password: {R}[OPEN NETWORK]{W}")
    except Exception as e:
        print(f"{R}[!] Error: {e}{W}")

def harvest_linux():
    print(f"{Y}[*] Detecting Linux System... Accessing NetworkManager...{W}")
    path = "/etc/NetworkManager/system-connections/"
    if not os.path.exists(path):
        print(f"{R}[!] Error: NetworkManager profiles not found. Are you root?{W}")
        return
    
    files = os.listdir(path)
    for file in files:
        with open(path + file, 'r') as f:
            content = f.read()
            ssid_match = re.search(r'ssid=(.*)', content)
            psk_match = re.search(r'psk=(.*)', content)
            if ssid_match:
                ssid = ssid_match.group(1)
                psk = psk_match.group(1) if psk_match else f"{R}[OPEN/No PSK]{W}"
                print(f"{G}SSID: {ssid:<20} | Password: {psk}{W}")

def main():
    os.system('clear' if os.name == 'posix' else 'cls')
    banner()
    current_os = platform.system()
    
    if current_os == "Windows":
        harvest_windows()
    elif current_os == "Linux":
        harvest_linux()
    else:
        print(f"{R}[!] OS {current_os} not supported yet for auto-harvesting.{W}")

if __name__ == "__main__":
    main()
