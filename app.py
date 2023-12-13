from flask import Flask
from database.database import db
from models.air_dsr import AIRDSR
from models.sea_dsr import SEADSR
from routes.routes import main_bp
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '123AAA'
app.config['SQLALCHEMY_ECHO'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://user1:localhost3306@localhost:3306/dsr'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost:3306/dsr'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://dsr_app:App_tsvglobal_123@localhost:3306/dsr'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
login_manager = LoginManager(app)
app.register_blueprint(main_bp)
