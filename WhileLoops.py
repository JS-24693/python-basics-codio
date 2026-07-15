# While Loops

# While Loop syntax with a count variable value of 0
count = 0 # counting variable

while count < 5: # Loop condition
    print("Hello")
    count = count + 1 # Increment the counting variable
    # Output: Hello
    #         Hello
    #         Hello
    #         Hello
    #         Hello

# Example two with a loop condition of < 10
count = 0 # counting variable

while count < 10:
    print("Hello")
    count = count + 1
    # Output: Hello
    #         Hello
    #         Hello
    #         Hello
    #         Hello
    #         Hello
    #         Hello
    #         Hello
    #         Hello
    #         Hello

# Example three with an increment value of count + 2
count = 0 # counting variable

while count < 10:
    print("Hello")
    count = count + 2
    # Output: Hello
    #         Hello
    #         Hello
    #         Hello
    #         Hello

# Example four with a loop condition of < 0
## Commented out so that .py runs
# count = 0 # counting variable

# while count < 0:
#    print("Hello")
#    count = count + 2
    # Command executes
    # Loop does not run because the condition is false from the start

# Infinite Loop syntax with a count variable value of 0
# count = 0 

# while count < 5:
#    print("Hello")
    # Outputs "Hello" until the Python interpreter is stopped
    # due to an output limit.

# Infinite Loop using while True:
# import random

# while True:
#    print("This is an infinite loop")
#    rand_num = random.randint(1, 101) # random integer between 1 and 100
     # Execution continues forever and must be manually interrupted.

# Break Statement
count = 0

while count < 5:
    print("Hello")

    if count == 3: # stop loop when count reaches 3
        break # stop the loop
    count = count + 1 # Increment the counting variable

# Break Statement for while True:
import random

while True:
    print("This is an infinite loop")
    rand_num = random.randint(1, 101) # random integer between 1 and 100

    if rand_num > 75:
        print("The loop has ended")
        break # stop the loop

# break before print:
# import random

while True:
    print("This is an infinite loop")
    rand_num = random.randint(1, 101) # random integer between 1 and 100

    if rand_num > 75:
        break # stop the loop
#       print("The loop has ended") # Statement is unreachable

# Turtle Graphics

import turtle

# Create a turtle object
t = turtle.Turtle()

t.color('red') # requires a color string

t.shape('turtle') # requires one of the allowed shape strings

t.pensize(4) # requires a positive number

t.speed(1) # requires a 0–10 speed value

# Challenge One: 
# Program draws one large square with four smaller square paths using fixed moves and turns
# The While loop cannot be used because the movement sequence
# has no repeating condition and no state change.

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

count = 0 # counting variable

while count < 360: # While loop condition
    t.forward(1)
    t.rt(1)
    count = count + 1 # Update the counting variable

# Challenge Three:
# Program draws 45 lines in a growing square maze format

t.color('turquoise') # requires a color string

t.shape('turtle') # requires one of the allowed shape strings

t.pensize(8) # requires a positive number

t.speed(4) # requires a 0–10 speed value

# draw 45 lines in a growing square maze format
count = 0 # counting variable

while count < 46: # while loop condition
    t.forward(count * 10)
    t.rt(90)
    count = count + 1 # update the counting variable

turtle.mainloop() # launch the turtle graphics window
