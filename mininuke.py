import pyglet
import pyglet.window
from pyglet.window import key
import sys
import os

import browser
import player
import labels

window = pyglet.window.Window(1024,768)
browse = browser.Browser('/home/nathan/tv')
selected = 0
keys_pressed = set()
stuff = []

def update_list():
    global stuff
    stuff = browse.list()

@window.event
def on_key_press (symbol, modifiers):
    keys_pressed.add(symbol)
    keys_update()

@window.event
def on_key_release (symbol, modifiers):
    if symbol in keys_pressed:
        keys_pressed.remove(symbol)
    keys_update()

def keys_update():
    global selected
    for i in keys_pressed:
        if i == key.Q:
            pyglet.app.exit()
        if i == key.DOWN:
            if selected < len(stuff)-1:
                selected += 1
        if i == key.UP:
            if selected > 0:
                selected -= 1
        if i == key.ENTER:
            path = stuff[selected]
            if browse.isdir(path):
                browse.down(path)
                update_list()
            else:
                player.Player((os.path.join(browse.getpath(),path),))
        if i == key.BACKSPACE:
            browse.up()
            update_list()

@window.event
def on_draw():
    window.clear()
    for i in listfiles():
        i.draw()

def listfiles():
    drawlist = []
    x = 100
    y = window.height - 100
    for i in xrange(len(stuff)):
        if y < 0:
            break
        else:
            if i is selected:
                label = labels.Selected(stuff[i],x,y)
            else:
                label = labels.Directory(stuff[i],x,y)
            y -= 40
            drawlist.append(label)
    return drawlist

update_list()

pyglet.app.run()

