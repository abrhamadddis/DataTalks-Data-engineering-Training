SELECT 
    DATE(lpep_pickup_datetime) AS pickup_day, 
    MAX(trip_distance) AS longest_trip_distance
FROM public.ny_taxi_green_data
GROUP BY pickup_day
ORDER BY longest_trip_distance DESC
LIMIT 1;