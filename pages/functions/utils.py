import pandas as pd
import sqlite3 as sql
import os
import datetime as dt

today = dt.datetime.today().strftime('%m/%d/%Y')
def create_db():
    if os.path.exists(r'C:\Users\Jake\Documents\GitHub\Life_Analytics'):
        conn = sql.connect(r'C:\Users\Jake\Documents\GitHub\Life_Analytics\life.db', check_same_thread=False)
    else:
        conn = sql.connect('life.db', check_same_thread=False)
    return conn

def create_values(conn):
    cursor = conn.cursor()
    CREATE = """ CREATE TABLE IF NOT EXISTS LIFE_DATA (
        DATE VARCHAR(255) NOT NULL,
        ATTRIBUTE VARCHAR(255) NOT NULL,
        VALUE VARCHAR(25) NOT NULL
    )"""
    cursor.execute(CREATE)
    conn.commit()
    cursor.close()
    return None

def insert_values(conn, data):
    cursor = conn.cursor()
    INSERT_LIFE = """ INSERT INTO LIFE_DATA VALUES (?, ?, ?)"""
    cursor.executemany(INSERT_LIFE, data)
    conn.commit()
    cursor.close()
    return None

def select_today(conn):
    SELECT = f"SELECT * FROM LIFE_DATA WHERE DATE = '{today}'"
    df = pd.read_sql_query(SELECT, conn)
    return df

def drop_life(conn):
    cursor = conn.cursor()
    DROP = """ 
    DROP TABLE LIFE_DATA;
    """
    cursor.execute(DROP)
    conn.commit()
    cursor.close()
    return None