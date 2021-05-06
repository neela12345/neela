class mammal():
    def __init__(self,name):
        print(name,'is a mammal')
class canfly(mammal):
    def __init__(self,canfly_name):
        print(canfly_name,'cannot fly')
        super().__init__(canfly_name)
class canswim(mammal):
    def __init__(self,canswim_name):
        print(canswim_name,'cannot swim')
        super().__init__(canswim_name)
class animal(canfly,canswim):
    def __init__(self,name):
        super().__init__(name)
carol=animal('dog')
