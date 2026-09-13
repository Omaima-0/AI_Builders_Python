def my_function():
    print("Hello from my_function!")


my_function()  # call the function


# the parameter is the function's variable that will hold the value of the argument passed to the function
def ferhenheit_to_celsius(temp):
    celsius = (temp - 32) * 5 / 9
    # send the the result back to the caller   (like printing the result)
    return celsius


print(ferhenheit_to_celsius(77))  # call the function with an argument of 77
print(ferhenheit_to_celsius(32))  # call the function with an argument of 32


def my_name(name, country="Germany"):  # default value for country is "Germany"
    print("Hello," + name + " from " + country + "!")


my_name("OMAIMA")  # call the function with an argument of "John"
