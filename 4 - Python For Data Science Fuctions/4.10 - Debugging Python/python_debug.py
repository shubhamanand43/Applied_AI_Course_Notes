#!/usr/local/bin/python
import pdb

#interactive debugging
def seq(n):
    for i in range(n):
	pdb.set_trace()
        print(i)
    return

seq(5)
