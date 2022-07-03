import os
import platform
import json
import requests
import time

greenlight = "\033[32m"
white = "\033[37m"

meme = """
───────▄▀▀▀▀▀▀▀▀▀▀▄▄
────▄▀▀░░░░░░░░░░░░░▀▄
──▄▀░░░░░░░░░░░░░░░░░░▀▄
──█░░░░░░░░░░░░░░░░░░░░░▀▄
─▐▌░░░░░░░░▄▄▄▄▄▄▄░░░░░░░▐▌
─█░░░░░░░░░░░▄▄▄▄░░▀▀▀▀▀░░█
▐▌░░░░░░░▀▀▀▀░░░░░▀▀▀▀▀░░░▐▌
█░░░░░░░░░▄▄▀▀▀▀▀░░░░▀▀▀▀▄░█
█░░░░░░░░░░░░░░░░▀░░░▐░░░░░▐▌
▐▌░░░░░░░░░▐▀▀██▄░░░░░░▄▄▄░▐▌
─█░░░░░░░░░░░▀▀▀░░░░░░▀▀██░░█
─▐▌░░░░▄░░░░░░░░░░░░░▌░░░░░░█
──▐▌░░▐░░░░░░░░░░░░░░▀▄░░░░░█
───█░░░▌░░░░░░░░▐▀░░░░▄▀░░░▐▌
───▐▌░░▀▄░░░░░░░░▀░▀░▀▀░░░▄▀
───▐▌░░▐▀▄░░░░░░░░░░░░░░░░█
───▐▌░░░▌░▀▄░░░░▀▀▀▀▀▀░░░█
───█░░░▀░░░░▀▄░░░░░░░░░░▄▀
──▐▌░░░░░░░░░░▀▄░░░░░░▄▀
─▄▀░░░▄▀░░░░░░░░▀▀▀▀█▀
▀░░░▄▀░░░░░░░░░░▀░░░▀▀▀▀▄▄▄▄▄

  ___  _   _   __  ____   __   ____  ___  ____
 / _ \| | | | |  \/  \ \ / /  / ___|/ _ \|  _ \ 
| | | | |_| | | |\/| |\ V /  | |  _| | | | | | |
| |_| |  _  | | |  | | | |   | |_| | |_| | |_| |
 \___/|_| |_| |_|  |_| |_|    \____|\___/|____/
"""

banner = """
────────────•◈•────────────

░█▀▀█ 　 ▀█▀ 　 ░█▀▀█ 　 ░█─░█ 　 ░█▀▀▀█ 
░█─▄▄ 　 ░█─ 　 ░█▄▄█ 　 ░█▀▀█ 　 ─▀▀▀▄▄ 
░█▄▄█ 　 ▄█▄ 　 ░█─── 　 ░█─░█ 　 ░█▄▄▄█    by: XI-RPL

────────────•◈•────────────
"""

if platform.system() == "Windows":
	clear = "cls"
else:
	clear = "clear"

def intro():
	os.system(clear)
	print(greenlight + meme + white)
	if platform.system() == "Windows":
		time.sleep(2)
		main()
	else:
		time.sleep(1)
		print("[*] Updating all package...")
		time.sleep(1)
		os.system("apt update && apt upgrade -y")
		time.sleep(1)
		main()

def main():
	os.system(clear)
	print(greenlight + banner + white)
	ipaddr = input("Masukan IP Address > ")
	ipreq = requests.get(f"http://ip-api.com/json/{ipaddr}")
	if ipreq.status_code == 200:
		ipdata = json.loads(ipreq.text)
		if ipdata["status"] == "success":
			for key in ipdata:
				print(f"{key.capitalize()} : {ipdata[key]}")
				if key == "lon":
					lat = ipdata["lat"]
					lon = ipdata["lon"]
					maps = f"https://www.google.com/maps/@{lat},{lon},9z"
					print(f"Maps: {maps}")
	if ipaddr == "127.0.0.1":
		print("Masukan alamat IP yang bener, itu localhost!!!")


if __name__ == "__main__":
	intro()
