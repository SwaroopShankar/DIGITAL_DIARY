
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


# Routes
# from user import routes




