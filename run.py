# run.py

from app import app, db

if __name__ == '__main__':
    # Cria uma aplicação Flask
    with app.app_context():
        # Cria as tabelas no banco de dados antes de iniciar o servidor
        db.create_all()

    # Inicia o servidor Flask
    app.run(host='0.0.0.0',debug=True)
