
import nuke
import nukescripts



def toggle_disable():

    if len(nuke.selectedNodes()) == 0:
        nuke.message("Please select the nodes")

    else:
        for i in nuke.selectedNodes():
            try:
                #print i.name()
                    
                if i['disable'].value() == True:
                    i['disable'].setValue(False)
                else:
                    i['disable'].setValue(True)
            except:
                pass


def toggle_selection():

    if len(nuke.selectedNodes()) == 0:
        nuke.selectAll()

    else:
    	nuke.invertSelection()

            
nuke.menu('Nuke').addMenu('TG').addCommand('toggle/toggle_disable', toggle_disable, 'Shift+D')
nuke.menu('Nuke').addMenu('TG').addCommand('toggle/toggle_selection', toggle_selection, 'Shift+A')