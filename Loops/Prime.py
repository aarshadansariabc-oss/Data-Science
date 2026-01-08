num = int(input("Enter Number : "))
i = 2
is_Prime = True

if num <=1 :
    is_Prime = False
else:
    while i < num :
        if num % i == 0:
            is_Prime = False
            break
        i +=1

if is_Prime:
    print(f"{num}, is a Prime Number")
else:
    print(f"{num}, is not a Prime Number")