#!/usr/bin/env python3

'''
Task 6
Create a function that will take a string as an argument and return a dictionary
where keys are symbols from the string and values are the count of inclusion of that symbol.
'''

def return_dict():
    x = input("Please, input a string:")
    ls = list(x)
    dictionary={i:ls.count(i) for i in set(ls)}
    print(dictionary)

return_dict()
