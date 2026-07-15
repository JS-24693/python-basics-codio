# Nested Loop Example:
for row in range(10): # iterate through 10 rows
    for column in range(10): # iterate through 10 columns in each row
        print("#", end="") # print a hashtag without a newline
    print("") # add a new line character after each row

# Nested Loop Example to iterate through 5 rows:
for row in range(5): # iterate through 5 rows
    for column in range(10): # iterate through 10 columns in each row
        print("#", end="") # print a hashtag without a newline
    print("") # add a new line character after each row

# Nested Loop Example to iterate through 20 columns:
for row in range(5): # iterate through 5 rows
    for column in range(20): # iterate through 20 columns in each row
        print("#", end="") # print a hashtag without a newline
    print("") # add a new line character after each row

## Same Nested Loop but without end=""
for row in range(5): # outer loop controls number of rows
    for column in range(20): # inner loop prints 20 characters per row
        print("#") # print a hashtag with a newline
    print("")      # add a new line character after each row

# Nested Loop Example with Even and Odd rows
for row in range(5): # iterate through 5 rows
    for column in range(10): # iterate through 10 columns in each row
        if row % 2 == 0: # if row is even
            print("#", end="") # print a hashtag without a newline
        else: # if row is odd
            print("*", end="") # print an asterisk without a newline
    print("") # add a new line character after each row

# Nested Loop Example: outer loop starts at 1
# * operator repeats the string based on row value
# Nested loop is not necessary
for row in range(1, 6): # row = digit (1 to 5)
    print(str(row) * row) # repeated string based on row value

## Same example but with a Nested Loop
for row in range(1, 6):        # row = digit
    for column in range(row):  # repeat row times
        print(row, end="")     # print repeated digit
    print("")                  # newline

# Nested example without new"" 
for i in range(4):          # four blocks
    print("&&")             # top of block
    for j in range(3):      # run three times to output three stars
        print("*")
