# Sets {}
my_set = {1, 2, 3, 4, 4, 5}
print(type(my_set))
print(len(my_set))  # the length of the set

# add an element to the set
my_set.add(6)
print(my_set)

fuits_set = {"apple", "banana", "cherry"}
my_set.update(fuits_set)  # add all elements of fruits_set to my_set
print(my_set)

# remove an element from the set
my_set.remove("banana")
my_set.remove(6)  # remove the element "banana" from the set
print(my_set)

# remove the element 10 from the set if it exists, otherwise do nothing
my_set.discard(10)

my_set.pop()
print(my_set)  # remove and return an arbitrary element from the set

my_set.clear()  # remove all elements from the set
print(my_set)
