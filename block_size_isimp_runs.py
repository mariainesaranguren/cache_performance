import numpy as np
import matplotlib.pyplot as plt
import csv
import os
import math
import os.path
import time


block_size_vals = []
miss_rate_vals = []

block_size_all = [] # list of block_size_vals of each capacity
miss_rate_all = [] # list of miss_rate_vals of each capacity
all_capacities = [32, 64]  # , 128, 256, 512, 1024, 2048, 4096

# for capacity in all_capacities:
capacity = 32
# for associativity in 1:
associativity = 1
for block_size in [2, 4, 8, 16, 32]:
    # capacity = associativity * sets * block_size
    sets = capacity/(associativity * block_size)
    cmd = ('isimp -dcache ' +
            str(associativity) + ' ' +
            str(int(math.log(sets, 2))) + ' ' +
            str(int(math.log((block_size * 4),2))) +
            ' a.out')

    print cmd
    os.system(cmd)

    f = open('stats.csv')
    reader = csv.reader(f)
    my_dict = dict(reader)
    miss_rate = float(my_dict['dCacheMissRate'])
    block_size_vals.append(block_size)
    miss_rate_vals.append(miss_rate)
    print "capacity: ", capacity, "miss_rate: ", miss_rate, "block_size: ", block_size

block_size_all.append(block_size_vals)
miss_rate_all.append(miss_rate_vals)


# Plotting
x = np.arange(0, 3 * np.pi, 0.1)
print x
x = block_size_all
print x
y = miss_rate_all
print y
plt.plot(x, y)
plt.xlabel('Block Size (words)')
plt.ylabel('Miss Rate')
plt.title('Miss Rate vs. Block Size and Capacity (in words)')
plt.legend(all_capacities)
plt.show()

# print x
