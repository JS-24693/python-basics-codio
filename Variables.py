# Variable Names
my_variable = "Hello world"
print(my_variable) # shows the value of the variable, Hello world

# Do not use quotation marks in variable names
my_variable = "Hello world"
print(my_variable)
print("my_variable") # shows the variable name, my_variable

# Assigning Values to Variables can change
my_variable = "Hello world" # shows the value of the variable, Hello world
print(my_variable)
my_variable = "Goodbye world"
print(my_variable) # shows the value of the variable, Goodbye world

# String Variables
string_variable = "This is a string"
second_string = 'This is a string also'
# shows the value of the variable, This is a string
print(string_variable) 
# shows the value of the variable, This is a string also
print(second_string) 

# Boolean Variables
boolean_variable = True
print(boolean_variable) # shows the value of the variable, True
boolean_variable = False
print(boolean_variable) # shows the value of the variable, False

# boolean_variable = true
# print(boolean_variable) # causes NameError message

# Integer Variables
integer_variable = 50
print(integer_variable) # shows the value of the variable, 50

# integer_variable = 050
# print(integer_variable) # causes SyntaxError message

# Floats Variables
float_variable = 50.0
print(float_variable) # shows the value of the variable, 50.0

float_variable = 50.
print(float_variable) # shows the value of the variable, 50.0

float_variable = .001
print(float_variable) # shows the value of the variable, 0.001