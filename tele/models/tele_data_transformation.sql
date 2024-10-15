{{config(materialized='table')}}


WITH filtered_data AS {
    SELECT * 
    FROM {{source('public', 'tele_data')}}
}
SELECT
    Channel_Title,
    Channel_Username,
    ID,
    UPPER(Message) AS transformed_message,
    Date,
    Media_path
FROM filtered_data