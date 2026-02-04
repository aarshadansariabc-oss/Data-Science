def add(d):
    key = input("Enter name : ").lower()
    value = int(input("Enter marks : "))
    d.update({key: value})
    return d


def update(d):
    key = input("Enter name : ").lower()
    updated_marks = input("Enter your new marks : ")
    if key in d:
        d[key] = updated_marks
    else:
        print(f"{key} is not present in our database")


def search(d):
    key = input("Enter name To search : ")
    if key in d:
        print(f"Marks of {key} is {d[key]}")
    else:
        print("Data not found")


d = {}

while True:
    print("A - Add a student : \nB - Update Marks : \nC - Search For Student : \nD - Display all student and marks : \nE - Exit")

    choise = input("Enter your choice : ").lower()

    if choise == "a":
        add(d)
    elif choise == "b":
        update(d)

    elif choise == 'c':
        search(d)
    elif choise == 'd':
        if d == {}:
            print("Dictonary is empty")
        else:
            print(d)
    elif choise == 'e':
        break
    else:
        print("You have entered wrong choice")
