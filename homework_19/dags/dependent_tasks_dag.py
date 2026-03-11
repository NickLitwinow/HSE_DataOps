"""
DAG с зависимыми задачами.
Демонстрирует цепочку задач: extract → transform → validate → load.
"""

from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator


def _transform(**context):
    """Имитация трансформации данных."""
    print("Трансформация данных...")
    print("Применение бизнес-правил и очистка")
    return "transformed_data"


def _validate(**context):
    """Имитация валидации данных."""
    print("Валидация данных...")
    print("Проверка целостности и корректности")
    return True


with DAG(
    dag_id="dependent_tasks_dag",
    description="Пайплайн с зависимыми задачами (ETL)",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["homework"],
) as dag:

    extract = BashOperator(
        task_id="extract",
        bash_command='echo "Извлечение данных из источника..." && sleep 2',
    )

    transform = PythonOperator(
        task_id="transform",
        python_callable=_transform,
    )

    validate = PythonOperator(
        task_id="validate",
        python_callable=_validate,
    )

    load = BashOperator(
        task_id="load",
        bash_command='echo "Загрузка данных в хранилище..." && sleep 1',
    )

    # Зависимости: extract → transform → validate → load
    extract >> transform >> validate >> load
