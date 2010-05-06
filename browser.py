import os
import sys

class Browser:
    def __init__(self,path):
        self.path = "/"
        self.root = os.path.expanduser(path)
        if not os.path.isdir(self.root):
            raise IOError('Path does not exist '+self.root)

    def getpath(self):
        return os.path.join(self.root+self.path)

    def isdir(self, path):
        return os.path.isdir(os.path.join(self.getpath(),path))

    def down(self, dir):
        newpath = os.path.join( self.getpath(),dir )
        if os.path.isdir(newpath):
            self.path = os.path.join( self.path,dir )
        else:
            raise IOError('Path does not exist '+newpath)

    def up(self):
        if not self.path == '/' or not self.path == '' or not self.path == '//':
            self.path = os.path.dirname( self.path )

    def curpath(self):
        path = self.path

        if path == '':
            path = '/'
        if path == '/':
            return '/'

        if len(path) > 1:
            if path.startswith('/'):
                path = path[1:]
            if path.endswith('/'):
                path = path[:-1]
        
        path = path.split('/')
        if len(path) > 1:
            if not path[0].startswith('/'):
                path[0] = "/"+path[0]

            for i in xrange(len(path)):
                if not path[i].endswith('/'):
                    path[i] += '/'

        return path

    def list(self):
        files = []
        folders = []

        filter = ['avi','.mkv','divx','wmv','mov']
        nodes = os.listdir( self.getpath() )

        if nodes > 0:
            for a in nodes:
                if os.path.isdir(os.path.join(self.getpath(),a)):
                    folders.append(a)
            folders.sort()

            for a in nodes:
                for i in filter:
                    if a.endswith(i):
                        files.append(a)
            files.sort()
        
        return (files, folders)

if __name__=="__main__":
    print sys.argv
    if len(sys.argv) != 2:
        print "Usage: browser.py directory"
        exit(1)
    b = Browser(sys.argv[1])
    print b.curpath()
    b.down("tv")
    print b.curpath()
    b.down("American Dad")
    print b.curpath()
    b.down('Season 1')
    print b.curpath()
    b.up()
    print b.curpath()
