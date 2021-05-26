"""
 Write a list comprehension to find factorial of each numbers in a given list L if and only
    if the numbers are even. For Example: If L = [1,2,3,4] then output should be [2, 24].
"""
import math
List = [1,2,3,4,5,6,7,8]
list_fact = []
#Method1: using math
fact_of_even = [ math.factorial(val) for val in List if val%2==0]
print(fact_of_even)

def recur_fact(n):
   if n == 1:
       return n
   else:
       return n*recur_fact(n-1)
#Method2: using basic operation

fact = [recur_fact(i) for i in List if i%2==0 ]
print(fact)
