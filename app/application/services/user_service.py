from app.infrastructure.mongodb.repositories.user_repository import UserRepository

class UserService:
    def __init__(self, user_repository: UserRepository = None):
        # Injeção de Dependência: O Repositório
        self.user_repository = user_repository or UserRepository()

    def add_new_user(self, user_data):
        if not user_data.get('name'):
            raise ValueError("Nome é obrigatório.")
        
        return self.user_repository.create(user_data)

