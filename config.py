import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'mysql+mysqlconnector://root:@localhost/dsr')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    from app import app
    app.register_blueprint(main_bp)
    # .env

    # SECRET_KEY=your-secret-key
    # DATABASE_URL=mysql+mysqlconnector://root:@localhost/dsr