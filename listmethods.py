# append(item)
my_list = [1, 2, 3]
new_element = 4 # add int to list

my_list.append(new_element) # Append the new element to the list
print(my_list) # Output: [1, 2, 3, 4]

new_element = "four" # add string to list
my_list.append(new_element) # Append the new element to the list
print(my_list) # Output: [1, 2, 3, 4, 'four']

new_element = len(my_list) # add length of list as integer to list
my_list.append(new_element) # Append the new element to the list
print(my_list) # Output: [1, 2, 3, 4, 'four', 5]

new_element = my_list[0] # add first element of list as integer to list

my_list.append(new_element)
print(my_list) # Output: [1, 2, 3, 4, 'four', 5, 1]

# remove and return the last element using pop()
my_list = [1, 2, 3, 4] # create a list with 4 elements
print(my_list)       # Output: [1, 2, 3, 4]
print(my_list.pop()) # remove and return the last element. Output: 4
print(my_list)       # print the modified list. Output: [1, 2, 3]

# remove and return the last element using pop() to empty the list
my_list = [1, 2, 3, 4] # create a list with 4 elements
print(my_list)       # Output: [1, 2, 3, 4]
print(my_list.pop()) # remove and return the last element. Output: 4
print(my_list.pop()) # remove and return the last element. Output: 3
print(my_list.pop()) # remove and return the last element. Output: 2
print(my_list.pop()) # remove and return the last element. Output: 1
print(my_list)       # print the modified list. Output: []

# specify index of the element to remove when using pop()
my_list = [1, 2, 3, 4] # create a list with 4 elements
delete = 0             # index 0 refers to the first element
print(my_list.pop(delete)) # remove and return the first element. Output: 1
print(my_list) # print the modified list. Output: [2, 3, 4]

# Create a loop using range() and pop() to remove the last element
# [1, 2, 3, 4]
# [1, 2, 3]
# [1, 2]
# [1]
my_list = [1, 2, 3, 4]   # list with 4 elements

for i in range(4):       # loop 4 times using range()
    print(my_list)       # print the current list
    my_list.pop()        # remove the last element

# Insert an object to an array
my_list = [1, 2, 3, 4] # create a list with 4 elements
my_list.insert(2, "Hi") # insert "Hi" at index 2, 
# element at index 2 and all subsequent elements are shifted to the right
print(my_list)         # Output: [1, 2, 'Hi', 3, 4]

# TypeError: insert() requires index first, then value
# my_list = [1, 2, 3, 4]
# my_list.insert("Hi", 2)  # incorrect usage
# print(my_list)

# remove() method to remove an element by value
my_list = [1, 2, 3, 3, 4] # create a list with 5 elements
my_list.remove(3)         # remove the first occurrence of 3
print(my_list)            # Output: [1, 2, 3, 4]

# remove() the first value of 4
my_list = [1, 2, 3, 3, 4] # create a list with 5 elements
my_list.remove(2 *2) # remove the first occurrence of 4
print(my_list)       # Output: [1, 2, 3, 3]

# ValueError to remove element not in list
# my_list = [1, 2, 3, 3, 4] 
# my_list.remove(0)         # try to remove 0, which is not in the list
# print(my_list)            # Output: [1, 2, 3, 3, 4]

# remove() vs. pop()
list_1 = [1, 2, 3, 4, 5]  
list_1.pop()             # remove and return the last element
print(list_1)            # Output: [1, 2, 3, 4]

list_2 = [1, 2, 3, 4, 5]
list_2.remove(5)         # remove the first occurrence of 5
print(list_2)            # Output: [1, 2, 3, 4]

# Output of both methods
list_1 = [1, 2, 3, 4, 5]
print(list_1.pop())  # Output: 5
print(list_1)        # Output: [1, 2, 3, 4]

list_2 = [1, 2, 3, 4, 5]
print(list_2.remove(5))  # Output: None
print(list_2)            # Output: [1, 2, 3, 4]

# pop(): remove by index, returns the element
list_1 = [1, 2, 3, 4, 5]
print(list_1.pop(2))   # removes index 2 → returns 3
print(list_1)          # [1, 2, 4, 5]

# remove(): delete by value, returns None
list_2 = [1, 2, 3, 4, 5]
print(list_2.remove(2))  # removes the value 2 → returns None
print(list_2)            # [1, 3, 4, 5]

# count() method to count occurrences of an element
my_var = 2    # Define a variable with the value 2
my_list = [2, "red", 2.0, my_var, "Red", 8 // 4] 
# Create a list with various elements
print(my_list.count(2))  # Count occurrences of 2. Output: 4

# Declare the count() variable
my_list = [2, 4, 4.0, 6, 16/4, 12 % 5, 2.0, 4 * 0.5]
x = my_list.count(2)  # Count occurrences of 2. 
if x > 3:
    print("The value 2 appears more than 3 times.")

# index() method
my_list = ["dog", True, 16, "house", 55.9, False, 16]

index = my_list.index("house") # Find the index of the first occurrence of "house"
print(index)                   # Output: 3

index = my_list.index(False) # Find the index of the first occurrence of False
print(index)                 # Output: 5

index = my_list.index(16) # Find the index of the first occurrence of 16
print(index)                 # Output: 2

# sort() method
my_list = [23, 55, 11, 7, 82.9, -14, 0, 34]
print(my_list) # Output: [23, 55, 11, 7, 82.9, -14, 0, 34]

my_list.sort() # Sort the list in ascending order
print(my_list)  # Output: [-14, 0, 7, 11, 23, 34, 55, 82.9]

# sort() method in descending order
my_list = [23, 55, 11, 7, 82.9, -14, 0, 34]
print(my_list) # Output: [23, 55, 11, 7, 82.9, -14, 0, 34]

my_list.sort(reverse=True) # Sort the list in descending order
print(my_list)  # Output: [82.9, 55, 34, 23, 11, 7, 0, -14]

# sort() method with string elements 
my_list = ["zebra", "door", "apple", "cat", "deer", "bark"]
my_list.sort()
print(my_list)  # Sorts alphabetically
# Output: ['apple', 'bark', 'cat', 'deer', 'door', 'zebra']

# string elements with uppercase letters
my_list = ["APPLE", "apple", "Apple"]
my_list.sort()
print(my_list)  # Output: ['APPLE', 'Apple', 'apple']

# TypeError with mixed elements
# my_list = [23, 15, "red", 90, -8, False]
# my_list.sort()  # cannot sort a list with mixed types

# reverse() method to reverse the order of elements in the list 
my_list = ["north", True, 45, 12, "red"]
print(my_list)  # Output: ['north', True, 45, 12, 'red'] 
my_list.reverse() # Reverse the order of elements in the list
print(my_list)  # Output: ['red', 12, 45, True, 'north']

# with int
my_list = [1, 4, 6, 2, 7, 3, 5]
print(my_list)  # Output: [1, 4, 6, 2, 7, 3, 5]
my_list.reverse() # Reverse the order of elements in the list
print(my_list)  # Output: [5, 3, 7, 2, 6, 4, 1]