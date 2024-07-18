# Initialize an empty list to store user inputs
user_data = []

# Get user's name
name = input("Enter your name: ")
user_data.append(name)

# Get user's selection
selection = input("Rock , Paper or Scissors ")
user_data.append(selection)

# Print user's name and selection using list indexing
print("User's name: {user_data[0]}")
print("User's selection: {user_data[1]}")
