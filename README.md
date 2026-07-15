# Python Basics – Codio Course

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

## M1Lab.py Overview
These labs demonstrate basic variable assignment, value reassignment, and printing behavior in Python. 

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

## M2Lab.py Overview
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

## Mod3Lab.py Overview
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

## Module4lab.py Overview
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

