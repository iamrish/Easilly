from easilly import regdb

class reg_database(regdb.Model):

	__tablename__ = "Registered_Docs"

	id = regdb.Column(regdb.Integer, primary_key = True)
	passwd = regdb.Column(regdb.String, nullable = False)

	def __init__(self, id, passwd):
		self.id = id
		self.passwd = passwd