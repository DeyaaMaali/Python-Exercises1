# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 09:22:32 2019

@author: OJO3
"""
# constructor or initializer 

# =============================================================================
# Exampe1
# class Person :
#     def __init__(self, name): 
#         self.name = name 
# # method which returns a string 
#     def whoami( self ): 
#         return "I am " + self.name
# # destructors 
#     def __del__( self ): 
#         print ( 'I have been deleted')
#         
#         
# p1 = Person('tom') 
# print(p1.whoami()) 
# print(p1.name)
# del p1
# =============================================================================

# =============================================================================
# Example 2
# class Encapsulation(object): 
#     def __init__(self, a, b, c): 
#         self.Apublic = a 
#         self._Bprotected = b 
#         self.___Cprivate = c 
#     def getprivate(self): 
#         return self.___Cprivate
#     
#     def setprivate(self, value):
#         self.___Cprivate = value
#     
# x = Encapsulation(11,13,17) 
# print ( x.Apublic )  
# print ( x._Bprotected ) 
# print(x.___Cprivate)
# x.setprivate(100)
# print ( x.getprivate())
# =============================================================================


# =============================================================================
# Example 3
# class Parent(object):
#     def __init__(self, name, age, salary):
#         self.name = name
#         self._age = age
#         self.__salary = salary
#         
#     def public(self):
#         print("calling public")
#         
#     def _protected(self):
#         print("calling protected")
#         
#     def __private(self):
#         print("is it really private?")
#         
# 
# class Child(Parent):
#     def foo(self):
#         self.public()
#         self._protected()
#         print(self.name)
#         print(self._age)
#         
#         
# c = Child("Hussam",40,100)
# c.foo()
# c.public()
# =============================================================================

# =============================================================================
# Exampe 4
# class Circle: 
#     def __init__(self, radius):        
#         self.__radius = radius
#     def setRadius(self, radius):        
#         self.__radius = radius
#         
#     def getRadius(self):
#          return self.__radius
#      
#     def __add__(self, another_circle):
#         if type(another_circle) == int:
#             return Circle( self.__radius + another_circle )
#         else:
#             return Circle( self.__radius + another_circle.__radius )
#     
#     
# c1 = Circle(4) 
# print(c1.getRadius()) 
# c2 = Circle(5) 
# print(c2.getRadius()) 
# c3 = c1 + c2 
# print(c3.getRadius())
# =============================================================================


class Employee:
    def __init__(self, number, name, address, salary, jobTitle):
        self.number = int(number)
        self.__name = str(name)
        self.__address = str(address)
        self.__salary = float(salary)
        self.__jobTitle = str(jobTitle)
    
    def getName(self):
        return self.__name
    
    def getAddress(self):
        return self.__address
    
    def setAddress(self, newAddress):
        self.__address = newAddress
        
    def getSalary(self):
        return self.__salary
    
    def getJobTitle(self):
        return self.__jobTitle
    
    def info1 (self):
        print("\t", "* Employee number:", self.number)
        print("\t", "* Name:", self.getName()) 
        print("\t", "* Address:", self.getAddress()) 
        print("\t", "* Salary:", self.getSalary())
        print("\t", "* Job Title:", self.getJobTitle())
        
    def info2 (self):
        print( "Employee number =", self.number, end=",")
        print( "Name =", self.getName(), end=",") 
        print( "Address =", self.getAddress(), end=",") 
        print( "Salary =", self.getSalary(), end=",")
        print( "Job Title =", self.getJobTitle())
    
    def __del__( self ): 
        print (self.__name, 'has been deleted')
        
        
emp1 = Employee(1, "Mohammad Khalid", "Amman, Jordan", 500, "Consultant")
emp2 = Employee(2, "Hala Rana", "Aqaba, Jordan", 750, "Manager")


print("Employee1 Information:")
emp1.info1()

print("\n")

print("Employee2 Information : ", end="")
emp2.info2()

print("\n")

emp1.setAddress("USA")
print("Employee1 New Address : ", end ="")
print(emp1.getAddress())

print("\n")

del emp1
del emp2
        






