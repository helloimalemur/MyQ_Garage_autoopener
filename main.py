#!/bin/python
import opengarage
import os
import time
import datetime

dtime = int(time.time())
ctime = int(time.time())

james = 1
koonts = 1
jk1 = ctime
jk2 = dtime
jkhost = "10.0.0.203"

matt = 1
bell = 1
mb1 = ctime
mb2 = dtime
mbhost = "10.0.0.212"

#tom = 1
#mac = 1
#tm1 = ctime
#tm2 = dtime


# 300 for 5 mins
timethres = 1800
def timepassage(t1, t2, ts):
	if t1 - t2 > ts:
		return True
	else:
		return False

def printtime():
	now = datetime.datetime.now()
	current_time = now.strftime("%H:%M:%S")
	print("Current Time =", current_time)


def check_host(x):
	hostname = x
	response = os.system("ping -c 1 " + hostname + ">/dev/null 2>&1")
	if response != 0:
		up = 0
	# and then check the response...
	elif response == 0:
		up = 1
	return up


def open_garage():
	opengarage.opengarage()



def runcheck(host, c2, c1, ct, dt):
	time.sleep(3)
	nc = check_host(host)
	c2 = nc
	if c1 != c2 and c2 == 1:
		print("---------------------")
		c1 = c2
		ct = time.time()
		if c2 == 1:
			print("Device connected", host)
			printtime()
			if timepassage(ct, dt, timethres):
				print("opening garage")
				printtime()
				open_garage()
				print("---------------------")
			else:
				print("15 mins has not passed")
				#print("opening garage")
				print("Time passed:", ct - dt, " of", timethres)
				printtime()
				#open_garage()
				print("---------------------")
	elif c1 != c2 and c2 == 0:
		print("---------------------")
		c1 = c2
		print("device disconnected", host)
		printtime()
		dt = time.time()
		print("---------------------")
	else:
		c1 = c2
		if c2 == 1:
			print(host, "still connected")
	return host, c2, c1, ct, dt



while True:
	jkhost,james,koonts,jk1,jk2 = runcheck(jkhost, james, koonts, jk1, jk2)
	mbhost,matt,bell,mb1,mb2 = runcheck(mbhost, matt, bell, mb1, mb2)
