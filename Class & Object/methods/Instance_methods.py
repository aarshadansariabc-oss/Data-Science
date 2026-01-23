# instance Methods

class Laptop:
    storage_type = "ssd"

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage

    def get_info(self): #instance method
        print(f'laptop has : {self.RAM} RAM and storage is {self.storage} {self.storage_type}')


l1 = Laptop('16gb', '512')
l2 = Laptop('8gb', '512')

l1.get_info()


