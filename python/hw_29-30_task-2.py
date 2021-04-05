#!/usr/bin/env python3

'''
Task 2
Develop a procedure to print all even numbers from a numbers list which is given as an argument.
Keep the original order of numbers in list and stop printing if a number 254 was met. 
Don't forget to add a check of the passed argument type.
'''

import sys

def print_numbers():
    try:
        x=sys.argv[1]
    except IndexError:
        print("Numbers list wasn't given as an argument to the script {}".format(sys.argv[0]))
        x = input("Please, input comma-separated numbers:")
       
    ls = x.split(',')
    for i in ls:
        try:
            a=int(i)
        except ValueError:
            print("{} - this is not number".format(i))
        else:
            if a==254:
                print("254 was found")
                break
            else:
                print(a)


print_numbers()
