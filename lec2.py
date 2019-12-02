# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 09:40:08 2019

@author: OJO3
"""
"""
x = int(input('enter number 1: '))

y = int(input('enter number 2: '))

if x <= y :
    print(x, y)
else:
    print (y, x)
    
"""
"""
name = str(input('Enter your name: '))

age = int(input('Enter your age: '))

if age < 18:
    print("Under Age.")
    avg = int(input('Enter your School Average: '))
    if avg >= 90:
        print("Excellent Average")
    elif avg >= 50 and avg < 90:
        print("Passed")
    else:
        print("Failed")
else:
    print("Adult")
    job = str(input('Enter your job title: '))
    print(age, name, job)
    
"""

"""
n = int(input('enter number '))
str = ""
for x in range(n):
    str = str + "*"
    print(str);
"""

"""
n = int(input('enter number '))

for x in range(n):
    for y in range (n-x-1):
        print(" ", end ="")
    for z in range (x+1):
        print("*", end="")
    print("\n", end ="")
"""

"""
Ex1:

x = int(input('enter number 1: '))

y = int(input('enter number 2: '))

if x >= y :
    print(x)
else:
    print (y)
"""

"""
Ex2:
    
n = int(input('enter number '))

for x in range(10):
    print(n, "*", x+1, "=", (x+1)*n)

"""


# =============================================================================
# Ex3:
# =============================================================================
    
# =============================================================================
# n = int(input('enter number '))
# str = ""
# for x in range(n):
#     str = str + "*"
#     print(str);
#     
# for y in range (n):
#     for a in range(n-1,y,-1): 
#         print("*", end="")
#     print("\n", end="")
# =============================================================================


"""
Ex4:
    x
    y
    z
    b
"""

"""
Ex5:
    12
    15
    18
    21
    24
"""

"""
Ex6:
   1
   2
   3
"""

"""
Ex7:
    
n = int(input('enter number '))
sum = 0
for a in range (n+1):
    sum = sum + a
print(sum) 

"""
"""
Ex8: 
n = int(input('enter number '))
if n % 2 == 0:
    print("even")
else:
    print("odd")
"""



# =============================================================================
# Ex9: But Printing Stars
# =============================================================================

# =============================================================================
# n = int(input('enter number '))
# 
# for x in range(n):
#     for y in range (n-x-1):
#         print(" ", end ="")
#         
#     for z in range (x+1):
#         print("*", end="")
#         if z == x:
#             for m in range (x):
#                 print("*",end="")
#     print("\n", end ="")
#     
# 
# 
# for x in range(n-2,-1,-1):
#     for y in range (n-1-x):
#         print(" ", end ="")
#         
#     for z in range (x*2+1):
#         print("*", end="")
#        
#     print("\n", end ="")
# 
# =============================================================================

# =============================================================================
# Ex9:
# =============================================================================
n = int(input('enter number '))
c = 1
for x in range(n):
    for y in range (n-x-1):
        print(" ", end ="")
        
    for z in range (x+1):
        print(c, end="")
        c=c+1
        if z == x:
            c=c-1
            for m in range (x):
                c=c-1
                print(c,end="")
    c = 1
    print("\n", end ="")
    

for x in range(n-2,-1,-1):
    for y in range (n-1-x):
        print(" ", end ="")
        
    for z in range (x*2+1):
        if(z >= (x*2+1)//2):
            print(c, end="")
            c=c-1
        else:
            print(c, end="")
            c=c+1
       
    print("\n", end ="")
    c=1
 

"""
Ex10:
    
while True:
    try: 
        n = input("Please enter an integer: ") 
        n = int(n)
        print("Great, you successfully entered an integer!")
        print("Your number is:", n)
        break 
    
    except ValueError: 
        print("No valid integer! Please try again ...") 

"""

"""
Ex11:
    Error Occurred and Handled
"""

    
    
    
