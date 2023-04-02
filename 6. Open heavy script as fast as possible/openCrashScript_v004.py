
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



def delViewers():

    for i in nuke.allNodes("Viewer"):
        i.setSelected(True)

    nukescripts.node_delete(popupOnError=True)
    try:
        nuke.selectedNode().setSelected(False)
    except:
        pass


def openscript_onlyRead():
    nuke.scriptClose()
    nuke.scriptOpen()
    delViewers()
    global disabledNodes

    for i in nuke.allNodes("Viewer"):
        i.setSelected(True)

    nukescripts.node_delete(popupOnError=True)
    #nuke.selectedNode().setSelected(False)

 
    disabledNodes = []
    for nodes in allReads():
        for i in nodes:
            if len(i) != 0 and i['disable'].value()==False:
                disabledNodes.append(i.name())
                i['localizationPolicy'].setValue('fromAutoLocalizePath')
                # print (i.name())
                i.setSelected(True)
                i['disable'].setValue(True) 
                i.setSelected(True)

    nuke.tprint("\n"*2)
    nuke.tprint("-----------Disabled Nodes----------")
    nuke.tprint("\n")
    nuke.tprint(disabledNodes)



def openscript_disableAll():
    nuke.scriptClose()
    nuke.scriptOpen()
    delViewers()


    for i in nuke.allNodes():
        i.knob("selected").setValue(False)

    for i in nuke.allNodes():
        # print (i.name())
        try:
            i.setSelected(True)
            i['disable'].setValue(True) 
            i.setSelected(False)
        except:
            pass




def toggle_all_readNodes():


    for i in disabledNodes:
        # print (i)
        nuke.toNode(i).setSelected(True)
        
        try:
                
            if nuke.toNode(i)['disable'].value() == True:
                nuke.toNode(i)['disable'].setValue(False)
            else:
                nuke.toNode(i)['disable'].setValue(True)
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


