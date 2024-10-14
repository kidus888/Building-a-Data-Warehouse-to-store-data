{{config(materialized='table')}}


WITH filtered_data AS {
    SELECT * 
    FROM {{source('public', 'tele_data')}}
}
SELECT
    channel_title,
    channel_username,
    id,
    UPPER(message) AS transformed_message,
    date,
    media_path
FROM filtered_data;