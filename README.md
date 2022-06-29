# MyQ_Garage_autoopener
Monitors for presence of specified IP address, such as a cell phone, and opens MyQ Garage upon device connection. Uses Cron to start and stop script within Screen session.



1. pip install aiohttp pymyq
2. Add/edit variables and commands at bottom/top of main.py (see example below)
3. add account info to closegarage.py and opengarage.py
4. Cron starting and stopping using screen-checkhost.sh and screen-checkhost-stop.sh
  
  
  
  
**example cron**;
{0 1 * * * /<path to scripts>/screen-checkhost-stop.sh}
{0 6 * * * /<path to scripts>/screen-checkhost.sh}
  
**example variables to add/edit in checkhost.py**;
james = 1
koonts = 1
jk1 = ctime
jk2 = dtime
jkhost = "10.0.0.203"
  
**command to be placed at bottom**;
(jkhost,james,koonts,jk1,jk2 = runcheck(jkhost, james, koonts, jk1, jk2)
  
  
  
