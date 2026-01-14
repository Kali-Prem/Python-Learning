import keyword
x = keyword.kwlist
y = keyword.softkwlist
print(x)
print(y)

#======================================================================================

import string
p= string.ascii_lowercase
low = string.ascii_uppercase
print(p,low)
print(len(p),len(low))

#======================================================================================

oxyz=10
print(oxyz)

kali= 86
print(kali)

x=19
y=23
print(x)
print(y)
print(type(x))
print(type(y))

k=39.3
l=32.3
print(k,l)
print(type(k),type(l))


x=10
print(10)

print(type(x))

print(id(x))

x=input("enter your name:")
print(x)



x = 2+5j
print(x)
print(type(x))


x = 'python'
y = "python"

z = '''php'''
print(x)
print(y)
print(z)

#======================LIST,Tuple,Dictionary,Sets============================

# List
I=[10,29,'python','hello']
print(I)
print(type(I))
print(id(I))

# Tuple
t = (10,48,59,'python')
print(t)
print(type(t))
print(id(t))

# Dictionary
d = {'name':'kali','age':37,'qualificaion':'M.tech'}
print(d)
print(type(d))
print(id(d))

# Sets
s = {10,20,10,10,'python','java'}
print(s)
print(type(s))
print(id(s))

# Frozen set
i = [10,20,30]
fs = frozenset(i)
print(fs)


# =====================OPERATORS====================================

# (IV) logical Operators
x = 10
y = 20
z = 30
print(x>y and x>z)



#IDENTITY OPERATOR(is or not is -- compare adress)
x = 10
print(id(x))
y = 10
print(id(y))

print(x is y) # is -comprae adress
print(x==y) #  '==' - compare on the basic of value
'''

'''#EMPTY DECLARATION
x = int() #value=0
print()
print(type(x))

x = float() #value=0.0
print(x)
print(type(x))


x = complex() #value= 0j
print(x)
print(type(x))

'''
list--list()-->[]
string---str()-->  
tuple --tuple()-->()
dict---Dict()---> {}
set---set()--> set()
frozenset---froxenset()-->frozenset()
'''


#=======================OTHER WAYS FOR DECLARE EMPTY======================
x = 0
print(x)
print(type(x))


x = input("enter any no \n")
print(x)
print(type(x))

x = int(input("enter nay number\n"))
print(x)
print(type(x))

x = eval(input("etner any thing"))  #input-- 'string', [dict], int
print(x)
print(type(x))


#========================PYTHON In-built Function==========================
print()
type()
i ()
input()
eval()
max()
min()
sum()
len()

s = 'Python'
print(max(s))
print(min(s))
print(len(s))
print(sum(sets))


#========================PYTHON In-built Classes=============================
'''int,str,list,tuple,set,dict,frozenset,float,complex'''


#========================PRINT FUNCTION=============================

#Default Inbuilt function in python --> print(sep='', end='\n')
print("Hello")
print('Hi')

print("Hello",end=',')
print("Hi") #o/p--Hello,Hi

x=20
y=10
print(x,y) #print(x,y,sep'\n')



#SIZEOF TO SHOW SIZE 
import sys
x = int()
y = str()
z = list()


print("Required bit for inter :",sys.getsizeof(x))

#=======================PYTHON OBJECTS AND MEMORY MANAGEMENT=======================
#memory management in python is done by python memory manager.
#python uses reference counting and garbage collection for memory management.
#every object in python has a unique id, type and value.
#id() function is used to get the unique id of an object.
#type() function is used to get the type of an object.
#value is the actual data stored in the object.
  #1.)MUTABLE-address diffent means change
  #2. Immutable- address same 
  #exceptional--frozensets are exceptional bz made by many sets

x = 10
y = 10
print(id(x),id(y)) #address will be same

x = 'python'
y = 'Python'
print(id(x),id(y)) #address will not be same change every times


#=================================INDEXING==================================
#indexing---to locate the postion of elemnt in a collection.
#collection.index('element',start,stop)
#in +ve direction, the last elemt is n-1 and in -ve diret n+1

s = 'python'
print(s.index('y',0,4))
print(s.index('t',1,4))
print(s.index('h',2,5))

# Output:
# 1
# 2
# 3


l = [10,20,30,'python','java']
print(l.index(30))
print(l.index(30,2))

# Output:
# 2
# 2

# print(l.index('java',3,4))
# Output:
# ValueError

#====================first and last element through indexing=======
#collection[index postion]
s = 'python'
print(s[0])
print(s[-1])

# Output:
# p
# n


#================================SLICE===================================
#syntax:- collection[start:stop:step/direction]
#steps---

s = 'I Love Python'
print(s[::2])
print(s[::-1])
print(s[2:10])
print(s[7:-10])
print(s[7:7])

# Output:
# ILoeyhn
# nohtyP evoL I
# Love Pyt
# (empty)
# (empty)


s = 'I Love python'
print(s[::-1][1:7][::-1][2:3])

# Output:
# v


#===============================RANGE==================================
#range- create collection of similar pattern sequential elements.
''''
syntex:- range(start,stop,step/direction)
         range(stop)
         range(start,stop)'''

n = int(input("enter any number"))
x = range(1,n+1)
print(list(x))

# Input:
# 5
# Output:
# [1, 2, 3, 4, 5]


print(list(range(-1,-10)))
# Output:
# []


print(list(range(-1,-10,-1)))
# Output:
# [-1, -2, -3, -4, -5, -6, -7, -8, -9]


print(list(range(2,11,2)))
# Output:
# [2, 4, 6, 8, 10]


print(list(range(1,11,2)))
# Output:
# [1, 3, 5, 7, 9]


print(list(range(-4,5,2)))
# Output:
# [-4, -2, 0, 2, 4]


print(tuple(range(-4,0,1)))
# Output:
# (-4, -3, -2, -1)


print(list(range(-5,-4)))
# Output:
# [-5]


print(list(range(-5,-6,-1)))
# Output:
# [-5]


print(list(range(-5,-9,-1)))
# Output:
# [-5, -6, -7, -8]


print(list(range(10,0,-1)))
# Output:
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]




# All basics notes
