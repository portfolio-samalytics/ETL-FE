import pandas as pd
import yaml
from pathlib import Path

class BaseVariables:
    def __init__(self):
        self.config = self.load_config_file()

    def load_config_file(self):
        for P in Path(__file__).parent.parent.rglob('*'):
            if str(P).endswith('config.yaml'):
                return yaml.safe_load(open(str(P)))

if __name__ == '__main__':
    BaseVariables().load_config_file()
