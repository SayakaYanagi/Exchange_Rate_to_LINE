from Exchange_Rate_to_LINE import utils
from airflow import DAG
from airflow.operators.python import PythonOperator
import datetime

default_args = utils.get_default_args

dag = DAG(
    dag_id="exchange-rate-to-line",    
    schedule="0 18 * * *",
    start_date=datetime.datetime(2023, 7, 15),
    default_args=default_args,
)


task = PythonOperator(
        task_id=f'send-message-to-LINE',
        python_callable= utils.send_message,
        dag=dag,
    )