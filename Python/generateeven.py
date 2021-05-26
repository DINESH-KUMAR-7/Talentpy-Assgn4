"""
 Write a generator to get even numbers from 1 to infinity.
"""
def gen_fun():
    i=1
    while(True):
        if i%2==0:
            yield f'{i}is even'
        i=i+1

for _ in gen_fun():
    print(_)
