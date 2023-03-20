import pandas as pd
import os
from pathlib import Path
import yaml


def find_file_in_project(filename, result=None):
    for p in Path(__file__).parent.parent.parent.rglob('*'):
        if str(p).endswith(filename):
            result = str(p)
            break
    return result

def get_all_db_files():
    db_files = []
    for p in Path(__file__).parent.parent.parent.rglob('*'):
        if str(p).endswith('.db'):
            db_files.append(str(p))
    return db_files

def load_config_file():
    file = find_file_in_project('config.yaml')
    return yaml.safe_load(open(str(file)))

def read_csv_from_this_project(filename):
    file_path = find_file_in_project(filename)
    return pd.read_csv(file_path)

def read_xlsx_from_this_project(filename):
    file_path = find_file_in_project(filename)
    return pd.read_excel(file_path)



