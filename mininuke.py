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
        if i == key.UP:
            if selected > 0:
                selected -= 1

def setimage():
    global image
    imagepath = browse.getimage()
    if os.path.exists(imagepath):
        #directory has an image
        image = pyglet.image.load(imagepath)
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2
    else:
        image = None

#select current item
def doitem(node):
    global selected
    if not node[1]:
        #directory
        browse.down(node[0])
        selected = 0
        fillnodes()
        setimage()
    else:
        #file
        window.set_exclusive_mouse(False)
        window.set_fullscreen(False)
        player.Player(filename, args, configurator.config.get("mplayer", "log"))
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
    if symbol == key.ENTER:
        if selected < len(nodes): # there must be files in this folder
            doitem(nodes[selected])
    elif symbol == key.BACKSPACE:
        browse.up()
        fillnodes()
        setimage()
        return
    elif symbol == key.Q or symbol == key.UP or symbol == key.DOWN:
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
    y = window.height/4 + (selected * 40)
    for i in xrange(len(nodes)):
        if y > 100 and y < window.height / 2.5:
            if nodes[i][1]:
                label = labels.File(nodes[i][0],x,y)
            else:
                label = labels.Folder(nodes[i][0],x,y)
            if i is selected:
                label.set_style('bold',True)
                label.set_style('italic',False)
                label.font_size += 2
            label.draw()
        y -= 40
    
    title = labels.Title('MININUKE', x=window.width/2-80, y=(window.height-60) )
    title.set_style('background_color', (0,0,0,255))
    title.draw()
    labels.Path(browse.curpath(), x=x, y=(window.height/2.5)).draw()
    if image != None:
        image.blit( (window.width/2) , (window.height-image.height) )

fillnodes()
pyglet.app.run()

