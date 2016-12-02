#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import csv
import os
import math
import os.path
import time

# List of lists
amat_all = []

capacities_all = [32, 64, 128, 256, 512, 1024, 2048, 4096]
associativity = 1
block_size_vals = [1, 2, 4, 8, 16, 32] # list of block_size_vals of each capacity
miss_rate_vals = [] # list of miss_rate_vals of each capacity
amat_vals = []

for capacity in capacities_all:
	for block_size in block_size_vals:
		sets = capacity/(associativity * block_size)
		cmd = ('isimp -dcache ' + str(associativity) + ' ' + str(int(math.log(sets, 2))) + ' ' + str(int(math.log((block_size * 4),2))) + ' a.out')
		# print cmd
		os.system(cmd)
		f = open('stats.csv')
		reader = csv.reader(f)
		my_dict = dict(reader)
		miss_rate = float(my_dict['dCacheMissRate'])
		miss_rate_vals.append(miss_rate)
		#Calculate AMAT -- AMAT = (hit time)+(hit rate)(miss penalty)
		amat = 1*(1.0-miss_rate)*(2.0+block_size)	# Assume hit time of 1 cycle, miss penalty of 2 cycles plus one additional cycle/word in block
		amat_vals.append(amat)
		# print "capacity: ", capacity, "miss_rate: ", miss_rate, "block_size: ", block_size
	amat_all.append(amat_vals)
	# Clear lists
	amat_vals = []

# Plotting
for capacity in range(len(capacities_all)):
	x = np.array(block_size_vals)
	y = np.array(amat_all[capacity])
	plt.plot(x, y, '-o')

plt.xscale('log', basex=2)
plt.xlabel('Block Size (words)')
plt.ylabel('AMAT (ns)')
plt.title('AMAT vs. Block Size and Capacity (in words)')
plt.legend(capacities_all)
plt.show()





#
