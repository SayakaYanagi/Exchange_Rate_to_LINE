import requests
import os
import json
from dotenv import load_dotenv
from datetime import date

load_dotenv()

def get_api_key():

    """
    Get api key of ExchangeRate-API
    """

    try:
        api_key = os.environ['EXCHANGE_RATE_API_KEY']
        return api_key
    except KeyError:
        print('Error in getting API key.')

def get_rate():

    """
    Get JPY exchange rate of 1 GBP
    """
    api_key = get_api_key()
    req = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/GBP'

    try:
        response = requests.get(req)
        jpy = response.json()['conversion_rates']['JPY']
        return jpy
    except Exception as e:
        print(f'Error in getting exchange rate. {type(e)} : {e}')

def get_line_credentials():

    """
    Get credentials for Line Messaging API
    """
    try:
        channel_access_token = os.environ['LINE_CHANNEL_ACCESS_TOKEN']
        user_id = os.environ['USER_ID']
        return channel_access_token, user_id
    except KeyError:
        print('Error in getting Line Messaging API credentials.')

def send_message():

    """
    Send message to Line

    Input
    exchange_rate : value of JPY rate
    """

    # Get JPY exchange rate
    exchange_rate = get_rate()
    # Round off to two decimal places
    exchange_rate_round = round(exchange_rate, 2)
    # Get today's date
    today_date = date.today()
    # Get LINE API credentials
    channel_access_token, user_id = get_line_credentials()

    # Define HTTP request
    url = 'https://api.line.me/v2/bot/message/push'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {channel_access_token}',
    }

    data = {
        'to': user_id,
        'messages': [
            {
                'type': 'text',
                'text': f'[{today_date}] \n Exchange Rate \n 1GBP = ¥{exchange_rate_round}'
            },
        ],
        'notificationDisabled' : 'true',
    }

    response = requests.post(url,headers=headers, data=json.dumps(data))

    if response.status_code != 200:
        print('Error in sending messages to LINE')
    



