from dotenv import load_dotenv
import os
import json
import requests
from datetime import datetime , timezone,timedelta

def get_messages ():
    load_dotenv()
    TOKEN = os.environ['TELEGRAM_TOKEN'] 

    base_url = f'https://api.telegram.org/bot{TOKEN}'
    messages = requests.get(url=f'{base_url}/getUpdates').json()['result']
    print(messages)

    tzinfo = timezone (offset=timedelta (hours=-3))
    date = datetime .now(tzinfo).strftime ('%Y-%m-%d' )
    timestamp = datetime .now(tzinfo).strftime ('%Y%m%d%H%M%S%f' )
    filename = f'{timestamp }.json'
    # print(filename)

    with open(f"./raw_data/{ filename }", mode='w', encoding ='utf8') as fp:

        json.dump(messages , fp)

