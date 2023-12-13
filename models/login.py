from app import db
from flask_login import UserMixin

# class USER(db.Model):
#     # Your model definition here
#     pass




class USER(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    createdby=db.Column(db.String(255),nullable=False)
    createddate=db.Column(db.Date,nullable=False)
    email = db.Column(db.String(255),unique=True,nullable=False)
    password = db.Column(db.String(255),nullable=False)
    updatedby=db.Column(db.String(255),nullable=True)
    updateddate=db.Column(db.Date,nullable=True)
    usertype=db.Column(db.String(255),nullable=False)
    accesstype=db.Column(db.String(255),nullable=False)
    company=db.Column(db.String(255),nullable=False)



    # Flask-Login requires a get_id method  
    def get_id(self):
        return str(self.id)

    def __init__(self,createdby,createddate,email,password,updatedby,updateddate,usertype,accesstype,company):
        self.createdby=createdby
        self.createddate=createddate
        self.email=email
        self.password=password
        self.updatedby=updatedby
        self.updateddate=updateddate
        self.usertype=usertype
        self.accesstype=accesstype
        self.company=company
