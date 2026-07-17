# 'min' function returns the smallest character
my_string = "abcdefghijklmnopqrstuvwxyz"
print(min(my_string))   # a

# 'A' is min because uppercase letters come before lowercase in ASCII/Unicode
my_string = "AaBbCcDd"
print(min(my_string))  # A

# returns space " " which is hard to see
my_string = "The brown dog jumps over the lazy fox."
print(min(my_string))  # 

# 'max' function returns the biggest character
my_string = "xyz321"
print(max(my_string)) # z

# mix of numbers and symbols
my_string = "123^&$"
print(max(my_string))  # ^
