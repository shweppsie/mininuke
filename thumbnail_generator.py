#!/usr/bin/python

from vc import VerboseControl
import sys
import os
import subprocess
import argparse

def generate_thumbnail(root,f):
	formats = ['.avi','.mp4','.mkv','.mov','.wmv','.divx','.m4v','.mpg','.iso','.flv']

	for i in xrange(len(formats)):
		if not f.endswith(formats[i]):
			if (len(formats)-1) == i:
				print "INFO: unsupported format"
				return
		else:
			break
	
	thumb = os.path.join(root+'.thumbs',f)
	thumb = thumb[:thumb.rfind('.')] + '.png'
	folder = thumb[:thumb.rfind('/')]

	f = os.path.join(root,f)

	if not os.path.exists(folder):
		os.mkdir(folder)
	
	if not os.path.exists(thumb):
		print "%s: thumbnail does not exist. creating..." % f
		args = ['/usr/local/bin/ffmpegthumbnailer', '-i', f, '-o', thumb, '-s', '512']
		try:
			output = subprocess.Popen(args, stderr=subprocess.PIPE).communicate()[0]
		except:
			if os.path.exists(thumb):
				os.remove(thumb)
			raise
		if output is not None:
			sys.stderr.write("ERROR: %s" % output)

	print "SUCCESS: %s" % f

parser = argparse.ArgumentParser()
parser.add_argument('-q','--quiet',action='store_true',default=False,help="Only output on errors")
parser.add_argument('-d','--debug',action='store_true',default=False,help="Enable debug mode")
parser.add_argument('-r','--recursive',action='store_true',default=False,
			help="Recursively look for files in folders")
parser.add_argument('root',metavar='ROOT',help="Root directory to work from")
parser.add_argument('folders',metavar='FOLDER',nargs='+',
			help="Folders to generate thumbnails for. Must be relative to the root folder")
args = parser.parse_args()
root = os.path.abspath(args.root)

if args.quiet:
	VerboseControl(0)
elif args.debug:
	VerboseControl(5)
else:
	VerboseControl(3)

for folder in args.folders:
	if args.recursive:
		for (base,folders,files) in os.walk(folder):
			for f in files:
				f = os.path.join(base,f)
				print "INFO: processing %s" % f
				generate_thumbnail(root,f)
	else:
		for f in os.listdir(folder):
			f = os.path.join(folder,f)
			print "INFO: processing %s" % f
			if os.path.isfile(f):
				generate_thumbnail(f)
