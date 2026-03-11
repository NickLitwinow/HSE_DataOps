"""
Пустой DAG без задач.
Демонстрирует минимальную структуру пайплайна Airflow.
"""

from datetime import datetime

from airflow import DAG

with DAG(
    dag_id="empty_dag",
    description="Пустой пайплайн без задач",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["homework"],
) as dag:
    pass
