# Task:

# I. Write a function that takes an array as input and returns the array in reverse order.

# *Conditions:*

# 1. Do not use built-in functions
# 2. Any programming language

def revert_array(array):
    if(array == None):
        return '"NoneType" object is not iterable'
    
    reverted_array = []
    for i in array:
        reverted_array = [i] + reverted_array
    return reverted_array
