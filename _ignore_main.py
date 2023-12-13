from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from logger import log_args_and_return

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from routes import *

@app.errorhandler(500)
def handle_500_error(e):
    app.logger.error(f'Server error: {str(e)}')
    return 'Internal Server Error', 500

@log_args_and_return
def run_app():
    app.run(debug=True)  # Set debug to False in production

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    try:
        run_app()
    except Exception as e:
        app.logger.error(f'Function run_app raised an exception: {str(e)}')
