#Questoin 1
name = input("Enter your name : ")
age = int(input("Enter Your age : "))

print(f"Hello {name}, you are {age} years old!")

#Question 2
a = int(input("Enter a : "))
b = int(input("Enter b : "))

print(f"Sum is : {a+b}, Difference is : {a-b}, Product is : {a*b}")

#Question 3
c = float(input("Enter your value : "))
print(f"Type casteing into float value of a =  {float(a)}, b = {float(b)}, and c is {c}")

#Question 4
Num_1 = int(input("Enter the value of a : "))
Num_2 = int(input("Enter the value of b : "))

temp = Num_1
Num_1 = Num_2
Num_2 = temp

print(f"The reuslt is {Num_1} and b is {Num_2}")

#Question 5

var_1 = float(input("Enter the number : "))

integer_val = int(var_1)
fraction = var_1 - integer_val

print(f"integer par is {integer_val}\nFractional part is {round(fraction,2)}")