#Q1. i/p n=12345
'''0/p- 52341
'''
#Q2. i/p l=[10,20,30,40,50]
'''o/p [50,20,30,40,10]'''
#Q3. i/p t=(10,20,30,40,50)
'''o/p-(50,20,30,40,50)
'''
#Q4. i/p s='python'
'''(o/p-'nythop')'''
#1
l=[10,20,30,40,50]
l[0],l[-1]=l[-1],l[0]
print(l)

#2
t=(10,20,30,40,50)
l=list(t)
l[0],l[-1]=l[-1],l[0]
t=tuple(l)
print(t)

#4
s='python'
l=list(s)
l[0],l[-1]=l[-1],l[0]
print(l)
s=''.join(l)
print(s)

#3.
n=12345
s=str(n)
l=list(s)
l[0],l[-1]=l[-1],l[0]
s=''.join(l)
n=int(s)


#n=5 given by user then make 
'''1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5-
1 2 3 4 5'''

n=5
i=1
for i in range(n):
    for j in range(1,n+1):
        print(j,end=' ')
    print()


#print A B C D E for five times
n=4
for i in range(n):
    x='A'
    for j in range(0,n):
        print(chr(ord(x)+j),end=' ')
    print()


