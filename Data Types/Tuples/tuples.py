#Tuples is immutable sequence of values

tup = (1,2,3,4,5,"PI ", 3.14159,)
print(tup)
print(type(tup))

# tup[2] = 11 is Not allowed

print(tup[5 : len(tup)])

# for single value 
# tups = (1) this is not allowed
# tups = (1,) this is allowed