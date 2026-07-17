# count uppercase and lowercase letters in a string, ignoring digits and symbols
lower_count = 0
upper_count = 0
my_string = "Roses are Red, Violets are Blue"

# count lowercase and uppercase characters, skip digits and symbols
for char in my_string:
    if char.islower():
        lower_count += 1
    elif char.isupper():
        upper_count += 1

print("There are {} lowercase characters.".format(lower_count))
print("There are {} uppercase characters.".format(upper_count))

# using f-string instead of .format() 
print(f"There are {lower_count} lowercase characters.")
print(f"There are {upper_count} uppercase characters.")

# print string in reverse order
my_string = "The brown dog jumps over the lazy fox"  # original string
reversed_string = ""  # strings are immutable, so build a new one
index = len(my_string) - 1    # start at last character

while index >= 0:
    reversed_string += my_string[index]  # append current character
    index -= 1    # move backward
print(reversed_string) 

# swap uppercase and lowercase characters
original_string = "THE BROWN DOG JUMPS over the lazy fox" # original string
modified_string = ""   # build a new one

for char in original_string:
    if char.islower():          # lowercase → uppercase
        modified_string += char.upper()
    else:                       # uppercase → lowercase
        modified_string += char.lower()

print("The original string is: {}".format(original_string))
print("The modified string is: {}".format(modified_string))

# using f-string instead of .format() 
print(f"The original string is: {original_string}")
print(f"The modified string is: {modified_string}")

# count vowels in a string
my_string = "The Brown Dog Jumps Over The Lazy Fox" # original string
vowels = "aeiou"
count = 0

for char in my_string:
    if char.lower() in vowels:  # convert to lowercase before checking vowel
        count += 1              # increment count

if count == 1:
    print("There is 1 vowel in the string")
else:
    print("There are {} vowels in the string".format(count))

# using f-string instead of .format() 
    print(f"There are {count} vowels in the string")

# replace each vowel with "*"
my_string = "Hello, World!"  # original string
masked_string = ""           # build a new string

for char in my_string:
    if char.lower() in "aeiou":  # check vowel in lowercase
        masked_string += "*"     # replace vowel
    else:
        masked_string += char    # keep original character

print(masked_string)

# program to print the first and last character of user input
txt = input("Enter a word or sentence: ")  # read user input
first = txt[0]        # first character
last = txt[-1]        # last character

print("{} is the first character and {} is the last character".format(first, last))

# print user input in a square (rows = columns = length of input)
txt = input("Enter a word or sentence: ")  # read user input

for _ in range(len(txt)):      # repeat for each row
    for _ in range(len(txt)):  # repeat for each column
        print(txt, end="")    # print the string without moving to a new line
    print()

# mark each character: u = uppercase, l = lowercase, - = neither
text = input("Enter a word or sentence: ")
result = ""  # build output string

for char in text:
    if char.isupper():      # uppercase → u
        result += "u"
    elif char.islower():    # lowercase → l
        result += "l"
    else:                   # non‑letter → -
        result += "-"

print(result)

# \n to print first half on one line, second half (extra char if odd) on next
txt = input("Enter text: ")
mid = len(txt) // 2  # second half gets the extra char when odd
print(txt[:mid] + "\n" + txt[mid:])

# swap letters two at a time in the string, assuming even number of characters.
text = input("Enter an even-length word: ")
result = ""

for i in range(0, len(text), 2):
    result += text[i + 1] + text[i]

print(result)
