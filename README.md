# Exchange_Rate_to_LINE

## List of Content
1. [Project](#project)  
1. [Installation](#installation)


## Project

An automated process to send the daily exchange rate of JPY (Japanese Yen) and GBP (Great Britain Pound) to LINE, a widely used messaging app in Japan, scheduled for 6 PM every day.   

The currency exchange rate is obtained by sending an HTTP request to ExchangeRate-API.
The process is automated and monitored by Airflow. If any errors occur, an email alert is sent.


![Exchange Rate](https://github.com/SayakaYanagi/Exchange_Rate_to_LINE/assets/72021349/b8b6ab43-d01f-4e25-8688-5bdfe38138ee)



## Installation

0. Set up [Airflow](https://airflow.apache.org/docs/apache-airflow/stable/index.html)


1. Clone this repository in your airflow dags folder.

2. Get Credentials for LINE Messaging API and Exchange Rates API
   
   1. Create an account in LINE, and set up a Messaging API channel on [LINE Developer](https://developers.line.biz/console)

   1. Get API key on [ExchangeRate-API](https://www.exchangerate-api.com/)

3. Fill in the credentials in `.env `
   - LINE_CHANNEL_ACCESS_TOKEN : Channel access token of your LINE messaging channel
   - USER_ID : User ID of your LINE messaging channel
   - EXCHANGE_RATE_API_KEY : API key of your Exchange Rates account
   - OWNER : Your Airflow user name

4. Use `pip install -r requirements.txt` to install modules.
