class outer:
    def __init__(self):
        self.in_obj = self.inner()

    def show(self):
        self.in_obj.show()

    class inner:
        def __init__(self):
            self.idata = 'Inner Data'

        def show(self):
            print(self.idata)

o = outer()
o.show()
                

            