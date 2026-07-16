# 2D list: list of lists
my_2d_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(my_2d_list) # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# empty lists
my_empty_2d_list = [[], [], []]
print(my_empty_2d_list) # Output: [[], [], []]

# readable 2D list
populous_cities = [
                    ["USA", "New York City", "Los Angeles", "Chicago"],
                    ["France", "Paris", "Marseille", "Lyon"],
                    ["China", "Shanghai", "Beijing", "Chongqing"],
                    ["India", "Mumbai", "Delhi", "Bangalore"]
                  ]
print(populous_cities) # outputs the inner lists in a single line

# access inner list by outer index
colors = [
            ["#de0c1c", "#fe2d2d", "#fb7830", "#fecf02", "#ffdd46"],
            ["#1db4d4", "#246fb4", "#100ab6", "#130976", "#110240"],
            ["#ebe9e7", "#c4bdb7", "#8a7b70", "#4f3928", "#3c2411"]
         ]
print(colors[2])

print(colors[0])  # print the first inner list.  
print(colors[1])  # print the second inner list.  
print(colors[2])  # print the third inner list.

# access inner list element by outer and inner index
print(colors[0][1])  # Print second element of the first inner list. 
                     # Output: #fe2d2d

# concatenate inner lists with + operator
list_1 = [[1, 2, 3], [4, 5, 6]]
list_2 = [[7, 8, 9], [10, 11, 12]]

print(list_1 + list_2) # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
print(list_2 + [[13, 14, 15]]) # Output: [[7, 8, 9], [10, 11, 12], [13, 14, 15]]

# concatenate traditional list to inner list with + operator
print(list_2 + [16, 17, 18]) # Output: [[7, 8, 9], [10, 11, 12], [13, 14, 15], 16, 17, 18]
# list changes to 6 elements, but the last 3 elements are not in a list.

# TypeError: can only concatenate list (not "int") to list
# list_2 = [[7, 8, 9], [10, 11, 12]]

# print(list_2 + 13) # This will raise a TypeError

# append a new inner list with append() method
my_list = [["a", "b", "c"], ["d", "e", "f"]]
another_list = ["g", "h", "i"]

my_list.append(another_list)
print(my_list) # Output: [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]

# append list_2 to add a traditional list to the end of list_2 for a new inner list
list_2 = [[7, 8, 9], [10, 11, 12], [13, 14, 15]]

list_2.append([16, 17, 18])
print(list_2) # Output: [[7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]

# for loop to access length of each inner list
mountains = [
              ["Mount Everest", "K2", "Kangchenjunga"],
              ["Denali", "Mount Logan", "Pico de Orizaba"],
              ["Mount Kilimanjaro", "Mount Kenya", "Mount Ngaliema"]
            ]

for mountain in mountains:
  if len(mountain) <= 6:
    print(mountain) # outputs each inner list that has 6 or fewer elements

# nested loop to access inner elements in mountains 2D list
for row in range(3): # loop through each inner list
    for column in range(3): # loop through each element in the inner list
        if len(mountains[row][column]) <= 6: # check if the element's str length <= 6
            print(mountains[row][column]) # Output: K2, Denali  

# iterate over the list of numbers and print Even and Odd starting with the first element in the first inner list
# Outputs a sequence of Odd and Even across all inner lists in the 2D list
numbers = [
            [11, 13, 22, 76, 54],
            [2, 65, 107, 112, 8],
            [33, 90, 34, 7, 804]
          ]

for row in range(3): # loop through each inner list
    for column in range(5): # loop through each element in the inner list
        if numbers[row][column] % 2 == 0: # check if the number is even
            print("Even") 
        else:
            print("Odd") 

# 10×10 2D list from list comprehension
# numbers declared with 10 outer lists (rows) and 10 inner lists (columns)
# each inner list has 10 random integers from 1 to 100
# new random values generated each time the code is run
import random

# numbers = [[random.randint(1, 101) for columns in range(10)] for rows in range(10)]
# print(numbers) # outputs in hard to read format with brackets and commas

# print using nested for loops for readability and remove brackets and commas from each inner list
# import random

numbers = [[random.randint(1, 101) for columns in range(10)] for rows in range(10)]
for row in numbers: # loop through each inner list
  for number in row: # loop through each element in the inner list
    print(f"{number} ", end="") # print each number with a space and no new line
  print()            # prints inner list and then prints newline character

# print a tab between each number instead of a space for better readability
for row in numbers:
  for number in row:
    print(f"{number}\t", end="")
  print()

# flipping columns and rows does not change the outer list and inner list structure
# import random

symbols = [["*" for columns in range(5)] for rows in range(7)]
print(symbols) # outputs 7 inner lists with 5 "*" in each inner list

# nested loop for formatted printing
for row in symbols:
  for symbol in row:
    print(f"{symbol} ", end="")
  print()

# loop to sort each outer list and each inner list
numbers = [
            [6, 7, 10, 9, 8],
            [12, 13, 14, 11, 15],
            [20, 18, 17, 19, 16],
            [1, 2, 3, 4, 5]
          ]
numbers.sort() # sorts the outer list in ASC based on the first element of each inner list
# loop to sort and print the 2D list
for row in numbers: # loop through each inner list
  row.sort()        # sort each inner list's elements in ascending order
  print(row)        # print each inner list after sorting

## loop to only sort each inner list

# numbers.sort() # comment out to not sort the inner lists 
# loop to sort and print the 2D list
for row in numbers: # loop through each inner list
  row.sort()        # sort each inner list's elements in ascending order
  print(row)        # print each inner list after sorting

# loop to compute sum of each inner list and total sum of all inner lists
numbers = [
            [6, 7, 10, 9, 8],
            [12, 13, 14, 11, 15],
            [20, 18, 17, 19, 16],
            [1, 2, 3, 4, 5]
          ]

# loop to print the sum of each inner list
for row in numbers:
  print(sum(row)) # outputs the sum of each inner list

## declare a variable to hold the total sum of all inner lists
total_sum = 0
# loop to add the sum of each inner list to total
for row in numbers:
  total_sum += sum(row)
print(total_sum)

# loop to compute the max of each inner list and the max of all inner lists
numbers = [
            [6, 7, 10, 9, 8],
            [12, 13, 14, 11, 15],
            [20, 18, 17, 19, 16],
            [1, 2, 3, 4, 5]
          ]

# loop to print the max of each inner list
for row in numbers:
  print(max(row)) # outputs the max of each inner list

## declare a variable to hold the max of all inner lists
largest = 0
# loop to find the max of all inner lists
for row in numbers:      # loop through each inner list
    if max(row) > largest: # check if the max of the current inner list is greater than the current largest
        largest = max(row) # update the largest variable with the new max value
print(largest)            # outputs the max of all inner lists

# reverse method to reverse the order of the outer list
cities = [
           ["Tokyo", "Paris", "Algiers"],
           ["New York", "Mexico City", "Lima"],
           ["Bangalore", "Moscow", "Nairobi"]
         ]

cities.reverse() # reverse the order of the outer list
print(cities) 

## loop to reverse the order of each inner list
cities = [
           ["Tokyo", "Paris", "Algiers"],
           ["New York", "Mexico City", "Lima"],
           ["Bangalore", "Moscow", "Nairobi"]
         ]

for row in cities: # loop through each inner list
    row.reverse()  # reverse the order of each inner list
    print(row)     # outputs the elements in each inner list reversed

## reverse method to reverse the order of the outer list and each inner list
cities = [
           ["Tokyo", "Paris", "Algiers"],
           ["New York", "Mexico City", "Lima"],
           ["Bangalore", "Moscow", "Nairobi"]
         ]

cities.reverse() # reverse the order of the outer list
for row in cities: # loop through each inner list
    row.reverse()  # reverse the order of each inner list
    print(row)     # outputs the inner lists in reverse order with the elements in each inner list also reversed
