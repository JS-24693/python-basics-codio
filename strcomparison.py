# comparing with ==
string1 = "It's Friday!"
string2 = "It's Friday!"
print(string1 == string2)  # True

# comparing with !=
string1 = "It's Friday!"
string2 = "It's Monday."
print(string1 != string2)  # True

# return False
string1 = "It's Friday!"
string2 = "It's Friday!"
print(string1 != string2)  

# comparing with is
string1 = "It's Friday!"
string2 = "It's Friday!"
print(string1 is string2)  # True

# comparing with is not
string1 = "It's Friday!"
string2 = "It's Monday."
print(string1 is not string2) # True

# Same object id number
a = 1
b = 1
print(id(a))  # 10914496
print(id(b))  # 10914496

# Different object id number
a += 1        # variable now has a different value
print(id(a))  # 10914528  # different object id 
print(id(b))  # 10914496

# Capitalization
text = input("Type something and press 'Return': ")
print(text)

# compare strings while ignoring capitalization with lower()
print("This program will check to see if two values are the same.")
string1 = input("Enter a value: ").lower()
string2 = input("Enter another value: ").lower()
if string1 == string2:
    print("They are the same!")
else:
    print("They are not the same.")

# compare strings while ignoring capitalization with upper()
print("This program will check to see if two values are the same.")
string1 = input("Enter a value: ").upper()
string2 = input("Enter another value: ").upper()
if string1 == string2:
    print("They are the same!")
else:
    print("They are not the same.")

# alphabetical order
string1 = "apple"
string2 = "cat"
if string1 < string2:
    print("{} comes before {}".format(string1, string2))  # apple comes before cat
elif string1 is string2:
    print("{} is the same as {}".format(string1, string2))
else:
    print("{} comes after {}".format(string1, string2))

# variation 1
string2 = "apple"
if string1 < string2:
    print("{} comes before {}".format(string1, string2))
elif string1 is string2:
    print("{} is the same as {}".format(string1, string2)) # apple is the same as apple
else:
    print("{} comes after {}".format(string1, string2))

# variation 2
string2 = "Apple"
if string1 < string2:
    print("{} comes before {}".format(string1, string2))
elif string1 is string2:
    print("{} is the same as {}".format(string1, string2)) 
else:
    print("{} comes after {}".format(string1, string2))   # apple comes after Apple