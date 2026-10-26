import json

PREDEFINED_PROBLEMS = [
    {
        "id": "p1_celsius_to_fahrenheit",
        "title": "Temperature Converter",
        "difficulty": "Beginner",
        "category": "Variables & Arithmetic",
        "order_index": 1,
        "description": """### Problem Statement
Write a function `celsius_to_fahrenheit(celsius)` that converts a temperature from degrees Celsius to Fahrenheit.

The conversion formula is:
\\[ F = (C \\times \\frac{9}{5}) + 32 \\]

### Arguments
* `celsius` (float or int): The temperature in Celsius.

### Returns
* `float`: The temperature in Fahrenheit, rounded to 2 decimal places if needed (or exact float).

### Example
```python
celsius_to_fahrenheit(0)    # Returns 32.0
celsius_to_fahrenheit(100)  # Returns 212.0
celsius_to_fahrenheit(-40)  # Returns -40.0
```
""",
        "learning_objective": "Master basic variable manipulation, arithmetic operations, operator precedence, and floating-point math in Python.",
        "starter_code": """def celsius_to_fahrenheit(celsius):
    # Calculate Fahrenheit from celsius and return the result
    pass
""",
        "function_name": "celsius_to_fahrenheit",
        "test_cases": [
            {"input": [0], "expected": 32.0, "is_hidden": False, "explanation": "Freezing point of water"},
            {"input": [100], "expected": 212.0, "is_hidden": False, "explanation": "Boiling point of water"},
            {"input": [25], "expected": 77.0, "is_hidden": False, "explanation": "Room temperature"},
            {"input": [-40], "expected": -40.0, "is_hidden": True, "explanation": "Point where Celsius equals Fahrenheit"},
            {"input": [37], "expected": 98.6, "is_hidden": True, "explanation": "Human body temperature"}
        ],
        "solution_approach": "Multiply celsius by (9 / 5) and add 32. Be mindful of operator precedence and integer division.",
        "edge_cases": [
            {"name": "Negative Temperatures", "input_example": "-40", "why_important": "Checks handling of negative numbers in arithmetic.", "what_could_go_wrong": "Sign errors or incorrect subtraction order."},
            {"name": "Float Inputs", "input_example": "36.6", "why_important": "Ensures float precision without truncation.", "what_could_go_wrong": "Accidental integer casting."}
        ]
    },
    {
        "id": "p2_leap_year",
        "title": "Leap Year Checker",
        "difficulty": "Beginner",
        "category": "Conditions",
        "order_index": 2,
        "description": """### Problem Statement
Write a function `is_leap_year(year)` that returns `True` if a given year is a leap year, and `False` otherwise.

A leap year in the Gregorian calendar occurs:
1. Every year that is evenly divisible by 4,
2. **Except** if it is divisible by 100,
3. **Unless** it is also divisible by 400.

### Arguments
* `year` (int): A positive integer representing the year.

### Returns
* `bool`: `True` if leap year, `False` otherwise.

### Examples
```python
is_leap_year(2024) # Returns True (divisible by 4)
is_leap_year(1900) # Returns False (divisible by 100 but not 400)
is_leap_year(2000) # Returns True (divisible by 400)
```
""",
        "learning_objective": "Understand compound conditional logic (`and`, `or`, `not`), modulus `%` operator, and order of boolean evaluation.",
        "starter_code": """def is_leap_year(year):
    # Return True if year is a leap year, otherwise False
    pass
""",
        "function_name": "is_leap_year",
        "test_cases": [
            {"input": [2024], "expected": True, "is_hidden": False, "explanation": "Typical leap year (divisible by 4)"},
            {"input": [2023], "expected": False, "is_hidden": False, "explanation": "Typical non-leap year"},
            {"input": [1900], "expected": False, "is_hidden": False, "explanation": "Centurial year not divisible by 400"},
            {"input": [2000], "expected": True, "is_hidden": True, "explanation": "Centurial leap year divisible by 400"},
            {"input": [1600], "expected": True, "is_hidden": True, "explanation": "Historic leap year divisible by 400"},
            {"input": [1800], "expected": False, "is_hidden": True, "explanation": "Historic non-leap centurial year"}
        ],
        "solution_approach": "(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)",
        "edge_cases": [
            {"name": "Centurial Boundaries", "input_example": "1900 vs 2000", "why_important": "Century years are the most common pitfall.", "what_could_go_wrong": "Checking only year % 4 == 0."},
            {"name": "Non-multiples of 4", "input_example": "2021", "why_important": "Simple odd and even non-leap years.", "what_could_go_wrong": "Inverted boolean conditions."}
        ]
    },
    {
        "id": "p3_sum_even_numbers",
        "title": "Sum of Even Numbers",
        "difficulty": "Beginner",
        "category": "Loops",
        "order_index": 3,
        "description": """### Problem Statement
Write a function `sum_of_evens(numbers)` that takes a list of integers and returns the sum of all the even numbers in the list. If there are no even numbers, return `0`.

### Arguments
* `numbers` (list of int): A list of integer numbers.

### Returns
* `int`: The total sum of all even numbers.

### Examples
```python
sum_of_evens([1, 2, 3, 4, 5, 6]) # Returns 12 (2 + 4 + 6)
sum_of_evens([1, 3, 5])          # Returns 0
sum_of_evens([])                 # Returns 0
```
""",
        "learning_objective": "Practice iterating over collections with `for` loops, accumulator patterns, and filtering elements with conditionals.",
        "starter_code": """def sum_of_evens(numbers):
    # Initialize accumulator and sum even numbers
    pass
""",
        "function_name": "sum_of_evens",
        "test_cases": [
            {"input": [[1, 2, 3, 4, 5, 6]], "expected": 12, "is_hidden": False, "explanation": "2 + 4 + 6 = 12"},
            {"input": [[1, 3, 5]], "expected": 0, "is_hidden": False, "explanation": "No even numbers"},
            {"input": [[]], "expected": 0, "is_hidden": False, "explanation": "Empty list"},
            {"input": [[-2, -4, 5, 6]], "expected": 0, "is_hidden": True, "explanation": "Negative evens: (-2) + (-4) + 6 = 0"},
            {"input": [[0, 2, 4]], "expected": 6, "is_hidden": True, "explanation": "Zero is even (0 + 2 + 4 = 6)"}
        ],
        "solution_approach": "Loop through each num in numbers: if num % 2 == 0, add to accumulator. Return total.",
        "edge_cases": [
            {"name": "Empty List", "input_example": "[]", "why_important": "The loop should not crash on empty input.", "what_could_go_wrong": "Uninitialized accumulator or IndexError."},
            {"name": "Negative Numbers", "input_example": "[-2, -4, 3]", "why_important": "In Python, -2 % 2 is 0.", "what_could_go_wrong": "Faulty check for positive evens only."}
        ]
    },
    {
        "id": "p4_is_palindrome",
        "title": "Palindrome Checker",
        "difficulty": "Beginner",
        "category": "Strings",
        "order_index": 4,
        "description": """### Problem Statement
Write a function `is_palindrome(text)` that checks whether a given string is a palindrome.

A palindrome is a word or phrase that reads the same backward as forward.
Your function should be **case-insensitive** and **ignore spaces and punctuation marks** (only consider alphanumeric characters).

### Arguments
* `text` (str): Input string.

### Returns
* `bool`: `True` if it is a palindrome, `False` otherwise.

### Examples
```python
is_palindrome("racecar")                   # Returns True
is_palindrome("A man, a plan, a canal: Panama") # Returns True
is_palindrome("hello")                     # Returns False
```
""",
        "learning_objective": "Master string methods (`lower()`, `isalnum()`), string slicing, and two-pointer/reversed comparisons.",
        "starter_code": """def is_palindrome(text):
    # Filter alphanumeric characters, convert to lowercase, and check if palindrome
    pass
""",
        "function_name": "is_palindrome",
        "test_cases": [
            {"input": ["racecar"], "expected": True, "is_hidden": False, "explanation": "Standard palindrome"},
            {"input": ["A man, a plan, a canal: Panama"], "expected": True, "is_hidden": False, "explanation": "Ignoring spaces and punctuation"},
            {"input": ["hello"], "expected": False, "is_hidden": False, "explanation": "Not a palindrome"},
            {"input": [""], "expected": True, "is_hidden": True, "explanation": "Empty string is trivially a palindrome"},
            {"input": ["No 'x' in Nixon"], "expected": True, "is_hidden": True, "explanation": "Mixed case with quotes"},
            {"input": ["12321"], "expected": True, "is_hidden": True, "explanation": "Numeric palindrome"}
        ],
        "solution_approach": "Clean the string keeping only c.lower() if c.isalnum(). Compare cleaned string with its reverse cleaned[::-1].",
        "edge_cases": [
            {"name": "Empty String or Punctuation Only", "input_example": "'   !!!   '", "why_important": "Leaves empty cleaned string.", "what_could_go_wrong": "Crash if slicing improperly."},
            {"name": "Single Character", "input_example": "'a'", "why_important": "A single character is always a palindrome.", "what_could_go_wrong": "Index out of range on short strings."}
        ]
    },
    {
        "id": "p5_second_largest",
        "title": "Find Second Largest Element",
        "difficulty": "Intermediate",
        "category": "Lists & Indexing",
        "order_index": 5,
        "description": """### Problem Statement
Write a function `second_largest(numbers)` that finds and returns the **second largest unique value** in a list of numbers.

If the list has fewer than two distinct numbers, return `None`.

### Arguments
* `numbers` (list of int/float): A list of numbers.

### Returns
* `int`, `float`, or `None`: The second largest distinct value, or `None`.

### Examples
```python
second_largest([10, 20, 4, 45, 99]) # Returns 45
second_largest([10, 10, 10])        # Returns None (no second distinct)
second_largest([5])                 # Returns None
```
""",
        "learning_objective": "Handle list deduplication (`set`), sorting vs linear scan, handling duplicates and boundary conditions without index errors.",
        "starter_code": """def second_largest(numbers):
    # Find second largest distinct number, or return None
    pass
""",
        "function_name": "second_largest",
        "test_cases": [
            {"input": [[10, 20, 4, 45, 99]], "expected": 45, "is_hidden": False, "explanation": "99 is 1st, 45 is 2nd"},
            {"input": [[10, 10, 10]], "expected": None, "is_hidden": False, "explanation": "No distinct second value"},
            {"input": [[5]], "expected": None, "is_hidden": False, "explanation": "Single item list"},
            {"input": [[]], "expected": None, "is_hidden": True, "explanation": "Empty list"},
            {"input": [[-10, -5, -2, -20]], "expected": -5, "is_hidden": True, "explanation": "All negative numbers: -2 is 1st, -5 is 2nd"},
            {"input": [[5, 5, 4, 3, 2]], "expected": 4, "is_hidden": True, "explanation": "Duplicate maximum value"}
        ],
        "solution_approach": "Convert to set to remove duplicates. If len < 2 return None. Else sort and return second to last, or use two variables in one pass.",
        "edge_cases": [
            {"name": "Duplicate Maximums", "input_example": "[10, 10, 8]", "why_important": "Students often sort and take list[-2], yielding 10 instead of 8.", "what_could_go_wrong": "Returning duplicate max instead of second distinct."},
            {"name": "All Negative Numbers", "input_example": "[-5, -1, -10]", "why_important": "Initializing second = 0 fails for negative sets.", "what_could_go_wrong": "Returning 0 instead of -5."}
        ]
    },
    {
        "id": "p6_word_frequencies",
        "title": "Word Frequency Counter",
        "difficulty": "Intermediate",
        "category": "Dictionaries",
        "order_index": 6,
        "description": """### Problem Statement
Write a function `count_word_frequencies(sentence)` that takes a string of words and returns a dictionary mapping each word to the number of times it appears in the sentence.

Words should be matched in **lowercase** and stripped of any leading/trailing punctuation.

### Arguments
* `sentence` (str): A string containing words separated by whitespace.

### Returns
* `dict`: Dictionary of word counts `{str: int}`.

### Examples
```python
count_word_frequencies("The cat sat on the mat")
# Returns: {"the": 2, "cat": 1, "sat": 1, "on": 1, "mat": 1}

count_word_frequencies("Hello, hello! World.")
# Returns: {"hello": 2, "world": 1}
```
""",
        "learning_objective": "Master Python dictionaries (`dict.get()`, `in` operator, keys, values) and string cleaning/splitting techniques.",
        "starter_code": """def count_word_frequencies(sentence):
    # Split into words, strip punctuation, lowercase, and count in dictionary
    pass
""",
        "function_name": "count_word_frequencies",
        "test_cases": [
            {"input": ["The cat sat on the mat"], "expected": {"the": 2, "cat": 1, "sat": 1, "on": 1, "mat": 1}, "is_hidden": False, "explanation": "'the' appears twice"},
            {"input": ["Hello, hello! World."], "expected": {"hello": 2, "world": 1}, "is_hidden": False, "explanation": "Case insensitive and punctuation stripped"},
            {"input": [""], "expected": {}, "is_hidden": False, "explanation": "Empty string yields empty dictionary"},
            {"input": ["apple Apple APPLE orange"], "expected": {"apple": 3, "orange": 1}, "is_hidden": True, "explanation": "Multiple case variations"},
            {"input": ["one"], "expected": {"one": 1}, "is_hidden": True, "explanation": "Single word"}
        ],
        "solution_approach": "import string; split sentence; for each word: word = word.strip(string.punctuation).lower(); if word: counts[word] = counts.get(word, 0) + 1. Return counts.",
        "edge_cases": [
            {"name": "Empty string or only punctuation", "input_example": "'... ! ??'", "why_important": "Ensure words stripped down to empty strings aren't counted.", "what_could_go_wrong": "Adding '' : 1 to dictionary."},
            {"name": "Consecutive Whitespace", "input_example": "'hello    world'", "why_important": "str.split() handles multiple spaces gracefully.", "what_could_go_wrong": "Using split(' ') produces empty token errors."}
        ]
    },
    {
        "id": "p7_factorial_validation",
        "title": "Factorial with Input Validation",
        "difficulty": "Intermediate",
        "category": "Functions & Exceptions",
        "order_index": 7,
        "description": """### Problem Statement
Write a function `safe_factorial(n)` that calculates the factorial of a non-negative integer $n$ ($n!$).

* If $n = 0$, $0! = 1$.
* If $n$ is negative or not an integer, the function must raise a `ValueError` with the message `"Input must be a non-negative integer"`.

### Arguments
* `n` (int): A non-negative integer.

### Returns
* `int`: The factorial of $n$.

### Raises
* `ValueError`: When $n < 0$ or $n$ is not of integer type.

### Examples
```python
safe_factorial(5)  # Returns 120
safe_factorial(0)  # Returns 1
safe_factorial(-3) # Raises ValueError("Input must be a non-negative integer")
```
""",
        "learning_objective": "Practice function definitions, recursive or iterative algorithms, explicit exception handling (`raise ValueError`), and type validation.",
        "starter_code": """def safe_factorial(n):
    # Validate input: must be an int and >= 0
    # Calculate and return factorial
    pass
""",
        "function_name": "safe_factorial",
        "test_cases": [
            {"input": [5], "expected": 120, "is_hidden": False, "explanation": "5 * 4 * 3 * 2 * 1 = 120"},
            {"input": [0], "expected": 1, "is_hidden": False, "explanation": "0! is defined as 1"},
            {"input": [1], "expected": 1, "is_hidden": False, "explanation": "1! = 1"},
            {"input": [7], "expected": 5040, "is_hidden": True, "explanation": "7! = 5040"},
            {"input": [-1], "expected": "EXCEPTION:ValueError", "is_hidden": True, "explanation": "Negative numbers should raise ValueError"},
            {"input": [3.5], "expected": "EXCEPTION:ValueError", "is_hidden": True, "explanation": "Non-integers should raise ValueError"}
        ],
        "solution_approach": "Check if not isinstance(n, int) or isinstance(n, bool) or n < 0: raise ValueError(...). Accumulate product from 1 to n.",
        "edge_cases": [
            {"name": "Zero (0!)", "input_example": "0", "why_important": "Mathematical convention where 0! = 1.", "what_could_go_wrong": "Returning 0 instead of 1."},
            {"name": "Boolean passed as int", "input_example": "True", "why_important": "In Python, bool is a subclass of int (isinstance(True, int) is True).", "what_could_go_wrong": "Accidentally treating True as 1 without typecheck."}
        ]
    },
    {
        "id": "p8_balanced_parentheses",
        "title": "Balanced Parentheses Checker",
        "difficulty": "Advanced",
        "category": "Data Structures",
        "order_index": 8,
        "description": """### Problem Statement
Write a function `is_balanced(brackets)` that takes a string containing only brackets `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`, and returns `True` if the brackets are balanced and closed in the correct order, and `False` otherwise.

### Arguments
* `brackets` (str): A string consisting of bracket characters.

### Returns
* `bool`: `True` if balanced, `False` otherwise.

### Examples
```python
is_balanced("()[]{}") # Returns True
is_balanced("([{}])") # Returns True
is_balanced("(]")     # Returns False
is_balanced("([)]")   # Returns False
is_balanced("(")      # Returns False
```
""",
        "learning_objective": "Implement the classic Stack data structure pattern (LIFO), dictionary mapping for closing brackets, and boundary conditions.",
        "starter_code": """def is_balanced(brackets):
    # Use a stack (list) to keep track of opening brackets
    pass
""",
        "function_name": "is_balanced",
        "test_cases": [
            {"input": ["()[]{}"], "expected": True, "is_hidden": False, "explanation": "All matched in sequence"},
            {"input": ["([{}])"], "expected": True, "is_hidden": False, "explanation": "Properly nested"},
            {"input": ["(]"], "expected": False, "is_hidden": False, "explanation": "Mismatched closing bracket"},
            {"input": ["([)]"], "expected": False, "is_hidden": False, "explanation": "Incorrect closing order"},
            {"input": [""], "expected": True, "is_hidden": True, "explanation": "Empty string is balanced"},
            {"input": ["("], "expected": False, "is_hidden": True, "explanation": "Unclosed opening bracket"},
            {"input": [")"], "expected": False, "is_hidden": True, "explanation": "Closing bracket with empty stack"},
            {"input": ["((()))"], "expected": True, "is_hidden": True, "explanation": "Deeply nested"}
        ],
        "solution_approach": "Map pairs = {')':'(', '}':'{', ']':'['}. For char in brackets: if char in pairs.values(): stack.append(char) elif char in pairs: if not stack or stack.pop() != pairs[char]: return False. Return len(stack) == 0.",
        "edge_cases": [
            {"name": "Closing bracket first", "input_example": "')('", "why_important": "Stack is empty when pop is attempted.", "what_could_go_wrong": "IndexError on empty list pop."},
            {"name": "Only opening brackets", "input_example": "'((('", "why_important": "Loop finishes without errors, but stack is not empty.", "what_could_go_wrong": "Returning True because no mismatch was hit."}
        ]
    }
]
