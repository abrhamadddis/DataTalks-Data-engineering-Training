SELECT 
    COUNT(CASE WHEN trip_distance <= 1 THEN 1 END) AS up_to_1_mile,
    COUNT(CASE WHEN trip_distance > 1 AND trip_distance <= 3 THEN 1 END) AS between_1_and_3_miles,
    COUNT(CASE WHEN trip_distance > 3 AND trip_distance <= 7 THEN 1 END) AS between_3_and_7_miles,
    COUNT(CASE WHEN trip_distance > 7 AND trip_distance <= 10 THEN 1 END) AS between_7_and_10_miles,
    COUNT(CASE WHEN trip_distance > 10 THEN 1 END) AS over_10_miles
FROM public.ny_taxi_green_data
WHERE lpep_pickup_datetime >= '2019-10-01' 
  AND lpep_pickup_datetime < '2019-11-01';


SELECT 
    DATE(lpep_pickup_datetime) AS pickup_day, 
    MAX(trip_distance) AS longest_trip_distance
FROM public.ny_taxi_green_data
GROUP BY pickup_day
ORDER BY longest_trip_distance DESC
LIMIT 1;


SELECT 
    z.Zone AS pickup_zone, 
    SUM(t.total_amount) AS total_amount_sum
FROM 
    ny_taxi_green_data t
JOIN 
    zone z ON t.PULocationID = z.locationID
WHERE 
    DATE(t.lpep_pickup_datetime) = '2019-10-18'
GROUP BY 
    z.Zone
HAVING 
    SUM(t.total_amount) > 13000
ORDER BY 
    total_amount_sum DESC;

SELECT 
    z_drop.Zone AS dropoff_zone, 
    MAX(t.tip_amount) AS largest_tip
FROM 
    ny_taxi_green_data t
JOIN 
    zone z_pick ON t.pulocationID = z_pick.LocationID
JOIN 
    zone z_drop ON t.dolocationid = z_drop.locationid
WHERE 
    z_pick.Zone = 'East Harlem North' 
    AND DATE(t.lpep_pickup_datetime) BETWEEN '2019-10-01' AND '2019-10-31'
GROUP BY 
    z_drop.Zone
ORDER BY 
    largest_tip DESC
LIMIT 1;