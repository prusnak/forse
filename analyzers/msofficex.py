class MSOfficeXAnalyzer:

	def __init__(self):
		self.title = 'Microsoft Office 2007+'
		self.exts = ['docx', 'docm', 'dotx', 'dotm',
		             'xlsx', 'xlsm', 'xltx', 'xltm', 'xlsb', 'xlam',
		             'pptx', 'pptm', 'potx', 'potm', 'ppam', 'ppsx', 'ppsm', 'sldx', 'sldm', 'thmx']
		self.cnt = 0

	def run(self, filename):
		self.cnt += 1
