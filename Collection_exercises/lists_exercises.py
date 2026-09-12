mylist = [1, 2, 3, 4, 4]
print(type(mylist))
print(mylist[0])
print(len(mylist))  # the length of the list

mylist.append(5)  # add an element to the end of the list
print(mylist)

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # add an element to the end of the list
print(fruits)

mylist.remove(4)  # remove the first occurrence of the element 4 give a value
print(mylist)

# remove at specific index
# mylist.pop(2)  # remove the element at index 2
# print(mylist)

# del mylist[0]  # delete the element at index 0
# print(mylist)

# mylist.clear()  # remove all elements from the list
# print(mylist)  # Output: []

# Merge two lists
mylist.extend(fruits)  # add all elements of fruits to mylist
print(mylist)

# list comperhension
new_list = []
new_list = [x for x in fruits if "a" in x]
print(new_list)
