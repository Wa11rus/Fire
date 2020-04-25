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
    COUNT(fire_id) AS "count_of_fires"
FROM
    fire_info
    JOIN locations ON fire_info.location_id = locations.location_id
WHERE
    round(locations.latitude, 1) = - 15.1
    AND round(locations.longitude, 1) = 135.2

"""

secondQuery = """
  SELECT
    params.brightness,
    COUNT(params.params_id) AS "count of brightness"
FROM
    params
GROUP BY
    params.brightness
"""

thirdQuery = """
  SELECT
    fire_id,
    confidence.confidence
FROM
    fire_info
    INNER JOIN confidence ON fire_info.confidence = confidence.confidence
"""

print("---frist query---")
print_table(cursor, firstQuery)
print("---second query---")
print_table(cursor, secondQuery)
print("---thrid query---")
print_table(cursor, thirdQuery)

cursor.close()