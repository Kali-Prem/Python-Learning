# It is a higher order function and which take a function as arguments and returns a function
#it is used to show anything without changing the main code

#Syntax : - 
def decor(x):
    def inner_func():
        p=x
        return p
    return inner_func
x = decor(10)
z = x()
print(z)



#This is for pvm 
def decor(x):
    def inner_func(r,s):
        p=x(r,s)
        return p
    return inner_func
def add(x,y):
    return x+y
x=decor(add)
z = x(10,50)
print(z)






#..

def decore(x):
    def inner (r,s):
        r =r+5
        s=s+5
        p=x(r,s)
        return p
    return inner
@decore
def add(x,y):
    return x+y
z=add(5,10)
print(z)