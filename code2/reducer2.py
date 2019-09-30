#!/usr/bin/python

import sys

total_value = 0
old_key = None

for line in sys.stdin:
    mapped_data = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue
    
    this_key, this_value = mapped_data

    if old_key is not None and old_key != this_key:
        print "{0}\t{1}".format(old_key, total_value)
        
        old_key = this_key
        total_value = 0
    else:
        old_key = this_key
        total_value += float(this_value)

# Print last value
if old_key is not None:
    print "{0}\t{1}".format(old_key, total_value)