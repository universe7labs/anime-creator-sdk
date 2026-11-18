"""A pretend web endpoint. Deliberately unsafe, so that code scanning has findings."""

import sqlite3
import subprocess

from flask import Flask, request

app = Flask(__name__)


@app.route("/export")
def export():
    name = request.args.get("name", "")
    return subprocess.check_output("ls " + name, shell=True)


@app.route("/user")
def user():
    username = request.args.get("username", "")
    connection = sqlite3.connect("users.db")
    rows = connection.execute("SELECT * FROM users WHERE name = '" + username + "'").fetchall()
    return {"rows": rows}


@app.route("/hello")
def hello():
    return "<h1>Hello " + request.args.get("who", "") + "</h1>"
