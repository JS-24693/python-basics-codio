# sum() function
my_list = [1, 2, 3, 4, 5]    # Create a list with 5 elements
total = sum(my_list)         # Calculate the sum of all elements
print(total)                 # Output: 15

# with negative ints and floats
my_list = [-45, 21, 6, 0.3]  # Create a list with negative integers and a float
total = sum(my_list)           # Calculate the sum of all elements
print(total)                   # Output: -17.7

# empty list
my_list = []
total = sum(my_list)
print(total)                 # Output: 0

# TypeError with non-numeric elements
# my_list = ["abc", "def", "ghi"]
# print(sum(my_list))    # Output: TypeError: unsupported operand type(s) for +: 'int' and 'str'

# my_list = [1, 2, 3, "red"]
# print(sum(my_list))    # Output: TypeError: unsupported operand type(s) for +: 'int' and 'str'

# use sum() function, length and average to calculate average of a list
my_list = [1, 2, 3, 4, 5] # declare a list with 5 elements
total = sum(my_list)      # declare the sum of all elements
num_elements = len(my_list) # declare the number of elements in the list

average = total / num_elements if num_elements > 0 else 0 # calculate and print the average
print(average)  # Output: 3.0

# min() function to return the smallest element
my_list = [45, 12, 9, 1]
smallest = min(my_list)
print(smallest)  # Output: 1

# min() function with negative numbers and floats
my_list = [0, 1, 0.5, -0.2, -1]
smallest = min(my_list)
print(smallest)  # Output: -1

# ValueError for empty list
# my_list = []
# my_list = []
# smallest = min(my_list)
# print(smallest)  # Output: ValueError: min() arg is an empty sequence

# str
my_list = ["apple", "boy", "cat", "aaron"]
smallest = min(my_list)
print(smallest)  # Output: "aaron"

# str and int
my_list = ["apple", "boy", "123", "cat"]
smallest = min(my_list) 
print(smallest)  # Output: "123"

# max() function to return the largest element
my_list = [45, 12, 9, 1]
largest = max(my_list)
print(largest)  # Output: 45

# using /, //, and % operators
my_list = [5 / 2, 5 // 2, 5 % 2] # Create a list with the results of division, floor division, and modulo operations
largest = max(my_list)     # Calculate the largest element in the list
print(largest)             # Output: 2.5

# TypeError with numeric and non-numeric elements
# my_list = [1, 2, 3, 4, "5"] # Create a list with a mix of numbers and a string
# largest = max(my_list)
# print(largest) # TypeError: '>' not supported between instances of 'str' and 'int'

# str elements
my_list = ["zzz", "zz", "zzzz", "z"] # Create a list with string elements
last = max(my_list)      # Calculate the largest string in the list
print(last)              # Output: "zzzz"