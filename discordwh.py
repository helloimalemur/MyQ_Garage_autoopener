import json
import requests


def discord_notif(message):
    url = ""
    payload = {'username':'Garage', 'content':message}
    headers = {"Content-Type": "application/json; charset=utf-8"}
    r = requests.post(url, data=json.dumps(payload), headers=headers)

#discord_notif("this is a test")