words = ['apple', 'banana', 'kiwi', 'cherry', 'mango']
dic = {}

count = []

for wd in words:
    dic.update({wd:len(wd)})



print(dic)


#output
# {'apple': 5, 'banana': 6, 'kiwi': 4, 'cherry': 6, 'mango': 5}
