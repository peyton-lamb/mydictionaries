person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)

# print out the name of the second child
print(person["children"][2])

# print out the name of the cat
print(person["pets"]["cat"])

# itnerate through all children and print out each child
for i in person["children"]:
    print(i)

# print out the pets in this format:
# type of pet: dog name of pet: Fido
for i, j in person["pets"].items():
    print(f"type of pet: {i} name of pet: {j}")
