#Given a list of tuples with info(name, subject)
#list all unique course
#

info = [
    ("Alice","Math"),
    ("Bob","Science"),
    ("Alice","Science"),
    ("Charlie","Math"),
    ("Bob","Math"),
    ("Alice","English"),
    ("Charlie","English")
]
courses_set = set()
for tup in info:
    courses_set.add(tup[1])

#or
# for name, course in info:
#     print(name,course)

print(courses_set)