from flask import Blueprint, render_template, request, current_app, redirect, abort, url_for, make_response, session, flash
from . import db, bcrypt, login_manager
from flask_login import UserMixin, login_user, logout_user, login_required, current_user
from bson.objectid import ObjectId

auth = Blueprint("auth", __name__)

#user class for login
class User(UserMixin):
    def __init__(self, user_data):
        self.id = str(user_data["_id"])
        self.username = user_data["username"]

#user registration
@auth.route("/register", methods=["GET", "POST"])
def register():
    users = db.users
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        #check if user already exists
        if users.find_one({"username": username}):
            flash("User already exists", "error")
            return render_template("register.html")

        #hash password and store user
        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
        user_id = users.insert_one({"username": username, "password": hashed_password}).inserted_id
        return redirect(url_for("auth.login"))

    return render_template("register.html")

#user login
@auth.route("/login", methods=["GET", "POST"])
def login():
    users = db.users
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user_data = users.find_one({"username": username})

        if user_data and bcrypt.check_password_hash(user_data["password"], password):
            user = User(user_data)
            login_user(user)
            return redirect(url_for("main.home"))
        
        flash("Invalid credentials", "error")

    return render_template("login.html")

@login_manager.user_loader
def load_user(user_id):
    users = db.users
    user_data = users.find_one({"_id": ObjectId(user_id)})
    return User(user_data) if user_data else None

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.home"))