class JPEGAnalyzer:

	def __init__(self):
		self.title = 'JPEG Image'
		self.exts = ['jpg', 'jpe', 'jpeg']
		self.cnt = 0

	def run(self, filename):
		self.cnt += 1
