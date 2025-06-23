from abc import ABC,abstractmethod
class parent(ABC):
    def meth1(self):
        print('parent meth--1')

    @abstractmethod
    def meth2(self):
        pass
class child(parent):
    def meth3(self):
        print('child meth--3')

    def meth2(self):
        print('child imp--1')


c=child()
c.meth2()