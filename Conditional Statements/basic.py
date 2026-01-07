#basic learing of conditional statement

age = int(input("Enter your age : "))
if age >= 18:
    print("You can vote")
else:
    print("You can't vote")

color = input("Enter color : ").lower()

if color == "red":
    print("Stop")
elif color == "yellow":
    print("Get Ready")
else:
    print("G0")