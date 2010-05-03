import subprocess
import sys
import os

import configurator

class Player:
    def __init__(self, filename, args, log):
        
        log = os.path.expanduser(log)
        logger = open(log,'w')
            
        command = ["/usr/bin/mplayer"]
        command.append(filename)

        args = args.split(' ')
        command.extend(args)

        p = subprocess.Popen(command, stdout=logger, stderr=logger).wait()
        sys.stdout.flush()
        sys.stderr.flush()
