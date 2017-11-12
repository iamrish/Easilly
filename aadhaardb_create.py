from easilly import aadhaardb
from aadhaarmodels import aadhaar_database
from flask import request

#create databse and the databse tables
aadhaardb.create_all()		#this initialises the database based on the schema in our aadhaarmodels.py file

#insert
aadhaardb.session.add(aadhaar_database(161263, "Rishabh Malhotra", "16/07/1998", "ABCD","male"))
aadhaardb.session.add(aadhaar_database(171380, "Deepesh Yadav", "15/10/1998","EFGH","male"))
aadhaardb.session.add(aadhaar_database(171813,	"Umang Maheshwari","09/05/1999","IJKL","male"))
#commit
aadhaardb.session.commit()