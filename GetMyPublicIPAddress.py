# Created by: Ruben Leonardo Sigalingging.
# Created on: Sunday, June 12, 2022, 1:54 PM.
# Using: Python Programming Language Version 3.8.10

# Function: This tool or Program serves to get all the information from a person's Public IP address.


# Dibuat oleh: Ruben Leonardo Sigalingging.
# Dibuat pada: Minggu, 12 Juni 2022, Pukul 1:54 Siang.
# Menggunakan: Bahasa Pemrogramman Python Versi 3.8.10

# Fungsi: Alat atau Program ini berfungsi untuk mendapatkan semua informasi dari alamat IP Publik seseorang.


#!/usr/bin/env python3


def import_python_module():
	import os
	import sys
	from sys import exit
	from sys import version_info
	import requests
	import urllib
	from urllib import request
	import json
	import pyfiglet
	from os import system
import_python_module()


# This tool or program using Indonesia Language.
# Alat atau program ini menggunakan Bahasa Indonesia.


# ---PENGANTAR---
def Introduction():
	print("---INTRODUCTION---")
	print("Source: https://id.wikipedia.org/wiki/Alamat_IP")
	print("Alamat IP")
	print("Internet Protocol Address (atau disingkat alamat IP)")
	print("Adalah label numerik yang ditetapkan untuk setiap perangkat yang terhubung ke jaringan komputer.")
	print("Yang menggunakan Protokol Internet untuk komunikasi.")
Introduction()


# TIME TO CODE
def time_to_code(created_by = "ruben leonardo sigalingging."):
	import os
	import sys
	from sys import exit
	from sys import version_info
	import requests
	import urllib
	from urllib import request
	import json
	import pyfiglet
	from os import system


	tema = pyfiglet.figlet_format("IP Address",font="slant")
	print(tema)
	print("\033[91m[\033[94m!\033[91m] \033[94mCreated by: \033[91mRuben Leonardo Sigalingging.")
	print("\033[91m[\033[94m!\033[91m] \033[94mCreated on: \033[91mSunday, June 12, 2022, 1:54 PM.")
	print("\033[91m[\033[94m!\033[91m] \033[94mUsing: \033[91mPython Programming Language Version 3.8.10")
	print("\033[91m[\033[94m!\033[91m] \033[94mFunction: \033[91mThis tool or Program serves to get all the information from a person's Public IP address.")
	print("\n")

	public_ip_address = requests.post("http://ip-api.com/json/",data={'queryIp' : 'public_ip_address'}).text

	parsing_json_data = json.loads(public_ip_address)
	print("\n")
	print(parsing_json_data)


	print(f"\033[91m[\033[94m!\033[91m] \033[94mStatus: \033[91m{parsing_json_data['status']}")
	print(f"\033[91m[\033[94m!\033[91m] \033[94mCountry: \033[91m{parsing_json_data['country']}")
	print(f"\033[91m[\033[94m!\033[91m] \033[94mCountry Code: \033[91m{parsing_json_data['countryCode']}")
	print(f"\033[91m[\033[94m!\033[91m] \033[94mRegion Name: \033[91m{parsing_json_data['regionName']}")
	print(f"\033[91m[\033[94m!\033[91m] \033[94mCity: \033[91m{parsing_json_data['city']}")
	print(f"\033[91m[\033[94m!\033[91m] \033[94mLatitude: \033[91m{parsing_json_data['lat']}")
	print(f"\033[91m[\033[94m!\033[91m] \033[94mLongitude: \033[91m{parsing_json_data['lon']}")
	print(f"\033[91m[\033[94m!\033[91m] \033[94mTimezone: \033[91m{parsing_json_data['timezone']}")
	print(f"\033[91m[\033[94m!\033[91m] \033[94mISP: \033[91m{parsing_json_data['isp']}")
	print(f"\033[91m[\033[94m!\033[91m] \033[94mOrganization: \033[91m{parsing_json_data['org']}")
	print(f"\033[91m[\033[94m!\033[91m] \033[94mAutonomous System Numbers: \033[91m{parsing_json_data['as']}")
	print(f"\033[91m[\033[94m!\033[91m] \033[94mQuery: \033[91m{parsing_json_data['query']}")
	print("\n\n\n")
# time_to_code()


# file permission
from os import system
system("chmod 777 GetMyPublicIPAddress.py")


answer = "Y"
while(answer=="Y"):
	time_to_code()
	ask = input("[!] Do You Want To Try Again?\n[!] (Y/n): ")
	if ask != "Y":
		break