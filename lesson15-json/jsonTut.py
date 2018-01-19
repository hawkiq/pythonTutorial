import json
dictionary = {}
while True:
    name = input("Name: ")
    age = input("Age: ")
    phone = input("phone: ")
    dictionary[name] = {"name":name,"age":age,"phone":phone}
    con = input("Continue: ")
    if con.lower() == "y":
        continue
    else:
        break

s = json.dumps(dictionary)
with open("api.json","w") as f:
    f.write(s)