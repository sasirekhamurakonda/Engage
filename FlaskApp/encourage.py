from flask import (Flask,render_template,jsonify)
from flask import render_template, url_for, redirect, flash
from auth.login import LoginForm
from flask_login import login_required
from db.database import Database
import datetime
from datetime import datetime
#from app.models import User
app = Flask(__name__,template_folder="templates")
app.config['SECRET_KEY'] = 'my-secret-key0000000-' #TODO:use random to generate later
@app.route('/')
def home():
    message="Hey User!"
    return render_template('home.html',message=message)
@app.route('/events/<time>', methods=['GET'])
def getEvents(time):
    res=[]
    current_date = datetime.now()
    count=0
    #return all open events
    if(time=='past'):
        query = {"eventDate": {"$lt": current_date}}
        events=Database.get_collection("Event").find(query)
        for event in events:
            event.pop('_id')
            res.append(event)
            if count==5:
                break
        return jsonify(res)
    else:
        query = {"eventDate": {"$gt": current_date}}
        events=Database.get_collection("Event").find(query)
        for event in events:
            event.pop('_id')
            res.append(event)
        return jsonify(res)



@app.route('/profile')
@login_required
def profile():
    return render_template('user/profile.html')

# @app.route('/admin')
# def admin():
#     return render_template('admin.html')
app.run(port=5000)