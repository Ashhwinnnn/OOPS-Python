class rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b

    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self,l):
        if l>=0:
            self._length=l
        else:
            self._length=1
r=rectangle(10,5)
r.length=-9
print(r.length)
