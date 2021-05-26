"""
Write a function called is_unique. This function should take a string and should check
whether all characters of the string is unique/not. Example: If the input string is
“abcd”, all characters are unique, hence it should return True. Another example, if the
string is “abaa”, then this function should return False.
1. Create a List L of size 10 with random strings of length > 1.
2. Write a python snippet to check is_unique nature for all elements of L. (Hint:
Use map function)
3. Apply filter function, to get only unique elements from L.
"""

def is_unique(i):
    val_str = set(i)
    return len(val_str) == len(i)


L = ["shin","aada","adbc","aaaa","ytpe","boss","fan","luck","dog","hint"]

map_fun = map(is_unique,L)
print(list(map_fun))
fil_fun = filter(is_unique,L)
print(list(fil_fun))
