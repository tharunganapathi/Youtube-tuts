import nuke

node = nuke.root()

def delAllKnobs():

	for i in range(2):
		for i in node.allKnobs():
			try:
				node.removeKnob(node[i.name()])
			except:
				pass


nuke.addOnDestroy(delAllKnobs)