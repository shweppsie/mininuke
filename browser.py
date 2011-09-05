import os
import sys
from Node import Node

class Browser:
	def __init__(self,path):
		self.filter = ['avi','.mkv','divx','wmv','mov','mp4']
		self.path = "./"
		self.root = os.path.expanduser(path)
		if not os.path.isdir(self.root):
			raise IOError('Path does not exist '+self.root)

	def getimage(self,item):
		full_path = os.path.join(self.getpath(), item)
		if os.path.isfile(full_path):
			thumb = self.get_thumb_path()+'/'+item[:item.rfind('.')]+'.png'
			if os.path.exists(thumb):
				return thumb
		elif os.path.isdir(full_path):
			directory = os.path.join(self.root,self.path,item,'folder.png')
			if os.path.exists(directory):
				return directory

	def getpath(self):
		return os.path.join(self.root,self.path)

	def get_thumb_path(self):
		return os.path.join(self.root,'.thumbs',self.path)

	def down(self, node):
		dir = node.getname()
		newpath = os.path.join( self.getpath(),dir )
		if os.path.isdir(newpath):
			self.path = os.path.join( self.path,dir )
		else:
			raise IOError('Path does not exist '+newpath)

	def up(self):
		if not self.path == '/' or not self.path == '' or not self.path == '//':
			self.path = os.path.dirname( self.path )

	def curpath(self):
		return self.path

	def list(self):
		items = os.listdir( self.getpath() )

		nodes = []

		if items > 0:
			for item in items:
				if item.startswith('.'):
					# hidden file
					continue;

				path = os.path.join(self.getpath(),item)

				if os.path.isdir(path):
					# folder
					nodes.append(Node(path,'folder'))
				else:
					# file
					for i in self.filter:
						if item.endswith(i):
							nodes.append(Node(path,'file',self.getimage(item)))
							continue
		
		return nodes

if __name__=="__main__":
	print sys.argv
	if len(sys.argv) != 2:
		print "Usage: browser.py directory"
		exit(1)
	b = Browser(sys.argv[1])
	print b.curpath()
	b.down("tv")
	print b.curpath()
	b.down("American Dad")
	print b.curpath()
	b.down('Season 1')
	print b.curpath()
	b.up()
	print b.curpath()
