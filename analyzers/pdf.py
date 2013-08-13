class PDFAnalyzer:

	def __init__(self):
		self.title = 'Portable Document Format'
		self.exts = ['pdf']
		self.cnt = 0

	def run(self, filename):
		self.cnt += 1
