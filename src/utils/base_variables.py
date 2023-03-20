from utils.helper_functions import load_config_file

class BaseVariables:
    config = load_config_file()



if __name__ == '__main__':
    BaseVariables().load_config_file()
