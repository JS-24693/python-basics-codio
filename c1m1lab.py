# Tutorial Lab 1: Printing
my_variable = 'I am learning' #step 1
print(my_variable, end='') #step 2, shows the value of the variable, I am learning
my_variable = " to program" #step 3
print(my_variable, end="") #step 4, shows the new value of the variable, to program
my_variable = " in Python." #step 5
print(my_variable) #step 6, shows the new value of the variable, in Python.
my_variable = "Hooray!" #step 7
print(my_variable) #step 8, shows the new value of the variable, Hooray!

# Tutorial Lab 2: Variables
string_variable = "This is a string" # declare variable, add value
float_variable = 3.14159 # declare variable, add value
int_variable = 42 # declare variable, add value
boolean_variable = True # declare variable, add value

string_variable = boolean_variable # change the value of string_variable to the value of boolean_variable
float_variable = string_variable # change the value of float_variable to the value of string_variable
int_variable = float_variable # change the value of int_variable to the value of float_variable
boolean_variable = int_variable # change the value of boolean_variable to the value of int_variable, but was already True

print(int_variable) # prints the value of int_variable, True

# Tutorial Lab Challenge
# print the output Python fundamentals are very useful
variable_1 = "Python fundamentals are very useful"
variable_2 = variable_1
print(variable_2)