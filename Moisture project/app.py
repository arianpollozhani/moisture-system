from flask import Flask, render_template, request
import pymysql
import time
import subprocess

app = Flask(__name__)

# Database configuration
host = 'localhost'
user = 'admin'
password = 'pi'
database = 'data'

# Connect to the MariaDB database
conn = pymysql.connect(host=host, user=user, password=password, database=database)
cursor = conn.cursor()


# Function to read moisture level from the sensor
def read_moisture_level():
    moisture_level = subprocess.check_output("./a.out")
    return float(moisture_level)

@app.route('/')
def index():
    # Retrieve data from the table
    select_query = "SELECT * FROM plant_data"
    cursor.execute(select_query)
    rows = cursor.fetchall()

    # Read moisture level from the sensor
    moisture_level = read_moisture_level()

    # Render the template with the retrieved data and moisture level
    return render_template('index.html', rows=rows, moisture_level=moisture_level)

@app.route('/insert', methods=['POST'])
def insert():
    moisture_level = request.form['moisture_level']
    watering_count = request.form['watering_count']

    # Insert data into the table
    insert_query = "INSERT INTO plant_data (moisture_level, watering_count) VALUES (%s, %s)"
    cursor.execute(insert_query, (moisture_level, watering_count))
    conn.commit()

    return 'Data inserted successfully.'

if __name__ == '__main__':
    app.run(debug=True, port=5001)
