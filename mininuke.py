#!/usr/bin/env python

import pyglet
import pyglet.window
from pyglet.window import key
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
selected = 0
keys_pressed = set()
nodes = []

def fillnodes():
    global nodes
    nodes = []
    (files,folders) = browse.list()
    for i in folders:
        nodes.append((i,False))
    for i in files:
        nodes.append((i,True))

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

def doitem(path):
    if browse.isdir(path):
        selected = 0
        browse.down(path)
        (files,folders) = browse.list()
    else:
        filename = os.path.join(browse.getpath(),nodes[selected][0])
        args = configurator.config.get("mplayer", "arguments")
        player.Player(configurator.config.get("mplayer", "path"), filename, args, configurator.config.get("mplayer", "log"))


@window.event
def on_key_press (symbol, modifiers):
    global selected,keys_pressed
    if symbol == key.ENTER:
        if selected < len(nodes): # there must be files in this folder
            if not nodes[selected][1]:
                selected = 0
                browse.down(nodes[selected][0])
                fillnodes()
            else:
                filename = os.path.join(browse.getpath(),nodes[selected][0])
                args = configurator.config.get("mplayer", "arguments")
                
                window.set_exclusive_mouse(False)
                window.set_fullscreen(False)
                player.Player(filename, args, configurator.config.get("mplayer", "log"))
                window.set_fullscreen(True)
                window.set_exclusive_mouse(True)
                window.activate()

                #ensure no more keypreses will be processed
                keys_pressed = set() 
                return
    elif symbol == key.BACKSPACE:
        browse.up()
        fillnodes()
        return
    elif symbol == key.Q or symbol == key.UP or symbol == key.DOWN:
        keys_pressed.add(symbol)

@window.event
def on_key_release (symbol, modifiers):
    if symbol in keys_pressed:
        keys_pressed.remove(symbol)
    keys_update()

@window.event
def on_draw():
    keys_update()
    window.clear()
    
    x = 100
    y = window.height/2 + (selected * 40)
    for i in xrange(len(nodes)):
        if y > window.height/3 and y < (window.height/3)*2:
            if i is selected:
                label = labels.Selected(nodes[i][0],x,y)
            else:
                label = labels.Item(nodes[i][0],x,y)
            label.draw()
        y -= 40
    
    title = labels.Title('MININUKE', x=window.width/2-80, y=window.height-60)
    title.set_style('background_color', (0,0,0,255))
    title.draw()
    labels.Footnote('* indicates folders', x=window.width-225, y=20).draw()

fillnodes()
pyglet.app.run()

