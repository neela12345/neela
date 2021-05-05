class details:
    x=7
    def __init__(self,name,age,gender):
        self.x=name
        self.y=age
        self.z=gender
    def display(self):
        print('my name is:',self.x)
        print('my age is:',self.y)
        print('my gender is:',self.z)
    def dummy(self):
        print('dummy')
obj=details('neela',19,'f')
print(obj.x)
obj.display()
obj.dummy()
