#ye easilly me apne aap hi ban jayegi ghonchu!

from easilly import regdb
from regmodels import reg_database
from flask import request

#create databse and the databse tables
regdb.create_all()		#this initialises the database based on the schema in our regmodels.py file

#insert
#egdb.session.add(reg_database(request.form['id'], request.form['passwd']))

#commit
regdb.session.commit()