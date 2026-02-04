# Given a tuple of integers create
#  a tuple of all even numbers
#   a tuple of all odd numbes

x = []

for i in range(1,101):
    x.append(i)

t = tuple(x)

l = list(t)

even = []
odd = []

for i in l:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

Even = tuple(even)
Odd = tuple(odd)

print(f"Even Number are : {Even}")
print(f"Odd Number are : {Odd}")