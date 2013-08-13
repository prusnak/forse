import os
from jpeg import JPEGAnalyzer
from msoffice import MSOfficeAnalyzer
from msofficex import MSOfficeXAnalyzer
from openoffice import OpenOfficeAnalyzer
from pdf import PDFAnalyzer

class Analyzers:

	def __init__(self):
		self.analyzers = [JPEGAnalyzer(), MSOfficeAnalyzer(), MSOfficeXAnalyzer(), OpenOfficeAnalyzer(), PDFAnalyzer()]
		self.exts = {}
		for a in self.analyzers:
			for e in a.exts:
				self.exts[e] = a

	def run(self, path, db):
		print 'Indexing path "%s" into file %s:' % (path, db)
		self.walk(path)

	def walk(self, path):
		for dirpath, dirnames, filenames in os.walk(path):
			for f in filenames:
				self.process(os.path.join(dirpath, f))
			for d in dirnames:
				self.walk(os.path.join(dirpath, d))

	def process(self, filename):
		ext = filename.split('.')[-1]
		if ext in self.exts:
			a = self.exts[ext]
			print filename, '...', a.title
			a.run(filename)

	def stats(self):
		for a in self.analyzers:
			print a.title, a.cnt
