
from flask import Blueprint,render_template
from decorators import login_required
from db import db
bp = Blueprint("dashboard_routes",__name__)

@bp.route('/')
def home():
  return render_template('home.html')

@bp.route('/dashboard/')
@login_required
def dashboard():
  return render_template('dashboard.html')


@bp.route('/dashboard/images/')
def images():
  return render_template('images.html')


@bp.route('/dashboard/diary/')
def diary():
  return render_template('diary.html',content=db.page.find())


@bp.route('/dashboard/expenses/')
def expenses():
  return render_template('expenses.html')


@bp.route('/dashboard/images/expenses/')
def images_expenses():
  return render_template('expenses.html')