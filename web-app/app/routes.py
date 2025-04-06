"""
Provides routes for main flask app
"""
from flask import Blueprint, render_template  # add more as needed

main = Blueprint("main", __name__)


@main.route("/")
def home():
    """
    home page, regardless whether user is logged in or not
    """
    return render_template('home.html')
