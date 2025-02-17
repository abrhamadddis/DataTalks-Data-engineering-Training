-- Creating external table referring to gcs path
CREATE OR REPLACE EXTERNAL TABLE `arctic-diode-446315-r1.nytaxi.external_yellow_tripdata`
OPTIONS (
  format = 'parquet',
  uris = ['gs://dezoomcamp_addis_hw3_2025/yellow_tripdata_2024-*.parquet']
);


CREATE OR REPLACE TABLE `arctic-diode-446315-r1.nytaxi.external_yellow_tripdata_2020` AS
SELECT * FROM `arctic-diode-446315-r1.nytaxi.external_yellow_tripdata`;

SELECT COUNT(DISTINCT PULocationID) AS pulocation_count
FROM `arctic-diode-446315-r1.nytaxi.external_yellow_tripdata`;

SELECT COUNT(DISTINCT PULocationID) AS pulocation_count
FROM `arctic-diode-446315-r1.nytaxi.external_yellow_tripdata_2020`;

SELECT PULocationID
FROM `arctic-diode-446315-r1.nytaxi.external_yellow_tripdata_2020`;

SELECT PULocationID
FROM `arctic-diode-446315-r1.nytaxi.external_yellow_tripdata_2020`;


SELECT PULocationID, DOLocationID
FROM `arctic-diode-446315-r1.nytaxi.external_yellow_tripdata_2020`;

SELECT COUNT(fare_amount) AS fare_amount_zero
FROM `arctic-diode-446315-r1.nytaxi.external_yellow_tripdata_2020`
WHERE fare_amount = 0;

-- Create a partitioned table from external table
CREATE OR REPLACE TABLE `arctic-diode-446315-r1.nytaxi.yellow_tripdata_partitioned`
PARTITION BY
  DATE(tpep_pickup_datetime) AS
SELECT * FROM `arctic-diode-446315-r1.nytaxi.external_yellow_tripdata_2020`;

SELECT DISTINCT VendorID
FROM `arctic-diode-446315-r1.nytaxi.external_yellow_tripdata_2020`
WHERE tpep_dropoff_datetime BETWEEN '2024-03-01 00:00:00' AND '2024-03-15 23:59:59';

SELECT DISTINCT VendorID
FROM `arctic-diode-446315-r1.nytaxi.yellow_tripdata_partitioned`
WHERE tpep_dropoff_datetime BETWEEN '2024-03-01 00:00:00' AND '2024-03-15 23:59:59';