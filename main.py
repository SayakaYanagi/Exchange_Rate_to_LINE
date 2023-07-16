from Exchange_Rate import utils
from airflow import DAG
from airflow.operators.python import PythonOperator
import datetime

default_args = {
'owner': 'admin',
'email':"sayaka.yanagi@scskeu.com"
}


dag = DAG(
    dag_id="exchange-rate-to-line",    
    schedule="0 18 * * *",
    start_date=datetime.datetime(2023, 7, 15),
    default_args=default_args,
)


task = PythonOperator(
        task_id=f'exchange_rate_to_line',
        python_callable= utils.send_message,
        dag=dag,
    )