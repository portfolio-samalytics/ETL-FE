import pandas as pd
import os
from pathlib import Path
import sqlite3
from sqlite3 import Error


def read_csv_from_this_project(filename):
    for p in Path(__file__).parent.parent.parent.rglob('*'):
        if str(p).endswith(filename):
            break
    return pd.read_csv(p)


def build_new_sqlite_file(db_filename):
    conn = None
    try:
        conn = sqlite3.connect(db_filename)
    except Error as E:
        raise E



if __name__ == '__main__':
    name = 'first_pass'
    build_new_sqlite_file(os.path.join(os.path.join(str(Path(__file__)).split('src')[0], 'src', 'data-storage', f'{name}.db')))
