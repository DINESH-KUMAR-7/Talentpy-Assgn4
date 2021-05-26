"""
Write python recursive function to perform multiplication of all elements of list L.
"""
from functools import reduce

lam = lambda x,y:x*y
list_of_elements = [1,23,45,667,8,9,23,77,234,4]

#reduce - used to trim the list
mul = reduce(lam,list_of_elements)
print(mul)