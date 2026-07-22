# Exercise 1: Use subclassing and override shuffle

import random

class Lottery:
    def shuffle(self):
        results = []
        for i in range(5):
            results.append(random.randint(1, 20))
        return results

class PowerBall(Lottery):
    """
    Child class of Lottery that overrides shuffle to return
    six random integers between 1 and 99 (inclusive).
    """
    def shuffle(self):
        results = []
        for i in range(6):
            results.append(random.randint(1, 99))
        return results

# Example usage:
pb = PowerBall()
print(pb.shuffle())  # e.g. [12, 87, 3, 45, 99, 21]


# Exercise 2: 
# Airplane and Train passenger totals
# Strict, self-contained module implementing total() for each vehicle

class Airplane:
    def __init__(self, first_class, business_class, coach):
        # store passenger counts for each cabin
        self.first_class = first_class
        self.business_class = business_class
        self.coach = coach

    def total(self):
        # return total passengers on the airplane
        return self.first_class + self.business_class + self.coach


class Train:
    def __init__(self, car1, car2, car3, car4, car5):
        # store passenger counts for each car
        self.car1 = car1
        self.car2 = car2
        self.car3 = car3
        self.car4 = car4
        self.car5 = car5

    def total(self):
        # return total passengers on the train
        return self.car1 + self.car2 + self.car3 + self.car4 + self.car5


def passengers(obj):
    print(f'There are {obj.total()} passengers on board.')

# Example usage:
a = Airplane(10, 20, 150)
t = Train(30, 28, 25, 22, 20)

passengers(a)  # There are 180 passengers on board.
passengers(t)  # There are 125 passengers on board.


# Exercise 3:
# Characters class: compare by total characters across all phrases

from typing import List


class Characters:
    def __init__(self, phrases):
        self.phrases = phrases
    
    def total_characters(self):
        """Return total number of characters across all phrases (includes spaces)."""
        total = 0
        for phrase in self.phrases:
            total += len(phrase)
        return total
    
    def __gt__(self, obj):
        return self.total_characters() > obj.total_characters()
  
    def __lt__(self, obj):
        return self.total_characters() < obj.total_characters()
  
    def __eq__(self, obj):
        return self.total_characters() == obj.total_characters()

# Example usage demonstrating the expected output
if __name__ == "__main__":
    sample_phrases1 = ['cat in the hat', 'green eggs and ham', 'the lorax']
    sample_phrases2 = ['the taming of the shrew', 'hamlet', 'othello']

    c1 = Characters(sample_phrases1)
    c2 = Characters(sample_phrases2)

    print(c1 > c2)   # True
    print(c1 < c2)   # False
    print(c1 == c1)  # True

    # Check work
    # Print per-phrase totals
    print("Total characters (c1):", c1.total_characters())  # Total characters (c1): 41
    print("Total characters (c2):", c2.total_characters())  # Total characters (c2): 36


# Exercise 3, Variation 1:
# Characters class: compare by total characters across all phrases

# from typing import List


class Characters:
    """
    Holds a list of phrase strings and compares instances by the total
    number of characters across all phrases.
    """

    def __init__(self, phrases: List[str]) -> None:
        self.phrases = list(phrases)

    def total_chars(self) -> int:
        """Return total number of characters across all phrases (includes spaces)."""
        return sum(len(s) for s in self.phrases)

    def __lt__(self, other: "Characters") -> bool:
        return self.total_chars() < other.total_chars()

    def __gt__(self, other: "Characters") -> bool:
        return self.total_chars() > other.total_chars()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Characters):
            return NotImplemented
        return self.total_chars() == other.total_chars()

# Example usage demonstrating the expected output
if __name__ == "__main__":
    sample_phrases1 = ['cat in the hat', 'green eggs and ham', 'the lorax']
    sample_phrases2 = ['the taming of the shrew', 'hamlet', 'othello']

    c1 = Characters(sample_phrases1)
    c2 = Characters(sample_phrases2)

    print(c1 > c2)   # True
    print(c1 < c2)   # False
    print(c1 == c1)  # True

    # Check work
    # Print per-phrase totals
    print("Total characters (c1):", c1.total_chars())  # Total characters (c1): 41
    print("Total characters (c2):", c2.total_chars())  # Total characters (c2): 36


# Exercise 4: 
"""
median.py

Strict, self-contained implementation of a Median calculator.

Provides:
- Median class with calculate_median method that accepts 2 to 5 integer arguments
  using optional parameters (n3, n4, n5).
- Detailed docstrings and inline comments explaining behavior and edge cases.
"""

from typing import Optional, Union


class Median:
    """
    Median calculator.

    The calculate_median method accepts between two and five integer arguments
    via positional parameters (n1, n2, n3=None, n4=None, n5=None). It computes
    the median of the provided integers.

    Behavior:
    - If an odd number of values is provided, returns the middle value as int.
    - If an even number of values is provided, returns the average of the two
      middle values as float.
    - Raises ValueError if fewer than 2 or more than 5 values are provided.
    - Raises TypeError if any provided argument is not an int.
    """

    # Overloading simulated: 
    # optional parameters (n3, n4, n5) allow calculate_median to accept 2–5 ints
    def calculate_median(
        self,
        n1: int,
        n2: int,
        n3: Optional[int] = None,
        n4: Optional[int] = None,
        n5: Optional[int] = None,
    ) -> Union[int, float]:

        """
        Calculate the median of 2 to 5 integers.

        Parameters
        ----------
        n1, n2 : int
            Required integer arguments.
        n3, n4, n5 : int or None, optional
            Optional integer arguments. Provide between 0 and 3 of these.

        Returns
        -------
        int or float
            The median value. Returns int for odd-length input, float for even-length input.

        Raises
        ------
        ValueError
            If the number of provided arguments is less than 2 or greater than 5.
        TypeError
            If any provided argument is not an int.
        """
        # Build the list of provided numbers in order, preserving the original
        # function signature style (optional trailing parameters).
        if n3 is not None and n4 is not None and n5 is not None:
            numbers = [n1, n2, n3, n4, n5]
        elif n3 is not None and n4 is not None:
            numbers = [n1, n2, n3, n4]
        elif n3 is not None:
            numbers = [n1, n2, n3]
        else:
            numbers = [n1, n2]

        # Validate argument count (defensive; the construction above already
        # ensures 2-5, but keep explicit check for clarity).
        if not (2 <= len(numbers) <= 5):
            raise ValueError("calculate_median requires between 2 and 5 integer arguments")

        # Validate types: ensure all entries are ints.
        for idx, value in enumerate(numbers, start=1):
            if not isinstance(value, int):
                raise TypeError(f"Argument #{idx} is not an int: {value!r}")

        # Sort the numbers to compute the median.
        numbers.sort()

        # Compute median index and value(s).
        median_index = len(numbers) // 2
        if len(numbers) % 2 == 0:
            # Even count: average the two middle values and return a float.
            median = (numbers[median_index] + numbers[median_index - 1]) / 2
        else:
            # Odd count: return the middle element (int).
            median = numbers[median_index]

        return median


if __name__ == "__main__":
    # Quick self-test demonstrating expected behavior.
    m = Median()
    print(m.calculate_median(3, 5, 1, 4, 2))  # 3
    print(m.calculate_median(8, 6, 4, 2))     # 5.0
    print(m.calculate_median(9, 3, 7))        # 7
    print(m.calculate_median(5, 2))           # 3.5


# Exercise 4, Variation 1:
# Median calculator with overloaded-style method (accepts 2 to 5 integer arguments)

from typing import List, Union


class Median:
    """Calculate median for 2 to 5 integer arguments."""
    # Simulated overloading: accept variable arity (2–5 ints) via *args;
    # validate argument count and types so one method behaves like multiple signatures.
    def calculate_median(self, *args: int) -> Union[int, float]:
        """
        Calculate the median of 2 to 5 integer arguments.

        Returns:
            int for odd-length input, float for even-length input.

        Raises:
            TypeError: if any argument is not an int.
            ValueError: if number of arguments is not between 2 and 5.
        """
        if not (2 <= len(args) <= 5):
            raise ValueError("calculate_median requires between 2 and 5 arguments")

        # Validate types
        for a in args:
            if not isinstance(a, int):
                raise TypeError("All arguments must be integers")

        nums: List[int] = sorted(args)
        n = len(nums)
        mid = n // 2

        if n % 2 == 1:
            # odd count -> return middle element (int)
            return nums[mid]
        else:
            # even count -> return average of two middle elements (float)
            return (nums[mid - 1] + nums[mid]) / 2.0


if __name__ == "__main__":
    m = Median()

    # Examples from the prompt
    print(m.calculate_median(3, 5, 1, 4, 2))  # 3
    print(m.calculate_median(8, 6, 4, 2))     # 5.0
    print(m.calculate_median(9, 3, 7))        # 7
    print(m.calculate_median(5, 2))           # 3.5


# Exercise 5: Create subclass to replace words with asterisks.

from pathlib import Path

# actual source file
source = Path(r"D:\DataScience DataEngineering\06 Intro to Python Programming Equivalents\01 Codio Programming in Python\Codio_Python\Pride&Prejudice.txt")
answer = Path(r"D:\DataScience DataEngineering\06 Intro to Python Programming Equivalents\01 Codio Programming in Python\Codio_Python\answer_exercise5.txt")

print("Source exists:", source.exists(), "->", source.resolve(strict=False))


class Substitute:
  """Read a text file into a 2D list of words, modify words, and write an answer file.

    Attributes
    ----------
    source_file : str | Path
        Path to the input text file to read.
    answer_file : str | Path
        Path where the modified output will be written.
    words : list[list[str]] | str | None
        Internal representation: a 2D list of words after reading, or a string after conversion.
    """
  def __init__(self, source_file, answer_file):
    """Initialize with source and answer file paths and prepare storage for words.

        Parameters
        ----------
        source_file : str | Path
            Path to the input file to read.
        answer_file : str | Path
            Path to the output file to write.
        """
    self.source_file = source_file
    self.answer_file = answer_file
    self.words = None
    
  def string_to_list(self):
    '''Read text file, turn it into a 2D list of words for each line'''
    words = []
    with open(self.source_file, 'r', encoding='cp1252', errors='replace') as file_object:
            lines = file_object.read().split('\n')
    for line in lines:
        words.append(line.split())
    self.words = words
    
  def list_to_string(self):
    '''Convert 2D list back into a string with newline characters'''
    lines = []
    for line in self.words:
      lines.append(' '.join(line))
    string = '\n'.join(lines)
    self.words = string
  
  def swap_words(self):
    self.string_to_list()
    for line in self.words:
      for i in range(len(line)):
        if (i + 1) % 5 == 0:
          word = line[i]
          line[i] = 'HELLO'
    self.list_to_string()


class Stars(Substitute):
    """
    Child class of Substitute that replaces every third word with asterisks.

    Behavior:
    - Starts by converting the source file into a 2D list via string_to_list().
    - For each inner list (line), every 3rd word (index where (i+1) % 3 == 0)
      is replaced by a string of '*' characters whose length matches the word.
    - Converts the modified 2D list back to a string via list_to_string().
    - Writes the resulting string to self.answer_file.
    """
    
    def __init__(self, source_file, answer_file=None):
        """
        Initialize Stars.

        Parameters
        ----------
        source_file : str | Path
            Path to the input text file to read.
        answer_file : str | Path, optional
            Path to write the modified output. Defaults to "answer_exercise5.txt".
        """
        super().__init__(source_file, answer_file)
        self.answer_file = answer_file or "answer_exercise5.txt"

    def swap_words(self) -> None:
        """Replace every third word in the source text with asterisks and write output.

        Steps
        -----
        1. Read the source file into `self.words` as a 2D list via `string_to_list()`.
        2. For each non-empty line, replace each word where `(i + 1) % 3 == 0`
           with a string of '*' characters matching the original word length.
        3. Convert the 2D list back to a single string via `list_to_string()`.
        
        The method leaves the final text in self.words 
        and that the caller is responsible for writing the file.

        Raises
        ------
        FileNotFoundError
        If the source file does not exist when `string_to_list()` attempts to open it.
        RuntimeError
        If `list_to_string()` does not produce a string (sanity check failure).
        """
        # Read source file into self.words as a 2D list
        self.string_to_list()

        # Iterate over each line (list of words)
        for line in self.words:
            # Skip empty lines
            if not line:
                continue

            # Replace every third word with '*' repeated to match word length
            for i in range(len(line)):
                if (i + 1) % 3 == 0:
                    word = line[i]
                    # Preserve length of the original word (including punctuation)
                    line[i] = '*' * len(word)

        # Convert the 2D list back into a single string stored in self.words
        self.list_to_string()

        # Sanity check
        if not isinstance(self.words, str):
            raise RuntimeError("list_to_string() did not produce a string")


# -------------------------
# Module-level usage (single, explicit write)
# -------------------------

# Instantiate Stars and produce the final string in s.words
s = Stars(str(source), str(answer))
s.swap_words()  # must convert lists to a single string (list_to_string)

# Validate and write (caller owns I/O)
out_path = Path(s.answer_file)
out_path.parent.mkdir(parents=True, exist_ok=True)

if not isinstance(s.words, str):
    raise RuntimeError("s.words must be a string; call s.list_to_string() first")

out_path.write_text(s.words, encoding="utf-8", errors="replace")

# Optional verification (prints to terminal)
print("Wrote:", out_path.exists())
print(out_path.read_text(encoding="utf-8", errors="replace"))
