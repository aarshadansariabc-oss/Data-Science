"""
Some methods of list
Syntax
    1 - l.append(val) add one elements at the end
    2 - l.inset(idx,val) insert elemtn at idx
    3 - l.short() arranges in increasing order
    4 - l.reverse() reverse order
"""


l = [19, 20, 17, 15, 12, 19, 18]
print(l)
l.append(20) # add value in the last
print(l)

l.insert(1,10)
print(l)

l.sort()
print(l)

l.reverse()
print(l)