"""
Write a simple generator which can give prime numbers from range 1 to 5000.
"""

def gen_fun(start,end=5000):
    for i in range(start,end+1):
        if i>1:
            #checking number%2...same_number (i)times..
            for _ in range(2, i):
                if (i % _) == 0:
                    break
                #break is neccessaty bcuz it will run the yeild i times..
                else:
                    yield f'{i}is a prime'
                    break

#for is used bcuz its a generator
#by for only we can get the output
for _ in gen_fun(1,5000):
    print(_)
