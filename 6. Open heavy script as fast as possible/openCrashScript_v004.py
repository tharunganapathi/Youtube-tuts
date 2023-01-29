
import nuke
import nukescripts



# allReads = [nuke.allNodes('DeepRead'),
#             nuke.allNodes('ReadGeo'),
#             nuke.allNodes('ReadGeo2'),
#             nuke.allNodes('Read')]



def allReads():

    allReads = [nuke.allNodes('DeepRead'),
                nuke.allNodes('ReadGeo'),
                nuke.allNodes('ReadGeo2'),
                nuke.allNodes('Read'),
                nuke.allNodes('Constant'),
                nuke.allNodes('Camera'),
                nuke.allNodes('Camera2'),
                nuke.allNodes('Camera3'),  # Nuke 13
                nuke.allNodes('Camera4')   # Nuke 14
                ]

    return allReads


def openscript_onlyRead():
    nuke.scriptClose()
    nuke.scriptOpen()


 

    for nodes in allReads():
        for i in nodes:
            print (i.name())
            i.setSelected(True)
            i['disable'].setValue(True) 
            i.setSelected(True)



def openscript_disableAll():
    nuke.scriptClose()
    nuke.scriptOpen()


    for i in nuke.allNodes():
        i.knob("selected").setValue(False)

    for i in nuke.allNodes():
        print (i.name())
        try:
            i.setSelected(True)
            i['disable'].setValue(True) 
            i.setSelected(False)
        except:
            pass




def toggle_all_readNodes():


    for nodes in allReads():
        for i in nodes:
            print (i.name())
            i.setSelected(True)
            
            try:
                    
                if i['disable'].value() == True:
                    i['disable'].setValue(False)
                else:
                    i['disable'].setValue(True)
            except:
                pass


def toggle_all_nodes():

    if len(nuke.selectedNodes()) == 0:
        nuke.message("Please select the nodes")

    else:
        for i in nuke.selectedNodes():
            try:
                if i['disable'].value() == True:
                    i['disable'].setValue(False)
                else:
                    i['disable'].setValue(True)
            except:
                pass





nuke.menu('Nuke').addMenu('TG').addCommand('Openscript/by disabling all "Read" inputs', openscript_onlyRead)
nuke.menu('Nuke').addMenu('TG').addCommand('Openscript/by disabling all nodes', openscript_disableAll)
nuke.menu('Nuke').addMenu('TG').addCommand('Toggle/Toggle all "Read" inputs', toggle_all_readNodes, 'Shift+R')
nuke.menu('Nuke').addMenu('TG').addCommand('Toggle/Toggle all Nodes', toggle_all_nodes, 'Shift+D')


