#!/usr/bin/env python3

'''
Task 4
We took a little look on os module. 
Write a small script which will print a string using all the types of string formatting which were considered during the lecture 
with the following context: 
This script has the following PID: <ACTUAL_PID_HERE>. 
It was ran by <ACTUAL_USERNAME_HERE> 
to work happily on <ACTUAL_OS_NAME>-<ACTUAL_OS_RELEASE>.
'''

import os
import pwd

def pr_format1(pid, usename, OS_NAME, OS_RELEASE):
    tx='''
    This script has the following PID: {0}.
    It was ran by {1}
    to work happily on {2}-{3}.
    '''.format(pid, usename, OS_NAME, OS_RELEASE)
    print(tx)
    
def pr_format2(pid, usename, OS_NAME, OS_RELEASE):
    tx=f'''
    This script has the following PID: {pid}.
    It was ran by {usename}
    to work happily on {OS_NAME}-{OS_RELEASE}.
    '''
    print(tx)


pid = os.getpid()
usename=pwd.getpwuid(os.getuid())[0]
OS_NAME=os.uname()[0]
OS_RELEASE=os.uname()[2]

pr_format1(pid, usename, OS_NAME, OS_RELEASE)
pr_format2(pid, usename, OS_NAME, OS_RELEASE)
