from ..mongo import get_db

from app.domain.entities.user_entity import User

class UserRepository:
    def __init__(self):
        self.db = get_db()
        self.collection = self.db['users']
        
    def find_user_by_email(self, email):
        query = {"email": email}
        user_data = self.collection.find_one(query)
        if user_data:
            user_data['id'] = str(user_data['_id']) 
            del user_data['_id'] 
            return User(**user_data)
        return None

    def find_user_by_id(self, id: str):
        return list(self.collection.find({}, {'_id': 0}))

    def create(self, user_data: User):
        self.collection.insert_one(user_data)
        return user_data