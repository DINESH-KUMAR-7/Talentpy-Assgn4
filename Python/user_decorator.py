"""
Create a function perform_n_calls(function, N), inside this function create another
function caller which makes N calls to the function which is coming as a first
parameter to perform_n_calls function. Create another py file and create a function
console() which prints “TalentpY”. Now, your job is to import perform_n_calls and use
it as a decorator to console function in order to print “TalentpY” N times, where N
ranges from 1 to any. (Hint: Use decorator feature)
"""
#decorator function.
def perform_n_calls(function):
    def wrap(*args):
        for _ in range(*args):
             function(*args)
    return wrap
