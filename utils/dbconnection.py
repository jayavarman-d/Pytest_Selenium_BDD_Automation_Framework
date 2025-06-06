import pyodbc
import configparser


class DatabaseCon:

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('C:/Py/Selenium/Capstone_Ecommerce_Updated/dbconfig.ini')
        db = config['database']
        driver = db['DRIVER']
        server = db['Server']
        database = db['Database']
        connection = db['Trusted_Connection']
        # self.server = config.get('Database_Config', 'Server')
        # self.database = config.get('Database_Config', 'Database')
        # self.connection = config.get('Database_Config', 'Trusted_Connection')
        self.conn = pyodbc.connect(
            f"DRIVER={{{driver}}};"
            f"Server={server};"
            f"Database={database};"
            f"Trusted_Connection={connection};"
        )
        self.cursor = self.conn.cursor()
