class details:
    neela=7
    def __init__(self,name,age,gender):
        self.x=name
        self.y=age
        self.z=gender
    def display(self):
        print('my name is:',self.x)
        print('my age is:',self.y)
        print('my gender is:',self.z)
    def dummy(nivi):
        print(nivi.neela)
obj=details('neela',19,'f')
print(obj.neela)
obj.display()
obj.dummy()
