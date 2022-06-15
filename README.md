# MyQ_Garage_autoopener
monitors for presence of specified IP address, such as a cell phone,and opens MyQ Garage upon device connection.
uses Cron to start and stop script within Screen session




1. place scripts in the same folder and replace "<path to scripts>" within checkhost.py and screen_checkhost.sh with this path
2. add account info to close-garage.py and open-garage.py
3. add webhook url in discord-notif.sh for discord notifications
4. Cron starting and stopping using screen-checkhost.sh and screen-checkhost-stop.sh
  
example cron;
0 1 * * * /<path to scripts>/screen-checkhost-stop.sh
0 6 * * * /<path to scripts>/screen-checkhost.sh
