#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import csv
import os
import math
import os.path
import time

# List of lists
miss_rate_all = []

capacities_all = [32, 64, 128, 256, 512, 1024, 2048, 4096]
associativity = 1
block_size_vals = [1, 2, 4, 8, 16, 32] # list of block_size_vals of each capacity
miss_rate_vals = [] # list of miss_rate_vals of each capacity

for capacity in capacities_all:
	for block_size in block_size_vals:
		sets = capacity/(associativity * block_size)
		print "capacity: ", capacity
		cmd = ('isimp -dcache ' + str(associativity) + ' ' + str(int(math.log(sets, 2))) + ' ' + str(int(math.log((block_size * 4),2))) + ' a.out')
		# print cmd
		os.system(cmd)
		f = open('stats.csv')
		reader = csv.reader(f)
		my_dict = dict(reader)
		miss_rate = float(my_dict['dCacheMissRate'])
		miss_rate_vals.append(miss_rate)
		# print "capacity: ", capacity, "miss_rate: ", miss_rate, "block_size: ", block_size
	miss_rate_all.append(miss_rate_vals)
	# Clear lists
	miss_rate_vals = []
	# Put results into list of list
	# block_size_all.append(block_size_vals)

# Plotting
for capacity in range(len(capacities_all)):
	x = np.array(block_size_vals)
	print x
	y = np.array(miss_rate_all[capacity])
	print y
	plt.plot(x, y, '-o')

plt.xscale('log', basex=2)
plt.xlabel('Block Size (words)')
plt.ylabel('Miss Rate')
plt.title('Miss Rate vs. Block Size and Capacity (in words)')
plt.legend(capacities_all)
plt.show()





#
