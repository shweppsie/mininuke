import cocos
import pyglet
import sys

import browser
import player

WINDOW_HEIGHT=768
WINDOW_WIDTH=1024

#browse = browser.Browser('/mnt/zoidberg/shared/videos/movies-other/')
browse = browser.Browser('/home/nathan/')

class Background(cocos.layer.util_layers.ColorLayer):
    def __init__(self):
        super( Background, self).__init__(255,255,255,255)

        sprite = cocos.sprite.Sprite('logo.png')

        x = WINDOW_WIDTH-sprite.image.width
        y = WINDOW_HEIGHT-(sprite.image.height/2)
        sprite.position = (x,y)
        
        sprite.image_anchor_x = 0
        sprite.image_anchor_Y = 0

        self.add( sprite )

class Events(cocos.layer.Layer):
    is_event_handler = True
    def __init__(self):
        super( Events, self).__init__()

        #a list to store pressed keys in
        self.keys_pressed = set()

    def on_mouse_press(self, x, y, buttons, modifiers):
        print "(%s,%s)" % (x,y)
        print "(%s,%s)" % cocos.director.director.get_virtual_coordinates(x,y)

    def on_key_press (self, key, modifiers):
        #pressing q quits the program
        self.keys_pressed.add(key)
        self.update()

    def on_key_release (self, key, modifiers):
        self.keys_pressed.remove(key)
        self.update()

    def update(self):
        """Deal with all currently pressed keys"""
        key_names = [pyglet.window.key.symbol_string (k) for k in self.keys_pressed]
        if 'Q' in key_names:
            sys.exit(0)
        print key_names

class Menu(cocos.layer.Layer):
    def __init__(self):
        super( Menu, self).__init__()
        
        x = 10
        y = WINDOW_HEIGHT - 100
        for i in browse.listdirs():
            #label = cocos.text.Label(i,font_name='Helvetica',font_size=16, x=100, y=ycoord, color=(0,0,0,255) )
            i = "<H2>"+i+"</H2>"
            label = cocos.text.HTMLLabel(i,(x,y))
            if y <= 0:
                break
            else:
                y -= 40
            self.add(label)


if __name__ == "__main__":
    cocos.director.director.init(width=WINDOW_WIDTH,height=WINDOW_HEIGHT,resizable=False,caption="MiniNuke Media Center")
    
    cocos.director.director.run(cocos.scene.Scene( Background(),Events(),Menu() ))
