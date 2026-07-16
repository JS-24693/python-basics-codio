# If statement
x = 5

if x < 10:
    print("Less than 10")
    # Output: Less than 10

# If block is skipped because the condition is False
x = 20

if x < 10:
    print("Less than 10")
print("And the program continues...")
# Output: And the program continues...

# If else statement
x = 10

if x > 50:
    print(str(x) + " is greater than 50")
else:
    print(str(x) + " is less than 50")
    # Output: 10 is less than 50

# If else statement with less than or greater than
x = 50

if x > 50:
    print(str(x) + " is greater than 50")
else:
    print(str(x) + " is less than 50")
    # Output: 50 is less than 50

# If else statement with "greater than or equal to" operator
x = 50

if x >= 50:
    print(str(x) + " is greater than or equal to 50")
    # Output: 50 is greater than or equal to 50
    # Execution stops.
else:
    print(str(x) + " is less than 50")

# Even or Odd number using If else statement with modulo operator
x = 7

if x % 2 == 0:
    print(str(x) + " is even")
else:
    print(str(x) + " is odd")
    # Output: 7 is odd

# Compound conditionals

# less than and greater than boolean expressions linked with and
x = 10

if x > 5 and x < 15:
    print(str(x) + " is between 5 and 15")
    # Output: 10 is between 5 and 15
else:
    print(str(x) + " is not between 5 and 15")

# less than and greater than boolean expressions linked with or
x = 10

if x > 5 or x < 15:
    print(str(x) + " is between 5 and 15")
    # Output: 10 is between 5 and 15
else:
    print(str(x) + " is not between 5 and 15")

# expression is true even if x is 5 (x < 15) or 15 (x > 5)
x = 5

if x > 5 or x < 15:
    print(str(x) + " is between 5 and 15")
    # Output: 5 is between 5 and 15
else:
    print(str(x) + " is not between 5 and 15")

# If Elif Else Statement
michelin_stars = 3

if michelin_stars == 1:
    print("This is a very good restaurant")
elif michelin_stars == 2:
    print("This is an excellent restaurant")
else:
    print("This restaurant is among the best in the world")
    # Output: This restaurant is among the best in the world

# Example 2 where variable x contains a value between 0 and 20
x = 15

if x <= 5:
    print(str(x) + " is less than or equal to 5")
elif x <= 10:
    print(str(x) + " is less than 10")
elif x <= 15:
    print(str(x) + " is between 10 and 15")
    # Output: 15 is between 10 and 15
    # Execution stops because the condition is True.
elif x <= 20:
    print(str(x) + " is between 15 and 20")
    # Not Outputted: 15 is between 15 and 20
    # because the remaining blocks are not evaluated.
else:
    print(str(x) + " is not between 0 and 20")

# Month of the Year: 
# determine the month of the year based on the value of a variable called month.
month = 7

if month == 1:
    print("January")
if month == 2:
    print("February")
if month == 3:
    print("March")
if month == 4:
    print("April")
if month == 5:
    print("May")
if month == 6:
    print("June")
if month == 7:
    print("July")
    # Output: July
    # execution continues even though the condition is True
if month == 8:
    print("August")
if month == 9:
    print("September")
if month == 10:
    print("October")
if month == 11:
    print("November")
if month == 12:
    print("December")
