from flask import redirect, url_for, session, request
from functools import wraps

def login_required(f):
    """
    Decorador que verifica se o usuário está logado.
    Se não estiver, ele é redirecionado para a página de login.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login', next=request.url))

        return f(*args, **kwargs)
    return decorated_function
