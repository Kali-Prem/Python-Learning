 #Loop
'''|____while_loop.py
│   ├── for_loop.py
│   ├── patterns.py
│   └── number_programs.py'''


#iterative/Looping statements///
#    while (infinite iteration)
#    for (finite iteration)



#================While Loop================================
'''while loop (finite as well as infinite iteration)'''
#Natural no
n = 10
i = 1
while i<=n:
    print(i)
    i = i+1


n = 10
while n>0:
    print(n)
    n=n-1

n =10
i = 1
while  i<=n:
    if i<n:
        print(i,end=',')
    else:
        print(i)
    i = i+1

n= 10
i=1
while i<=n:
    if i<n:
        print(i,end='+')
    else:
        print(i,end='=')
    i=i+1

n=10
i,sum=1,0
while i<=n:
    sum=sum+1
    if i<n:
        print(i,end='+')
    else:
        print(i,end='='+str(sum))
    i=i+1
print(sum)


n=10
i,multi=1,1
while i<=n:
    multi=multi*i
    if i<n:
        print(i,end='+')
    else:
        print(i,end='=')
    i=i+1
print(multi)


#factorial
n=5
multi=1
while n>0:
    multi=multi*n
    if n>1:
        print(n,end='*')
    else:
        print(n,end='=')
    n=n+1
print(multi)

#HW--N EVEN NO AND N TK KE EVEN NO AND ASLO ODD NUMBER AND THEIR SUM ALSO
















#=================Pattern.================
n = 5
i =1
while i<=n:
    print('*'*i+' '*i)
    i=i+1

n = 5
i=1
while i<=n:
    print(' '*(n-i)+'*'*i)
    i=i+1


n = 5
i = 0
while i<n:
    print('*'*(n-i) + ' '*i)
    i=i+1


n = 5
i = 0
while i<n:
    print(' '*i+'*'*(n-i))
    i=i+1

# ..............
n = 5
i=0
while i<n:
    print(' '*i+'*'*(n-i))
    i=i+1
i=i-1
while i>=0:
    print(' '*i+'*'*(n-i))
    i=i-1

#..............
n = 5
i=0
while i<n:
    print(' '*i+'* '*(n-i))
    i=i+1
i=i-1
while i>=0:
    print(' '*i+'* '*(n-i))
    i=i-1

#...............
n = 5
i=0
while i<n:
    print('*'*(n-i)+' '*i)
    i=i+1
i=i-1
while i>=0:
    print('*'*(n-i)+' '*i)
    i=i-1
#....................
n = 5
i=0
while i<n:
    print('* '*(n-i)+' '*i)
    i=i+1
i=i-1
while i>=0:
    print('* '*(n-i)+' '*i)
    i=i-1

#======================...........
n = int(input('enter any number'))
i = 1
while i<=n:
    print(' '*(n-1)+'*'*i)
    i=i+1
i=i-2
while i>0:
    print(' '*(n-1)+'*'*i)
    i=i-1



#////////..............
#Armstrong no

#=============WAP to find total no of digits in given no.
n=int(input('Enter any no'))
x = str(n)
print(len(x))

#or
n = 12345
x=n
digit=0
while n>0:
    n=n//10
    digit=digit+1
print(f'total digits is {digit} in given no{n}')


#====================SUM of total no========
n = int(input('enter any no'))
sum=0
while n>0:
    last_digit=n%10
    sum=sum+last_digit
    n=n//10
print(f'total sum is {sum}')

#======Armstrong no/////
n=int(input('enter ant numver'))
digit=0
sum=0
x=y=n
while n>0:
    digit=digit+1
    n=n//10
while x>0:
    last_digit=x%10
    sum=sum+last_digit**digit
    x=x//10
if y==sum:
    print(f'given no{y}is armstrong')
else:
    print(f'given no{y}is not armstrong')

'''all single digit no is armstrong no
'''


#Palindrom no((reverse and can be anything in this no or any string)///////
n=input('enter any thing')
if n==n[::-1]:
    print(f'given valaue{n}is palindron')
else:
    print(f'given value{n}is not palindrom')


#or
n=int(input('enter any numvber'))
x=n
rev=0
while n>0:
    last_digit=n%10
    rev=rev*10+last_digit
    n=n//10
if x==rev:
    print(f'given no is {x}palindrom')
else:
    print('not palindrom')


#Orr
s='madam'
palindrom=True
l=int(len(s)/2)
i,j=0,-1
while l>0:
    if s[i]==s[j]:
        pass
    else:
        palindrom=False
        break
    i=i+1
    j=j-1
    l=l-1
if palindrom:
    print(f'given string{s}is palindrom')
else:
    print('Non palindrom')



###======================================For Loops(finite itration)/===================
#syntax--for i in collection:

l=[1,2,3,4,5]
l1=[]
for i in l:
    l1.append(i**2)
    print(l1)
print(l1)



s='hello'
for i in s:
    print(i)


x='a'
#print(ord(x))
print(ord(x)+4)
print(chr(ord(x)+4))



s='abcde'
for i in s:
    print(chr(ord(i)+4))


'''make all output in a string 'efghi' with join in string'''




s='abcde'
s1=''
for i in s:
    chr(ord(i)+4)
    s1=''.join(s1,chr(ord(i)+4))
print(s1)


s='abcde'
s1=''
for i in s:
    s1=''.join(i,s1)
    s1=''.join()



#==============sum of natural number by for loop==============
n=int(input('enter any no'))
sum=0
for i in range(1,n+1):
    sum=sum+i
    if i<n:
        print(i,end='+')
    else:
        print(i,end='=')
print(sum)


n=int(input('enter any number'))
sum=0
for i in range(2,n+1,2):
    sum=sum+i
    if i<=n-2:
        print


#==============even no===========
n=int(input('input any number'))
sum=0
for i in range(1,n+1):
    sum=sum+(2*i)
    if n<(n-2):
        print(2*i,end='+')
    else:
        print(2*i,end='=')
print(sum)

#or

n=int(input('any no'))
sum=0
for i in range(2,(2*n+1),2):
    sum=sum+1
    if i<2*n:
        print(i,end='+')
    else:
        print(i,end='=')
print(sum)

#=================odd
n=int(input('any no'))
sum=0
for i in range(2,(2*n-1+1),2):
    sum=sum+1
    if i<(2*n-1):
        print(i,end='+')
    else:
        print(i,end='=')
print(sum)

#odd
n=int(input('input any number'))
sum=0
for i in range(1,n+1):
    sum=sum+(2*i-1)
    if n<n:
        print((2*i-1),end='+')
    else:
        print((2*i-1),end='=')
print(sum)



#TRANSFER STATEMETNS//////////////////////////////
'''1.continue 2.break. 3.pass'''
#continue(skip current iteration)

n=10
i=1
while i<=n:
    if i==5:
        continue
    else:
        print(i)
    i=i+1


n=10
i=1
while i<=n:
    if i==5:
        i=i+1
        continue
    else:
        print(i)
    i=i+1

#BREAK(TERMINTATE THE LOOP)
n=10
i=1
while i<=n:
    if i==5:
        break
    else:
        print(i)
    i=i+1
print("hello")

#PASS-(SKIP CURRENT BLOCK)
'''pass is also used to synthetical correct to a block code'''

n=10
i=1
while i<=n:
    if i==5:
        pass
    else:
        print(i)
    i=i+1
print("hello")



n=2
if n>=1:
    pass
else:
    print(i)













