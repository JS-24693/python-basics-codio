# Lab 1 odd or Even lists
import random  # import random library to generate random numbers

numbers = []            # declare an empty list to hold random numbers
for i in range(20):     # loop to generate 20 random numbers
    numbers.append(random.randint(0, 100))  # append a random number between 0 and 100 to the list

odd = []                # declare an empty list to hold odd numbers
even = []               # declare an empty list to hold even numbers

for number in numbers:  # loop through each number in the numbers list
    if number % 2 == 0: # check if the number is even
        even.append(number) # append the even number to the even list
    else:               # if the number is odd
        odd.append(number)  # append the odd number to the odd list

print("The odd numbers: ", odd)
print("The even numbers: ", even)
print(len(odd) + len(even)) # check that the total number of odd and even numbers equals 20 elements

# Lab 2 coding sum
# import random
numbers = []             # declare an empty list to hold random numbers
total = 0                # declare a variable to hold the total sum of the numbers

for i in range(20):      # loop to generate 20 random numbers
    numbers.append(random.randint(0, 100)) # append a random number between 0 and 100 to the list

for number in numbers:   # loop through each number in the numbers list
    total += number      # add the number to the total sum

print("The sum of numbers is ", total)
print(sum(numbers))  # check that the total sum equals the sum function output

# Lab 3 slicing a list 
# import random
numbers = []           # declare an empty list to hold random numbers

for i in range(9):     # loop to generate 9 random numbers
    numbers.append(random.randint(0, 100)) # append a random number between 0 and 100 to the list

length = len(numbers)  # declare a variable to hold the length of the numbers list
start = length // 3    # declare a variable to hold the starting index for slicing the list
stop = length // 3 * 2 # declare a variable to hold the stopping index for slicing the list
middle = numbers[start:stop] # slice the numbers list from the starting index to the stopping index 
                             # and assign it to the middle variable

print(numbers)                  # print the original numbers list
print("The middle is ", middle) # print the middle sliced list

# Lab 4 cross-referencing color lists
warm = ["red", "orange", "yellow", "burgundy", "pink", "rose", "pumpkin", "marigold", "gold", "citron", "amber"]
cool = ["blue", "green", "purple", "cyan", "violet", "indigo", "azure", "teal", "mint", "lime", "emerald"]
neutral = ["black", "white", "gray", "grey", "brown", "beige"]

# declare the variable colors with a list of random colors
colors = ["red", "black", "pink", "beige", "dark green", "azure", "amber", "light yellow"]
# declare count variables for each color category
warm_count = 0
cool_count = 0
neutral_count = 0
# declare a count variable for elements outside of the warm, cool or neutral lists
misc_count = 0

for color in colors:    # loop through each color in the colors list
    if color in warm:      # check if the color is in the warm list
        warm_count += 1      # increment the warm_count variable by 1
    elif color in cool:    # check if the color is in the cool list
        cool_count += 1      # increment the cool_count variable by 1
    elif color in neutral: # check if the color is in the neutral list
        neutral_count += 1   # increment the neutral_count variable by 1
    else:                  # if the color is not in the warm, cool or neutral lists
        misc_count += 1      # increment the misc_count variable by 1

print("The total # of colors is ", len(colors)) # print the total number of colors in the colors list
print("There are ", warm_count, " warm colors") # print the count of warm colors
print("There are ", cool_count, " cool colors") # print the count of cool colors
print("There are ", neutral_count, " neutral colors") # print the count of neutral colors
print("There are ", misc_count, " miscellaneous colors") # print the count of miscellaneous colors

# Lab challenge: changing a list of integers called numbers to print a list of elements odd or even

numbers = [1, 2, 3, 4] # declare a list of integers

final_result = [] # declare an empty list to hold the final result

for number in numbers:      # loop through each number in the numbers list
    if number % 2 == 0:        # check if the number is even
        final_result.append("even")       # append "even" to the final result list
    else:                      # if the number is odd
        final_result.append("odd")       # append "odd" to the final result list

print("The results are: ", final_result)

# Replace each element greater than 10 with "*"
numbers = [30, 1, 20, 4]

for number in numbers:
    if number > 10:
        numbers[numbers.index(number)] = '*'

print(numbers)

# print a list called my_list three times if the length of the list is less than 5, otherwise print the list once
# and one time if the length of the list is greater than or equal to 5
my_list = ['hi', 'hello']

if len(my_list) < 5:  # check if the length of my_list is less than 5
    print(my_list * 3)  # print the list three times
else:                 # if the length of my_list is greater than or equal to 5
    print(my_list)      # print the list once

my_list = [65, 111, 2, 81, 65, 32]

if len(my_list) < 5:  # check if the length of my_list is less than 5
    print(my_list * 3)  # print the list three times
else:                 # if the length of my_list is greater than or equal to 5
    print(my_list)      # print the list once

# print the first string when arranged in alphabetical order
strings = ['luck', 'cat', 'kid', 'house']
strings.sort()
print(strings.pop(0))   # remove and return the first element of the list after sorting

strings = ['duck', 'dddd', 'mouse', 'kite']
strings.sort()
print(min(strings))    # print the first string when arranged in alphabetical order using the min() function

# add the next two increasing numbers to a list that contains ints
numbers = [1, 2, 3, 4]

for i in range(2):            # loop to add the next two increasing numbers to the list
  new_number = numbers[-1] + 1 # add 1 to the last number in the list
  numbers.append(new_number)  # append the new number to the list
print(numbers)

## with negative ints
numbers = [-5, -4, -3, -2]

for i in range(2):   
  new_number = numbers[-1] + 1
  numbers.append(new_number)
print(numbers)

# Print the list in rows and columns without the brackets and commas
# and move diagonally from the top-left to the bottom right, replace each 0 with a 1
# data is the 2D list with 3 rows and 3 columns. 
# the variable number represents the number of rows and columns in the 2D list
data =   [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
          ]  # declare a 2D list with 3 rows and 3 columns

number = 3  # declare a variable to hold the number of rows and columns in the 2D list

for row in range(number):   # loop through each row in the 2D list
  for column in range(number):  # loop through each column in the 2D list
    if row == column:             # check if the row index is equal to the column index (diagonal elements)
      data[row][column] = 1          # replace the diagonal elements with 1
    print(f"{data[row][column]} ", end="") 
    # print the element in the current row and column with a space, without moving to a new line 
  print() 
  # print a new line after printing all columns in the current row