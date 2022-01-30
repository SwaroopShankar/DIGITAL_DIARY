
from flask import Blueprint,render_template
from decorators import login_required
from db import db
from datetime import date
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
  def intersection(lst1, lst2):
      lst3 = [value for value in lst1 if value in lst2]
      return lst3
  cont1 = db.page.find()
  cont2 = db.expense.find()
  date1 = []
  date2 = []
  for data1 in cont1:
    date1.append(data1["date"])
  for data2 in cont2:
    date2.append(data2["date"])
  print(intersection(date1,date2))
  cont = []
  dat = intersection(date1,date2)
  for _ in dat:
    cont.append(cont2)
  return render_template('diary.html',content2=db.expense.find(),content1=db.page.find(),date = intersection(date1,date2),cont = cont)


@bp.route('/dashboard/expenses/')
def expenses():
  return render_template('expenses.html')


@bp.route('/dashboard/images/expenses/')
def images_expenses():
  return render_template('expenses.html')