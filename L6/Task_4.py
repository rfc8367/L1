import json
from datetime import timedelta

def open_file():
    with open('acdc.json', 'r+') as file:
        data = json.load(file)

        new_duration = data['album']['tracks']['track']
        total_duration = 0
    for i in new_duration:
        total_duration += int(i['duration'])
        
    print(timedelta(seconds=total_duration))

open_file()