#Given a list of tuples with info(name, subject)

    # creare dictonary (student, set of courses)

info = [
    ("Alice","Math"),
    ("Bob","Science"),
    ("Alice","Science"),
    ("Charlie","Math"),
    ("Bob","Math"),
    ("Alice","English"),
    ("Charlie","English")
]

dic = {}

for name, course in info:
    if dic.get(name) == None:
        dic.update({name:set()})
        dic[name].add(course)
    else:
        dic[name].add(course)
    

print(dic)