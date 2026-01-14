#here only file is imported
'''import first
p = first.x
q= first.y
z=first.add(p,q)
print(z)'''

#here all things of file is imported
'''from first import *
p = x
q = y
z = add(p,q)
print(z)'''

#If only x is needed
from first import x
p = x
print(p)

#replace to fast response
from first import calculator as c
obj = c()
x = obj.add(10,20)
print(x)