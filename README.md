# MyQ_Garage_autoopener
Monitors for presence of specified IP address, such as a cell phone, and opens MyQ Garage upon device connection. Uses Cron to start and stop script within Screen session.



1. pip install aiohttp pymyq requests asyncio
2. Add/edit variables and commands at bottom/top of main.py (see example below)
3. add account info to garagecontrol.py
  
  
  
  
**example cron**;
{0 1 * * * /<path to scripts>/screen-checkhost-stop.sh}
{0 6 * * * /<path to scripts>/screen-checkhost.sh}

**screen-checkhost.sh**
#!/bin/bash  
screen -XS checkhost quit
screen -dmS checkhost bash -c "python3 /home/foxx/.scripts/MyQ_Garage_autoopener/main.py"
