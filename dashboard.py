
import cx_Oracle
import chart_studio.plotly as py
import plotly.graph_objs as go
import re
import chart_studio.dashboard_objs as dashboard

username = 'crispyyv'
password = '19680401'
database = 'localhost/xe'


def fileId_from_url(url):
    """Return fileId from a url."""
    raw_fileId = re.findall("~[A-z.]+/[0-9]+", url)[0][1:]
    return raw_fileId.replace('/', ':')


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

cursor.execute(firstQuery)

fire = ["fire_info"]
fire_count = []

for row in cursor:
    print(row)
    fire_count += [row[0]]

data = [go.Bar(
    x=fire,
    y=fire_count
)]

layout = go.Layout(
    title='Загальна кількість пожарів, за заданими координатами',
    xaxis=dict(
        title='Fire info',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='Count of fires',
        rangemode='nonnegative',
        autorange=True,
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
)

fig = go.Figure(data=data, layout=layout)

fires_count = py.plot(fig, filename='fires-count')

cursor.execute(secondQuery)

brightness = []
count_of_brightness = []

for row in cursor:
    brightness += [row[0]]
    count_of_brightness += [row[1]]

pie = go.Pie(labels=brightness, values=count_of_brightness)
fire_brightness = py.plot([pie], filename ='fire-brightness')

cursor.execute(thirdQuery)

fire_id = []
cofidence = []

for row in cursor:
    fire_id += [row[0]]
    cofidence += [row[1]]


car_prices = go.Scatter(
    x=cofidence,
    y=fire_id,
    mode='lines+markers'
)

data = [car_prices]
fire_confidence = py.plot(data, filename='fire-confidence')

my_dboard = dashboard.Dashboard()

fires_count = fileId_from_url(fires_count)
fire_brightness = fileId_from_url(fire_brightness)
fire_confidence = fileId_from_url(fire_confidence)

box_1 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': fires_count,
    'title': 'Кількість в заданих координатах'
}

box_2 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': fire_brightness,
    'title': 'Яркость та пожар'
}

box_3 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': fire_confidence,
    'title': 'Пожар та впевненість'
}

my_dboard.insert(box_1)
my_dboard.insert(box_2, 'below', 1)
my_dboard.insert(box_3, 'left', 2)

py.dashboard_ops.upload(my_dboard, 'My First Dashboard with Python')