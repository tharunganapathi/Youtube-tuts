import nuke
node = nuke.selectedNode()
frame_range = str(node['first'].value()) + '-' + str(node['last'].value())
total_frames = str(node['last'].value() - node['first'].value() + 1)


string = {
'frame_range'   :  frame_range,
'total_frames'  :  total_frames
}

root = eval(str(string))


import json
nuke.root()['label'].setValue(json.dumps(root, indent = 0))
nuke.root()['label'].setEnabled(False)
