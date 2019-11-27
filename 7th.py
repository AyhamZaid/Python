# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27  14:20:25 2019

@author: Ayham
"""

import numpy as np
import matplotlib.pyplot as plt
# EX1:
# =============================================================================
print("---------EX1------------")
num1=np.zeros((1,10))
num2=np.ones((1,10))
num3=np.ones((1,10))*5
print(num1)
print(num2)
print(num3)
# =============================================================================
#  EX2:
# =============================================================================
print("---------EX2------------")
Numbers=np.arange(30,71)
print(Numbers)
# =============================================================================
#  EX3:
# =============================================================================
print("---------EX3------------")
Numbers=np.arange(30,71,2)
print(Numbers)
# =============================================================================
#  EX4:
# =============================================================================
print("---------EX4------------")
matrix = np.eye(3)
print(matrix)
# =============================================================================
#  EX5:
# =============================================================================
print("---------EX5------------")
rand=np.random.normal(0,1)
print(rand)
# =============================================================================
#  EX6:
# =============================================================================
print("---------EX6------------")
Array=np.arange(10,22).reshape((3,4))
for x in Array:
    print(x)
# =============================================================================
#  EX7:
# =============================================================================
print("---------EX7------------")    
vector=np.arange(0,21)
print(vector)
vector[(vector>=9)&(vector<=15)]*=-1
print(vector)

# =============================================================================
#  EX8:
# =============================================================================
print("---------EX8------------")
mul1=[1,8,3,5]
mul2=np.random.randint(0,11,4)
print("mul1*mul2:",mul1*mul2)
# =============================================================================
# EX9:
# =============================================================================
print("---------EX9------------")
number= np.arange(10,22).reshape((3, 4))
print(number)
print(number.shape)
# =============================================================================
# EX10:
# =============================================================================
print("---------EX10------------")
Array = np.random.random((3, 3, 3))
print(Array)
# =============================================================================
# EX11:
# =============================================================================
print("---------EX11------------")
a=np.array([9,-1,2,5])
b=np.array([1,-6,0,10])
c=np.array([[1,8,2,5],[3,1,7,9]])

print("TheResult of " ,"a-b: ",a-b)
print("TheResult of " ,"a*b: ",a*b) 

print("TheResult of " ,"a.dot(b): ",a.dot(b)) 
print("TheResult of " ,"a*2: ",a*2) 

print("TheResult of " ,"np.sin(a): ",np.sin(a)) 
print("TheResult of " ,"a<3: ",a<3) 

print("TheResult of " ,"a.sum(): ",a.sum()) 
print("TheResult of " ,"a.sum(axis=0): ",a.sum(axis=0)) 

print("TheResult of " ,"c.sum(): ",c.sum()) 
print("TheResult of " ,"c.sum(axis=0): ",c.sum(axis=0)) 

print("TheResult of " ,"a.min(): ",a.min()) 
print("TheResult of " ,"a.max(): ",a.max()) 

print("TheResult of " ,"a.mean(): ",a.mean()) 
print("TheResult of " ,"a average(): ",np.average(a)) 

print("TheResult of " ,"a median(): ",np.median(a)) 
print("TheResult of " ,"a std(): ",np.std(a)) 

print("TheResult of " ,"a var(): ",np.var(a)) 
print("TheResult of " ,"c.cumsum(): ",c.cumsum()) 

print("TheResult of " ,"a[1:2] :  ",a[1:2]) 
print("TheResult of " ,"a[2:] :  ",a[2:]) 

print("TheResult of " ,"c[-1] :  ",c[-1])
# =============================================================================
# EX12:
# =============================================================================

print("---------EX12------------")
X = range(1, 50)
Y = [value * 3 for value in X]
print("Values of X:")
print(*range(1,50)) 
print("Values of Y (thrice of X):")
print(Y)
plt.plot(X, Y)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Draw a line.')
plt.show()
# =============================================================================
# Ex13:
# =============================================================================
print("---------EX13------------")
x1 = [10,20,30]
y1 = [20,40,10]
plt.plot(x1, y1, label = "line 1")
x2 = [10,20,30]
y2 = [40,10,30]
plt.plot(x2, y2, label = "line 2")
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('TwoOrMoreLinesOnSamePlotWithSuitableLegends ')
plt.legend()
plt.show()
# =============================================================================
# EX14:
# =============================================================================
print("---------EX14------------")
t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'g^', t, t**2, 'bs', t, t**3, 'r--')
plt.show()
# =============================================================================
# EX15:
# =============================================================================
print("---------EX15------------")
x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]
plt.bar(x_pos, popularity, color=['red', 'black', 'green', 'blue', 'yellow', 'cyan'])
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Popularity of Programming Language")
plt.xticks(x_pos, x)
plt.minorticks_on()
plt.show()