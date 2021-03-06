import pyglet

font_name = 'Helvetica'
font_size = 20

class Title(pyglet.text.Label):
    def __init__(self, filename,x,y):
        super(Title, self).__init__(filename, font_name, 25, True, False, (200,255,255,255), x, y)

class Path(pyglet.text.Label):
    def __init__(self, filename,x,y):
        super(Path, self).__init__(filename, font_name, 25, True, False, (255,255,255,255), x, y)

class File(pyglet.text.Label):
    def __init__(self, directory,x,y):
        super(File, self).__init__(directory, font_name, font_size, False,True, (0,255,0,255), x, y)

class Folder(pyglet.text.Label):
    def __init__(self, directory,x,y):
        super(Folder, self).__init__(directory, font_name, font_size, False,True, (0,100,255,255), x, y)
