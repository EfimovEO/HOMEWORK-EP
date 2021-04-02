#!/usr/bin/env python3

'''
Task 5
Develop a function that takes a list of integers (by idea not in fact) as an argument and returns list of top-three max integers.
If passed list contains not just integers collect them and print the following error message:
You've passed some extra elements that I can't parse: [<"elem1", "elem2" .... >]. 
If return value will have less than 3 elements for some reason it's ok and shouldn't cause any problem, 
but some list should be returned in any case.
'''


x = input("Please, input comma-separated list of integers:")
ls = x.split(',')
error_ls=[]

# этим циклом заполняем список со значениями, которые не int и коныертируем в int числа
i=0
for l in ls:
    try:
        ls[i]=int(l)
    except ValueError:
        error_ls.append(l)
    i+=1

# этим циклом удаляем из исходного списка значения, которые не int 
for l in error_ls:
    ls.remove(l)

# чтобы оставить уникальные значения сделаем из списка множество    
myset = set(ls)
# вернем список, чтобы далее можно было его отсортировать
ls=list(myset)
ls.sort(reverse=True)

if len(ls)<3:
    top=len(ls)
else:
    top=3

print("List of top max integers: {}".format(ls[0:top]))
print("You've passed some extra elements that I can't parse: {}".format(error_ls))
