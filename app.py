from flask import *
import sqlite3
import json

app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome to the Student API!"

