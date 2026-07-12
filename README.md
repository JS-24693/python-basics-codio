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