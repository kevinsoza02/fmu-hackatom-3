from pymongo import MongoClient
import os

_mongo_client = None

def get_mongo_client():
    """
    Retorna a instância única do MongoClient.
    Se a instância não existir, ela será criada.
    """
    global _mongo_client
    
    if _mongo_client is None:
        MONGO_URI = os.getenv("MONGO_URI", "")
        
        try:
            _mongo_client = MongoClient(MONGO_URI)
            
            _mongo_client.admin.command('ping')
            print(">>> Mongo connection established.")
            
        except Exception as e:
            print(f">>> Error establishing connection to MongoDB: {e}")
            raise
            
    return _mongo_client

def get_db():
    """Retorna o objeto Database, usando o cliente Singleton."""
    client = get_mongo_client()
    DB_NAME = os.getenv("MONGO_DB_NAME", "")
    return client[DB_NAME]