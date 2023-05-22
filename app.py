from flask import *
import sqlite3
import json

app = Flask(__name__)

@app.route("/")
def go_home():
    return "Welcome to the Student API!"

