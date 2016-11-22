import csv
import os

associativity = 2
log2_sets = 5
log2_bytes_per_block = 4

cmd = ('isimp -dcache ' +
        str(associativity) + ' ' +
        str(log2_sets) + ' ' +
        str(log2_bytes_per_block) +
        ' a.out')
print cmd
os.system(cmd)

f = open('stats.csv')
reader = csv.reader(f)
my_dict = dict(reader)
miss_rate = float(my_dict['dCacheMissRate'])
print miss_rate
