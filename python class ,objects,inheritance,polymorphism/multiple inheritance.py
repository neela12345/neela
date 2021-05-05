class calc1():
    def summation(self,a,b):
        return a+b
class calc2():
    def product(self,a,b):
        return a*b
class derived(calc1,calc2):
    def divide(self,a,b):
        return a/b
obj=derived()
print(obj.summation(2,3))
print(obj.product(2,3))
print(obj.divide(4,2))
    
