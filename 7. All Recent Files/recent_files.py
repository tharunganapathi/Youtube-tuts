import nuke
import os
import sys

def recent_files():
	user = os.path.expanduser('~')
	dot_nuke = user + '\.nuke'

	recent_files = os.path.abspath(os.path.join(dot_nuke,'recent_files') )


	text = open(recent_files,"r")
	recentFile_list = (text.read())
	print (recentFile_list)


	p = nuke.Panel('RecentFiles v1.0')
	p.addEnumerationPulldown('Open Recent Files', recentFile_list)

	if p.show():
	    nuke.scriptOpen(p.value('Open Recent Files'))


nuke.menu('Nuke').addMenu('TG').addCommand('Open Recent Files', recent_files)
