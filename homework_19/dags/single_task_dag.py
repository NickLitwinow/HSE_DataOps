"""
DAG с одной задачей.
Демонстрирует использование BashOperator.
"""

from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="single_task_dag",
    description="Пайплайн с одной задачей",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["homework"],
) as dag:

    hello_task = BashOperator(
        task_id="say_hello",
        bash_command='echo "Hello from Airflow! Current date: $(date)"',
    )
