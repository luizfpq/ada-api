# config.py

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SECRET_KEY = '2eecdae4c7866551d62fa910051fb6658ff347bf5ef1da64d3adda7899e01df4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = '26361e7fcb00fda02dadffd793fdd70702306b2608ed28e96fe0a0e45b696d8a'