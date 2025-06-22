class rectangle:

    def __init__(self,l=1,b=1):
        self.length=l
        self.breadth=b

    def area(self):
            return self.length * self.breadth
        
    def perimeter(self):
            return 2 * (self.length + self.breadth)
    
r1=rectangle(15,8)
r2=rectangle(7,4)
r3=rectangle()
r4=rectangle(5)

print(r1,r2,r3,r4)