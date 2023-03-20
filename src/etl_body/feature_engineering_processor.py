from src.utils.helper_functions import read_csv_from_this_project
from src.utils.base_variables import BaseVariables

class ProcessorClass():
    def csv_to_sqlite(self):
        df = read_csv_from_this_project()
