# Excahnge_Rate

An automated process to send the daily exchange rate of JPY (Japanese Yen) and GBP (Great Britain Pound) to LINE, a widely used messaging app in Japan, scheduled for 6 PM every day.

## Installation

1. Get Credentials of LINE Messaging API and exchangerates API
   Create an account in LINE, and set up a Messaging API channel on LINE Developer
   [LINE Divelopers Console website](https://developers.line.biz/console)

   Get API key on exchangerates
   [exchangerates website](https://exchangeratesapi.io/)

2. Fill in the credentials in .env file
   - LINE_CHANNEL_ACCESS_TOKEN : Channel access token of your LINE messaging channel
   - USER_ID : User ID of your LINE messaging channel
   - EXCHANGE_RATE_API_KEY : API key of your exchangerates account
   
