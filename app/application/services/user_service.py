from werkzeug.security import check_password_hash

from app.domain.dtos.login_dto import LoginDto
from app.infrastructure.mongodb.repositories.user_repository import UserRepository

class UserService:
    def __init__(self, user_repository: UserRepository = None):
        # Injeção de Dependência: O Repositório
        self.user_repository = user_repository or UserRepository()
    
    def login_user(self, dto: LoginDto):
        user = self.user_repository.find_user_by_email(dto.email)
        if user:
            if check_password_hash(user.password, dto.password):
                return user
            return None
        return None

    def add_new_user(self, user_data):
        if not user_data.get('name'):
            raise ValueError("Nome é obrigatório.")
        return self.user_repository.create(user_data)
