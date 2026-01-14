
'''├── oops/
│   ├── class_and_object.py
│   ├── constructors.py
│   ├── instance_class_static.py
│   ├── abstraction.py
│   └── oop_summary.py
'''





#class->> dummy model/design/blueprint of an object or blueprint of a n object
'''      behaviour--->methods
         property--> variables'''
#Object- >>physical existance of Class

#syntax:-
'''class Class_name:
    "doc string"
    variables---------->>class variable
                        >>instance variable--variable which is in with self.
                        >>local variable
    constractor
    methods----------->>instance method---methods having first self paramter
                      >>class method
                      >>static method'''
#Note:->class and clssname is required and all are optional
#doc string are the 

'''class Demo:
    "This is demo class"
    pass
print(id(Demo))
print(dir(Demo))
print(Demo.__doc__)'''


#Note --->  __main__ is the file entry point in python like void main() in c++
#Note----> __init__ constructor is already by default in class.
#constructor is a special method whcih is automatic call when object is created
#()-- is used to call extreranl constructor like used in Obj = demo() or demo.
'''class Demo:
    "this is demo class"
    x = 10
    y = 20
    def new(self):
        pass
print(id(Demo))
obj = Demo #address same
obj = Demo()#address different
print(id(obj))
#print(Demo.__dict__)'''

'''class Student:
    def __init__(self,name,gread):
        self.n = name
        self.g = gread
        print(id(self))'''

#obj = Student
'''obj = Student('Kali','B.tech')
print(id(obj))'''
#Note-- here self and obj are same because the adress is same
#Note-- self is a variable which hold current adress of Current class



'''class Student:
    def __init__(self):
        print('contructor called')

obj = Student()
obj.__init__()#constructor externally called
print(obj)


class Student:
    #constructor called automatecally
    def __init__(self):
        print('contructor called')

obj = Student()
obj.__init__()#constructor externally called
print(obj)'''

#we can access inside the class through self and outside the class through object
#Note-- n number of constructor can be created

'''class Student:
    #constructor called automatecally
    def __init__(self):
        print('contructor called')
    def __init__(self,x):
        print("2nd consturcotr called")
    def __init__(self,x,y,z):
        print("3rd constructor called")
    def __init__(self):#only this recent constructor will be clled
        print("4th construcotr called")

obj = Student()'''
#Note-- only recent constructor will be called and this is called overlaod(python doest not support overlaod)



'''class Student:
    def __init__(self,name,city,roll):
        self.n = name
        self.c = city
        self.r = roll
x = input('enter name')
y = input('enter city')
z = input('eenter rooll')
stu1 = Student(x,y,z)
print(stu1.n)
print(stu1.c)
print(stu1.r)'''


#Define instances in many ways in pythons

'''class Student:
    def __init__(self,name,city,roll):
        self.n = name #n is instance variable
        self.c = city
        self.r = roll
    def Show(self):
        print(self.n) #instance variable access in sid ecalss method or instance method
        print(self.c)
        print(self.r)
obj = Student('kali','bhop',101)
obj.Show()'''


#we can declare an instance outside the class
'''class Student:
    def __init__(self,name,city,roll):
        self.n = name #n is instance variable
        self.c = city
        self.r = roll
    def Show(self):
        print(self.n) #instance variable access in sid ecalss method or instance method
        print(self.c)
        print(self.school)

obj = Student('kali','bhop',101)
obj.school = 'SHSC'
obj.Show()'''



'''class Student:
    def __init__(self,name,city,roll):
        self.n = name #n is instance variable
        self.c = city
        self.r = roll
    def Show(self):
        print(self.n) #instance variable access in sid ecalss method or instance method
        print(self.c)
        print(self.school)
    def add(self,principal):
        self.p = principal

obj = Student('kali','bhop',101)
obj.school = 'SHSC'
obj.Show()
obj.add('python')
print(obj.p)
'''




#...................Class variable /static variable -->>which value don't change............

'''class Student:
    school = 'SHSS' #declaration of class variable /static variable
    def __init__(self,name,gread,roll):
        self.n = name
        self.g = gread
        self.r = roll
        Student.principal='python'
    def Show(self):
        print(self.n)
        print(self.g)
        print(self.r)
        print(Student.school) #accessing of class variable inside method

obj = Student('kali','m.tech',101)
obj.Show()
obj1 = Student('RAHYL','B.TECH',102)
obj1.Show()
'''

#static variable can be define inside the constructor
'''class Student:
    school = 'SHSS' #declaration of class variable /static variable
    def __init__(self,name,gread,roll):
        self.n = name
        self.g = gread
        self.r = roll
        Student.principal='python'
    def Show(self):
        print(self.n)
        print(self.g)
        print(self.r)
        print(Student.school)
obj = Student('kali','hello,109')
print(Student.principal)'''

#static variable also can be define outside the constructor
'''class Student:
    school = 'SHSS' #declaration of class variable /static variable
    def __init__(self,name,gread,roll):
        self.n = name
        self.g = gread
        self.r = roll
        Student.principal='python'
        print(Student.city)
    def Show(self):
        print(self.n)
        print(self.g)
        print(self.r)
        print(Student.school)
        #print(Student.city)'''

'''Student.city = 'Bhopal'
obj = Student('kALI','BTECH',103)
obj.Show()'''

#.........DECLARATION-------------------->
'''        In-side class--    # 1.class body
                            ->2. constructor
                            -->3. Instence method
        Out-side class---
                        ->1.outside class'''



#..............Class Method...................................

'''@classmethod
first paramter is cls insted of self
used to create/update any class variable'''

# class Student:
#     grade = '1st'
#     def __init__(self,name,roll):
#         self.n = name
#         self.r = roll
#     def Show(self):
#         print(self.n)
#         print(self.r)
#         print(Student.grade)
#     @classmethod
#     def update(cls,x):
#         cls.grade = x
# obj = Student('klai',101)
# obj.Show()
# obj.update('2nd')
# obj.Show()



#...........LOCAL VARIABLE.......
'''class Student:
    def new(self):
        x = 10
        print(x)
    def new1(self):
        print(x)
obj1 = Student()
obj1.new()'''

#.........STATIC METHOD....................


class Student:
    def first(self):
        print("from first method")
    @staticmethod
    def wel_great():
        print("welcome to this webpage")
    @staticmethod
    def thanks_great():
        print("Thanks for visit")
obj = Student()
#obj.wel_great()

#....SUMMARY..........
'''class Class_Nmae:
    "doc string"
    variables---> instance
            ----> class
            ----> local
    
    Constructor:--> __init__(self)
    
    Method: ---> instance
            ---> class
            ---> Static '''   


#......PROPERTIES:----------------------
'''1.Abstraction
2.Encapsulation
3.Inheritance
4.Polymorphism
'''









