node = nuke.selectedNode()
read = node['file'].value().split('/')[-1].split('.')[0]
print read
frame_range = str(node['first'].value()) + '-' + str(node['last'].value())
total_frames = str(node['last'].value() - node['first'].value() + 1)
print (total_frames)

tab_knob = nuke.Tab_Knob(read)
file_knob = nuke.String_Knob('file','file')
frame_range_knob = nuke.String_Knob('frame_range','frame_range')
total_frames_knob = nuke.String_Knob('total_frames','total_frames')

root = nuke.root()


try:
    nuke.root()[read]

except:
    root.addKnob(tab_knob)


try:
    nuke.root()['file']

except:
    root.addKnob(file_knob)

try:
    nuke.root()['frame_range']

except:
    root.addKnob(frame_range_knob)

try:
    nuke.root()['total_frames']

except:
    root.addKnob(total_frames_knob)



nuke.root()['file'].setValue(node['file'].value())
nuke.root()['frame_range'].setValue(frame_range)
nuke.root()['total_frames'].setValue(total_frames)

nuke.root()['file'].setEnabled(False)
nuke.root()['frame_range'].setEnabled(False)
nuke.root()['total_frames'].setEnabled(False)