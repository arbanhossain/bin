# send me a message on whatsapp if my laptop reaches 85% while being charged

import psutil
import time
import requests

battery_percentage = 85
wait_time = 180

while True:
    battery = psutil.sensors_battery()
    if battery.power_plugged == True:
        if battery.percent >= battery_percentage:
            wait_time = 60
            # do your stuff
            r = requests.get('https://api.callmebot.com/whatsapp.php', params={'phone': 'phone number', 'text': 'unplug your charger', 'apikey': 123456})
            print('sent message to unplug battery')
    else:
        print('battery is unplugged')
    time.sleep(wait_time)
