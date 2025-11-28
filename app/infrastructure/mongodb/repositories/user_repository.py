from ..mongo import get_db

from app.domain.entities.user_entity import User

class UserRepository:
    def __init__(self):
        self.db = get_db()
        self.collection = self.db['user']
        
    def find_user_by_email(self, email):
        query = {"email": email}
        user_data = self.collection.find_one(query)
        if user_data:
            user_data['id'] = str(user_data['_id']) 
            del user_data['_id'] 
            return User(**user_data)
        return None
