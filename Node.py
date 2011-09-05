import os

class Node:
	def __init__(self,filename,kind,imagefile=None):
		self.kind = kind
		self.imagefile = imagefile
		self.image = None
		if kind is 'folder':
			# full folder path
			self.filename = filename
			# folder name
			self.name = os.path.basename(filename)
		elif kind is 'file':
			# filename including path and extension
			self.filename = filename
			# just the name of the file
			self.name = os.path.splitext(os.path.basename(filename))[0]

	def __repr__(self):
		return self.name

	def __str__(self):
		return self.name

	def getname(self):
		return self.name

	def gettype(self):
		return self.kind

	def getfilename(self):
		return self.filename

	def getimagefile(self):
		return self.imagefile
	
	def setimage(self,image):
		self.image = image

	def getimage(self):
		return self.image

