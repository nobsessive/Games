import numpy as np
def add(a):
    return a+a
def add2(a):
    return a+a+a

li=[add, add2]
for i in li:
    print(i(1))