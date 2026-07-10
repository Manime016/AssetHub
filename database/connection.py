import mysql.connector
from config import Config

def get_db_connection():
    try:
        # 1. Connect to the database
        connection = mysql.connector.connect(            
            host=Config.MYSQL_HOST,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            database=Config.MYSQL_DB
        )
        
        # 2. Check connection inside the try block before returning
        if connection.is_connected():
            print("✅ Successfully connected to MySQL database.")
            return connection
        else:
            print("❌ Connection object created, but is_connected() returned False.")
            return None
            
    except Exception as e:
        print(f"❌ Error connecting to MySQL: {e}")
        return None

