# attempt to read missing file (raises FileNotFoundError)
# read_file = open("student_folder/text/readpractice.txt", "r")
# read_file.close()

# open + print file object
# read_file = open("student_folder/text/read_practice.txt", "r")
# print(read_file)  # print file object metadata
                  # expected output: <_io.TextIOWrapper name='student_folder/text/read_practice.txt' mode='r' encoding='UTF-8'>
# read_file.close()

# print each line
# read_file = open("student_folder/text/read_practice.txt", "r")
# print(read_file.readlines)
# read_file.close()    # expected: ['Python was created by Guido van Rossum.\n',
                     #            "It was named for the TV show Monty Python's Flying Circus.\n",
                     #            'Version 1 was released in January 1994.\n',
                     #            'Python 2.0 was released in October 2000.\n',
                     #            'The third version came out in December 2008.']

# print each line individually.
# with open("student_folder/text/read_practice.txt", "r") as read_file:
#    for line in read_file.readlines():
#      print(line) # expected: Python was created by Guido van Rossum.
                  #
                  #           It was named for the TV show Monty Python's Flying Circus.
                  #
                  #           Version 1 was released in January 1994.
                  #
                  #           Python 2.0 was released in October 2000.
                  #
                  #           The third version came out in December 2008.

# remove blank line spacing
# with open("student_folder/text/read_practice.txt", "r") as read_file:
#    for line in read_file.readlines():
#        print(line, end="")

# print uppercase lines
# with open("student_folder/text/read_practice.txt", "r") as read_file:
#    for line in read_file.readlines():
#        print(line.upper(), end="")

# replace "a" with emoji
# with open("student_folder/text/read_practice.txt", "r") as read_file:
#    for line in read_file.readlines():
#        print(line.replace("a", "\U0001F61C"), end="")

# read one line
# with open("student_folder/text/read_practice.txt", "r") as read_file:
#   print(read_file.readline()) # expected: Python was created by Guido van Rossum.

# read two lines
# with open("student_folder/text/read_practice.txt", "r") as read_file:
#    print(read_file.readline(), end="") # Python was created by Guido van Rossum.
#    print(read_file.readline(), end="") # It was named for the TV show Monty Python's Flying Circus.

# for loop readlines() variation
# with open("story.txt", "r") as input_file:
#    lines = input_file.readlines()
#    for line in lines:
#        print(line, end='') # expected: file contents printed verbatim

# while loop readline()
# with open("student_folder/text/read_practice.txt", "r") as read_file:
#    line = read_file.readline()
#    while line != "":
#        print(line)
#        line = read_file.readline() # expected output matches for loop readlines

# while loop readlines()
# with open("student_folder/text/read_practice.txt", "r") as read_file:
#    line = read_file.readlines()
#    while line != "":
#        print(line)
#        line = read_file.readline() # expected out matches read_file.readlines

# seek to offset then read using index parameter
# with open("student_folder/text/read_practice.txt", "r") as read_file:
#    read_file.seek(30)          # n Rossum.
#    print(read_file.readline())
#    read_file.seek(0)
#    print(read_file.readline()) # Python was created by Guido van Rossum.

# seek far beyond EOF
# with open("student_folder/text/read_practice.txt", "r") as read_file:
#    read_file.seek(1000)        # 0 reads
#    print(read_file.readline()) # returns empty string. 
#    read_file.seek(0)           # 1 read
#    print(read_file.readline()) # Python was created by Guido van Rossum.

# invalid negative seek ValueError: negative seek position -1
# with open("student_folder/text/read_practice.txt", "r") as read_file:
#    read_file.seek(-1)
#    print(read_file.readline())
#    read_file.seek(0)
#    print(read_file.readline())

# read file twice
# with open("student_folder/text/read_practice.txt", "r") as read_file:
#    print("First Time")                 # First Time
#    for line in read_file.readlines():
#        print(line, end="")             # Prints text 
#    read_file.seek(0)
#    print("\n\nSecond Time")            # Second Time
#    for line in read_file.readlines():
#        print(line, end="")             # Prints text

# copy file contents
# with open("student_folder/text/read_practice.txt", "r") as source, open("student_folder/text/destination.txt", "w") as dest:
#    for line in source.readlines():
#        dest.write(line)

# write uppercase to destination
# with open("student_folder/text/read_practice.txt", "r") as source, open("student_folder/text/destination.txt", "w") as dest:
#    for line in source.readlines():
#        dest.write(line.upper())

# add newline before writing
# with open("student_folder/text/read_practice.txt", "r") as source, open("student_folder/text/destination.txt", "w") as dest:
#    for line in source.readlines():
#        line += "\n"
#        dest.write(line)
