import os

class Browser:
    def __init__(self,path):
        #remove white space
        self.path = ""
        self.root = os.path.abspath(path)

    def down(self, dir):
        path = os.path.join(self.root,self.path)
        if os.path.isdir(os.path.join(path,dir)):
            self.path = os.path.join(self.path,dir)

    def up(self):
        self.path = os.path.dirname(self.path)

    def curpath(self):
        path = self.path
        
        if path.startswith('/'):
            path = path[1:]
        if path.endswith('/'):
            path = path[:-1]
        path = path.split('/')
        if len(path) > 0:
            if not path[0].startswith('/'):
                path[0] = "/"+path[0]
            if not path[len(path)-1].endswith('/'):
                path[len(path)-1] += '/'

        return path

    def listdirs(self):
        path = os.path.join(self.root,self.path)
        files = os.listdir(path)
        dirs = []
        for i in files:
            if os.path.isdir(os.path.join(path,i)):
                dirs.append(i)
        return sorted(dirs)

    def listvids(self):
        filter = ['avi','.mkv','divx','wmv']
        files = os.listdir(os.path.join(self.root,self.path))
        videos = []
        for a in files:
            for i in filter:
                if a.endswith(i):
                    videos.append(a)
        return sorted(videos)

if __name__=="__main__":
    b = Browser('/media/mount/videos/')
    print b.curpath()
    b.down("tv")
    print b.curpath()
    #print b.listdirs()
    b.down("American Dad")
    print b.curpath()
    #print b.listdirs()
    b.down('Season 1')
    print b.curpath()
    #print b.listvids()
