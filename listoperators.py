# List concatenation using + operator
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

print(list_1 + list_2)  # Output: [1, 2, 3, 4, 5, 6]

# List concatenation, reversed
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

print(list_2 + list_1)  # Output: [4, 5, 6, 1, 2, 3]

# Concatenating list_1 to [4] in print statement
print(list_1 + [4])  # Output: [1, 2, 3, 4]

# TypeError: can only concatenate list (not "int") to list
# print(list_1 + 4)  # This will raise a TypeError

# List repetition using * operator
list_1 = ["Hi!"]

print(list_1 * 4)  # Output: ['Hi!', 'Hi!', 'Hi!', 'Hi!']

# Use * operator to empty the list using 0 or a negative number
list_1 = ["Hi!"]

print(list_1 * 0)  # Output: []
print(list_1 * -1)  # Output: []

# Use in operator to check if an element is in a list
my_list = ["red", "orange", "yellow", "green"]

print("red" in my_list)  # Output: True
print("blue" in my_list)  # Output: False
print("Red" in my_list)  # Output: False
print(my_list in my_list)  # Output: False

# List length
list_1 = [12, 66, 52, 97, 28, 41, 7] # 7 elements
list_2 = [68, True, 34, False, 41.897, "apple"] # 6 elements

if len(list_1) > len(list_2): # Check if list_1 is longer than list_2
    print("list_1 is longer than list_2") 
elif len(list_1) == len(list_2): # Check if list_1 and list_2 are the same length
    print("list_1 and list_2 are the same length")
else:                         # If neither of the above conditions are true, list_2 must be longer than list_1
    print("list_2 is longer than list_1")
    # Output: list_1 is longer than list_2

## Removing a list_1 element
list_1 = [12, 66, 52, 97, 28, 41] # 6 elements
list_2 = [68, True, 34, False, 41.897, "apple"] # 6 elements

if len(list_1) > len(list_2): # Check if list_1 is longer than list_2
    print("list_1 is longer than list_2") 
elif len(list_1) == len(list_2): # Check if list_1 and list_2 are the same length
    print("list_1 and list_2 are the same length")
else:                         # If neither of the above conditions are true, list_2 must be longer than list_1
    print("list_2 is longer than list_1")
    # Output: list_1 and list_2 are the same length

## Adding items to list_2
list_1 = [12, 66, 52, 97, 28, 41] # 6 elements
list_2 = [68, True, 34, False, 41.897, "apple", "pigeon", 6] # 8 elements

if len(list_1) > len(list_2): # Check if list_1 is longer than list_2
    print("list_1 is longer than list_2") 
elif len(list_1) == len(list_2): # Check if list_1 and list_2 are the same length
    print("list_1 and list_2 are the same length")
else:                         # If neither of the above conditions are true, list_2 must be longer than list_1
    print("list_2 is longer than list_1")
    # Output: list_2 is longer than list_1

## Changing list_2 to use a range‑bound loop variable
list_1 = [12, 66, 52, 97, 28, 41] # 6 elements
list_2 = [i for i in range(0, 20)] # 20 elements

if len(list_1) > len(list_2): # Check if list_1 is longer than list_2
    print("list_1 is longer than list_2") 
elif len(list_1) == len(list_2): # Check if list_1 and list_2 are the same length
    print("list_1 and list_2 are the same length")
else:                         # If neither of the above conditions are true, list_2 must be longer than list_1
    print("list_2 is longer than list_1")
    # Output: list_2 is longer than list_1

# Access a range of elements in a list with slicing [start:stop]
my_list = [5, 10, 15, 20]
print(my_list[1:3]) # This will print [10, 15]

# Access a range of elements in a list with slicing [start:stop:step]
my_list = [5, 10, 15, 20]
print(my_list[0:4:2]) # This will print [5, 15]

# Access a range of str elements
my_list = ["red", "orange", "yellow", "green"]
my_slice = my_list[0:2]

print(my_slice) # Output: ['red', 'orange']

# Print the whole list
my_slice = my_list[0:len(my_list)]

print(my_slice) # Output: ['red', 'orange', 'yellow', 'green']

# Print first two elements without listing start
my_slice = my_list[:2]
print(my_slice) # Output: ['red', 'orange']