#Desgin & create an online store for products (name, price)
#Track total products being created.
#Create a static method to calculate discount on each product based on a parameter
class Product:
    count = 0
    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1 

    def getInfo(self):
        print(f"Product name is {self.name} and price is {self.price}")

    @classmethod
    def get_totalProduct(cls):
        print(f"The Total product is {cls.count}")
    
    #static Method
    @staticmethod
    def discounted_Price(price, discount):
        dis = price - (price * discount /100)
        print(f"After discounted the price is {dis}")

smartphone = Product('Vivo',15000)
laptop = Product('Lenovo', 30000)

smartphone.getInfo()
Product.get_totalProduct()

smartphone.discounted_Price(smartphone.price,10)

