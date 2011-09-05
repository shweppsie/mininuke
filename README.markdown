# Mininuke #

Media Center File Browser

(c) 2010 GNU GPL v3

Author: Nathan Overall

I tried so many media center software 
packages but none met my needs. So I
wrote my own. Tell me if you like it.

# Aims for Mininuke #
*   Simplicity
*   Modular

# Installation #
Mininuke requres Python and Pyglet to run. 

On Debian or Ubuntu run:

    $ apt-get install python python-pyglet

Alternatively get pyglet from [here](http://www.pyglet.org/download.html) 

Finally run ./mininuke

# Configuration #
mininuke will read a config file from 
    ~/.mininuke.rc
of the form below. Below the defaults 
are shown.

    [mininuke]
    path=./
    [mplayer]
    path=/usr/bin/mplayer
    arguments=""

# Thumbnails for files #
mininuke looks for a folder named .thumbs. If it exists it will load thumbnails for files from there.

e.g.

	file = somefile.mp4
	thumbnail = .thumbs/somefile.png

	file = animated/somefile.avi
	thumbnail = .thumbs/animated/somefile.png

#Thumbnails for folders #
mininuke will show an image when you hover over a folder and there is a folder.png image in that folder.
