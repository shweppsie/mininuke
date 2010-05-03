import pyglet

class Selected(pyglet.text.Label):
    def __init__(self, filename,x,y):
        super(Selected, self).__init__(filename, 'Times New Roman', 13, True, False, (255,255,255,255), x, y)
        self.filename = filename

class Video(pyglet.text.Label):
    def __init__(self, filename,x,y):
        super(Video, self).__init__(filename, 'Times New Roman', 13, False, False, (255,255,255,255), x, y)
        self.filename = filename

class Directory(pyglet.text.Label):
    def __init__(self, directory,x,y):
        super(Directory, self).__init__(directory, 'Times New Roman', 13, False, False, (255,255,255,255), x, y)
        self.dir = directory

