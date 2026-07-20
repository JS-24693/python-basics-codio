# Factorial - basic recursive version for multiplication
def factorial(n):
    """Return n! using basic recursion."""
    # Base case: factorial(1) = 1
    if n == 1:              # when only one element left in the list
        return 1
    # Recursive case: n! = n * (n-1)!
    return n * factorial(n - 1)  # 120

# test
print(factorial(5))

# Factorial - corrected base case (handles 0 and negatives)
def factorial(n):
    """Return n! with safe base case for n <= 0."""
    # Base case: factorial only defined for positive integers; return 1 for n <= 0
    if n <= 0:
        return 1
    # Recursive case: reduce n toward base case
    return n * factorial(n - 1)

print(factorial(0))     # Output 1 - safe base case for 0
print(factorial(-3))    # Output 1 - safe base case for -3

# Factorial - basic recursive version for addition: sum of n integers
def find_sum(n):
    """Recursively calculate the sum of the first n numbers."""
    if n == 0:        # base case: stop recursion
        return 0
    else:
        return n + find_sum(n - 1)   # recursive case: reduce n toward base case

# test
print(find_sum(5))  # 15 - prints the RETURN value of find_sum(5) 

# Fibonacci - basic recursive version
def fibonacci(n):
    """Return Fibonacci number using naive recursion."""
    # Base case: F0 = 0, F1 = 1
    if n <= 1:
        return n
    # Recursive case: Fn = F(n-1) + F(n-2)
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(3))  # 2

# Fibonacci - printing a sequence (naive, slow) - length of 10 has 1000 steps
# def fibonacci(n):
#    """Return Fibonacci number using naive recursion."""
#    if n <= 1:
#        return n
#    return fibonacci(n - 1) + fibonacci(n - 2)

# fibonacci_length = 10
# for num in range(fibonacci_length):
#    print(fibonacci(num)) # prints sequence of length 10
                          # 0 1 1 2 3 5 8 13 21 34 

# Fibonacci - efficient version with dictionary cache (memorization)
# Cache dictionary for memorization
fibcache = {}

def fibonacci(n):
    """Return Fibonacci number using memoization."""
    # If not cached, compute and store
    if n not in fibcache:
        fibcache[n] = _fibonacci(n)
    return fibcache[n]

def _fibonacci(n):
    """Internal Fibonacci calculation."""
    # Base case
    if n <= 1:
        return n
    # Recursive case with memoized calls
    return fibonacci(n - 1) + fibonacci(n - 2)

# Efficient sequence generation
fibonacci_length = 90
for num in range(fibonacci_length):
    print(fibonacci(num))

