import psycopg2
import os
from flask import Flask

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ['DB_HOST'],
        database=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD']
    )
    return conn

@app.route('/')
def index():
    try:
        conn = get_db_connection()
        return "Con to DB container!"
    except:
        return "Error con to DB"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)