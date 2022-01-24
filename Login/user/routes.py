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
    

    diary={
    "_id": uuid.uuid4().hex,
    "body": request.form.get('page'),
    "date":str(date.today())
    }
    cont = db.page.find()
    for i in cont:
      if i["date"] == str(date.today()):
        db.page.update_one({"_id":i["_id"]},{"$set":{"body":request.form["page"]}})
        return render_template("diary.html",content=db.page.find())
    db.page.insert_one(diary)
    return render_template("diary.html",content=db.page.find())
  


  
