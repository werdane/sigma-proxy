import requests
import os
import time
import subprocess
import psutil
import colorama 

tor_path = "Browser\\TorBrowser\\Tor\\tor.exe"
torrc = "Browser\\TorBrowser\\Data\\torrc"

print(colorama.Fore.LIGHTGREEN_EX+'''

  .-')                        _   .-')      ('-.                      _ (`-.                   ('-. .-.   ('-.         .-') _               ('-.  _  .-')   
 ( OO ).                     ( '.( OO )_   ( OO ).-.                 ( (OO  )                 ( OO )  /  ( OO ).-.    ( OO ) )            _(  OO)( \( -O )  
(_)---\_)  ,-.-')   ,----.    ,--.   ,--.) / . --. /        ,-.-')  _.`     \         .-----. ,--. ,--.  / . --. /,--./ ,--,'  ,----.    (,------.,------.  
/    _ |   |  |OO) '  .-./-') |   `.'   |  | \-.  \         |  |OO)(__...--''        '  .--./ |  | |  |  | \-.  \ |   \ |  |\ '  .-./-')  |  .---'|   /`. ' 
\  :` `.   |  |  \ |  |_( O- )|         |.-'-'  |  |        |  |  \ |  /  | |        |  |('-. |   .|  |.-'-'  |  ||    \|  | )|  |_( O- ) |  |    |  /  | | 
 '..`''.)  |  |(_/ |  | .--, \|  |'.'|  | \| |_.'  |        |  |(_/ |  |_.' |       /_) |OO  )|       | \| |_.'  ||  .     |/ |  | .--, \(|  '--. |  |_.' | 
.-._)   \ ,|  |_.'(|  | '. (_/|  |   |  |  |  .-.  |       ,|  |_.' |  .___.'       ||  |`-'| |  .-.  |  |  .-.  ||  |\    | (|  | '. (_/ |  .--' |  .  '.' 
\       /(_|  |    |  '--'  | |  |   |  |  |  | |  |      (_|  |    |  |           (_'  '--'\ |  | |  |  |  | |  ||  | \   |  |  '--'  |  |  `---.|  |\  \  
 `-----'   `--'     `------'  `--'   `--'  `--' `--'        `--'    `--'              `-----' `--' `--'  `--' `--'`--'  `--'   `------'   `------'`--' '--' 

Created by AK

[*] Ip Rotation
[*] Windows Support only
[*] Utilizes Tor relays as proxies

Keep your internet activity hidden with this simple IP masker.
Open Mozilla Firefox and set your proxy to SOCKS5, IP: 127.0.0.1, PORT: 9050.
''')

delay = input("Enter seconds between IP rotation (0 for no rotation): ")
delay = float(delay)
subprocess.Popen(tor_path, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def close_tor():
    for proc in psutil.process_iter(['pid', 'name']):
        if 'tor.exe' in proc.info['name']:
            proc.terminate()
            return

version_info = os.popen(f"{tor_path} --version").read().strip()
version = version_info.split('\n')[0].split(' ')[2]
print(f"[-] Current Tor Version: {version}")

response = requests.get("https://httpbin.org/ip")
ip = response.json().get('origin')
print(f"[-] Your IP: {ip}")

time.sleep(10)

url = "https://httpbin.org/ip"
proxy = {
    'http': 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'
}

try:
    session = requests.Session()
    session.proxies.update(proxy)
    response = session.get(url)
    if response.status_code == 200:
        try:
            ip = response.json().get('origin')
            print(f"[✔] IP Changed -> {ip}")
        except ValueError:
            print("[X] Failed to parse JSON response.")
    while True:
        session = requests.Session()
        session.proxies.update(proxy)
        response = session.get(url)
        if response.status_code == 200:
            try:
                ip = response.json().get('origin')
                print(f"[✔] socks5://127.0.0.1:9050 || IP Changed -> {ip}")
            except ValueError:
                print("[X] Failed to parse JSON response.")
        else:
            print(f"[X] Received unexpected status code {response.status_code}")
        
        if delay != float(0):
            time.sleep(float(delay))
            close_tor()
            subprocess.Popen(tor_path, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
except requests.exceptions.ConnectionError as error:
    print(f"[X] {error}")
except KeyboardInterrupt:
    close_tor()
except Exception as Error:
    print(Error)
