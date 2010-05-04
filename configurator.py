import ConfigParser
import os

config=ConfigParser.RawConfigParser()

def readconfig():
    config.add_section("mininuke")
    config.set("mininuke","path","./")
    
    config.add_section("mplayer")
    config.set("mplayer","arguments","")
    config.set("mplayer","log","~/.mininuke.mplayer.log")

    config.read(os.path.expanduser("~/.mininuke.rc"))

if __name__=="__main__":
    readconfig()
    for section in config.sections():
        print "Section",section
        for option in config.options(section):
            print "",option,config.get(section,option)
else:
    readconfig()
