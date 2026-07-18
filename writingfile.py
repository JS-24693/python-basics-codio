# create empty file
# output_file = open("student_folder/text/practice1.txt", "w")
# output_file.close()

# write single string
# output_file = open("student_folder/text/practice1.txt", "w")
# output_file.writelines("Hello there")
# output_file.close() # Hello there

# variation 1: change single string
# output_file = open("student_folder/text/practice1.txt", "w")
# output_file.writelines("Goodbye")
# output_file.close() # Goodbye

# variation 2: erase single string
# output_file = open("student_folder/text/practice1.txt", "w")
# output_file.writelines("")
# output_file.close() #

# write multiple strings separately
# output_file = open("student_folder/text/practice2.txt", "w")
# output_file.writelines("Hello ")
# output_file.writelines("there")
# output_file.close() # Hello there

# variation 1: \n
# write multiple strings separately
# output_file = open("student_folder/text/practice2.txt", "w")
# output_file.writelines("Hello\n")
# output_file.writelines("there")
# output_file.close() # prints on two lines

# variation 2: \n
# write multiple strings separately
# output_file = open("student_folder/text/practice2.txt", "w")
# output_file.writelines("Hello\nthere")
# output_file.close() # prints on two lines

# writelines() with list (fixed missing bracket)
# lines_to_write = ["First sentence. ", "Second sentence. ", "Third sentence. "]
# output_file = open("student_folder/text/practice2.txt", "w")
# output_file.writelines(lines_to_write)
# output_file.close()

# variation 1: \n
# lines_to_write = ["First sentence.\n", "Second sentence.\n", "Third sentence.\n"]
# output_file = open("student_folder/text/practice2.txt", "w")
# output_file.writelines(lines_to_write)
# output_file.close()  # prints on three lines

# write initial text
# output_file = open("student_folder/text/practice3.txt", "w")
# output_file.writelines("First sentence")
# output_file.close()

# append text to the file
# output_file = open("student_folder/text/practice3.txt", "a")
# output_file.writelines("Second sentence")
# output_file.close()

# append new line + text
# output_file = open("student_folder/text/practice3.txt", "a")
# output_file.writelines("\nSecond sentence")
# output_file.close()  # writes newline, then string

# append list of lines
# new_text = ["How many boards\n", "Could the Mongols hoard\n", "If the Mongols hordes got bored?"]

# append all lines to file
# output_file = open("student_folder/text/practice3.txt", "a")
# output_file.writelines(new_text)
# output_file.close()

# append mode using context manager
# with open("student_folder/text/practice3.txt", "a") as output_file:
#    output_file.writelines("Some new text!")

# append multiple new lines using context manager
# with open("student_folder/text/practice3.txt", "a") as output_file:
#    output_file.writelines("\nSome new text!")
#    output_file.writelines("\nAnd some more text!")
#    output_file.writelines("\nYet even more text!")