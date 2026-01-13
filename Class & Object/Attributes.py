class Student:
    # class 
    collage_name = "Integral University"
    PI = 3.14159
    def __init__(self,name, gpa):
        self.name = name
        self.gpa = gpa
        self.PI = 3.14

s1 = Student("Anuj",7.8)

print(s1.name)
print(s1.PI)
print(Student.PI)
print(Student.collage_name)