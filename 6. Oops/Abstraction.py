#..............Abstraction..............................
'''only name is defined not body in abstract and pass is used to make correct'''

from abc import ABC,abstractmethod
class Senior(ABC):
    def add(self,x,y):
        return x+y
    def sub(self,x,y):
        return x-y
    @abstractmethod
    def multi(self):
        pass
class Junior(Senior):
    def multi(self,x,y):
        return x*y
obj = Junior()

