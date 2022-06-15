#!/bin/python
import os
import time
import datetime


# replace <path to scripts> below

HostUp = "null"


# 900 for 15 mins
def timepassage(t1, t2):
	if t1 - t2 > 900:
		return True
	else:
		return False


def check_host(x):
	hostname = x
	response = os.system("ping -c 1 " + hostname + ">/dev/null 2>&1")
	if response != 0:
		pingstatus = "inactive"
		up = 0
	# and then check the response...
	else:
		pingstatus = "active"
		up = 1
	return pingstatus, up


def open_garage():
	os.system("python3 <path to scripts>/open-garage.py")


def discord(string):
	Message = string
	Notif = "<path to scripts>/discord-notif.sh Garage "
	Command = Notif + Message
	os.system(str(Command))


dtime = int(time.time())
ctime = int(time.time())

check = ["active", 1]
oldcheck = ["active", 1]

while True:
	time.sleep(3)
	check = check_host("10.0.0.241")

	if oldcheck[1] != check[1] and check[1] == 1:
		oldcheck = check
		ctime = time.time()
		if check[0] == "active":
			if timepassage(ctime, dtime):
				print("opening garage")
				discord("opening")
				open_garage()
			else:
				print("15 mins has not passed")
	elif oldcheck[1] != check[1] and check[1] == 0:
		oldcheck = check
		print("device disconnected")
		dtime = time.time()
