# Sigma Proxy v1
# Created by AK
# Date: 08/21/24

import requests
import os
import time
import subprocess
import psutil
import colorama, fake_useragent


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
[*] Windows & Linux Support only
[*] Utilizes Tor relays as proxies

Keep your internet activity hidden with this simple IP masker.
Open Mozilla Firefox and set your proxy to SOCKS5, IP: 127.0.0.1, PORT: 9050.
''')
rotate = input("Want to rotate your proxies, this can improve operational security? (Y/n)")
delay = 30 # time between ip rotation
delay = float(delay)

subprocess.Popen("service tor start", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
def close_tor():
    for proc in psutil.process_iter(['pid', 'name']):
        if 'tor.exe' in proc.info['name']:
            proc.terminate()
            return

version_info = os.popen(f"tor --version").read().strip()
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
    if rotate.lower() != "n':
          while True:
              #session = requests.Session()
              #session.proxies.update(proxy)
              #session.headers.update({"User-Agent": fake_useragent.UserAgent().random})
              #response = session.get(url)
              if 200 == 200:
                  try:
                      #ip = response.json().get('ip')
                      print(f"[✔] socks5://127.0.0.1:9050 || IP Changed {ip}")
                      if delay != float(0) and rotate.lower() != 'n':
                          time.sleep(float(delay))
                          subprocess.Popen("service tor reload", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                  except ValueError:
                      print("[X] Failed to parse JSON response.")
              else:
                  pass
                  #print(f"[X] Received unexpected status code {response.status_code}")
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
                subprocess.Popen("service tor stop", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                exit()
            except ValueError:
                print("[X] Failed to parse JSON response.")
                subprocess.Popen("service tor stop", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                exit()
        
except requests.exceptions.ConnectionError as error:
    print(f"[X] {error}")
    input("You are still connected via the Tor network but rotation might not be functioning properly, press enter to quit everything...")
    subprocess.Popen("service tor stop", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    exit()

except KeyboardInterrupt:
    subprocess.Popen("service tor stop", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

except Exception as Error:
    print(Error)
    subprocess.Popen("service tor stop", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    close_tor()
    exit()
