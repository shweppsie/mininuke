#!/usr/bin/env python

import pyglet
import pyglet.window
from pyglet.window import key

from operator import itemgetter
import sys
import os
import optparse

import browser
import player
import labels
import configurator

window = pyglet.window.Window(fullscreen=True)
window.set_exclusive_mouse(True)

browse = browser.Browser(configurator.config.get("mininuke", "path"))
keys_pressed = set()
selected = 0
nodes = []
image = None

def update_image():
	global image
	if len(nodes)>selected:
		imgpath = browse.getimage(nodes[selected][0])
		if imgpath != None:
			try:
				image = pyglet.image.load(imgpath)
			except:
				print "Corrupt Image: %s" % imgpath
				image = None
		else:
			image = None
	else:
		image = None

#updates the list of nodes (files and directories)
def fillnodes():
	global nodes
	nodes = []
	(files,folders) = browse.list()
	for i in folders:
		nodes.append((i,False))
	for i in files:
		nodes.append((i,True))
	nodes = sorted(nodes, key=itemgetter(0))

#keys that have action when held down go here
def keys_update():
	global selected,files,folders,keys_pressed
	for i in keys_pressed:
		if i == key.Q:
			pyglet.app.exit() # q quits the program as does escape
		if i == key.DOWN:
			if selected < len(nodes)-1:
				selected += 1
				update_image()
		if i == key.UP:
			if selected > 0:
				selected -= 1
				update_image()
		#page down and up take you to the next and previous character
		if i == key.PAGEDOWN:
			char = nodes[selected][0][0]
			while selected + 1 < len(nodes):
				selected += 1
				if nodes[selected][0][0] != char:
					update_image()
					break
		if i == key.PAGEUP:
			char = nodes[selected][0][0]
			while selected - 1 >= 0:
				selected -= 1
				if nodes[selected][0][0] != char:
					update_image()
					break
		if i == key.HOME:
			selected = 0
		if i == key.END:
			selected = len(nodes)-1

#select current item
def doitem(node):
	global selected
	if not node[1]:
		#directory
		browse.down(node[0])
		selected = 0
		fillnodes()
	else:
		#file
		window.set_exclusive_mouse(False)
		window.set_fullscreen(False)
		player.Player(os.path.join(browse.getpath(),node[0]), configurator.config.get("mplayer", "arguments"), configurator.config.get("mplayer", "log"))
		window.set_fullscreen(True)
		window.set_exclusive_mouse(True)
		window.activate()
	
		#ensure no more keypreses will be processed
		keys_pressed = set() 
		return

#key press event
@window.event
def on_key_press (symbol, modifiers):
	global selected,keys_pressed
	if symbol == key.ENTER or symbol == key.RIGHT:
		if selected < len(nodes): # there must be files in this folder
			doitem(nodes[selected])
			update_image()
	elif symbol == key.BACKSPACE or symbol == key.LEFT:
		selected = 0
		browse.up()
		fillnodes()
		update_image()
		return
	else:
		keys_pressed.add(symbol)

#unmark held down keys
@window.event
def on_key_release (symbol, modifiers):
	if symbol in keys_pressed:
		keys_pressed.remove(symbol)
	keys_update()

#draw method
@window.event
def on_draw():
	keys_update()
	window.clear()
	
	x = 100
	y = (selected * 40) + (window.height/2)
	#y = (window.height/2) - (selected * 40)
	for i in xrange(len(nodes)):
		if y > 100 and y < (window.height-160):
			if nodes[i][1]:
				label = labels.File(nodes[i][0],x,y)
			else:
				label = labels.Folder(nodes[i][0],x,y)
			if i is selected:
				label.set_style('bold',True)
				label.set_style('italic',False)
				label.font_size += 5
			label.draw()
		y -= 40
	
	title = labels.Title('MININUKE', x=window.width/2-80, y=(window.height-60) )
	title.set_style('background_color', (0,0,0,255))
	title.draw()
	labels.Path(browse.curpath(), x=x, y=(window.height-120)).draw()
	if image != None:
			image.blit((window.width/3)*2-image.width/2, window.height/2-image.height/2, 0)

fillnodes()
pyglet.app.run()

