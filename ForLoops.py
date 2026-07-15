# For Loops
# Spot the pattern:
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello") # Print "Hello" five times

# For Loop Example:
for i in range(5):
    print("Hello")
    # Output: Hello (printed five times)

# Understanding the For Loop with a range of 5:
for i in range(5):
    print("Loop #" + str(i))
    # Output: Loop #0
    #         Loop #1
    #         Loop #2
    #         Loop #3
    #         Loop #4

# Example 2: (i + 1) - Adjust loop indices:
for i in range(5):
    print("Loop #" + str(i+ 1))
    # Output: Loop #1
    #         Loop #2
    #         Loop #3
    #         Loop #4
    #         Loop #5

# Example 3: custom range(1, 6) - start, stop:
for i in range(1, 6):
    print("Loop #" + str(i))
    # Output: Loop #1
    #         Loop #2
    #         Loop #3
    #         Loop #4
    #         Loop #5

# Example 4: custom range(0, 10, 2) - start, stop, step:
for i in range(0, 10, 2):
    print("Loop #" + str(i))
    # Output: Loop #0
    #         Loop #2
    #         Loop #4
    #         Loop #6
    #         Loop #8

# Example 5: custom range(10, 0, -1) - start, stop, step:
for i in range(10, 0, -1):
    print("Loop #" + str(i))
    # Output: Loop #10
    #         Loop #9
    #         Loop #8
    #         Loop #7
    #         Loop #6
    #         Loop #5
    #         Loop #4
    #         Loop #3
    #         Loop #2
    #         Loop #1

# Running Total from 0 through 100:

# declare running total variable and set to 0
total = 0 

# loop from 0 to 100 and accumulate values
for i in range(101): # iterate through numbers 0 to 100
    total += i       # add current number to total
    print("Total: ", total) # print the running total

# Turtle Graphics:

import turtle

t = turtle.Turtle() # Create a turtle object called t

t.color('red') # requires a color string

t.shape('turtle') # requires one of the allowed shape strings

t.pensize(4) # requires a positive number

t.speed(1) # requires a 0–10 speed value

# Challenge One: 
# Program draws one large square with four smaller square paths using fixed moves and turns
# The for loop cannot be used because the movement sequence
# does not follow a predictable pattern of repeated distances or angles.

t.forward(100)

t.rt(90)

t.forward(20)

t.rt(90)

t.forward(20)

t.rt(90)

t.forward(120)

t.rt(90)

t.forward(20)

t.rt(90)

t.forward(20)

t.rt(90)

t.forward(120)

t.rt(90)

t.forward(20)

t.rt(90)

t.forward(20)

t.rt(90)

t.forward(120)

t.rt(90)

t.forward(20)

t.rt(90)

t.forward(20)

t.rt(90)

t.forward(20)

# Challenge Two:
# Program draws a circle

t.color('purple') # requires a color string

t.shape('turtle') # requires one of the allowed shape strings

t.pensize(6) # requires a positive number

t.speed(3) # requires a 0–10 speed value

for _ in range(360):
    t.forward(1)
    t.rt(1)

# Challenge Three:
# Program draws 45 lines in a growing square maze format

t.color('turquoise') # requires a color string

t.shape('turtle') # requires one of the allowed shape strings

t.pensize(8) # requires a positive number

t.speed(4) # requires a 0–10 speed value

# draw 45 lines in a growing square maze format
for i in range(46):
    t.forward(i * 10)  # side length grows each square
    t.rt(90)           # fixed right turn for square

turtle.mainloop() # launch the turtle graphics window
