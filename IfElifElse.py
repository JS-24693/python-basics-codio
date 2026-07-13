# Elif statement
a = 20

if a < 10:
    print(str(a) + " is less than 10")
    # does not output
elif a < 20:
    print(str(a) + " is less than 20")
    # does not output
elif a < 30:
    print(str(a) + " is less than 30")
    # Outputs because 20 is less than 30
else:
    print(str(a) + " is greater than 30")
    # does not output because an elif condition is true

# Example 2: change a to 0
a = 0

if a < 10:
    print(str(a) + " is less than 10")
    # Outputs because 0 is less than 10
elif a < 20:
    print(str(a) + " is less than 20")
    # does not output
elif a < 30:
    print(str(a) + " is less than 30")
    # does not output
else:
    print(str(a) + " is greater than 30")
    # does not output because an elif condition is true

# Example 3: Change a to 100
a = 100

if a < 10:
    print(str(a) + " is less than 10")
    # does not output
elif a < 20:
    print(str(a) + " is less than 20")
    # does not output
elif a < 30:
    print(str(a) + " is less than 30")
    # does not output
else:
    print(str(a) + " is greater than 30")
    # Outputs because none of the previous conditions are true

# Example 4: Change a to 30
a = 30

if a < 10:
    print(str(a) + " is less than 10")
    # does not output
elif a < 20:
    print(str(a) + " is less than 20")
    # does not output
elif a < 30:
    print(str(a) + " is less than 30")
    # does not output
else:
    print(str(a) + " is greater than 30")
    # Outputs because none of the previous conditions are true

# Multiple elif statements for decision making precision
grade = 82

if grade < 70:
    print("You got an F.")
elif grade < 80:
    print("You got a C.")
elif grade < 90:
    print("You got a B.")
else:
    print("You got an A.")

# Example 2: Change grade to 65 and add letter grade D for the range grade from 60 to 69.
grade = 65

if grade >= 60 and grade < 70:
    print("You got a D.")
    # outputs because 65 is between 60 and 70
elif grade < 70:
    print("You got an F.")
    # does not output because if condition is true
elif grade < 80:
    print("You got a C.")
elif grade < 90:
    print("You got a B.")
else:
    print("You got an A.")

# Example 2a: change grade to 59.
grade = 59

if grade >= 60 and grade < 70:
    print("You got a D.")
    # does not output because 59 is not between 60 and 70
elif grade < 70:
    print("You got an F.")
    # outputs because 59 is less than 70
elif grade < 80:
    print("You got a C.")
elif grade < 90:
    print("You got a B.")
else:
    print("You got an A.")

# Efficiency of elif

# All five If Statements are evaluated,
# even though the fourth condition is True  
# and prints "You got a B."
# because none of the earlier conditions stop execution.
grade = 82

if grade < 60:
    print("You got an F.")
if grade >= 60 and grade < 70:
    print("You got a C.")
if grade >= 70 and grade < 80:
    print("You got a C.")
if grade >= 80 and grade < 90:
    print("You got a B.")
    # Outputs because 82 is between 80 and 90
    # execution continues for remaining execution blocks
if grade >= 90 and grade <= 100:
    print("You got an A.")

# Series of Elif statements
# when the condition is met in one of the elif statement blocks, 
# the remaining elif statement blocks are skipped.
grade = 82

if grade < 60:
    print("You got an F.")
elif grade < 70:
    print("You got a D.")
elif grade < 80:
    print("You got a C.")
elif grade < 90:
    print("You got a B.")
    # Executes here for 82
    # Remaining elif statement blocks are skipped
else:
    print("You got an A.")

# Example 2: Change grade to 79.
grade = 79

if grade < 60:
    print("You got an F.")
elif grade < 70:
    print("You got a D.")
elif grade < 80:
    print("You got a C.")
    # Executes here for 79
    # Remaining elif statement blocks are skipped
elif grade < 90:
    print("You got a B.")
else:
    print("You got an A.")

# Example 3: Change grade to 0.
grade = 0

if grade < 60:
    print("You got an F.")
    # Executes here for 0
    # Remaining elif statement blocks are skipped
elif grade < 70:
    print("You got a D.")
elif grade < 80:
    print("You got a C.")
elif grade < 90:
    print("You got a B.")
else:
    print("You got an A.")

# Example 4: Change grade to 100.
grade = 100

if grade < 60:
    print("You got an F.")
elif grade < 70:
    print("You got a D.")
elif grade < 80:
    print("You got a C.")
elif grade < 90:
    print("You got a B.")
else:
    print("You got an A.")
    # Execution reaches the else block
    # because all earlier conditions are false
    # so outputs "You got an A." for 100