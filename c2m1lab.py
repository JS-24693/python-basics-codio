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
