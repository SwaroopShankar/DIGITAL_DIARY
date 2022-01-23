from flask import Flask, render_template, session, redirect 
from functools import wraps
import pymongo

app = Flask(__name__)
app.secret_key = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'
app.config['TESTING'] = False
# Database
client = pymongo.MongoClient('localhost', 27017)
db = client.diary
# Decorators
def login_required(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
      return f(*args, **kwargs)
    else:
      return redirect('/')
  
  return wrap

# Routes
from user import routes

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/dashboard/')
@login_required
def dashboard():
  return render_template('dashboard.html')


@app.route('/dashboard/images/')
def images():
  return render_template('images.html')

@app.route('/dashboard/diary/')
def diary():
  return render_template('diary.html')

@app.route('/dashboard/expenses/')
def expenses():
  return render_template('expenses.html')


@app.route('/dashboard/images/expenses/')
def images_expenses():
  return render_template('expenses.html')

