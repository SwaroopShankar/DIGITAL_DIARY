from flask import Flask,request,redirect,url_for,Blueprint
from flask.templating import render_template
from user.models import User
from route import diary as diary_route
import uuid,pymongo
from db import db
from datetime import date

bp = Blueprint("user_routes",__name__,url_prefix="/user")
@bp.route('/signup', methods=['POST'])
def signup():
  return User().signup()

@bp.route('/signout')
def signout():
  return User().signout()

@bp.route('/login', methods=['POST'])
def login():
  return User().login()

@bp.route('/add_one',methods=['POST'])
def save():
    dates = []
    diary={
    "_id": uuid.uuid4().hex,
    "body": request.form.get('page'),
    "date":str(date.today())
    }
    cont = db.page.find()
    for i in cont:
      if i["date"] == str(date.today()):

        db.page.update_one({"_id":i["_id"]},{"$set":{"body":request.form["page"]}})
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
        cont = []
        dat = intersection(date1,date2)
        for _ in dat:
          cont.append(cont2)
        return render_template("diary.html",content2=db.expense.find(),content1=db.page.find(),date = dat , cont = cont)
    db.page.insert_one(diary)
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
    cont = []
    dat = intersection(date1,date2)
    for _ in dat:
      cont.append(cont2)
    return render_template("diary.html",content2=db.expense.find(),content1=db.page.find(),date = intersection(date1,date2),cont = cont)

@bp.route('/add_exp',methods=['POST'])
def expense():
    expense={
      "_id": uuid.uuid4().hex,
      "cat": request.form.get('cat'),
      "exp": int(request.form.get('exp')),
      "date":str(date.today())
      }
    db.expense.insert(expense)
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
    cont = []
    dat = intersection(date1,date2)
    for _ in dat:
      cont.append(cont2)
    return render_template("diary.html",content2=db.expense.find(),content1=db.page.find(),date = dat,cont = cont)
    
  
@bp.route('/update/<id>',methods=['POST','GET'])
def upd(id):
   
    return redirect(url_for('/'))

@bp.route('/update/{{diary._id}}',methods=['POST'])
def update(_id):
   
    db.page.update_one({"_id":_id},{"$set":{"body":request.form["page"]}})
    return render_template("diary.html",content=db.page.find())

  
