# Given a list of integers compute the average of all numbers in the list
List = [10,20,30]


print(f"Average is {sum(List)/len(List)}")

#or
s =0
for i in List:
    s += i

print(f"Average is {s/len(List)}")