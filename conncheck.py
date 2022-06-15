#!/bin/python
import os
import time


ip = "10.0.0.1"

def check_host(host):
        response = os.system("ping -c 1 " + host + ">/dev/null 2>&1")
        if response != 0:
                status = "inactive"
                up = 0
        # and then check the response...
        else:
                status = "active"
                up = 1
        return status, up


while True:
	test = check_host(ip)
	if test[1] == 1:
		print("status: online")
	else:
		print("Status offline -- rebooting")
		os.system("sudo init 6")
	time.sleep(3600)
