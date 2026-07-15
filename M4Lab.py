# For Loop Example
for x in range(0, 10): # range from 0 to 9
    if x % 2 == 0: # if x is even
        print("Even")
    else: # if x is odd
        print("Odd")

# For Loop range from 1 to 10
for x in range(1, 11): # range from 1 to 10
    if x % 2 == 0: # if x is even
        print("Even")
    else: # if x is odd
        print("Odd")

# For Loop Example with a heading
my_string = "Here is the word 'Hello' 15 times:"
print(my_string)
for i in range (0, 5):
    print("Hello " * 3)

# For Loop Example for calculating powers (exponents)
exp = 4 # exponent
base = 2 # base
result = 1 # initial value
for x in range(exp): # loop through the exponent
    result = base * result # multiply the base by the current result
    
print(result) # print the final result

# While Loop Counter Example
counter = 0 # initialize the counter

while(counter < 10): # while the counter is less than 10
    print(counter) # print the current value of the counter
    counter = counter + 1 # increment the counter by 1 
print('while loop ended') # print a message when the while loop has ended

# Breaking from the while loop
result = 0 # initialize the result

while True: # infinite loop
    print('Enter numbers to sum, enter q to quit') # print instructions
    inp = input('> ') # get user input, read user input as a string
    if inp != 'q': # if the input is not 'q'
        if inp.isdigit(): # if the input is a digit
            result += int(inp) # add the input to the result
        else:
            print("Please enter a valid number.") # print an error message
    else: # if the input is 'q'
        print(result) # print the final result
        break # exit the loop

# Interrupt a while loop
time = 2 # initialize the time

while True: # infinite loop
    print('The time is ', str(time)) # print the current time
    if time == 2: # if the time is 2
        time = 6 # change the time to 6
    else:
        break # exit the loop

# Nested Loop Chessboard 
for row in range(8):
    if row % 2 == 0: # if the row index is even
        for column in range(8): # loop through the columns
            if column % 2 == 0: # if the column index is even
                print("X", end="") # print a X
            else:
                print("O", end="") # print a O
        print()
    else:
        for column in range(8): # loop through the columns
            if column % 2 == 0: # if the column index is even
                print("O", end="") # print a O
            else:
                print("X", end="") # print a X
        print()

# create a for loop that prints the sum of all the numbers between 0 and 100. 
total = 0
for i in range(101):
    total += i
print(total)

# create a while loop that prints the sum of all the numbers between 0 and 100.
total = 0 # initialize the total
count = 0 # initialize the count

while True: # infinite loop
    if count > 100: # if count exceeds 100
        break   # exit the loop
    else:     # if count is not greater than 100
        total = total + count # add the current count to the total
        count += 1 # increment the count by 1
print(total) # print the final total

# Nested loop to produce a pattern
# ....1
# ...2
# ..3
# .4 
# 5
for num in range(1, 6):              # outer loop
    print("", end="")                # outer-loop print (does not affect pattern)
    for dots in range(5 - num, 0, -1):  # inner loop: print decreasing dots - start, stop, step
        print(".", end='')              # print each dot without newline
    print(num)        # prints the number and defaults to a newline character

# Count‑controlled for loop using string‑multiplication for the pattern
for i in range(1, 6): # loop through numbers 1 to 5 - start, stop
    print("." * (5 - i) + str(i))   # build dots by string‑multiplication, then append the number

# Turtle Graphics 

import turtle

# Create a turtle object
t = turtle.Turtle()

t.color('green') # requires a color string

t.shape('turtle') # requires one of the allowed shape strings

t.pensize(4) # requires a positive number

t.speed(2) # requires a 0–10 speed value

# line drawing with five separated boxes
for outer_loop in range(4): # loop through the outer loop
    for inner_loop in range(4): # loop through the inner loop
        t.forward(50) # move the turtle forward by 50 units
        t.rt(90)      # turn the turtle right by 90 degrees
    t.forward(100) # move the turtle forward by 100 units
for last_loop in range(4): # loop through the last loop
    t.forward(50) # move the turtle forward by 50 units
    t.rt(90)      # turn the turtle right by 90 degrees

turtle.mainloop() # launch the turtle graphics window