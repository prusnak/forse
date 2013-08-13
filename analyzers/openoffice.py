class OpenOfficeAnalyzer:

	def __init__(self):
		self.title = 'Open/Libre Office'
		self.exts = ['odt', 'ott', 'odm', 'ods', 'ots', 'odg', 'otg', 'odp', 'otp', 'odf', 'odb']
		self.cnt = 0

	def run(self, filename):
		self.cnt += 1
