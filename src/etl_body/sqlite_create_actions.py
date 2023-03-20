from utils.base_variables import BaseVariables
from utils.helper_functions import get_all_db_files, find_file_in_project, read_csv_from_this_project
from utils.sqlite_helper_functions import all_tables_in_db_file, create_new_table_in_db
from utils.logging import Logger
import pandas as pd

class UpdateSqliteTables(BaseVariables):
    logger = Logger('CreateNewTableWithNewData').logger

    def run_process(self):
        self.update_db_tables()

    def update_db_tables(self):
        db_files = get_all_db_files()
        for dataset in self.config:
            for market in self.config[dataset]['datasets']:
                db_file = self.config[dataset]['datasets'][market]['db_file']
                all_tables = all_tables_in_db_file(db_file)
                for freq in self.config[dataset]['datasets'][market]['frequencies']:
                    table = self.config[dataset]['datasets'][market]['frequencies'][freq]['raw_table']
                    if table not in all_tables:
                        self.logger.info(f'Creating new table in {db_file} for {market}-{freq}')
                        data_file = self.config[dataset]['datasets'][market]['frequencies'][freq]['csv_extract_file']
                        if find_file_in_project(data_file) != None:
                            data = read_csv_from_this_project(data_file)
                            create_new_table_in_db(data=data, db=db_file, table=table)
                        else:
                            self.logger.info(f'{data_file} not in project so cannot create new table')
                    else:
                        self.logger.info(f'{table} is already in {db_file} tables: {str(all_tables)[1:-1]}')
        self.logger.info('all dbs and tables are up to date')



if __name__ == '__main__':
    UpdateSqliteTables()


