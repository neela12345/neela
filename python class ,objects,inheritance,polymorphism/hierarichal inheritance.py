class base():
    def fun1(self):
        print('base class function')
class derived1(base):
    def fun2(self):
        print('derived1 class function')
class derived2(base):
    def fun3(self):
        print('derived2 class function')
obj=derived1()
obj1=derived2()
obj.fun1()
obj.fun2()
obj1.fun1()
obj1.fun3()
