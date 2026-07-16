# List iteration for loop
numbers = [1, 2, 3, 4]   # declare a list with 4 elements
for number in numbers:   # iterate through each element in the list
    print(number)        # print each element in the list. 
    # Output: 
    # 1
    # 2
    # 3 
    # 4

# numbers print from index 0 to final index
numbers = [101, 12, 36, 24, 55, 6]
for number in numbers:
    print(number)
    # Output: 
    # 101
    # 12
    # 36
    # 24
    # 55
    # 6

# str
numbers = ["cat", "dog", "mouse", "bird", "fish"]
for number in numbers:
    print(number)
    # Output:
    # cat
    # dog
    # mouse
    # bird
    # fish

# print each iteration's full list
numbers = ["cat", "dog", "mouse", "bird", "fish"]
for number in numbers:  # loops once for each element in the list
    print(numbers)  # prints the entire list in each iteration
    # Output:
    # ['cat', 'dog', 'mouse', 'bird', 'fish']
    # Output:
    # ['cat', 'dog', 'mouse', 'bird', 'fish']
    # Output:
    # ['cat', 'dog', 'mouse', 'bird', 'fish']
    # Output:
    # ['cat', 'dog', 'mouse', 'bird', 'fish']
    # Output:
    # ['cat', 'dog', 'mouse', 'bird', 'fish']

# while loop list iteration
numbers = [1, 2, 3, 4]   # list with 4 elements
length = len(numbers)    # list length
i = 0                    # index counter

while i < length:     # iterate while index < length
    print(numbers[i]) # print element at current index
    i += 1            # increment index