from dotenv import dotenv_values
from abc import ABC, abstractmethod
import pandas as pd
import pymysql
from config import CSV_PATH, SQL_QUERY

# Load the .env file
config = dotenv_values("src/.env")

class Dataloader(ABC):
    """
    Set Dataloader template using abstract base class
    """
    @abstractmethod
    def load_data(self):
        pass
    
class CSV_Loader(Dataloader):
    """
    CSV loader class that inherits from the Dataloader abstract base class
    """
    def __init__(self):
        self.path = CSV_PATH

    def load_data(self):
        df = pd.read_csv(self.path)
        return df
    
class SQL_Loader(Dataloader):
    """
    SQL loader class that inherits from the Dataloader abstract base class
    """
    def __init__(self):
        super().__init__()
        self.connection = self.initiate_remote_connection()
        self.query = SQL_QUERY

    def load_data(self):
        assert self.connection is not None, "Connection cannot be None"
        assert self.query is not None, "Query cannot be None"

        try:
            df = self.get_records(self.connection, self.query)
            return df
        except Exception as e:
            print(f'Error encountered: {e}')

    @staticmethod
    def initiate_remote_connection():
        try:
            connection = pymysql.connect(
                host=config.get('ENDPOINT'),
                port=int(config.get('PORT')),
                user=config.get('USERNAME'),
                passwd=config.get('PASSWORD'),
                db=config.get('DBNAME'),
                cursorclass=pymysql.cursors.DictCursor
            )
            print('[+] Remote Connection Successful')
            return connection
        except Exception as e:
            print(f'[+] Remote Connection Failed: {e}')

    @staticmethod
    def get_records(connection, sql_query):
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql_query)
                results = cursor.fetchall()
                df = pd.DataFrame(results)
                print('Successfully retrieved records')
                return df
        except Exception as e:
            print(f'Error encountered: {e}')
        

        
        
        
        
        

