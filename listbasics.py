# List Examples
int_list = [1, 2, 3, 4, 5]
string_list = ["John", "Paul", "George", "Ringo"]
mixed_list = [0.87, "hello", True, 17]

print("this is int_list: ", int_list)
print("this is str_list: ", string_list)
print("this is mixed_list: ", mixed_list)

# Invalid syntax error when remove commas
# int_list = [1 2 3 4 5] # SyntaxError: invalid syntax

# NameError when remove quotes from "hello"
# mixed_list = [0.87, hello, True, 17] # name 'hello' is not defined

# Declare variable hello
hello = "hi" # Declare variable hello
mixed_list = [0.87, hello, True, 17] # Changed hello to "hi"
print("this is mixed_list with declared variable: ", mixed_list) 
 
# Populate a list with range()
my_list = [i for i in range(1, 51)] # -start, -stop
print(my_list)

# Populate a list counting by 2s from 0 to 48
my_list = [i for i in range(0, 50, 2)] # -start, -stop, -step
print(my_list)

# Populate a list counting backwards from 50 to 1
my_list = [i for i in range(50, 0, -1)] # -start, -stop, -step
print(my_list)

# Access the first element in a list with index [0] 
my_list = [5, 10, 15, 20]
print(my_list[0])

# Access the third element in a list with index [2] 
my_list = [5, 10, 15, 20]
print(my_list[2])

# IndexError for accessing an index that doesn't exist
# my_list = [5, 10, 15, 20]
# print(my_list[4]) # This will raise an IndexError

# TypeError: Indices must be int or slice objects, not float
# my_list = [5, 10, 15, 20]
# print(my_list[1.5]) # This will raise a TypeError

# Access the last element in a list with index [-1]
my_list = [5, 10, 15, 20]
print(my_list[-1])

# Modify a list element with = operator
my_list = [1, 2, 3]
print(my_list) # Output: [1, 2, 3]

my_list[0] = 4 # Modify the first element
my_list[1] = 5 # Modify the second element
my_list[2] = 6 # Modify the third element
print(my_list) # Output: [4, 5, 6]

# Modify a list element with = operator with mixed data types
my_list = [1, 2, 3]
print(my_list) # Output: [1, 2, 3]

my_list[0] = "hello"
my_list[1] = 5 % 2 > 0
my_list[2] = my_list[0]
print(my_list) # Output: ['hello', True, 'hello']
