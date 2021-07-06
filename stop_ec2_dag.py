from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils import timezone
from datetime import datetime, timedelta
import pendulum

local_tz = pendulum.timezone("Europe/Madrid")

default_args = {
        'owner': 'airflow',
        'start_date': datetime(year=2021, month=6, day=29, tzinfo=local_tz),
        'retries': 5,
        'retry_delay': timedelta(minutes=5),
        }

dag = DAG(
        'stop_ec2',
        default_args=default_args,
        schedule_interval='22 7 * * *',
        )

create_command = 'python ~/scripts/start_stop_ec2.py stop [InstanceId] '

t1 = BashOperator(
        task_id='stop_instance',
        bash_command=create_command,
        dag=dag,
        )



