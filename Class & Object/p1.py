class Product:
    count = 0

    def __init__(self,name, price):
        self.name = name
        self.price = price
        Product.count +=1

    def get_info(self):
        print(f"Price of {self.name} is Rs. {self.price}")

    @classmethod
    def get_count(cls):
        print(f"Total object is {cls.count}")

    @staticmethod
    def get_discount(price,discount):
        final_price = price - (discount*price/100)
        print(f"The final price is {final_price}")


p1 = Product("Phone",10_000)
p2 = Product("Laptop",50_000)
p3 = Product("Register",100)

p1.get_info()
Product.get_count()

p1.get_discount(p1.price,10)
    