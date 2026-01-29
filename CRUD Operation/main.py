from pathlib import Path


print("Press 1 to Create a  file : ")
print("Press 2 to Read a  file : ")
print("Press 3 to Updating a  file : ")
print("Press 3 to Delete a  file : ")

choice = int(input("Enter Your Choice : "))



if choice == 1:
    create_File()