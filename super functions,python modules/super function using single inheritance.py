class computer():
    def __init__(self,system,ram,storage):
        self.system=system
        self.ram=ram
        self.storage=storage
class mobile(computer):
    def __init__(self,system,ram,storage,model):
        super().__init__(system,ram,storage)
        self.model=model
obj_mo=mobile('oppo',2,36,'xxx')
print('mobile is:',obj_mo.system)
print('ram is:',obj_mo.ram)
print('storage is:',obj_mo.storage)
print('model is:',obj_mo.model)
