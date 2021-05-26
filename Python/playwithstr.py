"""
Create three functions as follows -
1. def remove_vowels(string) - which will remove all vowels from the given
string. For example if the string given is “aeiru”, then the return value should
be ‘r’
2. def remove_consonants(string) - which will remove all consonants from
given string. For example, if the string given is “aeri”, then the return value
should be ‘aei’.
3. def caller -> This function should 2 parameters
1. Function to call
2. String argument
This caller function should call the function passed as a parameter, by
passing second parameter as the input for the function. Example: caller(remove_vowles,
“aeiru”) should call remove_vowels function and should return ‘r’ as the output.
"""
def caller(func,string):

    result = func(string)
    return result

def remove_vowels(string):

    #using list join method vowels are removed and other words are stored
    up_str ="".join([word for word in string if word not in 'aeiouAEIOU'])
    return up_str

def remove_consonants(string):

    #using list join method , vowels in string are collected and stored
    # at update_str
    update_str ="".join([word for word in string if word in 'aeiouAEIOU'])
    return update_str


print(caller(remove_vowels,"aeiru"))
print(caller(remove_consonants,"aeiru"))