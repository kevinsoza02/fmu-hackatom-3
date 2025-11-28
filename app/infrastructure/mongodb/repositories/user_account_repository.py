from ..mongo import get_db

from bson.objectid import ObjectId

from app.domain.entities.user_account_entity import UserAccount

class UserAccountRepository:
    def __init__(self):
        self.db = get_db()
        self.collection = self.db['user_account']
        
    def find_account_by_user_id(self, user_id):
        query = {"user_id": ObjectId(user_id)}
        account_data = self.collection.find_one(query)
        if account_data:
            account_data['id'] = str(account_data['_id']) 
            del account_data['_id'] 
            account_data['user_id'] = str(account_data['user_id']) 
            return UserAccount(**account_data)
        return None
