
CONNECTION_ID = "postgres_connection"
DB_NAME = "Amazon-DWH"
SCHEMA_NAME = "analytics"

ROOT_PATH = '/opt/airflow/dags/dbt'
DBT_PROJECT_PATH = f"{ROOT_PATH}/amazon_sales_dbt"

profile_config = ProfileConfig(
    profile_name="amazon_sales_dbt",
    target_name="analitics",
    profile_mapping=RedshiftUserPasswordProfileMapping(
        conn_id=CONNECTION_ID,
        profile_args={"schema": SCHEMA_NAME},
    )
)


@dag(
    start_date=datetime(2023, 10, 14),
    schedule=None,
    catchup=False
)
def dag_dbt_sales_dw_cosmos():

    start_process = DummyOperator(task_id='start_process')

    transform_data = DbtTaskGroup(
        group_id="transform_data",
        project_config=ProjectConfig(DBT_PROJECT_PATH),
        profile_config=profile_config,
        default_args={"retries": 2},
    )

    start_process >> transform_data


dag_dbt_sales_dw_cosmos()
CONNECTION_ID = "redshift_default"
DB_NAME = "amazon_sales"
SCHEMA_NAME = "public"

ROOT_PATH = '/opt/airflow/dags/dbt'
DBT_PROJECT_PATH = f"{ROOT_PATH}/sales_dw"

profile_config = ProfileConfig(
    profile_name="sales_dw",
    target_name="dev",
    profile_mapping=RedshiftUserPasswordProfileMapping(
        conn_id=CONNECTION_ID,
        profile_args={"schema": SCHEMA_NAME},
    )
)


@dag(
    start_date=datetime(2023, 10, 14),
    schedule=None,
    catchup=False
)
def dag_dbt_sales_dw_cosmos():

    start_process = DummyOperator(task_id='start_process')

    transform_data = DbtTaskGroup(
        group_id="transform_data",
        project_config=ProjectConfig(DBT_PROJECT_PATH),
        profile_config=profile_config,
        default_args={"retries": 2},
    )

    start_process >> transform_data


dag_dbt_sales_dw_cosmos()