import subprocess
import sys
import os

import configurator

class Player:
    def __init__(self, filename, args):
        log = os.path.expanduser(configurator.config.get("mplayer", "log"))
        logger = open(log,'w')
            
        command = [configurator.config.get("mplayer", "path")]
        command.append(filename)

        args = args.split(' ')
        command.extend(args)

        p = subprocess.Popen(command, stdout=sys.stdout, stderr=sys.stderr).wait()
        sys.stdout.flush()
        sys.stderr.flush()
