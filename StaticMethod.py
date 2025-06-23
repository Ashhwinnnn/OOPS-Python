class rectangle:

    def __init__(self,l,b):
        self.length=l
        self.breadth=b

    @staticmethod
    def calc_area(length,breadth):
        return length * breadth
        
print(rectangle.calc_area(10,7))