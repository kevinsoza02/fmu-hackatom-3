import os
import json

from dataclasses import asdict
from dotenv import load_dotenv
from flask import Flask, render_template, request, session, redirect, url_for, jsonify

from app.application.utils.route_guard import login_required
from app.application.utils.data_validation import data_validation

from app.domain.dtos.login_dto import LoginDto

from app.application.services.user_service import UserService
from app.application.services.user_account_service import UserAccountService

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

user_service = UserService()
user_account_service = UserAccountService()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.is_json:
            # valida o corpo da requisição
            data = data_validation()
            if data is None:
                return jsonify({'error': 'Invalid data'}), 400 
            
            # valida o conteudo da requisição
            try:
                login_dto = LoginDto(**data)
            except TypeError as e:
                return jsonify({"error": f"Invalid data. Error: {e}"}), 400
            
            user = user_service.login_user(login_dto)
            if not user:
                return jsonify({'error': 'Wrong email or password'}), 400
            
            session['user_id'] = user.id
            session['username'] = user.name
            next_url = request.args.get('next')
            return jsonify({
                    "success": True, 
                    "message": "Login realizado com sucesso! Redirecionando...",
                    "redirect_url": "/" 
                }), 200
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
    user_id = session.get('user_id')
    user_name = session.get('username')
    account = user_account_service.get_user_account_by_user_id(user_id)
    if not account:
        return jsonify({'error': 'Invalid data'}), 400
    return render_template(
        'home/home.html',
        balance=account.balance,
        account=account.account,
        agency=account.agency,
        username=user_name,
    )
            
if __name__ == '__main__':
    app.run(debug=True)