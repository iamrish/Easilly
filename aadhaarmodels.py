from easilly import aadhaardb

class aadhaar_database(aadhaardb.Model):

	__tablename__ = "AadhaarInfo"

	id = aadhaardb.Column(aadhaardb.Integer, primary_key = True)
	fullname = aadhaardb.Column(aadhaardb.String, nullable = False)
	dob = aadhaardb.Column(aadhaardb.String, nullable = False)
	address = aadhaardb.Column(aadhaardb.String, nullable = False)
	sex = aadhaardb.Column(aadhaardb.String, nullable = False)

	def __init__(self, id, fullname, dob, address, sex):
		self.id = id
		self.fullname = fullname
		self.dob = dob
		self.address = address
		self.sex = sex