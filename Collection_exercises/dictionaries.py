# Dictionaries

my_dict = {"name": "John", "age": 30, "city": "New York"}
print(type(my_dict))
print(my_dict["name"])  # access the value associated with the key "name"
print(len(my_dict))  # the length of the dictionary
print(my_dict.keys())  # get all the keys in the dictionary
print(my_dict.values())  # get all the values in the dictionary
print(my_dict.items())  # get all the key-value pairs in the dictionary
print(my_dict.get("age"))  # get the value associated with the key "age"

# get the value associated with the key "gender", if it doesn't exist, return "Not Found"
print(my_dict.get("gender", "Not Found"))
# get the value associated with the key "gender", if it doesn't exist, set it to
print(my_dict.setdefault("gender", "Not Found"))

print(my_dict)

print(my_dict["city"])

my_dict["age"] = 31  # update the value associated with the key "age"
print(my_dict)


my_dict.pop("age")  # remove the key-value pair with the key "age"
print(my_dict)

del my_dict["city"]  # remove the key-value pair with the key "city"
print(my_dict)

my_dict.clear()  # remove all key-value pairs from the dictionary
print(my_dict)  # Output: {}
