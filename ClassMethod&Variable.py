class rectangle:
    count=0
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
        rectangle.count+=1

    @classmethod
    def get_count(cls):
            return cls.count
r1=rectangle(15,8)
r2=rectangle(7,4)
print(rectangle.get_count())