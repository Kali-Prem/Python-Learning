#=======================Interger data type===========================
x = 10
print(x)
print(type(x))

#float
x = 10.5
print(x)
print(type(x))

#=========complex
x = 10+2j
print(x)
print(type(x))

x = 10
print(max(x))
print(lan(x))
print(min(x))
print(x)
print(type(x))

#===========================Ordered Collection========================
'''string
list
tuple'''
'''string:-collection of charactors
- represented through '',"",''' '''
- Ordered collection
- indexing supported
- slicing supported
- immutable in  nature'''

#Inbuilt functions
x = 'python'
print(max(x))
print(min(x))
print(len(x))
print(type(x))
print(id(x))


s = 'This is python class'
print(s.lower())
print(s.upper())
print(s.swapcase())
print(s.title())
print(s.capitalize())
print(s.center(100))
print(s.center(100,'!'))

s1 = 'Kali'
s2 = 'Linux'
#syntex----'separate'.join(iterator)
print(''.join(s1))
print(''.join((s1,s2)))

#==================Split()//===========
'''syntex:-
s.split(_,_)'''


s = 'This is python class'
print(s.split())
print(s.split('s'))
print(s.split('s',0))
print(s.split('s',2))


#=================
'''s = 'python'
print(s.isascii())
print(s.isdigit())
print(s.isspace())
print(s.isnumeric())
print(s.isdecimal())
'''
#=============================/LIST/================================
'''ist-collection of homogeneous as well as hetrogenious elements'''

l = ['python', 10,20] #error
l1 = ['python','java','php']
l2 = [10,20,30,40]
print(max(l1))
print(max(l2))

print(min(l1))
print(min(l2))

print(sum(l1))
print(sum(l2))
print(len(l1))
print(len(l2))

#=======================list methods=================
'''copy(),clear(),append(),extend(),pop(),insert(),index(),count(),reverse(),remove()'''

l = [10,20,30,'python']
l.append('java')
print(l)

l.append([2,4,6,8,10])
print(l)

l.extend('java','php')
print(l) #error

l.extend(['java','php'])
print(l)

l.extend('python')
print(l) # add - 'p','y','t','h','o','n'

l.extend('p')
print(l)

#@insert
#syntax-insert(index.position,element)

l = (10,20,30,40,'python')
l.insert(0,'java')
print(l)

l.insert([20,30])
print(l1)



print(l.index(20))




#===========================Dictionary===============================
d = {'name':'kali','age':20,'quali':'CEH'}
print(len(d))
print(max(d))
print(min(d))
print(sum(d))
print(type(d))
print(id(d))
d = {'name':'kali',1:20,'quali':'CEH'}
print(len(d))
print(max(d))
print(min(d))

d = {2:'kali',2:20,'3':'CEH'}
print(d)
d = {2:100,2:20,3:'CEH'}
print(sum(d))
print(len(d))

#===========================Dictionary Methods/=======================
d = {'name':'kali','age':20,'quali':'CEH'}
print(d.keys())
print(d.values())
print(d.items())
print(d.get('kali'))
print(d.get('age'))
#================d.pop('age')
print(d)
d.popitem()
print(d)

l = {1,2,3,'z','p','q','r'}
d = dict.fromkeys(l,10)
print(d)
#d.clear()
#d.copy()
d1 = {'name':'hello'}
d.update(d1)
print(d)

d = {'name':'kali','age':20,'quali':'CEH'}
d.setdefault(('name1','kali'))
print(d)


#=================================/SET()/=================================
st = {2,4,5,3,4,2,'python','janva'}
print(st)
print(id(st))
print(len(st))

st = (2,3,4,5)
print(max(st))
print(min(st))
print(sum(st))
print(id(st))
print(type(st))

#In-built methods
'''s = {2,3,4,5,'python','java'}
s.add('php')
print(s)
s.update([2,4,5])
print(s)
s.update((2,4,5,6,7))
print(s)
s.update((2,3,'pyt'),'python')
print(s)
s.pop()
print(s)
s.remove('java')
print(s)
#s.remove('javva')
#print(s)
s.discart('javva')
print(s)

s.clear()
print(s)

s1 =s.copy()
print(s,s1)
print(id(s,id(s1)))
'''

#========================================/SETS/===============================

s1 = {1,2,3,4,9,8}
s2 = {3,4,5,6,8,7}
#print(s1.union(s2))
#print(s1.intersection(s2))
#print(s1.difference(s2))

s1.intersection_update(s2)
print(s1)
print(s2)

s1.difference_update(s2)
print(s1)
print(s2)

s1.symmetric_difference(s2)
print(s1)
print(s2)


s1 = {2,3,4}
s2 = {2,3,5,6,7,8}

print(s1.isdisjoint(s2))#false-because s1 is not disjoint
print(s1.isubset(s2))
print(s1.issuperset(s2))
print(s2.issuperset(s1))


#===========================/Frozenset/=======================================

l =[10,20,40,10,20]
fs = frozenset(l)
print(fs)

l1=[10,20,10,30,20,40]
l2=[2,4,6,8]
fs1=frozenset(l1)
fs2=frozenset(l2)
print(fs1.union(fs2))
print(fs1.isdisjoint(fs2))
print(fs1.intersection(fs2))
print(fs1.difference(fs2))
print(fs1.symmetric_difference(fs2))
print(fs1.issuperset(fs2))











