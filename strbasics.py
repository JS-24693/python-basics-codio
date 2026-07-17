# string length
my_string = 'Hello'  
length = len(my_string)
print(length)  # Output: 5

# Counts every character, including space
my_string = "Hello world"  
length = len(my_string)
print(length)  # Hello world

# string length
my_string = ""
length = len(my_string)
print(length) # Output: 0

# compare string length with 'if'
string1 = 'Hello'
string2 = "Hello world" 

if len(string1) > len(string2):
    print("String1 is longer.")

# reference a string character with index
my_string = "Hello!"
character = my_string[1]
print(character)    # Output: e

# strings are immutable; item assignment raises TypeError
# my_string = "House"
# my_string[0] = "M"      # invalid operation
# print(my_string)        # TypeError: 'str' object does not support item assignment

# assignment operator replaces the entire string
my_string = "House"
my_string = "Mouse"   # new value overwrites old value
print(my_string)    # Output: Mouse

# backslash joins physical lines into one logical string
# multiline literal prints as a single continuous line
my_string = "Hello world! This is a very, very long string. \
Even though this string is on three different lines, it should \
print as one line. Notice how the line breaks are different."
print(my_string)

# triple quotes preserve whitespace exactly as written
long_string = """Notice how this weird looking
    string is being
        printed."""
print(long_string)  # prints with original indentation and new lines

# 'in' checks whether a substring exists inside a string
my_string = "The brown dog jumps over the lazy fox."

print("dog" in my_string)  # True
print("cat" in my_string)  # False

# 'in' is case sensitive
print("Dog" in my_string)  # False

# returns True because the entire string contains itself
print(my_string in my_string)  # True

# slice returns characters from index 4 up to (not including) 9
my_string = "The brown dog jumps over the lazy fox."
my_slice = my_string[4:9]  # extracts "brown"
print(my_slice)            # brown

# slice with identical start/stop indexes returns empty string
my_string = "The brown dog jumps over the lazy fox."
my_slice = my_string[1:1]  # empty slice
print(my_slice)

# '\n' prints to a new line
my_string = "Hello\nworld"
print(my_string)  # Output Hello
                  #        world

# '\n\n' skips two lines
my_string = "Hello\n\nworld"
print(my_string)

# Use "" for outer string and '' inside to avoid syntax error
my_string = "And then she said, 'Hi there.'"
print(my_string)    # Outputs: And then she said, 'Hi there.'
