# instance Methods

class Laptop:
    storage_type = "ssd"

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage

    @classmethod
    def get_Storage_Type(cls):
        print(f"The Storage type is {cls.storage_type}")

    def get_info(self):  # instance method
        print(
            f'laptop has : {self.RAM} RAM and storage is {self.storage} {self.storage_type}')


l1 = Laptop('16gb', '512')
l2 = Laptop('8gb', '512')

Laptop.get_Storage_Type()
l1.get_Storage_Type()

