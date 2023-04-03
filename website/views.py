import json

from flask_login import current_user, login_required

from flask import Blueprint, flash, jsonify, render_template, request

from . import db
from .models import NPC

views = Blueprint('views', __name__)

#All of the website links
@views.route("/")
@login_required
def home():
    return render_template("index.html", user=current_user)

@views.route("/view_npc")
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
