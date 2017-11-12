from easilly import docsdb
from docmodels import doc_database
from flask import request

#create databse and the databse tables
docsdb.create_all()		#this initialises the database based on the schema in our docmodels.py file

#insert
docsdb.session.add(doc_database(123,"NAME1","name1.1@hos.com","12345"))
docsdb.session.add(doc_database(456,"NAME2","name2.2@hos.com","12345"))
docsdb.session.add(doc_database(789,"NAME3","name3.3@hos.com","12345"))
#commit
docsdb.session.commit()