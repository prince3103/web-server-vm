"""
This module creates app instance of Flask class from flask package.
"""
from flask import Flask

app = Flask(__name__)

from app import views
