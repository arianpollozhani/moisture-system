from flask import Flask, render_template
import pymysql

app = Flask(__name__)

# Database configuration
host = 'localhost'
user = 'your_username'
password = 'your_password'
database = 'your_database_name'

@app.route('/')
def index():
    # Connect to the MariaDB database
    conn = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = conn.cursor()

    # Retrieve data from the table
    cursor.execute("SELECT * FROM plant_data")
    rows = cursor.fetchall()

    # Render the template with the retrieved data
    return render_template('index.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)
