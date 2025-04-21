from files import password
# config.py
def load_config():
    return {
        'dbname': 'postgres',
        'user': 'postgres',
        'password': password,
        'host': 'localhost',
        'port': '5433'
    }
