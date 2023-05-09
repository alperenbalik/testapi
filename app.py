from flask import *
import sqlite3
import json
from student import Student

app = Flask(__name__)

@app.route("/", methods=["GET"])
def go_home():
    return "Welcome to the Student API!"

