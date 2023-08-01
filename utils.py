import requests
import os
import json
from dotenv import load_dotenv
from datetime import date
import logging

# Logging setting
logger = logging.getLogger()
logger.setLevel(20)
fhandler = logging.FileHandler(filename=r'Exchange_Rate_to_LINE/main.log')
formatter = logging.Formatter('%(asctime)s - %(message)s')

load_dotenv()

def get_api_key():

    """
    Get api key of ExchangeRate-API
    """

    try:
        logging.info('Getting exchange rate API key...')
        api_key = os.environ['EXCHANGE_RATE_API_KEY']
        return api_key
    except KeyError:
        logging.error('Key Error in get_api_key(). Check the environmental variable EXCHANGE_RATE_API_KEY.')
        raise
    except Exception as e:
        logging.error(f'Error in get_api_key(). {type(e)} : {e}')
        raise

def get_rate():

    """
    Get JPY exchange rate of 1 GBP
    """
    api_key = get_api_key()
    req = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/GBP'

    try:
        logging.info('Sending HTTP request to exchange rate API...')
        response = requests.get(req, timeout = 10)
        jpy = response.json()['conversion_rates']['JPY']
        return jpy
    except Exception as e:
        logging.error(f'Error in get_rate(). {type(e)} : {e}')
        raise

def get_line_credentials():

    """
    Get credentials for Line Messaging API
    """
    try:
        logging.info('Getting LINE API credentials...')
        channel_access_token = os.environ['LINE_CHANNEL_ACCESS_TOKEN']
        user_id = os.environ['USER_ID']
        return channel_access_token, user_id
    except KeyError:
        logging.error('Error in get_line_credentials(). Check Line Messaging API credentials.')
        raise
    except Exception as e:
        logging.error(f'Error in get_line_credentials(). {type(e) : {e}}')
        raise

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

    logging.info('Sending message to LINE...')
    response = requests.post(url,headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        logging.info('Message sent to LINE successfully')
    else :
        logging.error(f'Error in send_message() : [{response.status_code}] {response.text}')
        raise

    
    



