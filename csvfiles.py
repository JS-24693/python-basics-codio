# CSV file
# import csv

# with open("student_folder/csv/monty_python_movies.csv", "r") as input_file:
#    reader = csv.reader(input_file)
#    for row in reader:
#        print(row) # Output: ['Movie Title', 'Rating']
                   #         ['Monty Python and the Holy Grail', '5']
                   #         ["Monty Python's Life of Brian", '4']
                   #         ['Monty Python Live at the Hollywood Bowl', '4']
                   #         ["Monty Python's The Meaning of Life", '5']

# next to skip headings
# import csv

# with open("student_folder/csv/home_runs.csv", "r") as input_file:
#    reader = csv.reader(input_file)
#    next(reader) #skip the header row
#    for row in reader:
#        print(row) # Output: ['Barry Bonds', '762', 'No']
                   #         ['Hank Aaron', '755', 'No']
                   #         ['Babe Ruth', '714', 'No']
                   #         ['Alex Rodriguez', '696', 'No']
                   #         ['Willie Mays', '660', 'No']
                   #         ['Albert Pujols', '656', 'Yes']
                   #         ['Ken Griffey Jr.', '630', 'No']
                   #         ['Jim Thome', '612', 'No']
                   #         ['Sammy Sosa', '609', 'No']
                   #         ['Frank Robinson', '586', 'No']

# variation without next to include header
# import csv

# with open("student_folder/csv/home_runs.csv", "r") as input_file:
#    reader = csv.reader(input_file)
#    for row in reader:
#        print(row) # Output: ['Player', 'Home Runs', 'Active Player']
                   #         ['Barry Bonds', '762', 'No']
                   #         ['Hank Aaron', '755', 'No']
                   #         ['Babe Ruth', '714', 'No']
                   #         ['Alex Rodriguez', '696', 'No']
                   #         ['Willie Mays', '660', 'No']
                   #         ['Albert Pujols', '656', 'Yes']
                   #         ['Ken Griffey Jr.', '630', 'No']
                   #         ['Jim Thome', '612', 'No']
                   #         ['Sammy Sosa', '609', 'No']
                   #         ['Frank Robinson', '586', 'No']

# variation with next listed two times
# import csv

# with open("student_folder/csv/home_runs.csv", "r") as input_file:
#    reader = csv.reader(input_file)
#    next(reader) #skip the header row
#    next(reader) #skip the next row
#    for row in reader:
#        print(row) # Output: ['Hank Aaron', '755', 'No']
                   #         ['Babe Ruth', '714', 'No']
                   #         ['Alex Rodriguez', '696', 'No']
                   #         ['Willie Mays', '660', 'No']
                   #         ['Albert Pujols', '656', 'Yes']
                   #         ['Ken Griffey Jr.', '630', 'No']
                   #         ['Jim Thome', '612', 'No']
                   #         ['Sammy Sosa', '609', 'No']
                   #         ['Frank Robinson', '586', 'No']

# use row to reference each element with an index
# import csv

# with open("student_folder/csv/home_runs.csv", "r") as input_file:
#    reader = csv.reader(input_file)
#    for row in reader:
#        print(row[0], row[1], row[2]) # Output: Player Home Runs Active Player
                                      #         Barry Bonds 762 No
                                      #         Hank Aaron 755 No
                                      #         Babe Ruth 714 No
                                      #         Alex Rodriguez 696 No
                                      #         Willie Mays 660 No
                                      #         Albert Pujols 656 Yes
                                      #         Ken Griffey Jr. 630 No
                                      #         Jim Thome 612 No
                                      #         Sammy Sosa 609 No
                                      #         Frank Robinson 586 No

# variation 1 to add a tab between each element for better readability
#        print(row[0], "\t", row[1], "\t", row[2]

# variation 2 to left-justify and use a width of 14.
#       print("{:<14} \t {:<9} \t {:^12}".format(row[0], row[1], row[2]))

# unpack the variables name, hr, and active and output a statement
# import csv

# with open("student_folder/csv/home_runs.csv", "r") as input_file:
#    reader = csv.reader(input_file)
#    next(reader) #skip the header names
#    for name, hr, active in reader:
#        print("{} hit {} home runs.".format(name, hr))
        # Output: Barry Bonds hit 762 home runs.
        #         Hank Aaron hit 755 home runs.
        #         Babe Ruth hit 714 home runs.
        #         Alex Rodriguez hit 696 home runs.
        #         Willie Mays hit 660 home runs.
        #         Albert Pujols hit 656 home runs.
        #         Ken Griffey Jr. hit 630 home runs.
        #         Jim Thome hit 612 home runs.
        #         Sammy Sosa hit 609 home runs.
        #         Frank Robinson hit 586 home runs.

# variation 1: remove next(reader)
# First line Output: Player hit Home Runs home runs.

# \t delimiter
# import csv

# with open("student_folder/csv/data_with_tabs.csv", "r") as input_file:
#    reader = csv.reader(input_file, delimiter="\t")
#    for row in reader:
#        print(row)
        # ['Month', 'Avg High', 'Avg Low']
        # ['January', '36', '22']
        # ['February', '39', '25']
        # ['March', '45', '31']
        # ['April', '56', '41']
        # ['May', '66', '50']
        # ['June', '76', '60']
        # ['July', '81', '65']
        # ['August', '80', '65']
        # ['September', '72', '57']
        # ['October', '61', '47']
        # ['November', '51', '38']
        # ['December', '41', '28']

# Writerow
# import csv

# with open("student_folder/csv/write_practice.csv", "w") as output_file:
#    writer = csv.writer(output_file, lineterminator="\n")
#    writer.writerow(["Greeting", "Language"])
#    writer.writerow(["Hello", "English"])
#    writer.writerow(["Bonjour", "French"])
#    writer.writerow(["Hola", "Spanish"])
#    writer.writerow(["Namaste", "Hindi"])
    # Outputs to the file listed: Greeting,Language
    #                             Hello,English
    #                             Bonjour,French
    #                             Hola,Spanish
    #                             Namaste,Hindi

# CSV with tab delimiter
# import csv

# with open("student_folder/csv/write_practice.csv", "w") as output_file:
#     writer = csv.writer(output_file, delimiter="\t")
#     writer.writerow(["Greeting", "Language"])
#     writer.writerow(["Hello", "English"])
#     writer.writerow(["Bonjour", "French"])
#     writer.writerow(["Hola", "Spanish"])
#     writer.writerow(["Namaste", "Hindi"])
#     # expected file output (tab‑separated):
#     # Greeting    Language
#     # Hello       English
#     # Bonjour     French
#     # Hola        Spanish
#     # Namaste     Hindi

# Writerows
# import csv

# with open("student_folder/csv/write_practice.csv", "w") as output_file:
#    writer = csv.writer(output_file, lineterminator="\n")
#    writer.writerows([
#      ["Artist", "Album", "Copies"],
#      ["Michael Jackson", "Thriller", "47 million"],
#      ["Eagles", "Their Greatest Hits 1971-1975", "38 million"],
#      ["Eagles", "Hotel California", "26 million"]
#    ])
    # Output: Artist,Album,Copies
    #         Michael Jackson,Thriller,47 million
    #         Eagles,Their Greatest Hits 1971-1975,38 million
    #         Eagles,Hotel California,26 million