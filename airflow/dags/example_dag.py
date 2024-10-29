from datetime import datetime
from airflow import DAG
from airflow.decorators import task

@task
def print_hello():
    print("Hello world!")


with DAG(
    dag_id="simple_dag",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    schedule=None,
    max_active_runs=1 # limit the number of active DAG runs (only for this DAG)
) as dag:
    print_hello()