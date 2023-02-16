from  numpy import random
import numpy as np

# shuffle - change the arrangement of element, change the original array

shf = np.array([1,67,89,34,90])
print("before shuffle:",shf)
random.shuffle(shf)
print("after shuffle:",shf)

""" 
The permutation() method returns a re-arranged array 
and leaves the original array un-changed).
"""
print("\npermutation")
per = np.array([45,78,23,10])
print("before permutation array: ",per)

aft_per = random.permutation(per)
print("after permutation new array:",aft_per)
print("after per.. original array:",per) # no change