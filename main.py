#!/bin/python
import os
import time
import datetime
import discordwh
import opengarage

# set connection and disconnection time variables
dtime = int(time.time())
ctime = int(time.time())

# set device variables
james = 1
ktz = 1
jk1 = ctime
jk2 = dtime
jkhost = "10.0.0.203"

# set time requirement between disconnect and reconnect
# 300 for 5 mins
timethres = 900


def timepassage(t1, t2, ts): #verify time requirement threshold has passed
	if t1 - t2 > ts:
		return True
	else:
		return False


# print current time
def printtime():
	now = datetime.datetime.now()
	current_time = now.strftime("%H:%M:%S")
	print("Current Time =", current_time)

#check whether host is active, return 1 if up 0 if down
def check_host(x):
	hostname = x
	response = os.system("ping -c1 -w2 " + hostname + ">/dev/null 2>&1")
	if response != 0:
		up = 0
	# and then check the response...
	elif response == 0:
		up = 1
	return up

# monitor changes in connection
# runcheck(hostname,newcheck,oldcheck,connectiontime,disconnectiontime)
# returns variables to retain globally
def runcheck(host, c2, c1, ct, dt):
	time.sleep(3)
	nc = check_host(host)
	c2 = nc # check host state and set c2 as current state
	if c1 != c2 and c2 == 1: # if old check c1 doesn't equal new check c2, and new check c2 returns host as up, fire.
		print("---------------------")
		c1 = c2 # old check = current check
		ct = time.time() # grab current time
		if c2 == 1: # double check current state is up
			print("Device connected", host)
			printtime()
			if timepassage(ct, dt, timethres): # verify time threshold has passed since last disconnection
				# print("opening garage")
				message = "Opening Garage: " + str(cc) + " of " + str(timethres)
				#discordwh.discord_notif(message)
				printtime()
				opengarage.opengarage()
				print("---------------------")
			else:
				print("15 mins has not passed")
				cc = ct - dt
				message = "Time Threshold not reached: " + str(cc) + " of " + str(timethres)
				#discordwh.discord_notif(message)
				print("Time passed:", ct - dt, " of", timethres)
				printtime()
				print("---------------------")
	elif c1 != c2 and c2 == 0: # if old check doesn't equal new check, and host is down, then
		print("---------------------")
		c1 = c2
		print("device disconnected", host)
		printtime()
		dt = time.time()
		print("---------------------")
	else: # otherwise the device is probably still connected
		c1 = c2
		if c2 == 1: # double check new check says host is up
			print(host, "still connected")
	return host, c2, c1, ct, dt



while True:
	jkhost,james,ktz,jk1,jk2 = runcheck(jkhost, james, ktz, jk1, jk2)
	# set tupled variables as their returned values, allowing us to pass new values in on each loop
	# monitor changes in connection
	# runcheck(hostname,newcheck,oldcheck,connectiontime,disconnectiontime)
	# returns variables to retain globally
