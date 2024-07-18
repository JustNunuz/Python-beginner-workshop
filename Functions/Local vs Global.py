# Define a global variable
global_var = "I am a global variable"

def my_function():
    # Define a local variable
    local_var = "I am a local variable"
    
    # Accessing the global variable inside the function
    print(global_var)
    
    # Accessing the local variable inside the function
    print(local_var)

# Call the function
my_function()

# Accessing the global variable outside the function
print(global_var)

# Trying to access the local variable outside the function (this will cause an error)
# print(local_var)  # Uncommenting this line will raise a NameError
