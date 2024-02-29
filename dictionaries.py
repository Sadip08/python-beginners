customer = {
    "name": "John Tamang",
    "age": 30,
    "is_verified": True
}

print(customer["name"])
# print(customer["DOB"]      returns keyerror as key named DOB doesnot exist in dictionaries

print(customer.get("birthdate"))  # returns "None" value instead of an error
# 'None' is an object that represents the absence of a value

print(customer.get("birthdate", "Jan 1 1980"))  # returns Jan 1 1980
print(customer.get('name1', 'Not found'))  # returns when the key is not found

# to update
customer["name"] = "Sadip Tamang"
customer.update({'name': 'Jane', 'age': 26})
print(customer)

# to add new key
customer["birthdate"] = "Jan 1 1980"

names = ['sadip', 'Madan', 'ujjwal']
sur_name = ['Tamang', 'tamang', 'limbu']
print(list(zip(names, sur_name)))

# to delete a key
del(customer['age'])
print(customer)

# to pop a value
age = customer.pop('name')
print(age)
print(customer)

# to get the number of keys
print(len(customer))
print(customer.keys())
print(customer.values())
print(customer.items())
