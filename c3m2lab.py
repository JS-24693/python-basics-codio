# Recursive Power
def recursive_power(base, exponent):
    """Return base^exponent using recursion."""
    # Base case: anything^0 = 1
    if exponent == 0:
        return 1
    # Recursive case: base^exp = base * base^(exp-1)
    return base * recursive_power(base, exponent - 1)

# test calls
print(recursive_power(5, 3))   # 125
print(recursive_power(4, 5))   # 1024

# Recursive summation from num down to 0
def my_recursive_function(num):
    """Recursive summation from num down to 0."""
    if num < 0:                 # base case: recursion stops when num is below 0
        return 1                # base-case return value (adds an extra 1 to total)
    else:
        return num + my_recursive_function(num - 1)  # recursive step: add num and reduce

# test call
print(my_recursive_function(15))  # 136

# Variation 1 base case returns 0 for summation
def my_recursive_function(num):
    """Recursive summation from num down to 0."""
    if num < 0:                 # base case: recursion stops when num is below 0
        return 0                # correct base case for standard summation
    else:
        return num + my_recursive_function(num - 1)  # recursive step: add num and recurse downward

# test call
print(my_recursive_function(15))  # 120

# Variation 2 using int as element

# Recursive summation from int down to 0
def recursive_sum(int):
    """Return the sum of all integers from int down to 0."""
    if int == 0:                # base case: stop recursion
        return 0                # correct base case for summation
    else:
        return int + recursive_sum(int - 1)  # recursive case: reduce int toward 0

# test call
print(recursive_sum(5))  # 15

# Recursive summation for a list of numbers
def list_sum(nums):
    """Return the sum of all numbers in the list."""
    if len(nums) == 0:              # base case: empty list
        return 0
    else:
        return nums[0] + list_sum(nums[1:])   # recursive case: head + sum(tail)

# test calls
print(list_sum([1, 2, 3, 4]))  # 10
print(list_sum([1, 2, 3, 4, 5]))  # 15
print(list_sum([10, 12.5, 10, 7]))  # 39.5

# Variation 1: Recursive summation with integer as element
# Recursive bunny-ears calculation
def bunny_ears(bunnies):
    """Return the number of bunny ears (2 per bunny) using recursion and addition."""
    if bunnies == 0:                # base case: no bunnies left
        return 0                    # contributes 0 ears
    else:
        return 2 + bunny_ears(bunnies - 1)   # recursive case: add 2 ears per bunny

# test call
print(bunny_ears(5))  # 10
print(bunny_ears(0))  # 0

# Recursive function to return str in reverse order
def reverse_string(s):
    """Return the string s in reverse order."""
    if len(s) == 0:          # base case: empty string
        return ""
    else:
        return s[-1] + reverse_string(s[:-1])   # last char + reverse of the rest

# test call
print(reverse_string("cat"))  # tac
print(reverse_string("house"))  # esuoh

# Recursive function for largest element
def get_max(nums):
    """Return the largest number in the list."""
    if len(nums) == 1:                 # base case: single element is the max
        return nums[0]
    else:
        return max(nums[0], get_max(nums[1:]))  # recursive case: compare head with max of remaining list

# test calls
print(get_max([1, 2, 3, 4, 5]))  # 5
print(get_max([11, 22, 3, 41, 15]))  # 41

# Recursive Tree
import turtle

t = turtle.Turtle()
t.lt(90)          # Point upward
t.penup()
t.backward(150)   # Move starting position down
t.pendown()
t.speed(10)       # Faster drawing

def recursive_tree(branch_length, angle, t):
    """Draw a binary fractal tree recursively."""
    # Base case: stop when branch is too small
    if branch_length > 1:
        t.forward(branch_length)      # Draw branch
        t.right(angle)                # Right branch
        recursive_tree(branch_length - 7, angle, t)

        t.left(angle * 2)             # Swing left past original heading
        recursive_tree(branch_length - 7, angle, t)

        t.right(angle)                # Restore heading
        t.backward(branch_length)     # Return to branch origin

# Initial call
recursive_tree(60, 20, t)
# turtle.mainloop()

# Variation 1: same fractal tree
# import turtle

t = turtle.Turtle()
t.speed(10)

# rotate turtle 90 degrees left before drawing
t.left(90)

def recursive_tree(branch_length, angle, t):
    """Draw a binary fractal tree recursively."""
    if branch_length > 1:                 # base case
        t.forward(branch_length)          # draw branch
        t.right(angle)                    # right branch
        recursive_tree(branch_length - 7, angle, t)

        t.left(angle * 2)                 # swing left past heading
        recursive_tree(branch_length - 7, angle, t)

        t.right(angle)                    # restore heading
        t.backward(branch_length)         # return to origin

# initial call
recursive_tree(60, 20, t)
# turtle.mainloop()

# Hilbert Curve
# import turtle

t = turtle.Turtle()
t.speed(10)

def hilbert(dist, rule, angle, depth, t):
    """Draw Hilbert curve recursively."""
    # Base case: stop when depth reaches zero
    if depth > 0:          # continue recursion only when depth > 0

        if rule == 1:      # rule 1 turn pattern
            t.left(angle)
            hilbert(dist, 2, angle, depth - 1, t)
            t.forward(dist)
            t.right(angle)
            hilbert(dist, 1, angle, depth - 1, t)
            t.forward(dist)
            hilbert(dist, 1, angle, depth - 1, t)
            t.right(angle)
            t.forward(dist)
            hilbert(dist, 2, angle, depth - 1, t)
            t.left(angle)

        if rule == 2:      # rule 2 turn pattern    
            t.right(angle)
            hilbert(dist, 1, angle, depth - 1, t)
            t.forward(dist)
            t.left(angle)
            hilbert(dist, 2, angle, depth - 1, t)
            t.forward(dist)
            hilbert(dist, 2, angle, depth - 1, t)
            t.left(angle)
            t.forward(dist)
            hilbert(dist, 1, angle, depth - 1, t)
            t.right(angle)

# Initial call
hilbert(5, 1, 90, 5, t)
# turtle.mainloop()

# Sierpinski Triangle
# import turtle

t = turtle.Turtle()
t.speed(10)

def draw_triangle(length):
    """Draw a single triangle of given side length."""
    t.setheading(180)         # Ensure consistent orientation
    for _ in range(3):
        t.rt(120)
        t.fd(length)

def sierpinski(length, n):
    """Draw Sierpinski triangle recursively."""
    # Base case: draw one triangle
    if n == 1:
        draw_triangle(length)
    else:
        # Recursive cluster of three triangles
        sierpinski(length, n - 1)
        t.rt(120)
        t.fd(length * 2 ** (n - 2))   # Correct spacing
        sierpinski(length, n - 1)
        t.lt(120)
        t.fd(length * 2 ** (n - 2))
        sierpinski(length, n - 1)
        t.fd(length * 2 ** (n - 2))

# Initial call
sierpinski(20, 4)
turtle.mainloop()
turtle.bye()