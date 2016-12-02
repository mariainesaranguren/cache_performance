# cache_performance

Summary:
This project tests out how different applications perform with different cache organizations by running experiments using SIMP to examine the effects of varying 
the cache configuration on the performance of a matrix multiply algorithm and selection sort.

In order to do this, must have SIMP installed.


How to run it:
Compile with SIMP using -O2 optimization
$mcc -O2 myapp.c mipslib.c	*Replace myapp.c with your application name
Run programs to see plots
$ block_size_isimp_runs.py
$ associativity_isimp_runs.py


