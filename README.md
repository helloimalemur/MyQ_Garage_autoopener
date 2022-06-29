# MyQ_Garage_autoopener
Monitors for presence of specified IP address, such as a cell phone, and opens MyQ Garage upon device connection. Uses Cron to start and stop script within Screen session.



1. pip install aiohttp pymyq
2. place scripts in the same folder and replace "path to scripts" within checkhost.py and screen_checkhost.sh with this path
3. Add/edit variables and commands at bottom/top of checkhost.py (see example below)
4. add account info to close-garage.py and open-garage.py
5. add webhook url in discord-notif.sh for discord notifications
6. Cron starting and stopping using screen-checkhost.sh and screen-checkhost-stop.sh
  
  
  
  
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
  
  
  
