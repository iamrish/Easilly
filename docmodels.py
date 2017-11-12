from easilly import docsdb

class doc_database(docsdb.Model):

	__tablename__ = "HospitalInfo"

	id = docsdb.Column(docsdb.Integer, primary_key = True)
	fullname = docsdb.Column(docsdb.String, nullable = False)
	email = docsdb.Column(docsdb.String, nullable = False)
	passwd = docsdb.Column(docsdb.String, nullable = False)
#	confpasswd = docsdb.Column(docsdb.String, nullable = False)

	def __init__(self, id, fullname, email, passwd):
		self.id = id
		self.fullname = fullname
		self.email = email
		self.passwd = passwd
#		self.confpasswd = confpasswd
