# ------------------------------------------------------------
# Lab 1 — Read CSV and Print Movie Data
# ------------------------------------------------------------

# figuring out fetch definition code
# import csv

# movie_csv = "student_folder/.labs/movie_data.csv"

# def fetch_movie_data(movie_csv):
#    """Return movie data from a CSV file"""
#    pass    # placeholder → returns None

# movie_data = fetch_movie_data(movie_csv) 
# print(movie_data)   # None

# fetch definition full code
# def fetch_movie_data(movie_csv):
#    """Return movie data from a CSV file"""
#    with open(movie_csv, "r") as movie_file:
#        reader = csv.reader(movie_file)
#        movie_info = []
#        for row in reader:
#            movie_info.append(row)
#        return movie_info

# variation 1: unpack rows and add print aligned columns
# import csv

# movie_csv = "student_folder/.labs/movie_data.csv"

# def fetch_movie_data(movie_csv):
#    """Return movie data from a CSV file"""
#    with open(movie_csv, "r") as movie_file:
#        reader = csv.reader(movie_file)
#        movie_info = []
#        for row in reader:
#            movie_info.append(row)
#        return movie_info
    
# def print_movie_data(data):
#    """Print movie data in aligned columns"""
#    for title, genre, rotten, gross, year in data:
        # padded formatting for readability
#        print("{:36} {:10} {:18} ${:16} {}".format(title, genre, rotten, gross, year))

# movie_data = fetch_movie_data(movie_csv) 
# print(movie_data)  # outputs formatted table

# ------------------------------------------------------------
# Lab 2 — Sorting Movie Data (list of lists)
# ------------------------------------------------------------

# figuring out code for sorting by elements of inner lists
# import csv, operator  # import csv and operator module

# movie_csv = "student_folder/.labs/movie_data.csv" # filepath for CSV

# def fetch_movie_data(movie_csv):
#    """Return movie data from a CSV file"""
#    with open(movie_csv, "r") as movie_file:
#        reader = csv.reader(movie_file)
#        movie_info = []
#        for row in reader:
#          movie_info.append(row)
#        return movie_info

# def print_movie_data(data):
#    """Print the movie data in easy to read columns"""
#    for title, genre, rotten, gross, year in data:
#      print("{:36} {:10} {:18} {:16} {}".format(title, genre, rotten, gross, year))
      
# def sort_movie_data(data, index):
#    """Sort movie data based on the column data"""
#    pass
      
# movie_data = fetch_movie_data(movie_csv) 
# print_movie_data(movie_data)

# sort definition full code with a header to sort all movies:  
# import csv, operator

# movie_csv = "student_folder/.labs/movie_data.csv"

# def fetch_movie_data(movie_csv):
#    """Return movie data from a CSV file"""
#    with open(movie_csv, "r") as movie_file:
#        reader = csv.reader(movie_file)
#        movie_info = []
#        for row in reader:
#          movie_info.append(row)
#        return movie_info

# def print_movie_data(data):
#    """Print the movie data in easy to read columns"""
#    for title, genre, rotten, gross, year in data:
#      print("{:36} {:10} {:18} {:16} {}".format(title, genre, rotten, gross, year))
      
# def sort_movie_data(data, index):
#    """Sort movie data based on the column data"""
#    header = data[0]          # first row containing column names
#    sorted_movies = data[1:]  # all movie rows except the header
#    sorted_movies.sort(key=operator.itemgetter(index))
#    sorted_movies.insert(0, header)
#    return sorted_movies

# does not work for index 3 because it is read as a string
# def get_money(gross):
#  return float(gross[3])

# movie_data = fetch_movie_data(movie_csv) 
# print_movie_data(sort_movie_data(movie_data, 0))

# variation 1: gross column (index 3) must sort numerically
# import csv, operator

# movie_csv = "student_folder/.labs/movie_data.csv"

# def fetch_movie_data(movie_csv):
#    """Return movie data from a CSV file"""
#    with open(movie_csv, "r") as movie_file:
#        reader = csv.reader(movie_file)
#        movie_info = []
#        for row in reader:
#          movie_info.append(row)
#        return movie_info

# def print_movie_data(data):
#    """Print the movie data in easy to read columns"""
#    for title, genre, rotten, gross, year in data:
#      print("{:36} {:10} {:18} {:16} {}".format(title, genre, rotten, gross, year))
      
# def sort_movie_data(data, index):
#    """Sort movie data based on the column data"""
#    header = data[0]
#    sorted_movies = data[1:]
#    if index == 3:        # test if index is equal to 3
#      sorted_movies.sort(key=get_money)  # sort moves with key set to get_money function
#    else:                 # if index is not equal to 3
#      sorted_movies.sort(key=operator.itemgetter(index)) # use sort code above
#    sorted_movies.insert(0, header)
#    return sorted_movies

# movie_data = fetch_movie_data(movie_csv) 
# print_movie_data(sort_movie_data(movie_data, 0))


# ------------------------------------------------------------
# Lab 3 — Ascending or Descending Order
# Already integrated into sort_movie_data via descending parameter.
# ------------------------------------------------------------

# import csv, operator

# movie_csv = "student_folder/.labs/movie_data.csv"

# def fetch_movie_data(movie_csv):
#    """Return movie data from a CSV file"""
#    with open(movie_csv, "r") as movie_file:
#        reader = csv.reader(movie_file)
#        movie_info = []
#        for row in reader:
#          movie_info.append(row)   # append each CSV row
#        return movie_info          # list of lists

# def print_movie_data(data):
#    """Print the movie data in easy to read columns"""
#    for title, genre, rotten, gross, year in data:
#      print("{:36} {:10} {:18} {:16} {}".format(title, genre, rotten, gross, year))

# def sort_movie_data(data, index, descending):
#    """Sort movie data based on the column data"""
#    header = data[0]                 # first row = column names
#    sorted_movies = data[1:]         # all movie rows except header
    
    # numeric sort for gross column
#    if index == 3:
#      sorted_movies.sort(key=get_money)
#    else:
#      sorted_movies.sort(key=operator.itemgetter(index))

#    if descending:                 # reverse list if descending=True
#        sorted_movies.reverse()

#    sorted_movies.insert(0, header) # reinsert header at top
#    return sorted_movies

# movie_data = fetch_movie_data(movie_csv) 
# print_movie_data(sort_movie_data(movie_data, 0, True)) # sort by title, descending

# print_movie_data(sort_movie_data(movie_data, 0, False)) # sort by title, ascending

# ------------------------------------------------------------
# Lab 4 — Command Line Interface
# ------------------------------------------------------------

# def user_interface():
#    """Ask user how they want to sort the movie data"""
#    while True:
#        column = ask_column()
#        if column == "6":
#            break
#        if sanitize_column(column):
#            order = ask_order()
#            if sanitize_order(order):
#                movie_data = fetch_movie_data(movie_csv) 
#                print_movie_data(sort_movie_data(movie_data, int(column) - 1, int(order) == 2))
#            else:
#                print("Enter a number 1 or 2.\n")
#        else:
#            print("Enter a number 1 to 6.\n")

# def sort_movie_data(data, index, descending):
#    """Sort movie data based on the column data"""
#    header = data[0]                 # first row = column names
#    sorted_movies = data[1:]         # all movie rows except header
    
    # numeric sort for gross column
#    if index == 3:
#      sorted_movies.sort(key=get_money)
#    else:
#      sorted_movies.sort(key=operator.itemgetter(index))

#    if descending:                 # reverse list if descending=True
#        sorted_movies.reverse()

#    sorted_movies.insert(0, header) # reinsert header at top
#    return sorted_movies

# movie_data = fetch_movie_data(movie_csv) 
# print_movie_data(sort_movie_data(movie_data, 0, True)) # sort by title, descending

# print_movie_data(sort_movie_data(movie_data, 0, False)) # sort by title, ascending

# ------------------------------------------------------------
# Lab 5 — Adding Helper Functions
# ------------------------------------------------------------
# import csv
import operator

def ask_column():
    """Ask the user by which criteria they want to sort the data"""
    column = input("""How do you want to sort the movie data? Enter '6' to exit the program.
        1) By Film Title
        2) By Genre
        3) By Rotten Tomatoes Score
        4) By Worldwide Gross
        5) By Year
        6) Quit\n""")
    return column
      
def sanitize_column(column):
    """Return True if the user entered a valid number, else return False"""
    try:
        int(column)
        return int(column) >= 1 and int(column) <= 5
    except ValueError:
        return False
    
def ask_order():
    """Ask the user how they want the data sorted: ascending or descending"""
    order = input("""How do you want the movie data ordered?
            1) Ascending Order
            2) Descending Order\n""")
    return order

def sanitize_order(order):
    """Return True if the user entered a valid number, else return False"""
    try:
        int(order)
        return int(order) >= 1 and int(order) <= 2
    except ValueError:
        return False

# def user_interface():
#    """Ask user how they want to sort the movie data"""
#    while True:
#        column = ask_column()
#        if column == "6":
#            break
#        if sanitize_column(column):
#            order = ask_order()
#            if sanitize_order(order):
#                movie_data = fetch_movie_data(movie_csv) 
#                print_movie_data(sort_movie_data(movie_data, int(column) - 1, int(order) == 2))
#            else:
#                print("Enter a number 1 or 2.\n")
#        else:
#            print("Enter a number 1 to 6.\n")

# def sort_movie_data(data, index, descending):
#    """Sort movie data based on the column data"""
#    header = data[0]                 # first row = column names
#    sorted_movies = data[1:]         # all movie rows except header
    
    # numeric sort for gross column
#    if index == 3:
#      sorted_movies.sort(key=get_money)
#    else:
#      sorted_movies.sort(key=operator.itemgetter(index))

#    if descending:                 # reverse list if descending=True
#        sorted_movies.reverse()

#    sorted_movies.insert(0, header) # reinsert header at top
#    return sorted_movies

# movie_data = fetch_movie_data(movie_csv)   # load all rows from the CSV into memory
# print_movie_data(sort_movie_data(movie_data, 0, True)) # sort by title, descending

# print_movie_data(sort_movie_data(movie_data, 0, False)) # sort by title, ascending

# Run the interface
# user_interface()


# ------------------------------------------------------------
# Lab Challenge — to_upper
# ------------------------------------------------------------
# import operator 

def to_upper(txt):
    """Return string in all caps"""
    return txt.upper()

# test
print(to_upper("hello"))   # HELLO

# -----------------------------------------------------------
# Additional function practice
# -----------------------------------------------------------
# import operator

# function to calculate average of two inputted numbers
def avg(n1, n2):
    """Return average of two numbers
    Return a message if a non-number is passed"""
    try:
        return (n1 + n2) / 2
    except TypeError:
        return "Please use two numbers as parameters"

# tests
print(avg(10, 25))      # 17.5
print(avg(10, "cat"))   # Please use two numbers as parameters

# function to take a bool and list of int as parameters
def odds_or_evens(my_bool, nums):
    """Returns all of the odd or
    even numbers from a list"""
    return_list = []
    for num in nums:
      if my_bool:
          if num % 2 == 0:
              return_list.append(num)
      else:
          if num % 2 != 0:
              return_list.append(num)
                
    return return_list

# test
print(odds_or_evens(True, [1, 2, 3, 4, 5]))   # [2, 4]
print(odds_or_evens(False, [1, 2, 3, 4, 5]))  # [1, 3, 5]

# function to search a list for a term ignoring capitalization
def search_list(items, term):
    """Return index of matching element or -1 if not found."""
    if isinstance(term, str):
        lower_term = term.lower()
        for index, item in enumerate(items):
            if isinstance(item, str) and item.lower() == lower_term:
                return index
    for index, item in enumerate(items):
        if item == term:
            return index
    return -1

# variation 1
def search_list(lst, term):
    """Search for item in a list
    Return the index if found
    Return -1 if not found"""
    for item in lst:
        if item.lower() == term.lower():
            return lst.index(item)
    return -1
# test
print(search_list(["apple", "Banana", "Cherry"], "banana"))  # 1
print(search_list(["dog", "fish", "cat"], "Cat")) # 2
print(search_list(["apple", "Banana", "Cherry"], "pear"))    # -1
print(search_list(["water", "Toy", "house"], "toy")) # 1
print(search_list(["box", "car", "hat"], "mouse"))  # -1

# function with CSV file as variable to find best team
# import csv, operator

# mlb_data = "student_folder/.exercises/mlb_data.csv"

# def best_team(file):
#    """Return the team name with the most wins in a CSV file."""
#    with open(file, "r") as csv_file:
#        reader = csv.reader(csv_file)
#        next(reader, None)          # skip header row Tm,Lg,G,W,L

#        most_wins = 0               # declare variable for most wins and set to 0
#        best_team = ""              # declare variable to track team with highest wins

#        with open(file, "r") as csv_file:
#            reader = csv.reader(csv_file)
#            next(reader)
#            most_wins = 0
#            best_team = ""
#            for row in reader:
#                if int(row[3]) > most_wins:
#                    most_wins = int(row[3])
#                    best_team = row[0]
#            return best_team   # return team with most wins
# test
# print(best_team(mlb_data))  # HOU

# variation 1
# import csv, operator

# def best_team(mlb_data):
#    """Return the team name with the most wins in a CSV file."""
#    with open(mlb_data, "r") as team_file:
#        reader = csv.reader(team_file)
#        next(reader, None)          # skip header row Tm,Lg,G,W,L

#        max_wins = -1               # track highest win total
#        best = None                 # track team with highest wins

#        for row in reader:
#            if len(row) < 5:        # skip malformed rows
#                continue

#            team, league, games, wins, losses = row

#            try:
#                wins = int(wins)    # convert wins to integer
#           except ValueError:
#                continue            # skip rows with non-numeric wins

#            if wins > max_wins:     # update best team
#                max_wins = wins
#                best = team

#    return best                     # return team with most wins

# test
# mlb_data = "student_folder/.exercises/mlb_data.csv"
# print(best_team(mlb_data))  # HOU

# function with string parameter
import operator

def is_palindrome(string):
    # build reversed string manually
    reversed_string = ""
    position = len(string) - 1      # start at last character index

    while position >= 0:            # walk backward through string
        reversed_string += string[position]
        position -= 1               # move left one position

    # compare forward vs backward
    if string == reversed_string:
        return True
    else:
        return False

# tests
print(is_palindrome("level"))  # True
print(is_palindrome("house"))  # False

# variation 1
def is_palindrome(s):
    """Return True if string is a palindrome, else False."""
    return s == s[::-1]  # compare original string to its reversed slice

# tests
print(is_palindrome("level"))  # True
print(is_palindrome("house"))  # False
