from werkzeug.security import check_password_hash

from app.infrastructure.mongodb.repositories.user_account_repository import UserAccountRepository

class UserAccountService:
    def __init__(self, user_account_repository: UserAccountRepository = None):
        self.user_account_repository = user_account_repository or UserAccountRepository()
    
    def get_user_account_by_user_id(self, id):
        account = self.user_account_repository.find_account_by_user_id(id)
        if account:
            return account
        return None

