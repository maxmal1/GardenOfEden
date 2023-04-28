# models.py

from flask_login import UserMixin
from sqlalchemy import Table, Column, Integer, ForeignKey
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    
class Plot_Location(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    street_addr = db.Column(db.String(1000))
    lon = db.Column(db.Integer)
    lat = db.Column(db.Integer)
    user_id = db.Column(db.Integer, ForeignKey(User.id))
    size = db.Column(db.String(100))
    
class Individual_Plot(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    plot_id = db.Column(db.Integer, ForeignKey(Plot_Location.id))
    user_id = db.Column(db.Integer, ForeignKey(User.id))
    plant = db.Column(db.String(1000))
    date = db.Column(db.String(100))
    
    