from tables import *
import numpy as np

# open previos file
h5file = open_file("tutorial1.h5", "a")

# file overview
print h5file

# see each node
print 'Nodes'
for node in h5file:
    print node

# see all groups
print 'Groups'
for group in h5file.walk_groups():
    print group

# see all arrays in a tree
print 'Arrays in root'
for group in h5file.walk_groups('/'):
    for array in h5file.list_nodes(group, classname= 'Array'):
        print array
# quick way
for array in h5file.walk_nodes("/", "Array"):
     print(array)

# setting attributes for a table
table = h5file.root.detector.readout
table.attrs.description = 'this is a frequency table'
table.attrs.author = 'rushin'
print 'description: ', table.attrs.description
print 'attributes: ', table.attrs

# detailed description of 'readout'
# h5ls -vr tutorial1.h5/detector/readout

freq_object = h5file.get_node("/detector",'readout')
print 'freq_object: ', freq_object


# reading data from array object
read_obj = freq_object.read()
print read_obj
