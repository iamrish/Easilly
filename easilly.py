from flask import Flask, render_template, \
 url_for, redirect, request, flash, session
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
import smtplib


app = Flask(__name__)
try:
	session['logged_in'] = False
except: RuntimeError
aadhaar_no = None

import os
app.config.from_object(os.environ['APP_SETTINGS'])

#db = SQLAlchemy(app)
docsdb = SQLAlchemy(app)
aadhaardb = SQLAlchemy(app)
regdb = SQLAlchemy(app)
regaadhaardb = SQLAlchemy(app)
from docmodels import *
from aadhaarmodels import *
from regmodels import *
from regaadhaardbmodels import *

#probably 2 type ke login req
def login_req(f):
  @wraps(f)
  def wrapper(*args, **kwargs):
    if 'logged_in' in session:	
      return f(*args, **kwargs)
    else:
      flash('You need to login first!')
      return redirect(url_for('home'))
  return wrapper


@app.route('/', methods = ['GET', 'POST'])
def home():
	if request.method == 'POST':
		if request.name == "register":
			return redirect(url_for('reg'))
		elif request.name == "login":
			return redirect(url_for('login'))
	return render_template('index.html')



#REGISTRATION BLOCK:


@app.route('/successful')
@login_req
def successful():
	return render_template('sucessfull.html')


@app.route('/aadhaar1', methods = ['GET', 'POST'])
@login_req
def aadhaar1():
	error = None
	flag = False
	temp2 = aadhaardb.session.query(aadhaar_database).all()
	if request.method == 'POST':
		for records in temp2:
			if request.form['id'] == records.id:
				flag = True
				break
		if flag == False:
			error = "Aadhaar not registered with government!"
		else:
			regaadhaardb.create_all()
			regaadhaardb.session.add(reg_database(request.form['sex'], request.form['height'], \
				request.form['Blood Group'],request.form['emergency_no'],\
				 request.form['prev_med_condn'], request.form['allergies'], \
				 request.form['prev_maj_treatmt'], request.form['drug']))
			regaadhaardb.session.commit()
			return redirect(url_for('successful'))

	return render_template('aadhaar1.html', error = error)

@app.route('/login')
@login_req
def login():
	temp = regdb.session.query(reg_database).all()
	error = None
	flag = False
	for records in temp:
		if request.form['license_no'] == records.id and request.form['passwd'] == records.passwd:
			session['logged_in'] = True
			flash("Successfully Logged in")
			redirect(url_for('index2'))
		elif request.form['license_no'] != records.id:
			error = "License_no Invalid"
		elif request.form['passwd'] != records.passwd:
			error = "Incorrect Password"
	return render_template("login.html", error = error)


@app.route('/reg', methods = ['POST', 'GET'])
def reg():
	error = None
	flag = False
	temp1 = docsdb.session.query(doc_database).all()
	if request.method == 'POST':
		for records in temp1:
			if request.form['id'] == records.id:
				flag = True
				break
		if flag == False:
			error = "Invalid ID"
		elif request.form['passwd'] != request.form['confpasswd']:
			error = "Passwords do not match"
		else:
			session['logged_in'] = True
			regdb.create_all()	
			regdb.session.add(reg_database(request.form['id'], request.form['password']))
			regdb.session.commit()
			flash("You were just logged in!")
			return redirect(url_for('next'))

	return render_template('reg.html',  error = error)


#LOGIN BLOCK:

@app.route('/index2')
@login_req
def index2():
	return render_template("index2.html")

"""@app.route('/details')
@login_req
def details():
	temp3 = regaadhaardb.session.query(regaadhaar_database).all()
	for records in temp3:
		if aadhaar_no == records.id:
			return render_template("details.html", aadhaar = records.aadhaar, height = records.height, sex = records.sex, blood_group = records.blood_group, /
				prev_med_condn = records.prev_med_condn, emergency_no = records.emergency_no, /
				allergies = records.allergies,prev_maj_treatmt = records.prev_maj_treatmt, drugs = records.drugs)
		else:
			error = "Aadhaar not registered with Easilly"
			return redirect(url_for('aadhaar2'))"""




@app.route('/aadhaar2', methods = ['GET', 'POST'])
@login_req
def aadhaar2():
	error = None
	flag = False
	temp2 = aadhaardb.session.query(aadhaar_database).all()
	if request.method == 'POST':
		for records1 in temp2:
			if request.form['id'] == records1.id:
				flag = True
				aadhaar_no = request.form['id']
				break
		if flag == False:
			error = "Aadhaar not registered with government!"
		else:
			server = smtplib.SMTP('smtp.gmail.com', 587)
			server.starttls()
			server.login("rishabhmalhotra57@gmail.com", "hahalol")
			temp3 = regaadhaardb.session.query(regaadhaar_database).all()
			for records in temp3:
				if aadhaar_no == records.id:
					msg = "Name: {}   DOB: {}  Sex: {}   Blood Group: {}   Height: {}   \
					Pevious medical condition: {}   Allergies/Complications: {}   \
					Previous Major Treatments: {}   Drugs: {}".format(request.form['fullname'], records.dob, \
						records.sex, records.blood_group, records.height, records.prev_med_condn, \
						records.allergies, records.prev_maj_treatmt, records.drugs)
					break
			server.sendmail("rishabhmalhotra57@gmail.com", "juit.deepesh@gmail.com", msg)
			server.quit()
			 

	return render_template('aadhaar2.html', error = error)


"""@app.route('/login', methods = ['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin': 
	    # 'username' and 'password' are the name attributes of input tag in login.html
			error = 'Invalid credentials. Please try again.'
		else:
			session['logged_in'] = True
			flash("You were just logged in")
			return redirect(url_for('home'))

	return render_template('login.html', error	= error)"""

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash("You were just logged out!")
	return redirect(url_for('welcome'))

#def connect_db():
#	return sqlite3.connect(app.database)

if __name__ == '__main__':
	app.run(debug = True)
