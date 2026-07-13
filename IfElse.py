# If Else Statement
if 5 > 4:
    print("The boolean expression is true") # Outputs because the condition is true
else:
    print("The boolean expression is false") # does not output

# Example 2
if 5 > 6:
    print("The boolean expression is true") # does not output
else:
    print("The boolean expression is false") # Outputs because the condition is false

# Else statement indentation
# Error message: Syntax Error: invalid syntax
# if 5 > 6:
#    print("The boolean expression is true")
#    else:
#    print("The boolean expression is false")

# If Else Statement using True and False
my_bool = True

if my_bool:
    print("The value of my_bool is true") # Outputs because my_bool is True
else:
    print("The value of my_bool is false") # does not output

my_bool = False

if my_bool:
    print("The value of my_bool is true") # does not output
else:
    print("The value of my_bool is false") # Outputs because my_bool is False

# Using not True and not False to form a boolean value
# If my_bool is True, the if-block runs; otherwise the else-block runs.
my_bool = not True and not False

if my_bool:
    print("The value of my_bool is true") 
else:
    print("The value of my_bool is false") 
    # Runs because False and True evaluates to False, so the else-block executes

# Determine if number is odd or even combining if else with the Modulo operator
number = 4

if number % 2 == 0:
    print(str(number) + " is an even number")
    # Outputs "4 is an even number"
else:
    print(str(number) + " is an odd number")
    # Does not output

# Example 2 Determining Odd or Even Number
number = 3

if number % 2 == 0:
    print(str(number) + " is an even number")
    # Does not output
else:
    print(str(number) + " is an odd number")
    # Outputs "3 is an odd number"

# Example 3 Determining Odd or Even Number with number = 0
number = 0

if number % 2 == 0:
    print(str(number) + " is an even number")
    # Outputs "0 is an even number"
else:
    print(str(number) + " is an odd number")
    # Does not output

# Example 4 Determining Odd or Even Number with number = -8
number = -8

if number % 2 == 0:
    print(str(number) + " is an even number")
    # Outputs " -8 is an even number"
else:
    print(str(number) + " is an odd number")
    # Does not output

# Nesting if-else statements to create four unique cases

# Declare variables with a boolean value
rainy = True
windy = False
cold = True

if rainy:
    if windy:
        print("Wear a rain jacket.") # does not output
    else:
        print("Bring an umbrella!") # Outputs
else:
    if cold:
        print("You might need a coat.") # does not output because rainy is True
    else:
        print("Enjoy your day!") # does not output

