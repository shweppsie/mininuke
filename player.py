import subprocess
import sys

class Player:
    def __init__(self, args):
        command = ["/usr/bin/mplayer"]
        command.extend(args)
        p = subprocess.Popen(command, stdout=sys.stdout, stderr=sys.stderr).wait()
        sys.stdout.flush()
        sys.stderr.flush()

if __name__=="__main__":
    p = Player(["/media/mount/videos/tv/The New Yankee Workshop/Season 14/0201 mitre bench and storage part 1.divx"])
