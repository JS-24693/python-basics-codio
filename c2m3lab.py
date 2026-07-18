# Reading a File into a List
text = []  # declare variable and value of an empty list

with open("student_folder/.labs/files-lab1.txt", "r") as input_file:  # open file in read mode
    text = input_file.readlines()           # read all text at once and assign it to text variable
    print(text) # outputs entirety of the list - including brackets and quotes

# variation 1: prints text in easy readability
text = []

with open("student_folder/.labs/files-lab1.txt", "r") as input_file:
    text = input_file.readlines()
    print(text[0]) # outputs text of the entire passage 

# variation 2: contents of file reside in variable text
text = []

with open("student_folder/.labs/files-lab1.txt", "r") as input_file:
    text = input_file.readlines()
print(text[0]) # outputs entire passage 

# Summing Rows in a CSV
import csv
from ctypes.util import test

with open("student_folder/.labs/files-lab2.csv", "r") as input_file: # open CSV file in read mode
    reader = csv.reader(input_file)                       # pass the file to csv.reader
    for row in reader:                            # add nested for loop
        total = 0                                 # declare variable after the first loop
        for num in row:
            total += int(num)                     # add each number in the row to total, typecast str as int
        print("The total value is: {}".format(total)) # after inner loop has finished, print total value
        # Output: The total value is: 10
        #         The total value is: 151
        #         The total value is: 63
        #         The total value is: 127

# Interactive CSV Writing
import csv

with open("student_folder/csv/superheroes.csv", "w") as output_file: # open CSV file in write mode as output_file
    writer = csv.writer(output_file, lineterminator="\n")  # set up csv.writer and set lineterminator to new line
    writer.writerow(["Superhero", "Power"])   # CSV file should be headers for each column of data
    print("Enter `stop` to quit the program")   # gather user input
    name = input("Enter the superhero's name: ")
    power = input("Enter their superpower: ")
    
    while True:    # while loop allows program to run again and again until user stops
        writer.writerow([name, power])   # write a line to the CSV file with user input variables
        name = input("Enter the superhero's name: ")
        if name == "stop":               # check if input == stop
            break                           # exit loop 
        power = input("Enter their superpower: ")

# Caesar Cipher Encryption/Decryption
# Read source text and write encrypted output.
with open("student_folder/.labs/source.txt", "r") as source, open("student_folder/text/encrypted.txt", "w") as destination:
    key = 13  # number of positions each char is shifted
    mode = "encrypt"  # Cipher mode
    SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.-;"  # Allowed characters
    new_text = ""  # Holds encrypted text

    line = source.readline()  # Read one line
    while line != "":  # Continue until EOF
        for char in line:  # Check each character
            if char in SYMBOLS:  # Ignore unsupported characters
                char_index = SYMBOLS.find(char)

                if mode == "encrypt":  # Shift forward by key
                    new_index = char_index + key
                elif mode == "decrypt":  # Shift backward by key
                    new_index = char_index - key

                # wrap index within SYMBOLS range
                if new_index >= len(SYMBOLS):
                    new_index = new_index - len(SYMBOLS)
                elif new_index < 0:
                    new_index = new_index + len(SYMBOLS)

                new_text += SYMBOLS[new_index]  # append shifted character

        destination.write(new_text) # write encrypted line
        line = source.readline()    # read next line

# decrypt text
with open("student_folder/text/encrypted.txt", "r") as source, open("student_folder/text/decrypted.txt", "w") as destination:
    mode = "decrypt"

# Lab Challenge — Replace Text in a File
# for loop processes each line and replaces Burma
with open("student_folder/.labs/myanmar.txt", "r") as input_file:
    lines = input_file.readlines()
    for line in lines:
        if "Burma" in line:  # replace only when Burma appears and print line
            print(line.replace("Burma", "Myanmar"), end="")
        else:  # print unchanged line
            print(line, end="")

# variation 1
# f-string not used for iteration; replace entire text at once
with open("student_folder/.labs/myanmar.txt", "r") as f:
    text = f.read().replace("Burma", "Myanmar")  # full-file replacement
    print(text)
    # Output: Myanmar is a country in Southeast Asia.
    #         The capital of Myanmar is Naypyidaw.
    #         Its population is about 54 million people.
    #         Myanmar is a former British colony.

# program that counts lines and total characters in a file
import sys

test_file = sys.argv[1]  # file path from command line

line_count = 0  # initialize line counter
char_count = 0  # initialize character counter

with open(test_file, "r") as input_file:  # open file for reading
    line = input_file.readline()  # read first line
    while line != "":  # loop until EOF
        line_count += 1  # increment line count
        char_count += len(line)  # add character count
        line = input_file.readline()  # read next line

print("{} lines".format(line_count))  # output line count
print("{} characters".format(char_count))  # output character count

# variation 1: loads all lines at once, counts with len() and sum()
import sys

test_file = sys.argv[1]  # file path from command line

with open(test_file, "r") as f:  # open file for reading
    lines = f.readlines()  # read all lines
    num_lines = len(lines)  # count lines
    num_chars = sum(len(line) for line in lines)  # count characters

print(num_lines, "lines")  # print line count
print(num_chars, "characters")  # print character count

# program that computes column averages using sum and len
import sys
import csv

test_file = sys.argv[1]  # CSV file path

cols = [[], [], [], []]  # store values for each column

with open(test_file, "r") as input_file:
    reader = csv.reader(input_file, delimiter=",")
    for row in reader:
        cols[0].append(float(row[0]))
        cols[1].append(float(row[1]))
        cols[2].append(float(row[2]))
        cols[3].append(float(row[3]))

averages = [sum(c) / len(c) for c in cols]  # compute averages

print(*averages)  # space‑separated output

# variation 1: program that reads a comma delimited CSV file with four colums and returns average of each column
import sys, csv

test_file = sys.argv[1]  # CSV file path

total1 = 0  # sum of column 1
total2 = 0  # sum of column 2
total3 = 0  # sum of column 3
total4 = 0  # sum of column 4
row_count = 0  # number of rows

with open(test_file, "r") as input_file:  # open CSV
    reader = csv.reader(input_file)  # CSV reader
    for num1, num2, num3, num4 in reader:  # unpack four columns
        row_count += 1  # increment row count
        total1 += int(num1)  # accumulate column 1
        total2 += int(num2)  # accumulate column 2
        total3 += int(num3)  # accumulate column 3
        total4 += int(num4)  # accumulate column 4

print("{} {} {} {}".format(total1/row_count,
                           total2/row_count,
                           total3/row_count,
                           total4/row_count))  # compute then print averages

# variation 2: accumulate columns as floats to preserve numeric precision
import sys
import csv

test_file = sys.argv[1]   # CSV file path

totals = [0, 0, 0, 0]  # running totals for 4 columns
count = 0  # number of rows

with open(test_file, "r") as input_file:  # open CSV
    reader = csv.reader(input_file, delimiter=",")  # CSV reader
    for row in reader:  # process each row
        totals[0] += float(row[0])
        totals[1] += float(row[1])
        totals[2] += float(row[2])
        totals[3] += float(row[3])
        count += 1

# compute averages
averages = [t / count for t in totals]

print(averages[0], averages[1], averages[2], averages[3])

# Program that reverses file contents
import sys

test_file = sys.argv[1]

with open(test_file, "r") as input_file:
    lines = input_file.readlines()  # Read all lines
    lines.reverse()  # Reverse the order
    for line in lines:      # Iterate through the lines
        print(line, end="")   # Print each line in reverse order

# read a tab delimited CSV file and write the oldest person's name
import sys, csv

test_file = sys.argv[1]  # CSV file path

oldest_age = 0   # track highest age found
oldest_name = ""  # track name of oldest person

with open(test_file, "r") as input_file:  # open tab‑delimited CSV
    reader = csv.reader(input_file, delimiter="\t")  # tab-separated reader
    next(reader)  # skip header row

    for name, age, career in reader:  # unpack each row
        age_val = int(age)  # convert age to integer
        if age_val > oldest_age:  # check if this is the oldest so far
            oldest_age = age_val  # update oldest age
            oldest_name = name    # update oldest name

print("The oldest person is {}".format(oldest_name))  # output name of oldest person

# Read a comma-delimited CSV file and print cities in the Southern Hemisphere.
import sys, csv

test_file = sys.argv[1]  # CSV file path

cities = []  # store matching city names

with open(test_file, "r") as input_file:  # open comma-delimited CSV file
    reader = csv.reader(input_file)  # CSV reader
    next(reader)  # skip header row

    for city, country, latitude, longitude in reader:  # unpack each row
        if float(latitude) < 0:  # check if latitude is negative
            cities.append(city)  # add matching city

print("The following cities are in the Southern Hemisphere: ", end="")
for city in cities:
    if city == cities[-1]: # check if city is the last element in cities
        print(city + ".")        # print city name followed by a period
    else:                      # print the city
        print(city, end=", ")    # followed by comma and space with no newline