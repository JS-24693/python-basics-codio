# Addition Operator
print(7 + 3) # shows 10

# Add two variables together
a = 7
b = 3
c = a + b
print(c) # shows 10

# Change variable a to float
a = 7.0
b = 3
c = a + b
print(c) # shows 10.0

# Change variable b to negative number
a = 7.0
b = -3
c = a + b
print(c) # shows 4.0

# Change variable b to explicitly positive number
a = 7.0
b = +3
c = a + b
print(c) # shows 10.0

# Incrementing Variables
a = 0
a = a + 1
print(a) # shows 1

# Incrementing Variables with += Operator
a = 0
b = 0
a = a + 1
b += 1
print(a) # shows 1
print(b) # shows 1

# Change incrementing variable for variable b
a = 0
b = 0
a = a + 1
b += 2
print(a) # shows 1
print(b) # shows 2

# Change incrementing variable for variable b
a = 0
b = 0
a = a + 1
b += -1
print(a) # shows 1
print(b) # shows -1

# Decrementing Variable for variable b
a = 0
b = 0
a = a + 1
b -= 1
print(a) # shows 1
print(b) # shows -1

# Type Casting Example 1
a = 3
print(type(a)) # shows <class 'int'>
a = str(a)
print(type(a))  # shows <class 'str'>

# Type Casting Example 2
a = 3.0
print(type(a)) # shows <class 'float'>
a = bool(a)
print(type(a)) # shows <class 'bool'>

# Type Casting Nonexample
# a = 5
# b = "3"
# print(a + b) # shows TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Type Casting Nonexample Correction
a = 5
b = "3"
print(a + int(b)) # shows 8

# String Concatenation
a = "This is an "
b = "example string"
c = a + b
print(c) # shows "This is an example string"

# String Concatenation with +=
a = "This is an "
b = "example string"
a += b
print(a) # shows "This is an example string"

# String Concatenation without space between variables
a = "This is an"
b = "example string"
a += b
print(a) # shows "This is anexample string"

# String Concatenation with an int
# a = "This is an " 3
# b = "example string"
# a += b
# print(a) # shows SyntaxError: invalid syntax

# String Concatenation with a number in quotes
a = "This is an " "3 "
b = "example string"
a += b
print(a) # shows "This is an 3 example string"

# Subtraction Operator
a = 10
b = 3
c = a - b
print(c) # shows 7

# Change the value of a variable b to a negative number
a = 10
b = -3
c = a - b
print(c) # shows 13

# Change the subtraction operator to double --
a = 10
b = -3
c = a - - b
print(c) # shows 7

# Change the type of a variable b to a float
a = 10
b = 3
c = a - b
print(c) # shows 7.0

# Change the value of variable b to False
a = 10
b = False
c = a - b
print(c) # shows 10

# Decrementing Variables using -= Operator
a = 10
b = 3
a -= b
print(a) # shows 7

# Division Operator
a = 25
b = 5
print(a / b) # shows 5.0

# Change value of variable b to 0
# a = 25
# b = 0
# print(a / b) # shows ZeroDivisionError: division by zero

# Change value of variable b to boolean value of True
a = 25
b = True
print(a / b) # shows 25.0

# Change value of variable b to a float
a = 25
b = 0.5
print(a / b) # shows 50.0

# Floor Division Operator
a = 5
b = 2
print(a // b) # shows 2

# Change value of variable b to a float
a = 5
b = 5.1
print(a // b) # shows 0.0

# Multiplication Operator
a = 5
b = 10
print(a * b) # shows 50

# Change value of variable b to a float
a = 5
b = 0.1
print(a * b) # shows 0.5

# Change the value of variable b to a negative int
a = 5
b = -3
print(a * b) # shows -15

# Change the value of variable b to a Boolean value of True
a = 5
b = True
print(a * b) # shows 5

# Multiplication and Strings
a = 3
b = "Hello! "
print(a * b) # shows "Hello! Hello! Hello!"

# Change value of variable a to a float
# a = 3.0
# b = "Hello! "
# print(a * b) # shows TypeError: can't multiply sequence by non-int of type 'float'

# Change value of variable a to a negative int
a = -3
b = "Hello! "
print(a * b) # Command executed successfully but shows nothing.

# Powers
a = 2 ** 2
print(a) # shows 4

# Change the value of the power in variable a to 0
a = 2 ** 0
print(a) # shows 1

# Change the value of the power in variable a to a negative number
a = 2 ** -2
print(a) # shows 0.25

# Change the value of the power in variable a to a Boolean value
a = 2 ** False
print(a) # shows 1

# Square Root
square_root = 4 ** 0.5
print(square_root) # shows 2.0

# Order of Operations
a = 2
b = 3
c = 4
result = 3 * a ** 3 / (b + 5) + c
# computes parenthethical b + 5, 
# then computes exponent of a ** 3,
# then computes multiplication & division
# from left to right, 3 * 8, 24/8
# then adds 3.0 and 4.
print(result) # shows 7.0 

# Modulo Operator
a = 5
b = 2
print(a % b) # shows 1

# Variation of modulo code
modulo = 5 % 2
print(modulo) # shows 1

# Change value of variable b to -2
a = 5
b = -2
print(a % b) # shows -1

# Change value of variable b to 0
a = 5
b = 0
# print(a % b) # shows ZeroDivisionError: modulo by zero

# Change value of variable b to Boolean value of True
a = 5
b = True
print(a % b) # shows 0