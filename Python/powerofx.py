"""
Create a lambda function which takes two inputs X and Y and performs X power Y
operation and returns the output. For Example: If X is 2 and Y is 3, then 2 power 3 = 2
* 2 * 2 = 8.
"""

lam_func = lambda X,Y: X**Y
X=int(input("X INput:"))
Y=int(input("Y INput:"))
print(X,"^",Y,"=",lam_func(X,Y))
