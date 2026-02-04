#Given a list of tuples with info(name, subject)
#list students enrolled in english


info = [
    ("Alice","Math"),
    ("Bob","Science"),
    ("Alice","Science"),
    ("Charlie","Math"),
    ("Bob","Math"),
    ("Alice","English"),
    ("Charlie","English")
]

l = []

for name, course in info:
    if course == "English":
        l.append(name)

print(l)