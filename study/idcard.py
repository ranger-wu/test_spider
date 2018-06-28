'''
cardno=input("请输入身份证号:")
year=cardno[6:10]
month=cardno[10:12]
day=cardno[12:14]
print ("出生日:%s年%s月%s日"%(year,month,day))

'''
'''
import re
s='kkk 192.168.1.136'
l=re.findall(r'\d+.\d+.\d+.\d+', s)
print (l)
'''
'''
list=[1,3,6,2,7]
print(sorted(list)) 
list=[1,3,6,2,7]
print(sorted(list,reverse=True)) '''


#利用sorted 排序:
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0].lower()

print('根据姓名排序结果: ')
print(sorted(L,key=by_name))


def by_score(t):
    return t[1]

print('根据分数排名结果: ')
print(sorted(L,key=by_score,reverse=True))

li = [1, 2, 3, 4, 4, 56, 32, 12, 4, 34]

import copy
def sort_list(li):
    li = copy.deepcopy(li)
    for n in range(len(li)):
        for i in range(len(li) - n - 1):
            if li[i] > li[i + 1]:
                li[i], li[i + 1] = li[i + 1], li[i]

        return (li)
print(sorted(li))