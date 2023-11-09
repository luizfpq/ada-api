# app/routes/users.py

from flask import Blueprint, request,jsonify
from app import db
from app.models import User
import hashlib
import time

users = Blueprint('users', __name__)

@users.route('/users/signup', methods=['POST'])
def signup():
    data = request.get_json()

    # Verifique se todos os campos necessários estão presentes na requisição
    required_fields = ['username', 'name', 'password', 'email', 'role']
    if not all(field in data for field in required_fields):
        return jsonify({'message': 'Missing required fields'}), 400

    # Verifique se o papel (role) é válido
    valid_roles = ['master', 'admin', 'user']
    if data['role'] not in valid_roles:
        return jsonify({'message': 'Invalid role'}), 400

    # Gere um salt usando o timestamp atual
    salt = str(int(time.time()))

    # Concatene a senha com o salt e aplique hash SHA-256
    hashed_password = hashlib.sha256((data['password'] + salt).encode('utf-8')).hexdigest()

    # Crie e adicione o usuário ao banco de dados
    new_user = User(
        username=data['username'],
        name=data['name'],
        password=hashed_password,
        email=data['email'],
        role=data['role'],
        salt=salt
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

@users.route('/users/login', methods=['POST'])
def login():
    # Implemente a lógica de autenticação aqui
    pass

@users.route('/users/<int:user_id>', methods=['PUT', 'DELETE'])
def edit_user(user_id):
    # Implemente a lógica de edição ou desativação de usuários aqui
    pass
