#Wrapping data & function into single unit

# _balance => for Protected
# __balance => for Private
class Bank_Account:

    def __init__(self,name, balance):
        self.name = name
        self.__balance = balance

    def get_Balance(self): #getter
        return self.__balance
    
    def new_Balance(self,Add_Balance): #setter
        self.__balance = Add_Balance


acc1 = Bank_Account("Shakid",15000)

# print(acc1.name, acc1.balance)
print(acc1.name, acc1.get_Balance())
print(acc1.name, acc1._Bank_Account__balance)


        
    
