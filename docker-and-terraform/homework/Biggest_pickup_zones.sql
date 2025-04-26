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