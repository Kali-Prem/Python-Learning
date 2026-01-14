
'''├── functions/
│   ├── function_basics.py
│   ├── arguments_types.py
│   ├── lambda_map_filter_reduce.py
│   ├── generators.py
│   └── decorators.py
'''




#Functions--(write ones call multiples)
#         --to achive code reusability
#        --- avoide sequentially or non-sequetially block of code repeation


#Types of functions- 1.user define 2.pre-define functions

#syntax:- 
'''def fun-name(parameters):
       to perform any function
       return Value
fun-name(arguments)'''




#.......function without name called del keyword
'''def first():
    pass
first()
print(first())



def first():
    return
first()
print(first())


def first():
    return 10
first()
print(first())
'''

#.........Even no......
def even_no(n):
    for  i in range(2,n+1):
        if i<n:
            print(2*i,end=',')
        else:
            print(2*i)
print("Hello")
print("Hi")
even_no(int(input('enter any no:')))
print('welcome')
even_no(int(input('enter any no:')))




#....Odd no.........
def odd_no(n):
    for  i in range(1,n+1):
        if i<n:
            print(2*i-1,end=',')
        else:
            print(2*i-1)
print("Hello")
print("Hi")
odd_no(int(input('enter any no:')))


#............factorial.......
def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(f'factorial of {n}is {fact}')
n=int(input("enter any value:"))
fact(n)



fact=1
for i in range(5,0,-1):
    fact=fact*i
    if i>1:
        print(i,end='*')
    else:
        print(i,end='=')
print(fact)



#.................2.USER DEFINE FUNCTIONS....................
#

#...Relationship b/w parameters & arguments


#......Position arguments.......
def sum(x,y):
    print(x+y)
#sum()
sum(10,2)

#......keyword arguments........

def sum(x,y):
    print("value of x:",x)
    print("value of y:",y)
sum(y=10,x=12)
#.....default argumetns.........

def sum(x=0,y=0):
    print("value of x:",x)
    print("valu3 of y:",y)
sum()
#.....Variable length positional arguments (* means all)(*args)

def sum(*args):
    print(args)
    print(type(args))
sum()
sum(10)
sum(10,20,30,40,50,60)


def sum(*args):
    sum=0
    for i in args:
        sum=sum+i
    print(sum)
sum(10,20,30,40)
sum()
x=eval(input("enter any tuple:"))#2,-comma lagane pr tuple hi aayegi default
print(x)
print(type(x))


def sum(*n):
    print(n)
    print(type(x))
x=eval(input("enter any tuple:"))
sum(x)


def sum(*n):
    sum=0
    for i in n:
        for j in i:
            sum=sum+j
    print(sum)
x=eval(input("enter any tuple:"))
sum(x)


def sum(*n):
    sum=0
    for i in n:
        for j in i:
            sum=sum+j
    print(sum)
x=eval(input(list()))
sum(x)


#.....Keyword variable length arguments(**krgs)...

def sum(**n):
    print(n)
    print(type(n))
sum(x=10,y=20,z=30)

def sum(**n):
    for k,v in n.items():
        print(k,'=',v)
sum(x=10,y=20,z=30)
sum(name='kali',quali='linux')


def sum(**n):
    for k in n.items():
        print(k)
sum(x=10,y=20,z=30)
sum(name='kali',quali='linux')



#..............Higher order functions..........
'''kisi bhi function ke arguments me hum jb ek function pass kr dete hen toh ussey hum high
er order funticon bolte hen '''

'''add(2,4) positional
add()defautl
add(x=4,y=2) key-word
add(2,4,6,8)*args
add(x=2,y=3,z=4) **kwargs
add(fun_name) higher order function'''

#.1..map()....
'''syntax:- map(fun_name,iterator1,iterator2)
         map(fun_nme,collection1,collet2)'''

l=[1,2,3,4,5]
def sqr(n):
    return n**2
x=map(sqr,l)
print(x)

l1=[1,2,3,4]
l2=[2,3,45,6]
def add(x,y):
    return (x+y)
p=map(add,l1,l2)
print(list(p))

#Note:- in filter ,conditions is used and in map ,arithmetic operator is used..



#2....Filter..............
'''Syntax:- filter(fun_name,iterate)#only one iterate'''

l1=[2,4,6,8,10]
l2=[1,2,3,4,5,6,7,8,9,10]
def even_no(n):
    if n%2==0:
        return n
x=filter(even_no,l1)
print(list(x))

l1=[2,4,6,8,10]
l2=[1,2,3,4,5,6,7,8,9,10]
def even_no(n):
    if n%2==0:
        return n #return is first stored the data then return but print only print them
#    they not stored tha object
y=filter(even_no,l2)
print(list(y))

# 3..........Reduce.....

#====min_no
from functools import reduce
l1=[2,4,6,8,10]
l2=[1,2,3,4,5,6,7,8,9,10]
def min_no(x,y):
    if x<y:
        return x
    else:
        return y
x=reduce(min_no,l1,0)
print(x)
#==========max_no
from functools import reduce
l1=[2,4,6,8,10]
l2=[1,2,3,4,5,6,7,8,9,10]
def min_no(x,y):
    if x>y:
        return x
    else:
        return y
x=reduce(min_no,l1,0)
print(x)
#=========SUm...
from functools import reduce
l1=[2,4,6,8,10]
l2=[1,2,3,4,5,6,7,8,9,10]
def min_no(x,y):
    return (x+y)
x=reduce(min_no,l1,0)
print(x)
#==========multi.........
from functools import reduce
l1=[2,4,6,8,10]
l2=[1,2,3,4,5,6,7,8,9,10]
def min_no(x,y):
    return (x*y)
x=reduce(min_no,l1)
print(x)

#..=========multi
from functools import reduce
l3=[1,2,3,4,5]
def main_no(sum,x):
    return sum+x*2
x=reduce(min_no,l3,1)
print(x)


#LAMBDA FUNCTIONS--- the functions which have not any name is called lambda functions in py
'''#python
lambda function is used to solve single line functiosn
Syntax:- lambda(parameter):expression'''

x=lambda x,y:print(x+y)
p=int(input('enter no'))
q=int(input('inter no'))
x(p,q)

x=lambda x,y:x+y
p=int(input('enter no'))
q=int(input('inter no'))
z=x(p,q)
print(z)

#......

l1 = [2,3,4,5,6]
l2 = [3,4,5,6,7]
l3 = [1,2,3,5,6]

x = map(lambda x,y,:x+y+z,l1,l2,l3)
print(x)

#..square
l1= [2,4,5,6,7]

x = map(lambda x:x**2,l1)
print(list(x))

#>.....List comprehension 
#       syntax:- [o/pfortrue if condition else o/pfor false]

n=10
p = lambda x:['even' if x%2==0 else 'odd']
print(p(n))

#...Filter

l1 = [1,2,3,4,5,6,7,8,9,10]

p = filter(lambda x:x%2==0,l1)
print(list(p))



l1 = [1,2,3,4,5,6,7,8,9,10]

p = map(lambda x:['even' if x%2==0 else 'odd'],l1)
print(list(p))


#.......Maximum number.......

from functools import reduce
l = [1,2,3,4,5,9,0,4]
x = reduce(lambda p,q:p if p>q else q,l)
print(x)

#==========sum
from functools import reduce
l = [1,2,3,4,5,9,0,4]
x = reduce(lambda p,q:p+q,l)
print(x)




#....Topic-- Decorator.......................................







