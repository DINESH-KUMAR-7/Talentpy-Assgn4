"""
Write python script to add elements of list L using reduce() function.
"""
from functools import reduce

List = [1,2,3,45,4,55.97,81,27]
#reduce function accepts 2arg-function so we can add the list easily.
red_fun = reduce(lambda x,y:x+y , List)
print(red_fun)
