import os

from dotenv import load_dotenv
from flask import Flask, render_template, request, session, redirect, url_for

from app.application.route_guard import login_required

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # *********** Lógica de Autenticação Real Aqui ***********
        # Exemplo: Se o username e senha estiverem corretos:
        # 1. Define uma chave na session para indicar que o usuário está logado
        session['user_id'] = 123
        session['username'] = 'ExemploUser'
        next_url = request.args.get('next')
        return redirect(next_url or url_for('index'))
    return render_template('login/login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/')
@login_required
def index():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)