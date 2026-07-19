# Python Basics: Selection and Iteration – Codio Course 1

Practice files from Codio Programming in Python Certificate Course.
Includes introductory Python scripts and exercises.

## Printing.py Overview

Practice examples showing how Python prints text to the console, how newline behavior works, how to override the default ending character, and how comments (single‑line and multi‑line) appear in code.

### Newline Character
The print command automatically adds a newline character each time it is called.

### Comments and Markdown in .py Files
In .py files:  
Use comments that explain code behavior, logic, purpose, or errors.
Python comments use # for single‑line and triple quotes for multi‑line blocks.

In a README (Markdown):  
Use explanations, section headings, descriptions of concepts, and instructions.
Markdown is for documentation, not executable code comments.

## Variables.py Overview

This file demonstrates basic variable creation, assignment, and updates using strings, integers, floats, and booleans.

### Variable Names
Variable declaration is when you create a variable and assign it a value.
Enter the name of the variable, the assignment operator =, and the value to store.

### String Variables
Text, numbers, or symbols inside quotes are strings.
Strings are always surrounded by '' or "".

### Boolean Variables
Boolean values are either True or False.
They are used in conditionals and loops to control program flow.
Python is case‑sensitive. Boolean literals/first letters must be capitalized.

### Integer Variables
Integers (ints) are whole numbers, positive or negative.
Do not use commas in large numbers.
Base‑10 integers do not use leading zeros.

### Floating Point (Float) Variables
Floats are numbers with a decimal point, positive or negative.

## c1m1.py Overview
Course 1 Module 1 labs demonstrate basic variable assignment, value reassignment, and printing behavior in Python. 

### Tutorial Labs Content Overview
Tutorial Lab 1 focuses on updating a variable and printing each new value, while Tutorial Lab 2 shows how different variable types can be reassigned and printed. The challenge below reinforces variable copying and output. 

### Tutorial Lab Challenge
Print the output **Python fundamentals are very useful**:

## ArithmeticOperators.py Overview
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

## BooleanOperators.py Overview
Boolean operators return a boolean value (True or False).

### Equal to and Not equal to operators
The == operator determines equality (N.B. = is the assignment operator). 
The != operator checks if two values are not equal. 

### Less-than operators
Less Than < operator checks if one value is less than another value. Less Than or Equal To operator, <=, checks if one value is less than or equal to another value. 

### Greater-than operators
Greater Than > operator checks if one value is greater than another value. Greater Than or Equal To >= checks if one value is greater than or equal to another value. 

### and operator
The and Operator allows for more than one Boolean expression. Both must by true for the whole to be True. Everything else is False. 
When chaining several and Statements together, they are evaluated in a left-to-right manner. 

### or operator
The or Operator allows for more than one boolean expression. Both must be false for the whole to be False. Everything else is true. 
When chaining several or Statements together, they are evaluated in a left-to-right manner.

### not operator
The not operator produces the opposite of the boolean expression that it modifies. 

### Short Circuiting 
If Python can determine the result of a boolean expression before evaluating the entire thing, it will stop and return the value. 
If the first boolean expression for the or Operator is true, then the entire thing is true. The second boolean expression is ignored.
If the first boolean expression for the and Operator is false, then the entire thing is false. The second boolean expression is ignored.

## c1m2lab.py Overview
These labs demonstrate arithmetic operators, concatenate and repeat strings, PEMDAS order of operations, and Boolean Operators in Python. 

### Tutorial Labs Content Overview
Tutorial Lab 1 shows basic arithmetic operators and their outputs.
Lab 2 shows how + concatenates strings and * repeats them.
Lab 3 applies standard order of operations (PEMDAS) to a combined expression.
Lab 4 evaluates a compound Boolean expression. 
The lab challenge requires constructing a boolean expression that evaluates to False.

### Tutorial Lab Challenge
Create a Boolean expression using one equality operator (== or !=), one less-than operator (<, <=), one greater- than operator (>, >=), and two different logical operators (and, or, not).

## If.py Overview
The most common conditional is the if statement.

An if statement runs specific code only when its boolean condition is True.

An if statement includes if, a boolean expression, a colon, and an indented block (four spaces) containing the code that executes when the condition is True. 

## IfElse.py Overview
Use an if–else statement when one action should run if a boolean expression is True, and a different action should run when it is False. The else keyword introduces the code for the false case.

if and else are conditional keywords; their headers are not indented.

You can combine if–else with the modulo operator to check if a number is even or odd.

Nest if–else statements to handle multiple distinct conditions.

## CompdConds.py Overview
A compound conditional is an if statement containing more than one boolean expression.

Use the and or or keywords to link expressions.
You may use not, but only together with and or or.

Use a compound conditional when you need to test multiple comparisons, such as combining a less‑than and a greater‑than operator in the same boolean expression.

## IfElifElse.py Overview
elif means else if and adds additional decision checks after an initial if.
Use elif when you need more than two possible outcomes.

An elif statement follows these rules:
-An if statement must come first.
-elif is followed by a boolean expression and a colon.
-Indent four spaces for the code that runs when the elif condition is True.
-You may include as many elif statements as needed.
-A final else must come after the last elif.

## c1m3lab.py Overview
Conditionals are pieces of code that make a decision about what the program is going to do next.

### Tutorial Labs Content Overview
Lab 1 covers if statements to check whether a condition is True and run the corresponding code.
Lab 2 covers if–else statements to run one block when True and a different block when False.
Lab 3 covers compound conditionals using less‑than and greater‑than comparisons linked with and or or.
Lab 4 covers if‑elif‑else statements to evaluate a sequence of conditions, stopping at the first True one.
The lab challenge is to write a program to determine the month of the year based on the value of a variable called month.

### Tutorial Lab Challenge
Using the simplest conditional, if statement, the program continues to execute even after it reached a condition that is true.

## ForLoops.py Overview
For loops run a repeated code block using range() followed by a colon. All repeated statements must be indented.
Identify the pattern first, then write the loop.

Turtle Graphics
Turtle graphics let you draw shapes by moving a “turtle” around the screen with commands like forward(), left(), and right(). It is often used to visualize loop patterns.

Challenge One draws a large square with four smaller square paths using fixed forward moves and right turns. A for loop cannot be used because the movement sequence does not follow a predictable pattern of repeated distances or angles.
Challenge Two draws a circle by repeating the same forward move and 1‑degree turn 360 times. It does not use the loop variable because the counter value never affects the movement — the loop simply runs 360 identical steps to complete the circle.
Challenge Three draws a square‑maze pattern by increasing the forward distance each loop. The program multiplies the loop index i to generate longer forward moves, producing 45 expanding lines across growing square segments.

## WhileLoops.py Overview
While loops are useful when you are waiting for a certain event to occur.
While loop syntax — runs as long as its condition remains true. 
Counting variable — declare count = _ before the loop.
Incrementing — update the counter inside the loop so it eventually ends. count = count + _

Infinite loop causes — a condition that never becomes false, such as while True: or a variable that never gets incremented. If the counting variable is 0, it remains 0 and if it is less than the while loop condition, it will forever be less so the loop will never stop.

Break statement — immediately exits a while loop when a specific condition is met.

Turtle Graphics
Challenge One: A While loop cannot be used. Each forward/turn pair is a fixed, manual instruction, so only straight-line commands works.
Challenge Two: A While loop can be used but it adds no benefit over the for loop. You just repeat the same 360 steps until a counter reaches 360.
Challenge Three: replaces for with a manual counter.

## NestedLoops.py Overview
Nested loops run one loop inside another to create repeated digit‑pattern output.  
Refactor the three nested loops to reduce unnecessary repetition.  
Syntax: the outer loop selects the digit; the inner loop controls how many times it prints. 

Relationship: the outer loop selects the unit of work (row, block, or digit), and the inner loop repeats that work a fixed number of times per cycle.  
The inner loop starts fresh on every outer‑loop iteration, producing structured repeated patterns.

Relationship example explanation: The outer loop selects the row, and the inner loop repeats the column work. range(10) in the inner loop runs 10 times per row, producing a fixed repeated pattern each cycle. end="" keeps the pattern in columns in each row.

Relationship example explanation: the outer loop defines one block, and the inner loop repeats the block’s contents.  
`i` selects the block header (`&&`), and `j` runs three times to emit the three `*` lines, producing a fixed repeated pattern each cycle.

Relationship example explanation: The outer loop selects the digit, and the inner loop repeats it.  
`range(row)` runs exactly `row` times, so each digit prints as many times as its value.

## c1m4lab.py Overview
Module 4 tutorial labs demonstrates core loop structures and control flow in Python. 
Control flow is the set of rules that determine which lines of code run and in what order.
Loops repeat code, conditionals choose between branches, and break or similar statements alter the normal execution path.

It includes for‑loop examples for even/odd checks, fixed‑count repetition, and exponent calculation. The purpose of range in a for loop is to set up the number of iterations the loop will execute. 

It also shows while‑loop counters, breaking from infinite loops, and interrupting loop execution. The while loop must have an exit condition. By incrementing the counter variable, we ensure that the loop will eventually end. If you do not increment counter in this loop, you will create an endless loop because counter will never reach 10 or greater.
 
Lab Challenge: The file ends with a nested‑loop chessboard example separating logic into row parity and then column parity.

Row parity determines which pattern the row uses (condition true for even rows, condition false for odd rows).  
Column parity then alternates characters within that pattern.

Parity means checking whether an index is even or odd, which controls the pattern selection.

### Tutorial Lab Challenge
Nested Loop with a decision‑making structure to create a Chessboard:

This program builds the checkerboard by separating the logic into row parity and column parity.

- The outer loop selects each row.
- The program checks whether the row index is even or odd.
  - If the row index is even, the condition is **true**, and the row uses the pattern: even columns print `X`, odd columns print `O`.
  - If the row index is odd, the condition is **false**, and the row uses the flipped pattern: even columns print `O`, odd columns print `X`.

Row parity determines which pattern the row uses, and column parity determines the alternating characters within that pattern. This produces a checkerboard.

# Python Basic Structures: Lists, Strings and Files – Codio Course 2

## listbasics.py Overview
Lists are a built‑in data structure declared with [], with elements separated by commas. Elements may be of different data types.

range() creates a sequence of numbers; in a for loop you bind its values to a loop variable.

An empty list is written as [].

List elements are accessed by index, starting at 0; negative indices access items from the end.

Modify a list by assigning a new value to the element at its index using =.

## listoperators.py Overview
List concatenation uses + to join two lists.
List repetition uses * to repeat a list n times.

The in operator returns True or False based on membership.

len() returns the number of elements; len(my_list) == 0 checks for an empty list.

Slicing (:) returns a sublist using start (inclusive), stop (exclusive), and step.

## listmethods.py Overview
List methods are called by writing the list variable, a dot, the method name, and any parameters.

append() adds a single element to the end of the list.

pop() removes and returns the last element, or the element in a specified index.

insert() adds an element at a specified index.

remove() deletes the first matching element by value and returns nothing.

count() returns how many times a value appears in the list.

index() returns the index of a given value.

sort() orders the list in ascending order; sort(reverse=True) orders it in descending.

reverse() flips the list so elements appear from last to first.

## listnumbers.py Overview
Functions that work with lists of numbers:
sum() returns the total of all numeric elements; works with ints and floats, not strings.
min() returns the smallest element. For strings, it selects the earliest alphabetically; digits sort before letters, so "123" is smallest.
max() returns the largest element. For strings, it selects the latest alphabetically.

## listiteration.py
Iterating over a list processes each element from index 0 to the final index.

A for loop is the standard way to iterate; the list name is plural, and the loop variable is its singular form for readability.

A while loop can iterate but is less efficient because you must track the list length, manage an index variable, and increment it manually to access each element.

## _2dlist.py
A 2D list is a list whose elements are themselves lists.

### Declaring a 2D List
A 2D list is a list of lists. Declare with outer brackets and inner brackets, separated by commas; indent inner lists for readability.

### Accessing Elements
Indexing returns an inner list. Use `+` to concatenate lists. Use `append()` to add an inner list.

### Iteration
Iterate with indexes or nested loops to access inner‑list elements. Use `for element in sequence` for index‑free iteration.

### Printing
Use a single print statement to print a 2D list on one line. Use one for loop to print each inner list on a separate line. Use nested loops to print individual elements without brackets or commas and to control spacing.

### Sorting and Aggregation
Sort inner lists with a loop. Use loops with `sum()`, `min()`, or `max()`; initialize a total variable before summing.

### List Comprehension
A 10×10 list comprehension of random digits creates ten inner lists of ten elements. New random values appear on each run.

## c2m1lab.py
Lab 1 iterates through a list of random integers, classifies each as odd or even, and appends the value to the correct list. random.randint(start, stop) generates integers in the given range, e.g., (0, 100).

Lab 2 manually computes the sum of a list, then verifies the result against Python’s built‑in sum().

Lab 3 prints the middle third of a list by slicing the correct index range. Slicing a list requires integer indices, not float indices, so if needing to divide to identify start and stop, use floor division '//' operator.

Lab 4 cross‑references a list of random colors against warm, cool, and neutral color lists and counts matches and non‑matches.

The lab challenge builds a program that takes a list of integers and outputs a new list labeling each element as odd or even.

## strbasics.py
Strings are sequences of characters inside quotes. Each string has a length and each character has an index.
You can replace an entire string with the assignment operator, but you cannot modify individual characters.
Use \n for line breaks.
Use triple quotes to preserve whitespace.
The in operator checks if a character or substring exists in another string.
The slice operator (:) returns part of a string using start and stop indexes.
Escape characters begin with \ and signal special meaning.
Use double quotes for the outer string and single quotes inside to avoid syntax errors.

## strfunctions.py
String functions operate on a string and follow the syntax functionname(str) where the string is passed as a parameter.
len(my_string) returns the total number of characters, including spaces.
min(my_string) returns the smallest character by ASCII/Unicode order.
max(my_string) returns the largest character by ASCII/Unicode order.

## strmethods.py
A string method is a built‑in operation that acts on a string.
Methods use the syntax string.method(parameters) and are called with a dot after the string.
Common string methods include upper(), lower(), strip(), replace(), and split().

upper() and lower() convert characters to uppercase or lowercase.
capitalize() returns a copy with only the first character uppercase.
title() returns a copy with each word’s first letter uppercase.

strip() removes leading or trailing characters and returns a modified copy.
startswith() returns True or False if the string begins with a given substring. Optional to add the index numbers for start and stop parameters. Start is inclusive and Stop is exclusive.
replace() returns a copy with one substring replaced by another.
find() returns the index of a character or substring, or -1 if not found.

## striteraction.py
String iteration means processing a string one character at a time.
You can iterate using a for loop or by indexing with a while loop. Using a while loop to iterate over a string requires a variable to represent the length of the string and another to represent the index.
Iteration works by stepping through each character in sequence, starting at index 0 and advancing until the final index is reached.

## strcomparison.py
Use == and != to compare string values.
Use is and is not to compare object identity, not content.

is compares object identity, while == compares value.
When a = 1 and b = 1, Python reuses the same integer object, so their IDs match.
After a += 1, a becomes a different value, so Python allocates a new object and the ID changes.
Use is for identity checks on strings and other objects; use == for numeric value comparison.

String comparisons are case‑sensitive, so different capitalizations are not equal.
Alphabetical order is determined by Unicode/ASCII value, so strings compare based on character sequence.

## strformatting.py
String interpolation inserts values into a string. You can combine strings with + and type casting, or use commas to avoid concatenation.

.format() uses {} placeholders and substitutes values in order, unless you specify indexes inside the curly braces.

Main interpolation forms include f‑strings, .format(), and % formatting.

F‑strings embed expressions inside {}, such as listing the variable inside {}. They run fastest.

% formatting uses specifiers like %s and %d. It is older, still readable, but not recommended for new code.
%s means that the variable that will go in this position is a string.
%i refers to integer
%f refers to float.

## c2m2lab.py
Lab 1 — Count Uppercase and Lowercase  
Write a program that counts uppercase and lowercase letters in a string, ignoring digits and symbols.

Lab 2 — Reverse a String  
Write a program that prints a string in reverse order.

Lab 3 — Swap Case  
Write a program that outputs a new string where uppercase becomes lowercase and lowercase becomes uppercase.

Lab 4 — Count Vowels  
Write a program that counts vowels (a, e, i, o, u) in a string.

Lab Challenge — Replace Vowels  
Write a program that replaces each vowel in my_string with *. For example, "Hello" becomes "H*ll*".

## writingfile.py
- Navigate to the correct folder before creating or writing files.
- Opening a file in write (`w`) mode creates the file if it does not exist.
- Writing to a non‑existent file automatically creates a new empty file.
- `writelines()` writes a list of strings without adding newline characters.
- Writing to an existing file in write (`w`) mode erases its previous contents.
- **Write (`w`)** replaces the file; **append (`a`)** adds new content to the end.
- `open()` requires manual close; `with open()` auto‑closes the file and is safer.

## readingfile.py

- Open a file in read (`r`) mode to access its contents.
- Reading a file that does not exist raises a `FileNotFoundError`.
- Iterate line by line using:
  - for loop — automatically stops at end of file.
  - while loop — read until an empty string is returned.
- The end of file (EOF) is represented by `""` when using `read()` or `readline()`.
- readlines() reads all of the text file and returns all the strings in a list.
- readline() reads one string at a time.
- To read a file more than once, reset the pointer with `seek(0)`.
- Use `seek()` to jump to a position and search for a keyword manually.

File Reading + Writing Modes
read + write: read and overwrite existing content.
read + append: read and add new content to the end.

Read → Write between two files: open both files and transfer lines. Direction of Transfer:

Reading from dest → writing to source  
You take the already‑written output file (destination.txt) and push its contents back into the original file (read_practice.txt). This overwrites the source with whatever was in the destination.

Reading from source → writing to dest  
You take the original input file (read_practice.txt) and copy or transform its contents into a new output file (destination.txt). This preserves the source and produces a modified or duplicated version in the destination.

Strict summary:
dest → source: overwrite original with processed output.
source → dest: create new output without altering original.

## csvfile.py
- A CSV file is plain text where each row is a record and each value is separated by a delimiter (commas by default).
- Use import csv because csv.reader will error if the module isn’t imported.
- Print CSV contents by reading each row and formatting the fields for clarity.
- Data for each CSV row is stored as a list of strings after reading.
- Unpack loop variables by assigning each column to its own variable inside the `for` loop.
- Read and write CSV files using different delimiters (e.g., `,`, `;`, `|`) by specifying the delimiter in `csv.reader` and `csv.writer`.
- Use `writerow()` to write a single row and `writerows()` to write multiple rows at once.

## c2m3lab.py

### Lab 1 — Reading a File into a List
- Instead of using `seek(0)` to reread a file, load all lines into a list.
- Lists can be iterated multiple times without resetting a file pointer.
- This avoids repositioning the file cursor and simplifies repeated processing.

### Lab 2 — Summing Rows in a CSV
- Use `files-lab2.csv`, a comma‑delimited CSV containing integers (3 columns × 4 rows).
- Read each row, convert values to integers, and compute the row sum.
- Print the sum for each row in a clear, readable format.

### Lab 3 — Writing Superheroes to a CSV
- Ask the user for a superhero name and superpower.
- Write each pair to `superheroes.csv`.
- When the user enters `stop` for the name, the program ends.
- Demonstrates interactive CSV writing and loop termination.

### Lab 4 — Caesar Cipher Encryption/Decryption
- Encrypt letters (A–Z, a–z), digits (0–9), and symbols: space, `!`, `?`, `.`.
- Other characters are ignored (not encrypted).
- The cipher uses a key from 0–25.
- Encryption steps:
  - Build a list of all supported characters.
  - Find the character’s index.
  - Add the key to compute the encrypted index.
  - Wrap around the list if needed.
- Example: with key 13, `"K"` becomes `"X"`.
- Read from `student_folder/.labs/source.txt` and write encrypted output to `student_folder/text/encrypted.txt`.
- Lab includes both encryption and decryption.

### Lab Challenge — Replace Text in a File
- Read `student_folder/.labs/myanmar.txt`.
- Replace every instance of Burma with Myanmar.
- Print the transformed lines:
  - Myanmar is a country in Southeast Asia.
  - The capital of Myanmar is Naypyidaw.
  - Its population is about 54 million people.
  - Myanmar is a former British colony.

### Program to count lines and total characters
import sys — allows access to command‑line arguments and system-level features.

# Python Object Basics: Functions, Recursion, and Objects – Codio Course 3

## functionbasics.py
This file demonstrates core Python function concepts:
- how to define a function (header + body). Defining a function does not cause Python to run it.
- how to call a function
- how indentation affects execution
- why order matters (functions must be defined before use)
- how to add a docstring for help(). Triple quotes create a docstring for user-defined functions only, which Python stores as the function’s internal documentation. Even if the function definition already explains what it does, the docstring is still needed because it becomes the function’s official help text (function.__doc__) and is what help() displays.
- how functions support divide‑and‑conquer problem solving. Divide‑and‑conquer breaks a complex drawing task into small, single‑purpose functions. Each shape—roof, house, door—is its own function. Calling the functions in sequence produces the full house. This modular structure makes the program easier to understand, maintain, and extend.

Examples include defining greet_twice(), calling it, observing whitespace effects, adding docstrings, and using functions to structure drawing tasks.

## parameters.py
This file demonstrates Python function parameters:
- defining functions with parameters
- understanding positional vs named parameters
- passing different data types as parameters
- using try/except to handle parameter errors
- customizing TypeError messages
- defining optional parameters with default values. 
Call: You do not have to specify the optional parameter with the function call.
Definition: You must specify the optional parameter and its default value in the function definition.
- using variable‑length parameter lists via *args

Exercises include addition, add/subtract, named parameters, type inspection, error handling, optional parameters, and variable parameter lists.

## variablescope.py
This file demonstrates Python variable scope rules:
- local scope — variables created inside a function exist only inside that function
- global scope — variables created in the main program can be referenced inside functions
- global keyword — allows modification of a global variable from inside a function
- precedence — local variables override global variables when names collide
- scope resolution — understanding when a variable is accessible or shadowed

Exercises mirror the instructional examples: local‑only variables, multiple independent local scopes, referencing globals, modifying globals with global, and collisions between local and global names.

## returningvalues.py
This file demonstrates how Python functions return values instead of printing them. It covers:
- using the return keyword. Return keyword returns a value calculated by a function back to the program. Functions can return any valid datatype.
- understanding that print() returns None
- returning multiple data types (int, float, string, list)
- defining and identifying side effects
- writing pure functions that return values without modifying external state. Side effects are operations that change state or produce output during execution. A side effect is when a function causes a change that is external to the function itself. External changes — printing, modifying globals, writing files, changing state — are side effects.
Pure functions avoid these changes, which makes programs easier to test and less error‑prone. Pure functions simplify debugging because you only inspect inputs and outputs, not hidden state changes.
- showing how returned values can update global variables without using global
- separating computation (pure functions) from side effects (printing)

Exercises mirror the instructional examples: returning values, returning different types, list‑returning functions, global updates via returned values, and pure functions used inside a program that prints results.

## advancedconcepts.py
This file demonstrates advanced user‑defined function concepts:
- helper functions — Helper functions are functions that return a result used by another function.
They may be defined outside the function they support or nested inside it.
- inner functions — functions defined inside another function, hidden from the global scope
- Function composition passes one function’s result directly into another.
Composition of built‑ins chains built‑in functions so one output becomes the next input.
- modularity — dividing programs into reusable, independent functions

Exercises mirror the instructional examples: radius/area helper functions, math.pow variations, inner functions, function composition, readability comparisons, built‑in function composition, and modular turtle‑graphics drawing.

## c3m1lab.py
This module implements a command‑line movie‑sorting application. It covers:
- reading CSV movie data
- printing formatted movie rows
- sorting a list of lists by any column
- handling numeric vs string sorting (gross column)
- supporting ascending/descending order
- building a user interface loop
- validating user input with helper functions
- using composition of functions to structure the program. When one function takes another function as a parameter, this is called function composition.

The pass keyword is a placeholder for a function body. This allows you code to run without errors even though the function has not yet been written.

Labs progress from basic CSV reading → formatting → sorting → descending order → full CLI → helper functions → final challenge.