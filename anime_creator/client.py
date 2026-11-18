"""A pretend client library. The unsafe code below is deliberate: it is here so that
code scanning has something to find. Do not copy it."""

import sqlite3
import subprocess

import yaml


def run_export(name):
    # Deliberately unsafe: a caller-supplied value reaches a shell.
    return subprocess.check_output("ls " + name, shell=True)


def find_user(connection: sqlite3.Connection, username):
    # Deliberately unsafe: a query built by joining strings.
    return connection.execute("SELECT * FROM users WHERE name = '" + username + "'").fetchall()


def load_settings(text):
    # Deliberately unsafe: yaml.load without a safe loader.
    return yaml.load(text)
