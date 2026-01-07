username = input("Enter your username : ")
password = input("Enter your password : ")

if(username == "admin" and password == "pass"):
    print("Login Successful!")
elif (username != "admin"):
    print("Wrong username")
else:
    print("Wrong password")