# ------------------------------------------------------------
# Exercise 1: Helper Functions
# radius() computes distance; area() calls radius() to compute area.
# ------------------------------------------------------------

import math

def radius(x1, y1, x2, y2):
    """Distance formula to determine radius"""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def area(x1, y1, x2, y2):
    """Area of a circle using radius helper function"""
    return math.pi * (radius(x1, y1, x2, y2)**2)

print(area(0, 0, 4, 4))   # 100.53096491487341


# ------------------------------------------------------------
# Exercise 2: Using math.pow Instead of **
# Rewrite radius() and area() using math.pow.
# ------------------------------------------------------------

def radius_pow(x1, y1, x2, y2):
    """Distance formula using math.pow"""
    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

def area_pow(x1, y1, x2, y2):
    """Area using math.pow and radius_pow"""
    return math.pi * math.pow(radius_pow(x1, y1, x2, y2), 2)

print(area_pow(0, 0, 4, 4)) # 100.53096491487341


# ------------------------------------------------------------
# Exercise 3: Inner Functions
# radius() is defined inside area(), hidden from global scope.
# ------------------------------------------------------------

def area_inner(x1, y1, x2, y2):
    """Area of a circle using inner radius function"""
    def radius(x1, y1, x2, y2):
        """Inner distance formula"""
        return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    return math.pi * math.pow(radius(x1, y1, x2, y2), 2)

print(area_inner(0, 0, 4, 4)) # 100.53096491487341

# Calling radius() here would cause an error:
# print(radius(0,0,4,4))  # radius only defined locally, not visible globally


# ------------------------------------------------------------
# Exercise 4: Function Composition
# radius() returns a value passed directly into area().
# ------------------------------------------------------------

def area_r(r):
    """Area of a circle given radius"""
    return math.pi * math.pow(r, 2)

def radius_comp(x1, y1, x2, y2):
    """Distance formula to calculate radius"""
    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

print(area_r(radius_comp(0, 0, 4, 4)))  # function composition: output of radius_comp passed into area_r
                                        # 100.53096491487341


# ------------------------------------------------------------
# Exercise 5: Composition with Built‑in Functions
# Built‑ins cannot contain helper functions, but composition works.
# ------------------------------------------------------------

# convert string → int, then sqrt
print(math.sqrt(int("25")))          # 5.0 
# convert strings → ints, then exponent
print(math.pow(int("2"), int("3")))  # 8.0 - composition of built‑ins

# variation 1: nested helper 
def force(mass, dv, time):          # main function 
    """Calculate force: F = m * a"""
    def acceleration(dv, time):         # nested helper
       """Calculate acceleration (change in velocity over time)"""
       return dv / time
    return mass * acceleration(dv, time)

# ------------------------------------------------------------
# Exercise 6: Modularity — Turtle House Drawing
# Each function draws one shape; reposition() moves turtle.
# ------------------------------------------------------------

import turtle

t = turtle.Turtle()

def triangle(size):
    """Draw a triangle of given size"""
    for _ in range(3):
        t.lt(120)
        t.forward(size)

def rectangle(width, height):
    """Draw a rectangle with given width and height"""
    for _ in range(2):
        t.forward(width)
        t.lt(90)
        t.forward(height)
        t.lt(90)

def reposition(x, y):
    """Move turtle without drawing"""
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()

# Draw house
rectangle(100, 100) #draw the house
reposition(100, 100) #move to starting point for the roof
triangle(100) #draw the roof

# Draw door
reposition(40, 0) #move to starting point for the door
rectangle(20, 40) #draw the door

# Draw windows
reposition(10, 50) #move to starting point for the left window
rectangle(20, 20) #draw the left window

reposition(70, 50) #move to starting point for the right window
rectangle(20, 20) #draw the right window

# turtle.mainloop()

# import turtle

t = turtle.Turtle()

def triangle(size):
    """Draw a triangle of given size"""
    for _ in range(3):
        t.lt(120)
        t.forward(size)

def rectangle(width, height):
    """Draw a rectangle with given width and height"""
    for _ in range(2):
        t.forward(width)
        t.lt(90)
        t.forward(height)
        t.lt(90)

def reposition(x, y):
    """Move turtle without drawing"""
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()

# Draw house
rectangle(50, 50) #draw the house
reposition(50, 50) #move to starting point for the roof
triangle(50) #draw the roof

# Draw door
reposition(5, 0) #move to starting point for the door
rectangle(10, 20) #draw the door

# Draw windows
reposition(5, 30) #move to starting point for the left window
rectangle(10, 10) #draw the left window

reposition(35, 30) #move to starting point for the right window
rectangle(10, 10) #draw the right window

turtle.mainloop()
