class vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other):
        x=self.x+other.x
        y=self.y+other.y
        return vector(x,y)
        
    def __str__(self):
        return'('+ str(self.x) + ',' + str(self.y)+ ')'
    
    
v1=vector(3,1)
v2=vector(2,5)
v3=v1+v2
print('vector sum:',v3)