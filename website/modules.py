from flask_login import current_user, login_required

from flask import Blueprint, flash, redirect, render_template, request, url_for

from . import db
from .models import NPC, Character, Note, Quest

modules = Blueprint('modules', __name__)

@modules.route("/character_creator", methods=['GET', 'POST'])
def character_creator():
    if request.method == 'POST':
        name = request.form.get('name')
        race = request.form.get('race')
        play_class = request.form.get('play_class')
        level = request.form.get('level', type=int)
        alignment = request.form.get('alignment')
        strength = request.form.get('strength', type=int)
        dexterity = request.form.get('dexterity', type=int)
        constitution = request.form.get('constitution', type=int)
        intelligence = request.form.get('intelligence', type=int)
        wisdom = request.form.get('wisdom', type=int)
        charisma = request.form.get('charisma', type=int)
        hp = request.form.get('hp', type=int)
        ac = request.form.get('ac', type=int)
        perception = request.form.get('perception', type=int)
        personality = request.form.get('personality')
        physical_description = request.form.get('physical_description')
        equipment1 = request.form.get('equipment1')
        equipment2 = request.form.get('equipment2')
        equipment3 = request.form.get('equipment3')
        equipment4 = request.form.get('equipment4')
        equipment5 = request.form.get('equipment5')
        action1 = request.form.get('action1')
        action2 = request.form.get('action2')
        action3 = request.form.get('action3')
        action4 = request.form.get('action4')
        action5 = request.form.get('action5')
        spell1 = request.form.get('spell1')
        spell2 = request.form.get('spell2')
        spell3 = request.form.get('spell3')
        spell4 = request.form.get('spell4')
        spell5 = request.form.get('spell5')
        if len(name) < 1:
            flash('Name must be at least 1 character long', category='error')
        elif level < 1:
            flash('Level must be at least 1', category='error')
        elif strength < 1:
            flash('Strength must be at least 1', category='error')
        elif strength > 30:
            flash('Strength can\'t be greater than 30', category='error')
        elif dexterity < 1:
            flash('Dexterity must be at least 1', category='error')
        elif dexterity > 30:
            flash('Dexterity can\'t be greater than 30', category='error')
        elif constitution < 1:
            flash('Constitution must be at least 1', category='error')
        elif constitution > 30:
            flash('Constitution can\'t be greater than 30', category='error')
        elif intelligence < 1:
            flash('Intelligence must be at least 1', category='error')
        elif intelligence > 30:
            flash('Intelligence can\'t be greater than 30', category='error')
        elif wisdom < 1:
            flash('Wisdom must be at least 1', category='error')
        elif wisdom > 30:
            flash('Wisdom can\'t be greater than 30', category='error')
        elif charisma < 1:
            flash('Charisma must be at least 1', category='error')
        elif charisma > 30:
            flash('Charisma can\'t be greater than 30', category='error')
        elif hp < 1:
            flash('HP must be at least 1', category='error')
        elif ac < 1:
            flash('AC must be at least 1', category='error')
        elif perception < 1:
            flash('Perception must be at least 1', category='error')
        elif len(personality) < 1:
            flash('Must include personality', category='error')
        elif len(physical_description) < 1:
            flash('Must include a physical description', category='error')
        else:
            new_character = Character(name=name, race=race, play_class=play_class, level=level, alignment=alignment, strength=strength, dexterity=dexterity, constitution=constitution, intelligence=intelligence, wisdom=wisdom, charisma=charisma, hp=hp, ac=ac, perception=perception, personality=personality, physical_description=physical_description, equipment1=equipment1, equipment2=equipment2, equipment3=equipment3, equipment4=equipment4, equipment5=equipment5, action1=action1, action2=action2, action3=action3, action4=action4, action5=action5, spell1=spell1, spell2=spell2, spell3=spell3, spell4=spell4, spell5=spell5, user_id=current_user.id)
            db.session.add(new_character)
            db.session.commit()
            return redirect(url_for('modules.character_creator'))
    return render_template("character_creator.html", user=current_user)

@modules.route("/npc_generator", methods=['GET', 'POST'])
@login_required
def npc_generator():
    if request.method == 'POST':
        name = request.form.get('name')
        race = request.form.get('race')
        play_class = request.form.get('play_class')
        level = request.form.get('level', type=int)
        alignment = request.form.get('alignment')
        strength = request.form.get('strength', type=int)
        dexterity = request.form.get('dexterity', type=int)
        constitution = request.form.get('constitution', type=int)
        intelligence = request.form.get('intelligence', type=int)
        wisdom = request.form.get('wisdom', type=int)
        charisma = request.form.get('charisma', type=int)
        hp = request.form.get('hp', type=int)
        ac = request.form.get('ac', type=int)
        perception = request.form.get('perception', type=int)
        personality = request.form.get('personality')
        physical_description = request.form.get('physical_description')

        
        if len(name) < 1:
            flash('Name must be at least 1 character long', category='error')
        elif level < 1:
            flash('Level must be at least 1', category='error')
        elif strength < 1:
            flash('Strength must be at least 1', category='error')
        elif strength > 30:
            flash('Strength can\'t be greater than 30', category='error')
        elif dexterity < 1:
            flash('Dexterity must be at least 1', category='error')
        elif dexterity > 30:
            flash('Dexterity can\'t be greater than 30', category='error')
        elif constitution < 1:
            flash('Constitution must be at least 1', category='error')
        elif constitution > 30:
            flash('Constitution can\'t be greater than 30', category='error')
        elif intelligence < 1:
            flash('Intelligence must be at least 1', category='error')
        elif intelligence > 30:
            flash('Intelligence can\'t be greater than 30', category='error')
        elif wisdom < 1:
            flash('Wisdom must be at least 1', category='error')
        elif wisdom > 30:
            flash('Wisdom can\'t be greater than 30', category='error')
        elif charisma < 1:
            flash('Charisma must be at least 1', category='error')
        elif charisma > 30:
            flash('Charisma can\'t be greater than 30', category='error')
        elif hp < 1:
            flash('HP must be at least 1', category='error')
        elif ac < 1:
            flash('AC must be at least 1', category='error')
        elif perception < 1:
            flash('Perception must be at least 1', category='error')
        elif len(personality) < 1:
            flash('Must include personality', category='error')
        elif len(physical_description) < 1:
            flash('Must include a physical description', category='error')
        else:
            new_npc = NPC(name=name, race=race, play_class=play_class, level=level, alignment=alignment, strength=strength, dexterity=dexterity, constitution=constitution, intelligence=intelligence, wisdom=wisdom, charisma=charisma, hp=hp, ac=ac, perception=perception, personality=personality, physical_description=physical_description, user_id=current_user.id)
            db.session.add(new_npc)
            db.session.commit()
            return redirect(url_for('modules.npc_generator'))
    return render_template("npc_generator.html", user=current_user)

@modules.route("/market_generator")
@login_required
def m_gen():
    return render_template("market_generator.html", user=current_user)

@modules.route("/dice_roller")
@login_required
def dice():
    return render_template("dice_roller.html", user=current_user)

@modules.route("/notes", methods=['GET', 'POST'])
@login_required
def notes():
    if request.method == 'POST':
        data = request.form.get('note')
        if len(data) < 1:
            flash('Must input a note to save', category='error')
        else:

            new_note = Note(data=data, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
    return render_template("notes.html", user=current_user)

@modules.route("/quests", methods=['GET', 'POST'])
@login_required
def quests():
    if request.method == 'POST':
        quest = request.form.get('quest')
        players_told = False
        is_active = False
        is_complete = False

        if len(quest) < 1:
            flash('Must input a quest to save', category='error')
        else:

            new_quest = Quest(data=quest, players_told = players_told, is_active=is_active, is_complete=is_complete, user_id=current_user.id)
            db.session.add(new_quest)
            db.session.commit()
    return render_template("quests.html", user=current_user)