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
    round(fire_params_locations.brightness) as "rounded brightness",
    COUNT(fire_params_locations.params_id) AS "count of brightness"
FROM
    fire_params_locations
GROUP BY
    round(fire_params_locations.brightness);

--3 query 

SELECT
    count(fire_id) as "count_of_fires",
    confidence
FROM
    fire_params_locations
   
    group by 
     confidence
    order by count(fire_id);
