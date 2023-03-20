'''

This is the main script of a primary package for this organisations ETL and data storage frameworks

'''
from src.etl_body.sqlite_create_actions import UpdateSqliteTables


def update_tables():
    UpdateSqliteTables().run_process()

def feature_engineering_model():


def run():
    #first we make sure we have all data up to date in the dbs
    update_tables()



if __name__ == '__main__':
    run()
