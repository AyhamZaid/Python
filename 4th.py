# =============================================================================
# # -*- coding: utf-8 -*-
# """
# Created on Sun Nov 24 12:07:31 2019
# 
# @author: Ayham
# """
# #EX1
# o=lambda x=1,y=2,z=3:x+y+z
# print(o())
# print(o(10))
# print(o(10,20))
# 
# #Ex2
#  
# def multiplyList(myList) : 
#       
#     result = 1
#     for x in myList: 
#          result = result * x  
#     return result  
#       
# list1 = [1, 2,3,4,5,6,7,8]  
# print(multiplyList(list1)) 
# 
# #Ex3
# x= (lambda x, y: x*y) (2,3)
# print(x)
# =============================================================================

# =============================================================================
# #Ex4
# number_list = range(-5,5)
# filtered = list(filter(lambda x: (x < 0), number_list)) 
# print("The Negative numbers :-",filtered)
# 
# #Ex5
# x = lambda a,b,c:a+b+c
# print(x(5,6,2))
# 
# #Ex6
# x=("joey","Monica","Rose")
# y=("Chandler","Pheobe")
# z=("Davied","Rachel","Countery")
# result = list(zip(x,y,z))
# print(result)
# 
# #Ex7
# coin =('Bitcoin','Ether','Ripple','Litecoin')
# code=('BTC','ETH','XRP','LTC')
# d=dict(zip(coin,code))
# print(d)
# 
# #Ex8
# def fun(variable):
#
#     letters = ['a','e','i','o','u']
#     if(variable in letters):
#         return True
#     else:
#         return False
# 
# sequence =['g','j','e','j','k','o','p','r']
# filtered = list(filter(fun, sequence))
# print(filtered)
# =============================================================================
# 
# 
# #Ex9
# x=list(map(int,input("Enter a multitple a value:").split()))
# print("List of students:",x)
# =============================================================================

#Ex10
# =============================================================================
# def newfunc(a):
#     return a*a
# x =list(map(newfunc,(1,2,3,4)))
# print(x)
# =============================================================================

#Ex11
# =============================================================================
# def func(a,b):
#     return a+b
# a=list(map(func,[2,4,5],[1,2,3,2,4]))
# print(a)
# =============================================================================
#EX12
# =============================================================================
# c =map(lambda x:x+x,filter(lambda x:(x>=3),(1,2,3,4)))
# print(list(c))
# =============================================================================
#EX13
# =============================================================================
# c =filter(lambda x: (x >= 3) , map(lambda x: x+x,(1,2,3,4)))
# print(list(c))
# =============================================================================
#Ex14
# =============================================================================
# import functools
# lis = [ 8,5,-9,-2,1,3, 5, 6, 2, ] 
# print ("The min element of the list is : ",end="")
# print (functools.reduce(lambda a,b : a if a < b else b,lis)) 
# =============================================================================
#EX15
#numbers = [1,2,3]
#letters= ['a','b','c']
#results = list(zip(numbers, letters))
#print(results)
