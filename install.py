import os
import sys
if sys.platform=='win32': os.system('cls')
if sys.platform=='linux': os.system('clear')

print("Sigma Proxy Installer")
print("Created by AK")
if sys.platform == "win32":
    os.system("pip install requests requests[socks] colorama psutil")
    os.system('cls')
    os.system("python sigmaproxy_win.py")
if sys.platform == "linux":
    os.system("sudo apt install python3-full")
    os.system("pip3 install requests requests[socks] colorama psutil")
    os.system('clear')
    os.system("python3 sigmaproxy_lin.py")
else:
    print("OS not supported")
