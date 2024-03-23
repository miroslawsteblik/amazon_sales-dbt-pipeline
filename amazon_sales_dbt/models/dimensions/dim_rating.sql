{{
    config(
        materialized='table'
    )
}}

SELECT
    user_id,
    product_id,
    rating,
    rating_count
FROM {{ ref('stg_sales_eph') }}  -- referencing name of the file from staging,