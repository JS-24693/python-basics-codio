# If Statement
if 5 > 4:
    print("1st command if true") # Outputs because If statement is true
    print("2nd command if true") # Outputs because If statement is true

# If Statement using != boolean operator
if 7 != 10:
    print("The above statement is true") # Outputs because the if statement is true
print("This is not related to the if statement") # Outputs because it's outside the if block

# If Statement using == boolean operator, returns False 
if 7 == 10:
    print("The above statement is true") # Does not output
print("This is not related to the if statement") # Outputs because it's outside the if block

# If Statement using a boolean value

# If True, the print inside the block runs.
# The second print runs because it is outside the if statement.
if True:
    print("The above statement is true") # Outputs
print("This is not related to the if statement")

if False:
    print("The above statement is true") # Does not output
print("This is not related to the if statement")

# Indentation Error
# No statements output
# Error Message: Indendation Error: expected an indented block
# if True:
# print("The above statement is true")
# print("This is not related to the if statement")

# Testing Multiple Cases of If Statements
grade = 90

if grade > 70:
    print("Congrats, you passed the class") # Outputs because grade (90) is greater than 70
    
if grade < 70:
    print("Condolences, you did not pass the class") # Does not output because grade (90) is not less than 70

# Example 2: Testing Multiple Cases of If Statements
grade = 60

if grade > 70:
    print("Congrats, you passed the class") # Does not output because grade (60) is not greater than 70
    
if grade < 70:
    print("Condolences, you did not pass the class") # Outputs because grade (60) is less than 70

# Example 3: Testing Multiple Cases of If Statements
grade = 70

if grade > 70:
    print("Congrats, you passed the class") # Does not output because grade (70) is not greater than 70
    
if grade < 70:
    print("Condolences, you did not pass the class") # Does not output because grade (70) is not less than 70

# Example 4: Testing Multiple Cases of If Statements
grade = 70

if grade >= 70:
    print("Congrats, you passed the class") # Outputs because grade (70) is greater than or equal to 70
    
if grade < 70:
    print("Condolences, you did not pass the class") # Does not output because grade (70) is not less than 70

# If Statement
num = 150

if num > 100:
    print("num is greater than 100") # Outputs because num (150) is greater than 100