class potato:
    def type(self):
        print('vegetable')
    def color(self):
        print('golden brown')
class mango:
    def type(self):
        print('fruits')
    def color(self):
        print('yellow')
def func(obj):
        obj.type()
        obj.color()
obj_po=potato()
obj_ma=mango()
func(obj_po)
func(obj_ma)
