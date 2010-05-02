import pyglet
import pyglet.window
from pyglet.window import key
import sys

import browser
import player

WINDOW_HEIGHT=768
WINDOW_WIDTH=1024

window = pyglet.window.Window(WINDOW_WIDTH,WINDOW_HEIGHT)
drawlist = []
selected = 0
keys_pressed = set()

@window.event
def on_key_press (symbol, modifiers):
    keys_pressed.add(key)
    update()

@window.event
def on_key_release (key, modifiers):
    keys_pressed.remove(key)
    update()

def update():
    for i in keys_pressed:
        if i == key.Q:
            sys.exit(0)
        elif i == key.DOWN:
            selected += 1


@window.event
def on_draw():
    window.clear()
    for i in drawlist:
        i[1].draw()

def listfiles(path):
    browse = browser.Browser(path)
    x = 100
    y = WINDOW_HEIGHT - 100
    for i in browse.listdirs():
        if y < 0:
            break
        else:
            label = pyglet.text.Label(i,font_name='Modern',
                                    font_size=13, x=x, y=y, 
                                    #margin_top=5,margin_bottom=5,
                                    color=(255,255,255,255) )
            y -= 40
            drawlist.append((i,label))


#get the list of files to display
listfiles('/home/nathan/')

pyglet.app.run()
