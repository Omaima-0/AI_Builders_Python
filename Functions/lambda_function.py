# lambda function is a small anonymous function that can take any number of arguments,
# but can only have one expression. It is defined using the `lambda` keyword.

# lambda arguments: expresstion

def my_lambda(x): return x * 2


print(my_lambda(5))  # Output: 10

# multiple lambda arguments


def my_lambda2(x, y): return x + y


print(my_lambda2(3, 4))  # Output: 7
