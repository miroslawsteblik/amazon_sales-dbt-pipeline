# Amazon Sales - DBT - Airflow - Cosmos

The data used relates to sales on the Amazon website, which can be found on [Kaggle](https://www.kaggle.com/datasets/karkavelrajaj/amazon-sales-dataset).

> Install DBT

`python -m pip install dbt-postgres`

`dbt init`

> Connection setup 

Use: `profiles.yml` located: `~/.dbt/profiles.yml` and test connection: `dbt debug`

> Models setup

![Alt text](https://github.com/miroslaw-steblik/amazon-sales-dbt-airflow/blob/main/extras/amazon_data_flow.png)

Sales table has been pre-loaded using python script and serves as data source in the staging schema

>> Staging

Add `staging.yml` and `stg_sales_eph.sql` to load memory

>> Facts

- fact_product_rating: This table contains data for extracting product rating metrics by users, e.g., the top-rated products.

- fact_sales_category: This table contains data for extracting sales metrics by product categories, e.g., the top categories with the most profit for the store.

>> Dimensions

- dim_product: This table contains data about the store's products.

- dim_user: It contains data about users who are customers of the store.

- dim_rating: It contains all the product ratings given by customers of the store.

> Airflow

Apache Airflow is a platform for programmatically authoring, scheduling, and monitoring workflows. It is especially useful for creating and orchestrating complex data pipelines.

![Alt text](https://github.com/miroslaw-steblik/amazon-sales-dbt-airflow/blob/main/extras/cosmos.png)

Instalation: `curl -sSL install.astronomer.io | sudo bash -s`

`mkdir <airflow>` -> `cd airflow` -> `astro dev init` -> `astro dev start`

To restart: `astro dev restart`

After your project builds successfully, open the Airflow UI in web browser at https://localhost:8080/ or change port on `/.astro/config.yaml`

Default user: admin , password: admin

On `/.astro/config.yaml` also change port for postgres to 5435 if another postgres instance is running

Configure an Airflow connection to postgres local database

>> DAG

1. DAG: Directed Acyclic Graph. An Airflow DAG is a workflow defined as a graph, where all dependencies between nodes are directed and nodes do not self-reference. For more information on Airflow DAGs, see Introduction to Airflow DAGs.

2. DAG run: The execution of a DAG at a specific point in time. A DAG run can be scheduled or manually triggered.

3. Task: A step in a DAG describing a single unit of work.

4. Task instance: The execution of a task at a specific point in time.