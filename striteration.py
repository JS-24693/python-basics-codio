# iterate through the string with a for loop and print each character
my_string = "Hello world"
for char in my_string:
    print(char)  # prints each character and prints newline 

# prints each character, comma, and space and prints newline
my_string = "10, 11, 12, 13, 14"
for char in my_string:
    print(char)

# prints each symbol represented by each description and prints newline 
my_string = "\u25A3\u25A8\u25D3\u25CC\u25A2"
for char in my_string:
    print(char)

# print full symbol sequence for each character in the string
my_string = "\u25A3\u25A8\u25D3\u25CC\u25A2"
for char in my_string:
    print(my_string)

# iterate through the string with a while loop and print each character
my_string = "Calvin and Hobbes"
length = len(my_string)
i = 0

while i < length:
    print(my_string[i])  # prints one character per iteration
    i += 1
