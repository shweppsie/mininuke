import pyglet

font_name = 'Helvetica'
font_size = 20

class Title(pyglet.text.Label):
    def __init__(self, filename,x,y):
        super(Title, self).__init__(filename, font_name, 25, True, False, (200,255,255,255), x, y)

class Footnote(pyglet.text.Label):
    def __init__(self, filename,x,y):
        super(Footnote, self).__init__(filename, font_name, 12, False, False, (255,255,255,255), x, y)

class File(pyglet.text.Label):
    def __init__(self, directory,x,y):
        super(File, self).__init__(directory, font_name, font_size, False,True, (255,255,255,255), x, y)

class Folder(pyglet.text.Label):
    def __init__(self, directory,x,y):
        super(Folder, self).__init__(directory, font_name, font_size, False,True, (0,0,255,255), x, y)
