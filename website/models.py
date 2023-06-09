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
    characters = db.relationship('Character')
    notes = db.relationship('Note')

class Character(db.Model):
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
    equipment1 = db.Column(db.String(150))
    equipment2 = db.Column(db.String(150))
    equipment3 = db.Column(db.String(150))
    equipment4 = db.Column(db.String(150))
    equipment5 = db.Column(db.String(150))
    action1 = db.Column(db.String(150))
    action2 = db.Column(db.String(150))
    action3 = db.Column(db.String(150))
    action4 = db.Column(db.String(150))
    action5 = db.Column(db.String(150))
    spell1 = db.Column(db.String(150))
    spell2 = db.Column(db.String(150))
    spell3 = db.Column(db.String(150))
    spell4 = db.Column(db.String(150))
    spell5 = db.Column(db.String(150))

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    data = db.Column(db.String(10000))
