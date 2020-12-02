from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:rootpassword123@35.246.6.246/practical_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from application import routes