# Combined example using 'and' and 'or'

age = 25
has_ticket = True

# Check if a person is allowed to enter a concert
if age >= 18 and (has_ticket or age >= 65):
    print("Allowed to enter the concert")
else:
    print("Not allowed to enter the concert")
