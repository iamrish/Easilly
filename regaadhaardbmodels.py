from easilly import regaadhaardb

class regaadhaar_database(regaadhaardb.Model):

	__tablename__ = "Easilly_Registered_Aadhaar"

	aadhaar = regaadhaardb.Column(regaadhaardb.Integer, primary_key = True) 
	height = regaadhaardb.Column(regaadhaardb.Integer, nullable = False)
	sex = regaadhaardb.Column(regaadhaardb.String, nullable = False)
	blood_group = regaadhaardb.Column(regaadhaardb.String, nullable = False)
	prev_med_condn = regaadhaardb.Column(regaadhaardb.String, nullable = False)
	emergency_no = regaadhaardb.Column(regaadhaardb.Integer, nullable = False)
	allergies = regaadhaardb.Column(regaadhaardb.String, nullable = False)
	prev_maj_treatmt = regaadhaardb.Column(regaadhaardb.String, nullable = False)
	drugs = regaadhaardb.Column(regaadhaardb.String, nullable = False)

	def __init__(self, aadhaar, height, sex, blood_group, prev_med_condn,\
		emergency_no, allergies, prev_maj_treatmt, drugs):
		self.aadhaar = aadhaar
		self.height = height
		self.sex = sex
		self.blood_group = blood_group
		self.prev_med_condn = prev_med_condn
		self.emergency_no = emergency_no
		self.allergies = allergies
		self.prev_maj_treatmt = prev_maj_treatmt
		self.drugs = drugs