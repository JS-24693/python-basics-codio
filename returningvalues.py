# ------------------------------------------------------------
# Exercise 1: Basic Return Keyword
# Functions return values instead of printing them.
# ------------------------------------------------------------

def add_five(num):
    """Add five to the parameter num and return the result"""
    return num + 5

new_number = add_five(10)     # function returns a value
print(new_number)             # printing the returned value

# print(add_five(10))         # direct print of return value

# understand return value: print() returns None
def print_hello():
    """Prints the string Hello"""
    print('Hello')              # prints Hello

print(type(print_hello()))      # NoneType class because print_hello() returns None
print(type(len('Hello')))       # int class because len() returns an integer

# ------------------------------------------------------------
# Exercise 2: Returning Different Data Types
# Demonstrates returning ints, floats, and strings.
# ------------------------------------------------------------

def return_int(num1, num2):
    """Return floor division result"""
    return num1 // num2

def return_float(num1, num2):
    """Return float division result"""
    return num1 / num2

def return_string(string):
    """Return 'Hello' concatenated with the given string"""
    return "Hello" + string

print(return_int(10, 3))
print(return_float(10, 3))
print(return_string(" friend"))

# ------------------------------------------------------------
# Exercise 3: Returning a List
# Functions can return lists; modify and return the list.
# ------------------------------------------------------------
#return list
def mult_by_5(my_list):
    '''Takes a list of ints and returns a new
    list where each element is multiplied by 5'''
    new_list = []
    for elem in my_list:
        new_list.append(elem * 5)
    return new_list

print(mult_by_5([1, 2, 3, 4, 5])) # [5, 10, 15, 20, 25]

# modify and return list
def modify_list(my_list):
    """Append a value and return the updated list"""
    my_list.append("added")
    return my_list

print(modify_list([1, 2, 3]))

# ------------------------------------------------------------
# Exercise 4: Side Effects — Updating a Global Variable
# Pure function returns a value; main program updates global.
# ------------------------------------------------------------

my_num = 0

def add_5(num):
    """Receive a number, add 5, return new number"""
    return num + 5

for i in range(10):
    my_num = add_5(my_num)    # global updated via return value
    print(my_num)             # side effect: output produced during update

# ------------------------------------------------------------
# Exercise 5: Side Effects — Why This Version Is Not Preferred
# Function reads global directly; less pure, harder to maintain.
# ------------------------------------------------------------

my_num = 0

def add_5_global():
    """Add 5 to global my_num and return new number"""
    return my_num + 5         # relies on external state

for i in range(10):
    my_num = add_5_global()   # updates global indirectly
    print(my_num)

# ------------------------------------------------------------
# Exercise 6: Pure Functions + Printing in Main Program
# No side effects inside functions; printing done outside.
# ------------------------------------------------------------

def is_even(num):
    """Return True if num is even"""
    return num % 2 == 0

def output(num):
    """Return even/odd message string"""
    if is_even(num):
        return "{} is an even number.".format(num)
    return "{} is an odd number.".format(num)

print(output(2))   # printing done in main program only
print(output(3))     # pure functions supply returned strings

# ------------------------------------------------------------
# Additional Practice
# ------------------------------------------------------------

# Create is_even function that takes the parameter num
def is_even(num):
    return(num % 2 == 0)

# Printing side effect: function produces external output
def has_letter_a(word):
    if "a" in word:
        print("{} has the letter 'a' in it.".format(word))   # side effect
    else:
        print("{} does not have the letter 'a' in it.".format(word))  # side effect
has_letter_a("apple")

# Pure function: returns a value, no internal side effects
def has_letter_a(word):
    if "a" in word:
        return "{} has the letter 'a' in it.".format(word)
    else:
        return "{} does not have the letter 'a' in it.".format(word)

print(has_letter_a("apple"))   # output happens here, outside the function

