# Define a function to greet a user
def greet_user(name):
    """
    This function takes a user's name as an argument
    and prints a greeting message.
    """
    print(f"Hello, {name}!")

# Define a function to add two numbers
def add_numbers(a, b):
    """
    This function takes two numbers as arguments,
    adds them together, and returns the result.
    """
    return a + b

# Call the greet_user function with an example name
greet_user("Alice")

# Call the add_numbers function with example numbers and print the result
result = add_numbers(3, 5)
print(f"The sum of 3 and 5 is: {result}")
