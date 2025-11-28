import os

from dotenv import load_dotenv
from flask import Flask, render_template, request, session, redirect, url_for, jsonify

from app.application.utils.route_guard import login_required
from app.application.utils.data_validation import data_validation

from app.domain.dtos.login_dto import LoginDto

from app.application.services.user_service import UserService

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

user_service = UserService()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.is_json:
            # valida o corpo da requisição
            data = request.get_json()
            data = data_validation(data)
            if data is None:
                return jsonify({'error': 'Invalid data'}), 400 
            
            # valida o conteudo da requisição
            try:
                login_dto = LoginDto(**data)
            except TypeError as e:
                return jsonify({"error": f"Invalid data. Error: {e}"}), 400
            
            
            session['user_id'] = 123
            session['username'] = 'ExemploUser'
            next_url = request.args.get('next')
            return redirect(next_url or url_for('index'))
        else: 
            return jsonify({'error': 'Invalid data'}), 400
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