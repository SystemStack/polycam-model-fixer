import configparser
config_parser = configparser.ConfigParser(
    interpolation=configparser.BasicInterpolation())
config_parser.read('config.ini')
config = dict()
config['RENDER_DIR'] = config_parser.get('DEFAULT', 'render_dir')
config['IMPORT_MODEL'] = config_parser.get('DEFAULT', 'import_model')
config['LOG_FILE'] = config_parser.get('DEFAULT', 'log_file')

with open(config['LOG_FILE'], 'w+') as file:
    file.write("")


def log(message):
    with open(config['LOG_FILE'], 'a+') as file:
        file.write(message + "\n")
