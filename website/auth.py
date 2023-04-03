from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from flask import Blueprint, flash, redirect, render_template, request, url_for

from . import db
from .models import User

auth = Blueprint('auth', __name__)

@auth.route("/sign_in", methods=['GET', 'POST'])
def sign_in():
    if request.method=='POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in Successfully!", category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect Password', category='error')
        else:
            flash("Email does not exist", category='error')

    return render_template("sign_in.html", user=current_user)

@auth.route("/sign_up", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email already exists', category='error')
        elif len(password1) < 8:
            flash('Password must be at least than 8 characters', category = 'error')
        elif len(username) < 6:
            flash('Username must be at least 6 characters', category = 'error')
        elif password2 != password1:
            flash('Passwords don\'t match', category = 'error')
        else:
            new_user = User(email=email, username = username, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account Created!', category = 'success')
            return redirect(url_for('auth.sign_in'))
    return render_template("sign_up.html", user=current_user)

@auth.route("/sign_out")
@login_required
def sign_out():
    logout_user()
    return redirect(url_for('auth.sign_in'))