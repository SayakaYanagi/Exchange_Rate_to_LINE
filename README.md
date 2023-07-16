# Exchange_Rate

An automated process to send the daily exchange rate of JPY (Japanese Yen) and GBP (Great Britain Pound) to LINE, a widely used messaging app in Japan, scheduled for 6 PM every day.

![Exchange Rate](https://github.com/SayakaYanagi/Exchange_Rate/assets/72021349/d54cb2df-2902-4fce-8adc-35a518a6fcd4)


## Installation

0. Set up [Airflow](https://airflow.apache.org/docs/apache-airflow/stable/index.html)

1. Clone this repository in dags folder set in airflow.cfg

2. Get Credentials of LINE Messaging API and exchangerates API
   
   1. Create an account in LINE, and set up a Messaging API channel on [LINE Developer](https://developers.line.biz/console)

   1. Get API key on [exchangerates](https://exchangeratesapi.io/)

3. Fill in the credentials in .env file
   - LINE_CHANNEL_ACCESS_TOKEN : Channel access token of your LINE messaging channel
   - USER_ID : User ID of your LINE messaging channel
   - EXCHANGE_RATE_API_KEY : API key of your exchangerates account
   
