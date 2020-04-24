--1 query
SELECT
    COUNT(fire_id) AS "count_of_fires"
FROM
    fire_info
    JOIN locations ON fire_info.location_id = locations.location_id
WHERE
    round(locations.latitude, 1) = - 15.1
    AND round(locations.longitude, 1) = 135.2;

--2 query

SELECT
    params.brightness,
    COUNT(params.params_id) AS "count of brightness"
FROM
    params
GROUP BY
    params.brightness;

--3 query 

SELECT
    fire_id,
    confidence.confidence
FROM
    fire_info
    INNER JOIN confidence ON fire_info.confidence = confidence.confidence;