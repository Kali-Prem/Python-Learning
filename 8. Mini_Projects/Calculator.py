#Calculator

while True:
    print(' add\n','sub\n','multi\n','division\n','\n5')
    n=int(input('enter your operation'))

    x=(1,2,3,4,5)
    if n in x:
        if n==1:
            p=input()
            q=input()
            print(p+q)
        elif n==2:
            p=input("Enter first number: ")
            q=input("Enter second number: ")
            print(int(p)-int(q))
        elif n==5:
            break
    else:
        print('please enter ight input')
