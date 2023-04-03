from flask_login import UserMixin

from . import db


class NPC(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(150))
    race = db.Column(db.String(150))
    play_class = db.Column(db.String(150))
    level = db.Column(db.Integer)
    alignment = db.Column(db.String(2))
    strength = db.Column(db.Integer)
    dexterity = db.Column(db.Integer)
    constitution = db.Column(db.Integer)
    intelligence = db.Column(db.Integer)
    wisdom = db.Column(db.Integer)
    charisma = db.Column(db.Integer)
    hp = db.Column(db.Integer)
    ac = db.Column(db.Integer)
    perception = db.Column(db.Integer)
    personality = db.Column(db.String(300))
    physical_description = db.Column(db.String(300))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    npcs = db.relationship('NPC')