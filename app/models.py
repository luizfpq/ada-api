# app/models.py

from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Adicionando uma coluna como chave primária
    username = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(20), nullable=False)
    salt = db.Column(db.String(20))  # Adicionando uma coluna para armazenar o salt

# Defina outros modelos como Item, Transaction, Category aqui
