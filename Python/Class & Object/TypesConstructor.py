#default constructor and partametrised consturctos
# python me hu eak class k ander sirf eak he construcotr bna sakte hai multiple nhi
# aur agar multiple constructor likh bhi diay hai toh last wala constructor consider karta hai pyton


class Student:
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa

    def getCgpa (self):
        return self.cgpa

s1 = Student("Aquib", 9.5)
s2 = Student("Manish", 8.1)

print(
    s1.getCgpa())


