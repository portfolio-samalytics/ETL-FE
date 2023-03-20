import sqlite3
import os
from pathlib import Path
from sqlite3 import Error
import pandas as pd

def full_db_string(db_name):
    full_name = os.path.join(
        os.path.join(str(Path(__file__)).split('src')[0], 'src', 'data-storage', f'{db_name}'))
    return full_name

def all_tables_in_db_file(db_file):
    db_file = full_db_string(db_file)
    conn = sqlite3.connect(db_file)
    query = """SELECT name FROM sqlite_master WHERE type='table'"""
    cursor = conn.cursor()
    cursor.execute(query)
    all_tables = cursor.fetchall()
    all_tables = [table[0] for table in all_tables]
    return all_tables

def create_new_table_in_db(data, db, table):
    conn = connect_to_db(db)
    data.to_sql(name=table, con=conn)

def connect_to_db(db_name, conn=None):
    db_name = full_db_string(db_name)
    try:
        conn = sqlite3.connect(db_name)
    except Error as E:
        raise E

    return conn

def load_table_from_db(db, table):
    query = """  SELECT * FROM {table} """.format(table=table)
    conn = connect_to_db(db)
    table_data = pd.read_sql_query(query, con=conn)
    a=1

if __name__ == '__main__':
    all_tables_in_db_file(db_file='currency_data.db')
