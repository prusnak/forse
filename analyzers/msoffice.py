class MSOfficeAnalyzer:

	def __init__(self):
		self.title = 'Microsoft Office'
		self.exts = ['doc', 'dot', 'xls', 'xlt', 'xlm', 'ppt', 'pps']
		self.cnt = 0

	def run(self, filename):
		self.cnt += 1
