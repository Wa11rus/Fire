import cx_Oracle
def print_table(cur, request):
    names = []
    cur.execute(request)
    for name in cur.description:
        names.append(name[0])
    print(" ; ".join(names))
    for row in cur:
        print(row)
    print("\n\n")
username = 'QWERTY'
password = 'Qwerty'
database = 'localhost/xe'

conn = cx_Oracle.connect(username, password, database)
cursor = conn.cursor()


firstQuery = """select
    count(fire_id) as "count_of_fire",
    round(latitude, 1) || ' ' || round(longitude, 1) as "coordinate"
    from fire_params_locations
    WHERE
    round(fire_params_locations.latitude, 1) >= - 15.1 and round(fire_params_locations.latitude, 1) <= -14.5
    AND round(fire_params_locations.longitude, 1) >= 135.2 and round(fire_params_locations.longitude, 1) <= 140.1 group by round(latitude, 1) || ' ' || round(longitude, 1)
"""

secondQuery = """
SELECT
    round(fire_params_locations.brightness) as "rounded brightness",
    COUNT(fire_params_locations.params_id) AS "count of brightness"
FROM
    fire_params_locations
GROUP BY
    round(fire_params_locations.brightness)
"""

thirdQuery = """
 SELECT
    count(fire_id) as "count_of_fires",
    confidence
FROM
    fire_params_locations
   
    group by 
     confidence
    order by count(fire_id)
"""

print("---frist query---")
print_table(cursor, firstQuery)
print("---second query---")
print_table(cursor, secondQuery)
print("---thrid query---")
print_table(cursor, thirdQuery)

cursor.close()
