"""
Write a generator which can give random values every time
"""
import random
def generate_random_value():
    rad_val = random.randint(0,1000)
    yield f'<{rad_val}>'

for _ in generate_random_value():
    print(_)