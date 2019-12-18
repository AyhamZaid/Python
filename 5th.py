# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 14:50:50 2019

@author: Ayham
"""

class Empolyee():
    def __init__(self,EmployeeNumber,Name,Address,NewAddress,Salary,JobTitle):
        self.EmployeeNumber = int(EmployeeNumber)
        self.__Name = str(Name)
        self.__Address=str(Address)
        self.__Salary=float(Salary)
        self.__JobTitle=str(JobTitle)
    def getName (self):
        return self.__Name
    def getAddress (self):
        return self.__Address
    def setAddress(self,newAddress):
        self.__Address = newAddress
        return print (self.getName(),"new Address :",self.getAddress())
    def getSalary (self):
        return self.__Salary
    def getJobTitle (self):
        return self.__JobTitle
    
    
    def Emp1 (self):    
        print("Employee Information :""Employee Number = ",self.EmployeeNumber ,"Name = ", self.__Name ,"Address = ", self.__Address , "Salary = " , self.__Salary , "Job title = ",self.__JobTitle)
        
    def Emp2 (self):
        print("Employee Information :","\nEmployee Number = ",self.EmployeeNumber ,"\nName = ", self.__Name ,"\nAddress = ", self.__Address , "\nSalary = " , self.__Salary , "\nJob title = ",self.__JobTitle)

    def __del__( self ):
        print (self.__Name ,"Has been deleted")
        


result = Empolyee(1234312,"AyhamZaid","Amman","Jordan",4423.32,"WebDevelpoer")
Emp1 = Empolyee(1,"Mohammad Khaled" , "Amman","Jordan" , 500,"Consultant")
Emp2 = Empolyee(2,"Hala Rana" , "Aqaba","Jordan" , 750,"Manager")

print(result.getName())
print(result.getAddress())
#update Address
print(result.setAddress("USA"))

print(result.getSalary())
print(result.getJobTitle())
print("----Horizantal-------")
print(result.Emp1())
print("----Vretical-------")
print(result.Emp2())

#Delete here 
# =============================================================================
# del result
# del Emp1
# del Emp2
# =============================================================================



    
        
        
