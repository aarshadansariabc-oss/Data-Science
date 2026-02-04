class Employee:
    start = '10am'
    end_time = "6pm"

class AdminStaff(Employee):
    def __init__(self, role):
        self.role = role

class Accountant(AdminStaff):
    def __init__(self, salary, role):
        super().__init__(role)
        self.salary = salary

acc1 = Accountant(12000,"ca")

print(acc1.role, acc1.salary, acc1.start, acc1.end_time)