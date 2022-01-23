
from flask import Flask, render_template, session, redirect, url_for 
from functools import wraps
import pymongo
from user import routes as user_routes
from db import db
import route
app = Flask(__name__)
app.secret_key = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'
app.config['TESTING'] = False
# Database
app.register_blueprint(user_routes.bp)
app.register_blueprint(route.bp)
# Decorators

# @app.route("/test_1")
# def test_1():
#   return redirect(url_for("test_2"))

# @app.route("/test_2")
# def test_2():
#   return "hi"


# Routes
# from user import routes




