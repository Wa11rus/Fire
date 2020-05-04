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


firstQuery = """
  SELECT
  count(fire_id) as "count_of_fire",
    round(latitude, 1) || ' ' || round(longitude, 1) as "coordinate"
FROM
    fire_info
    JOIN locations ON fire_info.location_id = locations.location_id
 WHERE
    round(latitude, 1) >= - 15.1 and round(latitude, 1) <= -14.5
    AND round(longitude, 1) >= 135.2 and round(longitude, 1) <= 140.1 group by round(latitude, 1) || ' ' || round(longitude, 1)
"""

secondQuery = """
  SELECT
   round(params.brightness) as "rounded brightness",
    COUNT(params.params_id) AS "count of brightness"
FROM
    params
GROUP BY
   round(params.brightness)
"""

thirdQuery = """
  SELECT
   count(fire_info.fire_id) as "count_of_fires",
   confidence.confidence
FROM
    fire_info
    INNER JOIN confidence ON fire_info.confidence = confidence.confidence
     group by 
     confidence.confidence
    order by count(fire_id)
"""

print("---frist query---")
print_table(cursor, firstQuery)
print("---second query---")
print_table(cursor, secondQuery)
print("---thrid query---")
print_table(cursor, thirdQuery)

cursor.close()
