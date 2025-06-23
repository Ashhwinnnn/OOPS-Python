class parent:
    def __init__(self,d):
        self._data=d

    def show(self):
        print(self._data)

class child(parent):
    def __init__(self,d):
        super().__init__(d)

    def display(self):
        print(self._data)

c=child(25)
c.show()
c.display()


        