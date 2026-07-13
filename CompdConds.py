# Compound Conditionals
if True and True:
    print("True") # Outputs because both conditions are true

if True or False:
    print("True") # Outputs because at least one condition is true

if False or False:
    print("True") # does not output because both conditions are false

# Using Not without And or Or
# Outputs Error: SyntaxError: invalid syntax
# if True not False:
#    print("True") 

# Using Not with And or Or
if True and not False:
    print("True") # Outputs because the condition is true

# Using less-than and greater-than operator
if 5 < 10 and 5 > 0:
    print("True") # Outputs because both conditions are true

# Example 2:
if 0 < 5 and 5 < 10:
    print("True") # Outputs because both conditions are true

# Use a compound condition with the Modulo operator
num = 16

if num % 2 == 0 and num > 10:
    print("Even and greater than 10") 
    # Outputs because the number is even and greater than 10

# Example 2: changing num to 8
num = 8

if num % 2 == 0 and num > 10:
    print("Even and greater than 10") 
    # does not output because the number is not greater than 10

# Example 3: changing and to or
num = 8

if num % 2 == 0 or num > 10:
    print("Even or greater than 10") 
    # Outputs because at least one condition is true

# Example 4: changing == to !=
num = 8

if num % 2 != 0 and num > 10:
    print("Even and greater than 10") 
    # does not output because the number is not odd and not greater than 10

# Using less-than and greater-than operator with or keyword
x = 3

if x > 5 or x < 20:
    print(x) 
    # Outputs 3 because it is less than 20