d = {
    "Name":"Ankit",
    "S.N":32,
    "Department":"Mca",
    "Fee":"Paid",
    "Phone No.":"898347938",
    "Address":"Lucknow Kursi Road"
}

keys = d.keys()
print(keys)

d.update({"Country":"India"})
d.update({"Fee":"pending"})
print("Updated successful")
print(d)