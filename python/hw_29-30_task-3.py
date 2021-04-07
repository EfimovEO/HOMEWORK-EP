#!/usr/bin/env python3

'''
Task 3
Something old in a new way :). Self-study positional arguments for Python scripts (sys.argv). 
Write a script that takes a list of words (or even phrases)
Script should ask a user to write something to stdin until user won't provide one of argument phrases.
'''

import sys

def check(lst, sub):
   for i in range(0, len(lst)):
       if lst[i:i+len(sub)] == sub:
           return True
   return False

args_list=sys.argv
args_list.pop(0)
x = input("Please, input some word or phrase: ")
y=x.split(' ')
while True:
    if check(args_list, y):
        print("You have provided one of argument phrases.")
        break
    else:
        x = input("Please, input some word or phrase one more time: ")
        y=x.split(' ')
