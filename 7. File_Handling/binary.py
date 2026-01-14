#pickle ---convert the python object to binary code
'''for this two methods are resposible
    1.dump()---python_object to byte code
    2.Load()--byte.code to python boject'''

import pickle
'''f = open('n1.pkl','ab+')
data = {'name':'kali','quali':'hacker'}
pickle.dump(data,f)
f.close()'''

f = open('n1.pkl','rb+')
data = pickle.load(f)
print(data)
f.close()