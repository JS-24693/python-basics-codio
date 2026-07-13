# Equal To == Operator
a = 5
b = 5
print(a == b)  # Output: True

# Change value of variable b to 1
b = 1
print(a == b)  # Output: False

# Change value of variable a to True and b to 1
a = True
b = 1
print(a == b)  # Output: True

# Change value of variable a to True and b to False
a = True
b = False
print(a == b)  # Output: False

# Not Equal To != Operator
a = 5
b = 5
print(a != b)  # Output: False

# Change value of variable b to 1
b = 1
print(a != b)  # Output: True

# Change value of variable a to True and b to 1
a = True
b = 1
print(a != b)  # Output: False

# Change value of variable a to True and b to False
a = True
b = False
print(a != b)  # Output: True

# Less Than < Operator
a = 5
b = 7
print(a < b)  # Output: True

# Change value of variable b to 1
a = 5
b = 1
print(a < b)  # Output: False

# Change the value of variable b to 5
a = 5
b = 5
print(a < b)  # Output: False

# Change the value of variable b to False
a = 5
b = False
print(a < b)  # Output: False

# Less Than or Equal To <= Operator
a = 5
b = 7
print(a <= b)  # Output: True

# Change value of variable b to 1
a = 5
b = 1
print(a <= b)  # Output: False

# Change the value of variable b to 5
a = 5
b = 5
print(a <= b)  # Output: True

# Change the value of variable a to False and b to True
a = False
b = True
print(a <= b)  # Output: True

# Greater Than > Operator
a = 9
b = 17
print(a > b)  # Output: False

# Change value of variable b to 1
a = 9
b = 1
print(a > b)  # Output: True

# Change the value of variable b to 9
a = 9
b = 9
print(a > b)  # Output: False

# Change the value of variable b to False 
a = 9
b = False
print(a > b)  # Output: True

# Greater Than or Equal To >= Operator
a = 9
b = 17
print(a >= b)  # Output: False

# Change value of variable b to 1
a = 9
b = 1
print(a >= b)  # Output: True

# Change the value of variable b to 9
a = 9
b = 9
print(a >= b)  # Output: True

# Change the value of variable a to True and b to False 
a = True
b = False
print(a >= b)  # Output: True

# The and Operator
a = True
b = True
c = False
print(a and b)  # Output: True
print(a and c)  # Output: False
print(c and b)  # Output: False

# Multiple and Statements
a = True
b = True
c = False
print(a and b and c)  # Output: False
print(a and b and a and b and a)  # Output: True
print(a and b and a and b and c)  # Output: False

# The or Operator
a = True
b = True
c = False
print(a or b)  # Output: True
print(a or c)  # Output: True
print(c or b)  # Output: True

# Multiple or Statements
a = True
b = True
c = False
print(a or b or c)  # Output: True
print(a or c or c or c or c)  # Output: True
print(c or c or c or c or c)  # Output: False

# The not Operator
print(not True)  # Output: False
print(not True and False)  # Output: False
print(not(True and False))  # Output: True
print(not not True) # Output: True
print(not not not True) # Output: False