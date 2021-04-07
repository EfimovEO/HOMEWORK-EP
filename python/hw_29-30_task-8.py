#!/usr/bin/env python3

'''
Task 8*
You have had AWK homework (3-4), please find a document in a homework Slack thread. Do all the same AWK tasks using Python.

Awk
* What is the most frequent browser (user agent)?
* Show number of requests per month for ip 95.108.129.196 (for example: Sep 2016 - 100500 reqs, Oct 2016 - 0 reqs, Nov 2016 - 2 reqs...)
* Show total amount of data which server has provided for each unique ip (i.e. 100500 bytes for 1.2.3.4; 9001 bytes for 5.4.3.2 and so on)
'''

import re
# variant 1
# What is the most frequent browser (user agent)?
def most_frequent_browser1():
    browser_dict = {}
    with open('access.log','r') as f:
        for l in f:
            a = re.split(' - |\"', l)
            try:
                browser_dict[a[6]] += 1
            except IndexError:
                pass
            except KeyError:
                browser_dict[a[6]] = 1
        browser_dict_sorted = {k: browser_dict[k] for k in sorted(browser_dict, key=browser_dict.get, reverse=True)}
        #browser_dict_sorted.keys())[0] - возвращает "первый" ключ словаря
        print('{0} - {1}'.format(list(browser_dict_sorted.keys())[0], browser_dict_sorted[list(browser_dict_sorted.keys())[0]])) 
        
# variant 2   Медленный     
# What is the most frequent browser (user agent)?
def most_frequent_browser2():
    browser_list = []
    with open('access.log','r') as f:
        for l in f:
            a = re.split(' - |\"', l)
            try:
                browser_list.append(a[6])
            except IndexError:
                pass
        browser_dict={i:browser_list.count(i) for i in set(browser_list)}
        browser_dict_sorted = {k: browser_dict[k] for k in sorted(browser_dict, key=browser_dict.get, reverse=True)}
        print('{0} - {1}'.format(list(browser_dict_sorted.keys())[0], browser_dict_sorted[list(browser_dict_sorted.keys())[0]]))



#Т.к. access.log обновился , то во втором задании по awk используйте ip 193.106.31.130
#Show number of requests per month for ip 95.108.129.196 (for example: Sep 2016 - 100500 reqs, Oct 2016 - 0 reqs, Nov 2016 - 2 reqs...)
def requests_per_month():
    requests_dict = {}
    with open('access.log','r') as f:
        for l in f:
            a = re.split(' - |\"', l)
            if a[0] == '193.106.31.130':
                b = re.split('/|:', a[1])
                try:
                    requests_dict[b[1],b[2]] += 1
                except KeyError:
                    requests_dict[b[1],b[2]] = 1
        for key in requests_dict.keys():
            print('{0[0]} {0[1]} - {1} reqs'.format(key, requests_dict[key]))


def total_amount_of_data():
    total_data = {}
    with open('access.log','r') as f:
        for l in f:
            a = re.split(' ', l)
            try:
                total_data[a[0]] += int(a[9])
            except KeyError:
                try:
                    total_data[a[0]] = int(a[9])
                except IndexError:
                    pass
                except ValueError:
                    pass
            except IndexError:
                pass
            except ValueError:
                    pass
        for key, value in total_data.items():
            print('{0} bytes for {1}'.format(value, key))


print("Task #1")
most_frequent_browser1()

input("Press ENTER for next task.")

print("Task #2")
requests_per_month()

input("Press ENTER for next task.")

print("Task #3")
total_amount_of_data()
