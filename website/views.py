import json

from flask_login import current_user, login_required

from flask import Blueprint, flash, jsonify, render_template, request

from . import db
from .models import NPC, Character, Note, Quest

views = Blueprint('views', __name__)

#All of the website links
@views.route("/")
@login_required
def home():
    return render_template("index.html", user=current_user)

@views.route("/view_npc")
@login_required
def view_npc():
    return render_template("view_npc.html", user=current_user)

@views.route("/ref")
def reference():
    return render_template("ref.html", user=current_user)

@views.route("/delete_npc", methods=['POST'])
def delete_npc():
    npc = json.loads(request.data) # this function expects a JSON from the npc_generator.js file 
    npcId = npc['npcId']
    npc = NPC.query.get(npcId)
    if npc:
        if npc.user_id == current_user.id:
            db.session.delete(npc)
            db.session.commit()

    return jsonify({})

@views.route("/delete_character", methods=['POST'])
def delete_character():
    character = json.loads(request.data) # this function expects a JSON from the npc_generator.js file 
    characterId = character['characterId']
    character = Character.query.get(characterId)
    if character:
        if character.user_id == current_user.id:
            db.session.delete(character)
            db.session.commit()

    return jsonify({})

@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route('/delete-quest', methods=['POST'])
def delete_quest():  
    quest = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    questId = quest['questId']
    quest = Quest.query.get(questId)
    if quest:
        if quest.user_id == current_user.id:
            db.session.delete(quest)
            db.session.commit()

    return jsonify({})