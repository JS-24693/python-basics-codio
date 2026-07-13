# Python Basics – Codio Course

Practice files from Codio Programming in Python Certificate Course.
Includes introductory Python scripts and exercises.

# Printing.py Overview

Practice examples showing how Python prints text to the console, how newline behavior works, how to override the default ending character, and how comments (single‑line and multi‑line) appear in code.

## Newline Character
The print command automatically adds a newline character each time it is called.

## Comments and Markdown in .py Files
In .py files:  
Use comments that explain code behavior, logic, purpose, or errors.
Python comments use # for single‑line and triple quotes for multi‑line blocks.

In a README (Markdown):  
Use explanations, section headings, descriptions of concepts, and instructions.
Markdown is for documentation, not executable code comments.

# Variables.py Overview

This file demonstrates basic variable creation, assignment, and updates using strings, integers, floats, and booleans.

## Variable Names
Variable declaration is when you create a variable and assign it a value.
Enter the name of the variable, the assignment operator =, and the value to store.

## String Variables
Text, numbers, or symbols inside quotes are strings.
Strings are always surrounded by '' or "".

## Boolean Variables
Boolean values are either True or False.
They are used in conditionals and loops to control program flow.
Python is case‑sensitive. Boolean literals/first letters must be capitalized.

## Integer Variables
Integers (ints) are whole numbers, positive or negative.
Do not use commas in large numbers.
Base‑10 integers do not use leading zeros.

## Floating Point (Float) Variables
Floats are numbers with a decimal point, positive or negative.

# Module 1 Tutorial Labs Overview
These labs demonstrate basic variable assignment, value reassignment, and printing behavior in Python. 
Tutorial Lab 1 focuses on updating a variable and printing each new value, while Tutorial Lab 2 shows how different variable types can be reassigned and printed. The challenge below reinforces variable copying and output. 

## Tutorial Lab Challenge
Print the output **Python fundamentals are very useful**:

variable_1 = "Python fundamentals are very useful"
variable_2 = variable_1
print(variable_2)

# Arithmetic Operators
Type casting (or type conversion) changes a variable’s data type.  
The type command, type() returns the data type of the value stored in a variable: int, float, str, bool.

Booleans map to ints: False = 0, True = 1.

The + operator concatenates strings; the * operator repeats strings. 

Incrementing or decrementing changes a variable by a fixed amount. You will most often have a counting variable, which means you will increment or decrement by 1. (a += 1, a -= 1).

Addition uses +.  
Incrementing: a = a + 1 or a += 1.
The + operator concatenates strings. 

String concatenation is the act of combining two strings together. String concatenation uses +.  
Subtraction uses -.  
Strings cannot use -.

Subtraction uses -.
Decrementing uses -=.

Multiplication uses *.  
Shorthand: *=.  
Strings can be multiplied by ints. The * operator repeats strings.

Division uses /. It returns a float.  
Shorthand: /=.  
Floor division uses // for an int result.

Modulo (%) returns the remainder.  
It uses division internally but is not division.  
It can check even/odd and more.

Powers use ** (exponents, raise a number to a specific power).  
Square roots require math.sqrt or ** 0.5

Order of operations follows PEMDAS.
1.Parenthesis, 2. Exponents- powers and square roots, 3. Multiplication and Division- left to right, 4. Addition and Subtraction- left to right.

# Boolean Operators
Boolean operators return a boolean value (True or False).

The == operator determines equality (N.B. = is the assignment operator). 
The != operator checks if two values are not equal. 

Less Than < operator checks if one value is less than another value. Less Than or Equal To operator, <=, checks if one value is less than or equal to another value. 

Greater Than > operator checks if one value is greater than another value. Greater Than or Equal To >= checks if one value is greater than or equal to another value. 

The and Operator allows for more than one Boolean expression. Both must by true for the whole to be True. Everything else is False. 
When chaining several and Statements together, they are evaluated in a left-to-right manner. 

The or Operator allows for more than one boolean expression. Both must be false for the whole to be False. Everything else is true. 
When chaining several or Statements together, they are evaluated in a left-to-right manner.

The not operator produces the opposite of the boolean expression that it modifies. 

Short Circuiting: If Python can determine the result of a boolean expression before evaluating the entire thing, it will stop and return the value. 
If the first boolean expression for the or Operator is true, then the entire thing is true. The second boolean expression is ignored.
If the first boolean expression for the and Operator is false, then the entire thing is false. The second boolean expression is ignored.

# Module 2 Tutorial Labs Overview
These labs demonstrate arithmetic operators, concatenate and repeat strings, PEMDAS order of operations, and Boolean Operators in Python. 
Tutorial Lab 1 shows basic arithmetic operators and their outputs.
Lab 2 shows how + concatenates strings and * repeats them.
Lab 3 applies PEMDAS to a combined expression.
Lab 4 evaluates a compound Boolean expression. 
The lab challenge is to create a False boolean expression.

## Tutorial Lab Challenge
Boolean expression using one equality operator (== or !=), one of the less than operators (<, <=), one of the greater than operators (>, >=), and two different logical operators (and, or, not).
print(4==5 and 4<=5 or 4>5) # Output: False