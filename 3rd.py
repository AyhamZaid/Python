# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 14:05:43 2019

@author: Ayham
"""

#Ex1
list=[21,23,31,42,43,52,53]
for x in list: print(x)

#Ex2
list=[21,23,31,42,43,52,53,100]
print(sum(list))

#3Ex3
list=[21,23,31,42,43,52,53,100]
print(max(list))

#Ex4
a = [10,20,30,20,10,50,60,40,80,50,40]
dup = set(a)
print(dup)

#EX5
list = []
if not list:
  print("List is empty")
else:
    print("List is Full")
  
#Ex6
Tuple=(21,"Apple",31,42,"Ayham",[52,53])
for x in Tuple: print(x)

#Ex7
iteration = set([10, 11, 12, 13, 14, 15])
for n in iteration:
  print(n)
  
#Ex8
list1 = {"Ayham","Zaid","Hacker"}
list2 = {"Ayham","Hacker","Orange"}
lists=list1 & list2
print(lists)

#Ex9
seta = set(["green","blue"])
setb = set(["blue","yellow"])

setall = seta | setb
print (setall)

#Ex10
nums = set([23,432,2,4234,324,34])
print (len(nums))

#Ex11
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
dic4 = {}

for d in (dic1,dic2,dic3):
    dic4.update(d)
    print (dic4)
# =============================================================================
# 
#Ex12
a = "Hello, World!"
print (a[1])
print (a[2:5]) 
print (a[-5:-2]) 
print (len(a))
print (a.lower())
print (a.replace("H","J"))