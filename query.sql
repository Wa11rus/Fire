--1 query
select
    count(fire_id) as "count_of_fire",
    round(latitude, 1) || ' ' || round(longitude, 1) as "coordinate"
    from fire_params_locations
    WHERE
    round(fire_params_locations.latitude, 1) >= - 15.1 and round(fire_params_locations.latitude, 1) <= -14.5
    AND round(fire_params_locations.longitude, 1) >= 135.2 and round(fire_params_locations.longitude, 1) <= 140.1 group by round(latitude, 1) || ' ' || round(longitude, 1);


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
