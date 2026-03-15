import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        port=os.getenv("DB_PORT")
    )


def create_table():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            id SERIAL PRIMARY KEY,
            city VARCHAR(100),
            temperature FLOAT,
            humidity INT,
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    conn.commit()
    cur.close()
    conn.close()


def save_weather(data):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO weather (city, temperature, humidity, description)
        VALUES (%s, %s, %s, %s)
    """, (
        data["city"],
        data["temperature"],
        data["humidity"],
        data["description"]
    ))

    conn.commit()
    cur.close()
    conn.close()

def get_weather_history():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
                SELECT city, temperature, humidity, description, created_at
                FROM weather
                ORDER BY created_at DESC
                """)

    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows