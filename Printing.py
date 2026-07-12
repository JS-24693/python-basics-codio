#Printing to the console
print("Hello world") # prints statement in ""

"Hello world" 

#Newline Character
print("Hello")
print("world")

# overrides print command default newline character behavior
print("Hello ", end='')
print("world")

# prints to same line as above
print("Hello ", end="")
print("world")

# replaces newline default to print on same line with a tab character
print("Hello ", end='\t')
print("world")

# prints to same line with a custom ending character, !, after first word
print("Hello ", end='!')
print("world")

# prints with a custom ending character, !
print("Hello ", end='')
print("world!")

# Comments

#This is a Python comment
print("This is regular Python code")

'''
This is a multi-line comment
Try making one at the end of the code file
The IDE (this window) tries to help by adding the ending triple quotes automatically
'''

#add code below this line
#. . . .   
print("Red")
print("Orange") #the comment STARTS at the hash symbol
#print("Yellow");
print("Green")
print("Blue")
print("Indigo")
print("Violet")
print("These are the colors of a rainbow!");
#. . . .    
#add code above this line

# Comment out the line of code with error
#add code below this line
#. . . .   
# prnt("Red")
print("Orange") 
print("Yellow")
print("Green")
print("Blue")
print("Indigo")
print("Violet")
print("These are the colors of a rainbow!");
#. . . .    
#add code above this line

#Comment blocks

'''
This is a multi-line comment
You can then easily end the comment with a triple quote (see below)
'''

#You can also do a multi-line comment
#like this!
    
print("Notice code that runs is not the same color as single-line comments");
print("This feature is called syntax highlighting");
print("It is a common feature of IDEs");
