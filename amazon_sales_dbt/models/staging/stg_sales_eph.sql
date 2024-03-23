{{
    config(
        materialized='ephemeral'
    )
}}

SELECT 
    *
FROM {{ source('staging', 'sales') }}

-- loading into memory