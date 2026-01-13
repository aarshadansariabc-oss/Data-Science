# static Method

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

    @staticmethod
    def cal_price(price, discount):
        final_price = price - (discount*price/100)
        print(f"Laptop final price is {final_price}")


l1 = Laptop('16gb', '512')


l1.cal_price(40000, 10)
