# Function definition
def greet_twice():
    # function body must be indented
    print("Hello")
    print("Hello")

# Calling a function
def greet_twice():
    # defining does not execute
    print("Hello")
    print("Hello")

greet_twice()  # explicit call required

# Whitespace behavior
def greet_twice():
    # only indented lines belong to the function
    print("Hello")
print("Hello")  # runs immediately; not part of function

# Order matters
# greet_twice()  # error: function not yet defined

def greet_twice():
    # must be defined before calling
    print("Hello")
    print("Hello")

# help fution to explain other functions
help(len) # Output: Help on built-in function len in module builtins:

          #         len(obj, /)
          #         Return the number of items in a container.

# Docstring usage
def greet_twice():
    """Print 'Hello' two times."""  # docstring for help()
    print("Hello")
    print("Hello")

help(greet_twice)  # displays docstring
                   # Output: Help on function greet_twice in module __main__:

                   #         greet_twice()
                   #             Print the string 'Hello' two times

# define and call the function caesar_quote
def caesar_quote():
    """Print the Latin version of 'I came, I saw, I conquered'""" # create docstring
    print("Veni, vidi, vici")

caesar_quote  # print caesar_quote
help(caesar_quote) # include docstring in output

# Divide and Conquer Example
# Each shape is its own function; combining them draws the house.
import turtle

t = turtle.Turtle()

def roof():
    """Draw a triangle roof."""
    for _ in range(3):
        t.lt(120)
        t.forward(100)

def house():
    """Draw a square house."""
    for _ in range(4):
        t.rt(90)
        t.forward(100)

roof()   # draw roof
house()  # draw house

# turtle.mainloop()

# Variation 1: Add door
import turtle

t = turtle.Turtle()

def roof():
    """Draw a triangle roof."""
    for _ in range(3):
        t.lt(120)
        t.forward(100)

def house():
    """Draw a square house."""
    for _ in range(4):
        t.rt(90)
        t.forward(100)

def door():
    """Draw a rectangle door."""
    # move to door start
    t.rt(90)
    t.forward(100)
    t.rt(90)
    t.forward(60)

    # draw door
    t.rt(90)
    t.forward(40)
    t.rt(90)
    t.forward(20)
    t.rt(90)
    t.forward(40)

# combine the functions → full house
roof()
house()
door()

turtle.mainloop()
