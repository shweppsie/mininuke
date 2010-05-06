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

window = pyglet.window.Window(1024,768)
browse = browser.Browser(configurator.config.get("mininuke", "path"))
selected = 0
keys_pressed = set()
nodes = []

def keys_update():
    global selected,nodes
    for i in keys_pressed:
        if i == key.Q:
            pyglet.app.exit() # q quits the program as does escape
        if i == key.DOWN:
            if selected < len(nodes)-1:
                selected += 1
        if i == key.UP:
            if selected > 0:
                selected -= 1
        if i == key.ENTER:
            if selected < len(nodes): # there must be files in this folder
                path = nodes[selected][:-1]
                if browse.isdir(path):
                    selected = 0
                    browse.down(path)
                    nodes = browse.list()
                else:
                    filename = os.path.join(browse.getpath(),nodes[selected])
                    args = configurator.config.get("mplayer", "arguments")
                    player.Player(filename, args, configurator.config.get("mplayer", "log"))
        if i == key.BACKSPACE:
            browse.up()
            nodes = browse.list()


@window.event
def on_key_press (symbol, modifiers):
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
        if y > 200 and y < 550:
            if i is selected:
                label = labels.Selected(nodes[i],x,y)
            else:
                label = labels.Item(nodes[i],x,y)
            label.draw()
        y -= 40
    
    title = labels.Title('MININUKE', x=window.width/2-80, y=window.height-60)
    title.set_style('background_color', (0,0,0,255))
    title.draw()
    labels.Footnote('* indicates folders', x=window.width-225, y=20).draw()

nodes = browse.list()

pyglet.app.run()

