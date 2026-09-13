# Conditional statements in Python

# if condition is true:
#    execute this block of code

# a = 10
# b = 20
# if a < b:
#     print("a is less than b")
# elif a > b:
#     print("a is greater than b")
# else:
#     print("a is equal to b")

# x = 17
# if x > 10:
#     print("x is greater than 10")
#     if x > 20:
#         print("x is also greater than 20")
#     else:
#         print("x is not greater than 20")
# else:
#     print("x is not greater than 10")

#####################################################

age = 17
has_license = True

if age >= 18:
    if has_license:
        print("You are eligible to drive.")
    else:
        print("You need a valid driver's license to drive.")

else:
    print("You are too young to drive.")


if age >= 18 and has_license:
    print("You are eligible to drive.")
else:
    print("You are not eligible to drive.")
