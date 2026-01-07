color = input("Enter color : ")

match color:
    case("green"):
        print("Go")
    case("red"):
        print("Stop")
    case("yellow"):
        print("Get Ready")
    case _:
        print("Wrong color")