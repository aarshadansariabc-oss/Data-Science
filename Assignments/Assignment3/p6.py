words = ['apple', 'banana', 'kiwi', 'cherry', 'mango']
dic = {}

count = []

for wd in words:
    dic.update({wd:len(wd)})



print(dic)