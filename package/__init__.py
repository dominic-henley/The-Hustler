from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '3f3040542f9e39e5cc0a30ac826f383d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///journal.db'

db = SQLAlchemy(app)