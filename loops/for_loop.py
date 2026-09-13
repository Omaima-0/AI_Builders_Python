# for loop:
# fruits = ["apple", "cucamber", "banana", "cherry"]

# for fruit in fruits:
#     if fruit == "cucamber":
#         continue  # skip the rest of the code inside the loop for this iteration
#     else:
#         print(fruit)

# for i in "apple":
#     print(i)

# for i in range(5):
#     print(i)

#####################################
# nested loop

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for i in adj:
#     for j in fruits:
#         print(i, j)

# list comperhenstion
fruits = ["apple", "banana", "cherry"]
# new_list = []
# for x in fruits:
#     if x != "apple":
#         new_list.append(x)
#         print(new_list)

# new_list = [x for x in fruits if x != "apple"]
# print(new_list)

list = [y for y in range(10) if y < 5]
print(list)
