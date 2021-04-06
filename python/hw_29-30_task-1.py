#!/usr/bin/env python3

'''
Task 1
Self-study input() function. Write a script which accepts a sequence of comma-separated numbers from user 
and generate a list and a tuple with those numbers and prints these objects as-is (just print(list) without any formatting).
'''
def gen_list_tuple():
    x = input("Please, input comma-separated numbers:")
    ls = x.split(',')
    print("This is list: {}".format(ls))
    tp=tuple(ls)
    print("This is tuple: {}".format(tp))

gen_list_tuple()
