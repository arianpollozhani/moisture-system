from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

# Database configuration
host = 'localhost'
user = 'root'
password = 'pi'
database = 'data'

# Connect to the MariaDB database
conn = pymysql.connect(host=host, user=user, password=password, database=database)
cursor = conn.cursor()

@app.route('/')
def index():
    # Retrieve data from the table
    select_query = "SELECT * FROM plant_data"
    cursor.execute(select_query)
    rows = cursor.fetchall()

    # Render the template with the retrieved data
    return render_template('index.html', rows=rows)

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
    app.run(debug=True)
