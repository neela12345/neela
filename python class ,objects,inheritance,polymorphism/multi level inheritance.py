class animal():
    def ani(self):
        print('eating')
class dog(animal):
    def bark(self):
        print('barking')
class babydog(dog):
    def weep(self):
        print('weeping')
obj=babydog()
obj.ani()
obj.bark()
obj.weep()
