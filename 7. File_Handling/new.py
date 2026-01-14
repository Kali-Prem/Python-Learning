#open()
#write()/read()
#write()
'''1.write()-single line Content
2.writelines()-multi-lines content'''

'''f=open('n1.txt','a+')
f.write('this is new lines')
#f.writelines('python','java','php')
data=['python\n','java\n','new\n']
f.writelines(data)'''


'''f=open('n1.txt','a+')
data ="""
n=
i=1
while i<=n:
print(i)
i=i+1
"""
f.write(data)
f.close()'''


#read()
'''f = open('n1.txt','r+')
#data = f.read()
#data1 = f.read(5)
#data = f.read(10)
#data= f.readline()
#data = f.readlines()
#print(data1)
#print(data)
f.readline()
f.write('hello')
f.close()'''



#Cursor_Movement
'''  tell()=to check current position
  seek() = (hwo many position move,from where){default-0 for from begining, 1- from current posstion,2-from last position}'''

'''f = open('n1.txt', 'r+')
print(f.tell())#0
f.read(5)#5
f.seek(0)
print(f.tell())'''




#tell()=findout cursor current positions  & seek()--to move our cursor...............................

'''f = open('n1.txt','rt')
data= f.read(10)
print(data)
print(f.tell())
data=f.read(5)
print(data)
print(f.tell())
#f.seek(0,0)#or f.seek(0)
f.seek(4,0)
print(f.tell()) #o/p=0

f = open('n1.txt','r+')
f.seek(-4,2)
print(f.tell())
data=f.read()
print(f.tell())'''



'''f = open('n1.txt','a+')
f.seek(5,0)
f.write('jython')
f.seek(0,0)
data=f.read()
print(data)
f.close()'''



f=open('n1.txt','r+')
print(f.closed)
f.close()
print(f.closed)








