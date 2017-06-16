from tables import *
import numpy as np
from random import *

class Freq(IsDescription):
    freq_id = Int64Col()
    freq_1 = Int64Col()
    freq_2 = Int64Col()
    freq_3 = Int64Col()

#creates a pytable file
h5file = open_file("tutorial1.h5", mode = "w", title = "Test file")

#create a group named 'detector' that branches from root node
# "/" means root object
group = h5file.create_group("/", 'detector', 'Detector information')


# create a new table
# "readout example" = table title
# "readout " = node name
table = h5file.create_table(group, 'readout', Freq, "Readout example")

# get pointer to a row from create 'table'
freq = table.row

# insert values
for i in xrange(10):
    freq['freq_id'] = i
    freq['freq_1'] = randint(0,100)
    freq['freq_2'] = randint(0,100)
    freq['freq_3'] = randint(0,100)
    freq.append()

# flush the table
# flushing a table is a very important step
# as it will not only help to maintain the
# integrity of your file, but also will free valuable memory resources
table.flush()


# access the data
table = h5file.root.detector.readout
freq_1_values = [x['freq_1'] for x in table.iterrows() if (x['freq_1'] > 50) & (x['freq_1'] <= 90)]
print 'values of freq_1 are: ',freq_1_values

# more powerful ways of performing selections
# which may be more suitable if you have very
# large tables or if you need very high query
# speeds. They are called in-kernel and indexed
# queries, and you can use them through Table.where()
names = [ x['freq_id'] for x in table.where("""( freq_1 > 50) & (freq_1 <= 90)""") ]
print 'freq_id: ', names


# close the file
h5file.close()

# read file
# h5ls -rd tutorial1.h5
