from utils.base_variables import BaseVariables
from utils.sqlite_helper_functions import load_table_from_db

class EURUSDExtractor(BaseVariables):
    def __init__(self, freq):
        self.currency_config = self.config['currencies']['datasets']['eurusd']
        self.freq_config = self.currency_config['frequencies'][freq]
        self.db = self.currency_config['db_file']

    def get_raw_data(self):
        data = load_table_from_db(self.db, self.freq_config['raw_table'])

        a=1

if __name__=='__main__':
    EURUSDExtractor(freq='1d').get_raw_data()

