# app/controllers/main.py

from flask import Blueprint
from flask import Blueprint, render_template, redirect, url_for, request, flash
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template("index.html")

