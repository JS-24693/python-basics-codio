# strip()
string1 = "Hello world"
string2 = "world"
print(string1.strip(string2)) # Hello

# string2
string1 = "Hello world"
string2 = "Hello"
print(string1.strip(string2)) # world

# remove just a few letters
string1 = "Hello world"
string2 = "ld"
print(string1.strip(string2)) # Hello wor

# strip() removes from beginning or end
string1 = "Hello world"
string2 = "ell"
print(string1.strip(string2)) # Hello world

# startswith()
my_string = "this is a string"
my_bool = my_string.startswith("this")
print(my_bool)  # True

# case sensitive
my_string = "this is a string"
my_bool = my_string.startswith("This")
print(my_bool)  # False

# add start parameter
my_string = "this is a string"
my_bool = my_string.startswith("is", 2)
print(my_bool)   # True

# add start and stop parameter
my_string = "this is a string"
my_bool = my_string.startswith("is", 2, 4) 
print(my_bool)   # True

# replace() method to replace a substring
my_string = "dog mouse fish dog bear"
new_string = my_string.replace("dog", "cat")
print(new_string)    # cat mouse fish cat bear

# find() returns index if word or character is found
string1 = "The brown dog jumps over the lazy fox."
string2 = "brown"
print(string1.find(string2))   # 4

# find() returns -1 if not found
string1 = "The brown dog jumps over the lazy fox."
string2 = "zebra"
print(string1.find(string2))   # -1

# upper() copies the original string and converts to uppercase
my_string = "the big brown dog"
print(my_string.upper())   # THE BIG BROWN DOG

# variation with upper and lowercase letters
my_string = "ThE bIg BrOwN dOg"
print(my_string.upper())   # THE BIG BROWN DOG

# variation with numbers and symbols
my_string = "123!@#"
print(my_string.upper())   # 123!@#

# lower()
my_string = "THE BIG BROWN DOG"
print(my_string.lower())   # the big brown dog

# variation with numbers and symbols
my_string = "214%#%"
print(my_string.lower())   # 214%#%

# capitalize()
my_string = "the big brown dog"
print(my_string.capitalize())  # The big brown dog

# variation
my_string = "tHe BiG bRoWn DoG"
print(my_string.capitalize())  # The big brown dog

# title()
my_string = "the big brown dog"
print(my_string.title())   # The Big Brown Dog

# variation
my_string = "thebigbrowndog"
print(my_string.title())   # Thebigbrowndog

# variation
my_string = "a1 1a a a a"
print(my_string.title())   # A1 1A A A A