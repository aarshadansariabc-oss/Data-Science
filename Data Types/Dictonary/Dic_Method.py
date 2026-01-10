#Methods in Dictonary
# d.keys() return all keyss
# d.values() return all values
# di.items() returns (key val) pairs
# diget(val) returns val acc, to key
# d.update(new_item) add new item to dicotnary

info = {"Name":"Adarsh",
       "Class":11,
       "Group":"B",
       "Subject":["Maths","English","Computer"]
       }

print(info.keys()) # it prints all key in the dictonary

print(info.items())

print(info.get("Group"))

info.update({"result":"Pass"})

print(info)



dict_Keys = list(info.keys())
print(type(dict_Keys))
print(dict_Keys)