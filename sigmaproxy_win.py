# Sigma Proxy v1
# Created by AK
# Date: 08/21/24

import requests
import os
import time
import subprocess
import psutil
import colorama, fake_useragent

tor_path = "Browser\\TorBrowser\\Tor\\tor.exe"
torrc = "Browser\\TorBrowser\\Data\\torrc"

print(colorama.Fore.LIGHTGREEN_EX+'''
      
  ██████   ██▓ ▄████  ███▄ ▄███▓ ▄▄▄          ██▓███   ██▀███   ▒█████  ▒██   ██▒▓██   ██▓
▒██    ▒ ▒▓██▒ ██▒ ▀█▓██▒▀█▀ ██▒▒████▄       ▓██░  ██ ▓██ ▒ ██▒▒██▒  ██▒▒▒ █ █ ▒░ ▒██  ██▒
░ ▓██▄   ▒▒██▒▒██░▄▄▄▓██    ▓██░▒██  ▀█▄     ▓██░ ██▓▒▓██ ░▄█ ▒▒██░  ██▒░░  █   ░  ▒██ ██░
  ▒   ██▒░░██░░▓█  ██▒██    ▒██ ░██▄▄▄▄██    ▒██▄█▓▒ ▒▒██▀▀█▄  ▒██   ██░ ░ █ █ ▒   ░ ▐██▓░
▒██████▒▒░░██░▒▓███▀▒▒██▒   ░██▒▒▓█   ▓██    ▒██▒ ░  ░░██▓ ▒██▒░ ████▓▒░▒██▒ ▒██▒  ░ ██▒▓░
▒ ▒▓▒ ▒ ░ ░▓  ░▒   ▒ ░ ▒░   ░  ░░▒▒   ▓▒█    ▒▓▒░ ░  ░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ▒▒ ░ ░▓ ░   ██▒▒▒ 
░ ░▒  ░  ░ ▒ ░ ░   ░ ░  ░      ░░ ░   ▒▒     ░▒ ░       ░▒ ░ ▒   ░ ▒ ▒░ ░░   ░▒ ░ ▓██ ░▒░ 
░  ░  ░  ░ ▒ ░ ░   ░ ░      ░     ░   ▒      ░░         ░░   ░ ░ ░ ░ ▒   ░    ░   ▒ ▒ ░░  
      ░    ░       ░        ░         ░                  ░         ░ ░   ░    ░   ░ ░     

Created by AK

[*] Ip Rotation
[*] Windows Support only
[*] Utilizes Tor relays as proxies

Keep your internet activity hidden with this simple IP masker.
Open Mozilla Firefox and set your proxy to SOCKS5, IP: 127.0.0.1, PORT: 9050.
''')

rotate = input("Want to rotate your proxies, this can improve operational security? (Y/n)")
delay = 30 # time between ip rotation
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

response = requests.get("https://api.myip.com")
ip = response.json().get('ip')
print(f"[-] Your IP: {ip}")

time.sleep(10)

url = "https://api.myip.com"
proxy = {
    'http': 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'
}

try:
    if rotate.lower() != 'n':
          while True:
              session = requests.Session()
              session.proxies.update(proxy)
              session.headers.update({"User-Agent": fake_useragent.UserAgent().random})
              response = session.get(url)
              if response.status_code == 200:
                  try:
                      ip = response.json().get('ip')
                      print(f"[✔] socks5://127.0.0.1:9050 || IP Changed {ip}")
                      if delay != float(0) and rotate.lower() != 'n':
                          time.sleep(float(delay))
                          close_tor()
                          subprocess.Popen(tor_path, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                  except ValueError:
                      print("[X] Failed to parse JSON response.")
              else:
                  print(f"[X] Received unexpected status code {response.status_code}")
    else:
        session = requests.Session()
        session.proxies.update(proxy)
        session.headers.update({"User-Agent": fake_useragent.UserAgent().random})
        response = session.get(url)
        if response.status_code == 200:
            try:
                ip = response.json().get('ip')
                print(f"[✔] socks5://127.0.0.1:9050 || IP Changed {ip}")
                input("Press Enter to continue...")
                close_tor()
                exit()
            except ValueError:
                print("[X] Failed to parse JSON response.")
                close_tor()
                exit()
        
        
except requests.exceptions.ConnectionError as error:
    print(f"[X] {error}")
    input("You are still connected via the Tor network but rotation might not be functioning properly.")
    close_tor()
    exit()
except KeyboardInterrupt:
    close_tor()
except Exception as Error:
    print(Error)
    close_tor()
