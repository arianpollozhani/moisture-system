from flask import Flask, render_template
import sqlite3
app = Flask(__name__)
@app.route('/')
def index():
    # Connect to the SQLite database
    conn = sqlite3.connect('plants.db')
    cursor = conn.cursor()

    # Retrieve data from the table
    cursor.execute("SELECT * FROM plant_data")
    rows = cursor.fetchall()

    # Render the template with the retrieved data
    return render_template('index.html', rows=rows)
if __name__ == '__main__':
    app.run(debug=True)
