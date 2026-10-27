# Curated Predefined Coding Problems (30 Total: 10 Easy, 10 Medium, 10 Hard)
PREDEFINED_PROBLEMS = [
    {
        "id": "p1_celsius_to_fahrenheit",
        "title": "Temperature Converter",
        "difficulty": "Beginner",
        "category": "Variables & Arithmetic",
        "order_index": 1,
        "description": "### Problem Statement\nWrite a function `celsius_to_fahrenheit(celsius)` that converts a temperature from degrees Celsius to Fahrenheit.\n\nThe conversion formula is:\n\\[ F = (C \\times \\frac{9}{5}) + 32 \\]\n\n### Arguments\n* `celsius` (float or int): The temperature in Celsius.\n\n### Returns\n* `float`: The temperature in Fahrenheit, rounded to 2 decimal places if needed (or exact float).\n\n### Example\n```python\ncelsius_to_fahrenheit(0)    # Returns 32.0\ncelsius_to_fahrenheit(100)  # Returns 212.0\ncelsius_to_fahrenheit(-40)  # Returns -40.0\n```\n",
        "learning_objective": "Master basic variable manipulation, arithmetic operations, operator precedence, and floating-point math in Python.",
        "starter_code": "def celsius_to_fahrenheit(celsius):\n    # Calculate Fahrenheit from celsius and return the result\n    pass\n",
        "function_name": "celsius_to_fahrenheit",
        "test_cases": [
            {
                "input": [
                    0
                ],
                "expected": 32.0,
                "is_hidden": False,
                "explanation": "Freezing point of water"
            },
            {
                "input": [
                    100
                ],
                "expected": 212.0,
                "is_hidden": False,
                "explanation": "Boiling point of water"
            },
            {
                "input": [
                    25
                ],
                "expected": 77.0,
                "is_hidden": False,
                "explanation": "Room temperature"
            },
            {
                "input": [
                    -40
                ],
                "expected": -40.0,
                "is_hidden": True,
                "explanation": "Point where Celsius equals Fahrenheit"
            },
            {
                "input": [
                    37
                ],
                "expected": 98.6,
                "is_hidden": True,
                "explanation": "Human body temperature"
            }
        ],
        "solution_approach": "Multiply celsius by (9 / 5) and add 32. Be mindful of operator precedence and integer division.",
        "edge_cases": [
            {
                "name": "Negative Temperatures",
                "input_example": "-40",
                "why_important": "Checks handling of negative numbers in arithmetic.",
                "what_could_go_wrong": "Sign errors or incorrect subtraction order."
            },
            {
                "name": "Float Inputs",
                "input_example": "36.6",
                "why_important": "Ensures float precision without truncation.",
                "what_could_go_wrong": "Accidental integer casting."
            }
        ],
        "hints": [
            "What is the formula converting Celsius to Fahrenheit? Look at the problem description.",
            "Be careful with Python operator precedence: multiplication happens before addition.",
            "Compute celsius * (9 / 5) + 32 and return the result."
        ]
    },
    {
        "id": "p2_leap_year",
        "title": "Leap Year Checker",
        "difficulty": "Beginner",
        "category": "Conditions",
        "order_index": 2,
        "description": "### Problem Statement\nWrite a function `is_leap_year(year)` that returns `True` if a given year is a leap year, and `False` otherwise.\n\nA leap year in the Gregorian calendar occurs:\n1. Every year that is evenly divisible by 4,\n2. **Except** if it is divisible by 100,\n3. **Unless** it is also divisible by 400.\n\n### Arguments\n* `year` (int): A positive integer representing the year.\n\n### Returns\n* `bool`: `True` if leap year, `False` otherwise.\n\n### Examples\n```python\nis_leap_year(2024) # Returns True (divisible by 4)\nis_leap_year(1900) # Returns False (divisible by 100 but not 400)\nis_leap_year(2000) # Returns True (divisible by 400)\n```\n",
        "learning_objective": "Understand compound conditional logic (`and`, `or`, `not`), modulus `%` operator, and order of boolean evaluation.",
        "starter_code": "def is_leap_year(year):\n    # Return True if year is a leap year, otherwise False\n    pass\n",
        "function_name": "is_leap_year",
        "test_cases": [
            {
                "input": [
                    2024
                ],
                "expected": True,
                "is_hidden": False,
                "explanation": "Typical leap year (divisible by 4)"
            },
            {
                "input": [
                    2023
                ],
                "expected": False,
                "is_hidden": False,
                "explanation": "Typical non-leap year"
            },
            {
                "input": [
                    1900
                ],
                "expected": False,
                "is_hidden": False,
                "explanation": "Centurial year not divisible by 400"
            },
            {
                "input": [
                    2000
                ],
                "expected": True,
                "is_hidden": True,
                "explanation": "Centurial leap year divisible by 400"
            },
            {
                "input": [
                    1600
                ],
                "expected": True,
                "is_hidden": True,
                "explanation": "Historic leap year divisible by 400"
            },
            {
                "input": [
                    1800
                ],
                "expected": False,
                "is_hidden": True,
                "explanation": "Historic non-leap centurial year"
            }
        ],
        "solution_approach": "(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)",
        "edge_cases": [
            {
                "name": "Centurial Boundaries",
                "input_example": "1900 vs 2000",
                "why_important": "Century years are the most common pitfall.",
                "what_could_go_wrong": "Checking only year % 4 == 0."
            },
            {
                "name": "Non-multiples of 4",
                "input_example": "2021",
                "why_important": "Simple odd and even non-leap years.",
                "what_could_go_wrong": "Inverted boolean conditions."
            }
        ],
        "hints": [
            "How do you test divisibility in Python? Use the % (modulo) operator.",
            "Remember that years divisible by 100 are NOT leap years unless also divisible by 400.",
            "Combine conditions: (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)."
        ]
    },
    {
        "id": "p3_sum_even_numbers",
        "title": "Sum of Even Numbers",
        "difficulty": "Beginner",
        "category": "Loops",
        "order_index": 3,
        "description": "### Problem Statement\nWrite a function `sum_of_evens(numbers)` that takes a list of integers and returns the sum of all the even numbers in the list. If there are no even numbers, return `0`.\n\n### Arguments\n* `numbers` (list of int): A list of integer numbers.\n\n### Returns\n* `int`: The total sum of all even numbers.\n\n### Examples\n```python\nsum_of_evens([1, 2, 3, 4, 5, 6]) # Returns 12 (2 + 4 + 6)\nsum_of_evens([1, 3, 5])          # Returns 0\nsum_of_evens([])                 # Returns 0\n```\n",
        "learning_objective": "Practice iterating over collections with `for` loops, accumulator patterns, and filtering elements with conditionals.",
        "starter_code": "def sum_of_evens(numbers):\n    # Initialize accumulator and sum even numbers\n    pass\n",
        "function_name": "sum_of_evens",
        "test_cases": [
            {
                "input": [
                    [
                        1,
                        2,
                        3,
                        4,
                        5,
                        6
                    ]
                ],
                "expected": 12,
                "is_hidden": False,
                "explanation": "2 + 4 + 6 = 12"
            },
            {
                "input": [
                    [
                        1,
                        3,
                        5
                    ]
                ],
                "expected": 0,
                "is_hidden": False,
                "explanation": "No even numbers"
            },
            {
                "input": [
                    []
                ],
                "expected": 0,
                "is_hidden": False,
                "explanation": "Empty list"
            },
            {
                "input": [
                    [
                        -2,
                        -4,
                        5,
                        6
                    ]
                ],
                "expected": 0,
                "is_hidden": True,
                "explanation": "Negative evens: (-2) + (-4) + 6 = 0"
            },
            {
                "input": [
                    [
                        0,
                        2,
                        4
                    ]
                ],
                "expected": 6,
                "is_hidden": True,
                "explanation": "Zero is even (0 + 2 + 4 = 6)"
            }
        ],
        "solution_approach": "Loop through each num in numbers: if num % 2 == 0, add to accumulator. Return total.",
        "edge_cases": [
            {
                "name": "Empty List",
                "input_example": "[]",
                "why_important": "The loop should not crash on empty input.",
                "what_could_go_wrong": "Uninitialized accumulator or IndexError."
            },
            {
                "name": "Negative Numbers",
                "input_example": "[-2, -4, 3]",
                "why_important": "In Python, -2 % 2 is 0.",
                "what_could_go_wrong": "Faulty check for positive evens only."
            }
        ],
        "hints": [
            "How do you identify whether an integer is even? Check if num % 2 == 0.",
            "Initialize an accumulator variable total = 0 before looping through the list.",
            "Iterate over each number in numbers: if even, add to total. Return total after the loop."
        ]
    },
    {
        "id": "p4_is_palindrome",
        "title": "Palindrome Checker",
        "difficulty": "Beginner",
        "category": "Strings",
        "order_index": 4,
        "description": "### Problem Statement\nWrite a function `is_palindrome(text)` that checks whether a given string is a palindrome.\n\nA palindrome is a word or phrase that reads the same backward as forward.\nYour function should be **case-insensitive** and **ignore spaces and punctuation marks** (only consider alphanumeric characters).\n\n### Arguments\n* `text` (str): Input string.\n\n### Returns\n* `bool`: `True` if it is a palindrome, `False` otherwise.\n\n### Examples\n```python\nis_palindrome(\"racecar\")                   # Returns True\nis_palindrome(\"A man, a plan, a canal: Panama\") # Returns True\nis_palindrome(\"hello\")                     # Returns False\n```\n",
        "learning_objective": "Master string methods (`lower()`, `isalnum()`), string slicing, and two-pointer/reversed comparisons.",
        "starter_code": "def is_palindrome(text):\n    # Filter alphanumeric characters, convert to lowercase, and check if palindrome\n    pass\n",
        "function_name": "is_palindrome",
        "test_cases": [
            {
                "input": [
                    "racecar"
                ],
                "expected": True,
                "is_hidden": False,
                "explanation": "Standard palindrome"
            },
            {
                "input": [
                    "A man, a plan, a canal: Panama"
                ],
                "expected": True,
                "is_hidden": False,
                "explanation": "Ignoring spaces and punctuation"
            },
            {
                "input": [
                    "hello"
                ],
                "expected": False,
                "is_hidden": False,
                "explanation": "Not a palindrome"
            },
            {
                "input": [
                    ""
                ],
                "expected": True,
                "is_hidden": True,
                "explanation": "Empty string is trivially a palindrome"
            },
            {
                "input": [
                    "No 'x' in Nixon"
                ],
                "expected": True,
                "is_hidden": True,
                "explanation": "Mixed case with quotes"
            },
            {
                "input": [
                    "12321"
                ],
                "expected": True,
                "is_hidden": True,
                "explanation": "Numeric palindrome"
            }
        ],
        "solution_approach": "Clean the string keeping only c.lower() if c.isalnum(). Compare cleaned string with its reverse cleaned[::-1].",
        "edge_cases": [
            {
                "name": "Empty String or Punctuation Only",
                "input_example": "'   !!!   '",
                "why_important": "Leaves empty cleaned string.",
                "what_could_go_wrong": "Crash if slicing improperly."
            },
            {
                "name": "Single Character",
                "input_example": "'a'",
                "why_important": "A single character is always a palindrome.",
                "what_could_go_wrong": "Index out of range on short strings."
            }
        ],
        "hints": [
            "How can you ignore punctuation, spaces, and case? Try .isalnum() and .lower().",
            "Build a cleaned string containing only lowercase alphanumeric characters.",
            "Compare the cleaned string with its reverse using slice notation: cleaned == cleaned[::-1]."
        ]
    },
    {
        "id": "p5_second_largest",
        "title": "Find Second Largest Element",
        "difficulty": "Beginner",
        "category": "Lists & Indexing",
        "order_index": 5,
        "description": "### Problem Statement\nWrite a function `second_largest(numbers)` that finds and returns the **second largest unique value** in a list of numbers.\n\nIf the list has fewer than two distinct numbers, return `None`.\n\n### Arguments\n* `numbers` (list of int/float): A list of numbers.\n\n### Returns\n* `int`, `float`, or `None`: The second largest distinct value, or `None`.\n\n### Examples\n```python\nsecond_largest([10, 20, 4, 45, 99]) # Returns 45\nsecond_largest([10, 10, 10])        # Returns None (no second distinct)\nsecond_largest([5])                 # Returns None\n```\n",
        "learning_objective": "Handle list deduplication (`set`), sorting vs linear scan, handling duplicates and boundary conditions without index errors.",
        "starter_code": "def second_largest(numbers):\n    # Find second largest distinct number, or return None\n    pass\n",
        "function_name": "second_largest",
        "test_cases": [
            {
                "input": [
                    [
                        10,
                        20,
                        4,
                        45,
                        99
                    ]
                ],
                "expected": 45,
                "is_hidden": False,
                "explanation": "99 is 1st, 45 is 2nd"
            },
            {
                "input": [
                    [
                        10,
                        10,
                        10
                    ]
                ],
                "expected": None,
                "is_hidden": False,
                "explanation": "No distinct second value"
            },
            {
                "input": [
                    [
                        5
                    ]
                ],
                "expected": None,
                "is_hidden": False,
                "explanation": "Single item list"
            },
            {
                "input": [
                    []
                ],
                "expected": None,
                "is_hidden": True,
                "explanation": "Empty list"
            },
            {
                "input": [
                    [
                        -10,
                        -5,
                        -2,
                        -20
                    ]
                ],
                "expected": -5,
                "is_hidden": True,
                "explanation": "All negative numbers: -2 is 1st, -5 is 2nd"
            },
            {
                "input": [
                    [
                        5,
                        5,
                        4,
                        3,
                        2
                    ]
                ],
                "expected": 4,
                "is_hidden": True,
                "explanation": "Duplicate maximum value"
            }
        ],
        "solution_approach": "Convert to set to remove duplicates. If len < 2 return None. Else sort and return second to last, or use two variables in one pass.",
        "edge_cases": [
            {
                "name": "Duplicate Maximums",
                "input_example": "[10, 10, 8]",
                "why_important": "Students often sort and take list[-2], yielding 10 instead of 8.",
                "what_could_go_wrong": "Returning duplicate max instead of second distinct."
            },
            {
                "name": "All Negative Numbers",
                "input_example": "[-5, -1, -10]",
                "why_important": "Initializing second = 0 fails for negative sets.",
                "what_could_go_wrong": "Returning 0 instead of -5."
            }
        ],
        "hints": [
            "The problem asks for the second largest UNIQUE value. What data structure eliminates duplicates?",
            "Convert numbers to a set to remove duplicates, and check if length is at least 2.",
            "If len(unique) < 2 return None. Otherwise sort the unique set and return sorted(unique)[-2]."
        ]
    },
    {
        "id": "p6_word_frequencies",
        "title": "Word Frequency Counter",
        "difficulty": "Beginner",
        "category": "Dictionaries",
        "order_index": 6,
        "description": "### Problem Statement\nWrite a function `count_word_frequencies(sentence)` that takes a string of words and returns a dictionary mapping each word to the number of times it appears in the sentence.\n\nWords should be matched in **lowercase** and stripped of any leading/trailing punctuation.\n\n### Arguments\n* `sentence` (str): A string containing words separated by whitespace.\n\n### Returns\n* `dict`: Dictionary of word counts `{str: int}`.\n\n### Examples\n```python\ncount_word_frequencies(\"The cat sat on the mat\")\n# Returns: {\"the\": 2, \"cat\": 1, \"sat\": 1, \"on\": 1, \"mat\": 1}\n\ncount_word_frequencies(\"Hello, hello! World.\")\n# Returns: {\"hello\": 2, \"world\": 1}\n```\n",
        "learning_objective": "Master Python dictionaries (`dict.get()`, `in` operator, keys, values) and string cleaning/splitting techniques.",
        "starter_code": "def count_word_frequencies(sentence):\n    # Split into words, strip punctuation, lowercase, and count in dictionary\n    pass\n",
        "function_name": "count_word_frequencies",
        "test_cases": [
            {
                "input": [
                    "The cat sat on the mat"
                ],
                "expected": {
                    "the": 2,
                    "cat": 1,
                    "sat": 1,
                    "on": 1,
                    "mat": 1
                },
                "is_hidden": False,
                "explanation": "'the' appears twice"
            },
            {
                "input": [
                    "Hello, hello! World."
                ],
                "expected": {
                    "hello": 2,
                    "world": 1
                },
                "is_hidden": False,
                "explanation": "Case insensitive and punctuation stripped"
            },
            {
                "input": [
                    ""
                ],
                "expected": {},
                "is_hidden": False,
                "explanation": "Empty string yields empty dictionary"
            },
            {
                "input": [
                    "apple Apple APPLE orange"
                ],
                "expected": {
                    "apple": 3,
                    "orange": 1
                },
                "is_hidden": True,
                "explanation": "Multiple case variations"
            },
            {
                "input": [
                    "one"
                ],
                "expected": {
                    "one": 1
                },
                "is_hidden": True,
                "explanation": "Single word"
            }
        ],
        "solution_approach": "import string; split sentence; for each word: word = word.strip(string.punctuation).lower(); if word: counts[word] = counts.get(word, 0) + 1. Return counts.",
        "edge_cases": [
            {
                "name": "Empty string or only punctuation",
                "input_example": "'... ! ??'",
                "why_important": "Ensure words stripped down to empty strings aren't counted.",
                "what_could_go_wrong": "Adding '' : 1 to dictionary."
            },
            {
                "name": "Consecutive Whitespace",
                "input_example": "'hello    world'",
                "why_important": "str.split() handles multiple spaces gracefully.",
                "what_could_go_wrong": "Using split(' ') produces empty token errors."
            }
        ],
        "hints": [
            "How can you split a sentence into words while ignoring varying whitespace? sentence.split().",
            "Strip punctuation from each word (using string.punctuation) and convert it to lowercase.",
            "Use a dictionary counts[w] = counts.get(w, 0) + 1 for each non-empty cleaned word and return it."
        ]
    },
    {
        "id": "p7_factorial_validation",
        "title": "Factorial with Input Validation",
        "difficulty": "Beginner",
        "category": "Functions & Exceptions",
        "order_index": 7,
        "description": "### Problem Statement\nWrite a function `safe_factorial(n)` that calculates the factorial of a non-negative integer $n$ ($n!$).\n\n* If $n = 0$, $0! = 1$.\n* If $n$ is negative or not an integer, the function must raise a `ValueError` with the message `\"Input must be a non-negative integer\"`.\n\n### Arguments\n* `n` (int): A non-negative integer.\n\n### Returns\n* `int`: The factorial of $n$.\n\n### Raises\n* `ValueError`: When $n < 0$ or $n$ is not of integer type.\n\n### Examples\n```python\nsafe_factorial(5)  # Returns 120\nsafe_factorial(0)  # Returns 1\nsafe_factorial(-3) # Raises ValueError(\"Input must be a non-negative integer\")\n```\n",
        "learning_objective": "Practice function definitions, recursive or iterative algorithms, explicit exception handling (`raise ValueError`), and type validation.",
        "starter_code": "def safe_factorial(n):\n    # Validate input: must be an int and >= 0\n    # Calculate and return factorial\n    pass\n",
        "function_name": "safe_factorial",
        "test_cases": [
            {
                "input": [
                    5
                ],
                "expected": 120,
                "is_hidden": False,
                "explanation": "5 * 4 * 3 * 2 * 1 = 120"
            },
            {
                "input": [
                    0
                ],
                "expected": 1,
                "is_hidden": False,
                "explanation": "0! is defined as 1"
            },
            {
                "input": [
                    1
                ],
                "expected": 1,
                "is_hidden": False,
                "explanation": "1! = 1"
            },
            {
                "input": [
                    7
                ],
                "expected": 5040,
                "is_hidden": True,
                "explanation": "7! = 5040"
            },
            {
                "input": [
                    -1
                ],
                "expected": "EXCEPTION:ValueError",
                "is_hidden": True,
                "explanation": "Negative numbers should raise ValueError"
            },
            {
                "input": [
                    3.5
                ],
                "expected": "EXCEPTION:ValueError",
                "is_hidden": True,
                "explanation": "Non-integers should raise ValueError"
            }
        ],
        "solution_approach": "Check if not isinstance(n, int) or isinstance(n, bool) or n < 0: raise ValueError(...). Accumulate product from 1 to n.",
        "edge_cases": [
            {
                "name": "Zero (0!)",
                "input_example": "0",
                "why_important": "Mathematical convention where 0! = 1.",
                "what_could_go_wrong": "Returning 0 instead of 1."
            },
            {
                "name": "Boolean passed as int",
                "input_example": "True",
                "why_important": "In Python, bool is a subclass of int (isinstance(True, int) is True).",
                "what_could_go_wrong": "Accidentally treating True as 1 without typecheck."
            }
        ],
        "hints": [
            "What check confirms n is an integer and non-negative? Notice isinstance(True, int) is True in Python.",
            "Check: if type(n) is not int or n < 0: raise ValueError(\"Input must be a non-negative integer\").",
            "After validation, multiply numbers from 1 to n (or return 1 if n == 0)."
        ]
    },
    {
        "id": "p8_balanced_parentheses",
        "title": "Balanced Parentheses Checker",
        "difficulty": "Beginner",
        "category": "Data Structures",
        "order_index": 8,
        "description": "### Problem Statement\nWrite a function `is_balanced(brackets)` that takes a string containing only brackets `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`, and returns `True` if the brackets are balanced and closed in the correct order, and `False` otherwise.\n\n### Arguments\n* `brackets` (str): A string consisting of bracket characters.\n\n### Returns\n* `bool`: `True` if balanced, `False` otherwise.\n\n### Examples\n```python\nis_balanced(\"()[]{}\") # Returns True\nis_balanced(\"([{}])\") # Returns True\nis_balanced(\"(]\")     # Returns False\nis_balanced(\"([)]\")   # Returns False\nis_balanced(\"(\")      # Returns False\n```\n",
        "learning_objective": "Implement the classic Stack data structure pattern (LIFO), dictionary mapping for closing brackets, and boundary conditions.",
        "starter_code": "def is_balanced(brackets):\n    # Use a stack (list) to keep track of opening brackets\n    pass\n",
        "function_name": "is_balanced",
        "test_cases": [
            {
                "input": [
                    "()[]{}"
                ],
                "expected": True,
                "is_hidden": False,
                "explanation": "All matched in sequence"
            },
            {
                "input": [
                    "([{}])"
                ],
                "expected": True,
                "is_hidden": False,
                "explanation": "Properly nested"
            },
            {
                "input": [
                    "(]"
                ],
                "expected": False,
                "is_hidden": False,
                "explanation": "Mismatched closing bracket"
            },
            {
                "input": [
                    "([)]"
                ],
                "expected": False,
                "is_hidden": False,
                "explanation": "Incorrect closing order"
            },
            {
                "input": [
                    ""
                ],
                "expected": True,
                "is_hidden": True,
                "explanation": "Empty string is balanced"
            },
            {
                "input": [
                    "("
                ],
                "expected": False,
                "is_hidden": True,
                "explanation": "Unclosed opening bracket"
            },
            {
                "input": [
                    ")"
                ],
                "expected": False,
                "is_hidden": True,
                "explanation": "Closing bracket with empty stack"
            },
            {
                "input": [
                    "((()))"
                ],
                "expected": True,
                "is_hidden": True,
                "explanation": "Deeply nested"
            }
        ],
        "solution_approach": "Map pairs = {')':'(', '}':'{', ']':'['}. For char in brackets: if char in pairs.values(): stack.append(char) elif char in pairs: if not stack or stack.pop() != pairs[char]: return False. Return len(stack) == 0.",
        "edge_cases": [
            {
                "name": "Closing bracket first",
                "input_example": "')('",
                "why_important": "Stack is empty when pop is attempted.",
                "what_could_go_wrong": "IndexError on empty list pop."
            },
            {
                "name": "Only opening brackets",
                "input_example": "'((('",
                "why_important": "Loop finishes without errors, but stack is not empty.",
                "what_could_go_wrong": "Returning True because no mismatch was hit."
            }
        ],
        "hints": [
            "Which data structure matches the most recently opened bracket with its closing counterpart? (Stack)",
            "Maintain a list stack. For opening brackets ( [ {, append. For closing, pop and verify.",
            "If stack is empty on pop or the popped bracket does not match, return False. At the end return len(stack) == 0."
        ]
    },
    {
        "id": "p9_count_vowels",
        "title": "Count Vowels",
        "difficulty": "Beginner",
        "category": "Strings",
        "order_index": 9,
        "description": "### Problem Statement\nWrite a function `count_vowels(text)` that counts and returns the number of vowels (`a`, `e`, `i`, `o`, `u`, case-insensitive) in a string.\n\n### Arguments\n* `text` (str): An input string.\n\n### Returns\n* `int`: The total number of vowels found.\n\n### Examples\n```python\ncount_vowels(\"hello\")  # Returns 2\ncount_vowels(\"Python\") # Returns 1\ncount_vowels(\"\")       # Returns 0\n```",
        "learning_objective": "Iterate through strings, use membership testing with `in`, and standardize casing with `.lower()`.",
        "starter_code": "def count_vowels(text):\n    # Count vowels (a, e, i, o, u) case-insensitively\n    pass\n",
        "function_name": "count_vowels",
        "test_cases": [
            {
                "input": [
                    "hello"
                ],
                "expected": 2,
                "is_hidden": False,
                "explanation": "'e' and 'o'"
            },
            {
                "input": [
                    ""
                ],
                "expected": 0,
                "is_hidden": False,
                "explanation": "Empty string has 0 vowels"
            },
            {
                "input": [
                    "aeiou"
                ],
                "expected": 5,
                "is_hidden": False,
                "explanation": "All vowels"
            },
            {
                "input": [
                    "bcdfg"
                ],
                "expected": 0,
                "is_hidden": True,
                "explanation": "No vowels"
            },
            {
                "input": [
                    "Python"
                ],
                "expected": 1,
                "is_hidden": True,
                "explanation": "Only 'o' is a vowel"
            },
            {
                "input": [
                    "AEIOU"
                ],
                "expected": 5,
                "is_hidden": True,
                "explanation": "Uppercase vowels"
            }
        ],
        "solution_approach": "Convert text to lowercase and count characters that are in 'aeiou'.",
        "edge_cases": [
            {
                "name": "Empty String",
                "input_example": "''",
                "why_important": "Function should return 0 without error.",
                "what_could_go_wrong": "Unbound accumulator variable."
            },
            {
                "name": "Uppercase Vowels",
                "input_example": "'AEIOU'",
                "why_important": "Requires case-insensitivity.",
                "what_could_go_wrong": "Only checking lowercase 'aeiou'."
            }
        ],
        "hints": [
            "What characters qualify as vowels? How do you check membership in Python?",
            "Think about iterating over each character and using 'in' with a collection of vowels.",
            "Loop through each character, convert to lowercase with .lower(), check if it is in 'aeiou', and increment a counter."
        ]
    },
    {
        "id": "p10_find_maximum",
        "title": "Find Maximum in List",
        "difficulty": "Beginner",
        "category": "Lists & Indexing",
        "order_index": 10,
        "description": "### Problem Statement\nWrite a function `find_maximum(numbers)` that finds and returns the largest number in a list **without** using Python's built-in `max()` function.\n\nIf the list is empty, return `None`.\n\n### Arguments\n* `numbers` (list of int or float): A list of numeric values.\n\n### Returns\n* `int`, `float`, or `None`: The maximum value found, or `None` if empty.\n\n### Examples\n```python\nfind_maximum([3, 1, 4, 1, 5, 9]) # Returns 9\nfind_maximum([-5, -2, -8])       # Returns -2\nfind_maximum([])                 # Returns None\n```",
        "learning_objective": "Implement linear scans, maintain running extremum state, and handle empty list boundary conditions.",
        "starter_code": "def find_maximum(numbers):\n    # Find the maximum value without using built-in max()\n    pass\n",
        "function_name": "find_maximum",
        "test_cases": [
            {
                "input": [
                    [
                        3,
                        1,
                        4,
                        1,
                        5,
                        9
                    ]
                ],
                "expected": 9,
                "is_hidden": False,
                "explanation": "9 is largest"
            },
            {
                "input": [
                    [
                        1
                    ]
                ],
                "expected": 1,
                "is_hidden": False,
                "explanation": "Single item list"
            },
            {
                "input": [
                    []
                ],
                "expected": None,
                "is_hidden": False,
                "explanation": "Empty list returns None"
            },
            {
                "input": [
                    [
                        -5,
                        -2,
                        -8
                    ]
                ],
                "expected": -2,
                "is_hidden": True,
                "explanation": "All negative numbers: -2 is largest"
            },
            {
                "input": [
                    [
                        0,
                        0,
                        0
                    ]
                ],
                "expected": 0,
                "is_hidden": True,
                "explanation": "All identical elements"
            }
        ],
        "solution_approach": "Check if numbers is empty. Initialize largest to numbers[0], loop through remaining and update largest when a bigger number is found.",
        "edge_cases": [
            {
                "name": "Empty List",
                "input_example": "[]",
                "why_important": "Guard against IndexError.",
                "what_could_go_wrong": "Accessing numbers[0] on empty list."
            },
            {
                "name": "All Negative Numbers",
                "input_example": "[-5, -2, -8]",
                "why_important": "Initializing maximum to 0 will fail.",
                "what_could_go_wrong": "Returning 0 instead of -2."
            }
        ],
        "hints": [
            "How would you find the biggest number if you had to scan a list one item at a time?",
            "Consider tracking a variable that holds the 'current largest seen so far' as you iterate.",
            "Initialize your running maximum to the first element numbers[0] (after checking if list is empty), then loop from index 1 comparing each element."
        ]
    },
    {
        "id": "p11_flatten_list",
        "title": "Flatten Nested List",
        "difficulty": "Intermediate",
        "category": "Lists & Indexing",
        "order_index": 11,
        "description": "### Problem Statement\nWrite a function `flatten(nested)` that flattens a list of lists by exactly one level of nesting.\n\n### Arguments\n* `nested` (list of lists): A list where each element is itself a list.\n\n### Returns\n* `list`: A flat 1D list containing all elements in order.\n\n### Examples\n```python\nflatten([[1, 2], [3, 4], [5]]) # Returns [1, 2, 3, 4, 5]\nflatten([[], [1]])              # Returns [1]\nflatten([])                     # Returns []\n```",
        "learning_objective": "Understand nested loops, list comprehension with double iterators, and `list.extend()`.",
        "starter_code": "def flatten(nested):\n    # Flatten one level of nesting into a single list\n    pass\n",
        "function_name": "flatten",
        "test_cases": [
            {
                "input": [
                    [
                        [
                            1,
                            2
                        ],
                        [
                            3,
                            4
                        ],
                        [
                            5
                        ]
                    ]
                ],
                "expected": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "is_hidden": False,
                "explanation": "Combines sublists"
            },
            {
                "input": [
                    []
                ],
                "expected": [],
                "is_hidden": False,
                "explanation": "Empty outer list"
            },
            {
                "input": [
                    [
                        [
                            1
                        ],
                        [
                            2
                        ],
                        [
                            3
                        ]
                    ]
                ],
                "expected": [
                    1,
                    2,
                    3
                ],
                "is_hidden": False,
                "explanation": "Single item sublists"
            },
            {
                "input": [
                    [
                        [
                            1,
                            2,
                            3
                        ]
                    ]
                ],
                "expected": [
                    1,
                    2,
                    3
                ],
                "is_hidden": True,
                "explanation": "Single sublist"
            },
            {
                "input": [
                    [
                        [],
                        [
                            1
                        ]
                    ]
                ],
                "expected": [
                    1
                ],
                "is_hidden": True,
                "explanation": "Empty sublist handled gracefully"
            }
        ],
        "solution_approach": "Initialize an empty list result, iterate over each sublist in nested, and extend result with sublist.",
        "edge_cases": [
            {
                "name": "Empty Sublists",
                "input_example": "[[], [1], []]",
                "why_important": "Ensures empty sublists do not introduce None or empty tokens.",
                "what_could_go_wrong": "Appending sublist instead of extending."
            },
            {
                "name": "Empty Input",
                "input_example": "[]",
                "why_important": "Loop should terminate immediately returning [].",
                "what_could_go_wrong": "IndexError."
            }
        ],
        "hints": [
            "How do you combine multiple lists into one? What list method appends all items from an iterable?",
            "Consider iterating over each sub-list in nested and extending a result list with its items.",
            "Start with result = [], loop over each sublist in nested, call result.extend(sublist), then return result."
        ]
    },
    {
        "id": "p12_group_anagrams",
        "title": "Group Anagrams",
        "difficulty": "Intermediate",
        "category": "Dictionaries",
        "order_index": 12,
        "description": "### Problem Statement\nWrite a function `group_anagrams(words)` that groups a list of strings into groups of anagrams.\n\nAn anagram is a word formed by rearranging the letters of another word. The relative order of groups does not matter, but words within each group should be clustered together.\n\n### Arguments\n* `words` (list of str): A list of lowercase words.\n\n### Returns\n* `list of lists of str`: Words grouped by anagram equivalence.\n\n### Examples\n```python\n# Returns groups like [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]\ngroup_anagrams([\"eat\", \"tea\", \"tan\", \"ate\", \"nat\", \"bat\"])\ngroup_anagrams([]) # Returns []\n```",
        "learning_objective": "Use canonical representations (sorted strings or character counts) as dictionary keys for grouping.",
        "starter_code": "def group_anagrams(words):\n    # Group words that are anagrams of each other\n    pass\n",
        "function_name": "group_anagrams",
        "test_cases": [
            {
                "input": [
                    [
                        "eat",
                        "tea",
                        "tan",
                        "ate",
                        "nat",
                        "bat"
                    ]
                ],
                "expected": [
                    [
                        "eat",
                        "tea",
                        "ate"
                    ],
                    [
                        "tan",
                        "nat"
                    ],
                    [
                        "bat"
                    ]
                ],
                "is_hidden": False,
                "explanation": "Standard anagram groups"
            },
            {
                "input": [
                    []
                ],
                "expected": [],
                "is_hidden": False,
                "explanation": "Empty list gives empty result"
            },
            {
                "input": [
                    [
                        "a"
                    ]
                ],
                "expected": [
                    [
                        "a"
                    ]
                ],
                "is_hidden": False,
                "explanation": "Single word group"
            },
            {
                "input": [
                    [
                        "cab",
                        "tin",
                        "pew",
                        "duh",
                        "may",
                        "ill",
                        "buy",
                        "bar",
                        "max",
                        "doc"
                    ]
                ],
                "expected": [
                    [
                        "cab"
                    ],
                    [
                        "tin"
                    ],
                    [
                        "pew"
                    ],
                    [
                        "duh"
                    ],
                    [
                        "may"
                    ],
                    [
                        "ill"
                    ],
                    [
                        "buy"
                    ],
                    [
                        "bar"
                    ],
                    [
                        "max"
                    ],
                    [
                        "doc"
                    ]
                ],
                "is_hidden": True,
                "explanation": "No anagrams"
            }
        ],
        "solution_approach": "Use a dict mapping ''.join(sorted(word)) to a list of matching words. Return list(dict.values()).",
        "edge_cases": [
            {
                "name": "Empty List",
                "input_example": "[]",
                "why_important": "Should return empty list immediately.",
                "what_could_go_wrong": "Crash on empty iteration."
            },
            {
                "name": "Single Character Words",
                "input_example": "['a', 'b', 'a']",
                "why_important": "Single characters are their own sorted form.",
                "what_could_go_wrong": "Key collision or missing duplicates."
            }
        ],
        "hints": [
            "What invariant do all anagrams of a word share when you reorder their letters alphabetically?",
            "Use a dictionary where the key is the sorted version of each word, e.g. ''.join(sorted(w)).",
            "For each word, compute key = ''.join(sorted(word)), append word to groups.setdefault(key, []), and return list(groups.values())."
        ]
    },
    {
        "id": "p13_binary_search",
        "title": "Binary Search",
        "difficulty": "Intermediate",
        "category": "Lists & Indexing",
        "order_index": 13,
        "description": "### Problem Statement\nWrite a function `binary_search(arr, target)` that implements the binary search algorithm on a sorted list of integers.\n\nIf `target` is present in `arr`, return its 0-based index. If not found, return `-1`.\n\n### Arguments\n* `arr` (list of int): A sorted list of integers in ascending order.\n* `target` (int): Value to search for.\n\n### Returns\n* `int`: Index of target, or `-1`.\n\n### Examples\n```python\nbinary_search([1, 3, 5, 7, 9], 5) # Returns 2\nbinary_search([1, 3, 5, 7, 9], 6) # Returns -1\nbinary_search([], 5)              # Returns -1\n```",
        "learning_objective": "Master logarithmic divide-and-conquer search, pointer management (`left`, `right`), and mid calculation.",
        "starter_code": "def binary_search(arr, target):\n    # Perform binary search on sorted arr for target, return index or -1\n    pass\n",
        "function_name": "binary_search",
        "test_cases": [
            {
                "input": [
                    [
                        1,
                        3,
                        5,
                        7,
                        9
                    ],
                    5
                ],
                "expected": 2,
                "is_hidden": False,
                "explanation": "Target 5 is at index 2"
            },
            {
                "input": [
                    [
                        1,
                        3,
                        5,
                        7,
                        9
                    ],
                    6
                ],
                "expected": -1,
                "is_hidden": False,
                "explanation": "Target 6 not found"
            },
            {
                "input": [
                    [],
                    5
                ],
                "expected": -1,
                "is_hidden": False,
                "explanation": "Empty list returns -1"
            },
            {
                "input": [
                    [
                        1
                    ],
                    1
                ],
                "expected": 0,
                "is_hidden": True,
                "explanation": "Single item match"
            },
            {
                "input": [
                    [
                        1,
                        2,
                        3,
                        4,
                        5
                    ],
                    1
                ],
                "expected": 0,
                "is_hidden": True,
                "explanation": "Target at first element"
            },
            {
                "input": [
                    [
                        1,
                        2,
                        3,
                        4,
                        5
                    ],
                    5
                ],
                "expected": 4,
                "is_hidden": True,
                "explanation": "Target at last element"
            }
        ],
        "solution_approach": "Maintain left = 0, right = len(arr) - 1. While left <= right: mid = (left + right) // 2. If arr[mid] == target: return mid. Else adjust left or right.",
        "edge_cases": [
            {
                "name": "Target at Extremities",
                "input_example": "arr=[1,2,3], target=1 or 3",
                "why_important": "Ensures boundary pointers don't skip the first or last element.",
                "what_could_go_wrong": "Using < instead of <= in while loop."
            },
            {
                "name": "Empty Array",
                "input_example": "arr=[], target=5",
                "why_important": "right becomes -1; while left <= right must not execute.",
                "what_could_go_wrong": "IndexError on empty array."
            }
        ],
        "hints": [
            "Binary search works by repeatedly halving the search space. What are your pointer boundary variables?",
            "Maintain left and right pointers. In a while left <= right loop, compute mid = (left + right) // 2.",
            "Compare arr[mid] with target: if equal return mid; if arr[mid] < target set left = mid + 1; else set right = mid - 1. Return -1 if loop ends."
        ]
    },
    {
        "id": "p14_rotate_list",
        "title": "Rotate List",
        "difficulty": "Intermediate",
        "category": "Lists & Indexing",
        "order_index": 14,
        "description": "### Problem Statement\nWrite a function `rotate_list(lst, k)` that rotates a list to the right by `k` steps.\n\n### Arguments\n* `lst` (list): The list to rotate.\n* `k` (int): A non-negative integer number of steps to rotate right.\n\n### Returns\n* `list`: A new list rotated right by `k` positions.\n\n### Examples\n```python\nrotate_list([1, 2, 3, 4, 5], 2) # Returns [4, 5, 1, 2, 3]\nrotate_list([1, 2, 3], 0)       # Returns [1, 2, 3]\nrotate_list([], 3)              # Returns []\n```",
        "learning_objective": "Practice Python list slicing, negative index slicing, and the modulo operator `%` for cyclic shifts.",
        "starter_code": "def rotate_list(lst, k):\n    # Rotate lst to the right by k steps\n    pass\n",
        "function_name": "rotate_list",
        "test_cases": [
            {
                "input": [
                    [
                        1,
                        2,
                        3,
                        4,
                        5
                    ],
                    2
                ],
                "expected": [
                    4,
                    5,
                    1,
                    2,
                    3
                ],
                "is_hidden": False,
                "explanation": "Shifted right 2 spots"
            },
            {
                "input": [
                    [
                        1,
                        2,
                        3
                    ],
                    0
                ],
                "expected": [
                    1,
                    2,
                    3
                ],
                "is_hidden": False,
                "explanation": "0 rotation"
            },
            {
                "input": [
                    [],
                    3
                ],
                "expected": [],
                "is_hidden": False,
                "explanation": "Empty list"
            },
            {
                "input": [
                    [
                        1,
                        2,
                        3
                    ],
                    3
                ],
                "expected": [
                    1,
                    2,
                    3
                ],
                "is_hidden": True,
                "explanation": "k equals length"
            },
            {
                "input": [
                    [
                        1,
                        2,
                        3,
                        4,
                        5
                    ],
                    7
                ],
                "expected": [
                    4,
                    5,
                    1,
                    2,
                    3
                ],
                "is_hidden": True,
                "explanation": "k greater than length (7 % 5 = 2)"
            }
        ],
        "solution_approach": "If not lst: return []. k = k % len(lst). If k == 0: return lst[:]. Otherwise return lst[-k:] + lst[:-k].",
        "edge_cases": [
            {
                "name": "k >= len(lst)",
                "input_example": "lst=[1,2,3], k=7",
                "why_important": "Requires modulo to avoid slicing past array length.",
                "what_could_go_wrong": "Over-rotating or wrong split point."
            },
            {
                "name": "Empty List",
                "input_example": "lst=[], k=5",
                "why_important": "ZeroDivisionError if calculating k % len(lst) without guard.",
                "what_could_go_wrong": "Crash with ZeroDivisionError."
            }
        ],
        "hints": [
            "What happens when k is larger than the length of the list? How can the % operator help?",
            "If the list is empty, return []. For non-empty lists, effective rotation is k % len(lst).",
            "Use slicing: lst[-k:] gives the elements moving to the front, and lst[:-k] gives the rest. Concatenate them."
        ]
    },
    {
        "id": "p15_prime_sieve",
        "title": "Count Primes",
        "difficulty": "Intermediate",
        "category": "Loops",
        "order_index": 15,
        "description": "### Problem Statement\nWrite a function `count_primes(n)` that returns the number of prime numbers strictly less than a non-negative integer `n`.\n\n### Arguments\n* `n` (int): Upper bound limit (exclusive).\n\n### Returns\n* `int`: Count of prime numbers < `n`.\n\n### Examples\n```python\ncount_primes(10) # Returns 4 (2, 3, 5, 7)\ncount_primes(0)  # Returns 0\ncount_primes(1)  # Returns 0\ncount_primes(20) # Returns 8\n```",
        "learning_objective": "Implement the classic Sieve of Eratosthenes algorithm for $O(n \\log \\log n)$ prime finding.",
        "starter_code": "def count_primes(n):\n    # Count prime numbers strictly less than n\n    pass\n",
        "function_name": "count_primes",
        "test_cases": [
            {
                "input": [
                    10
                ],
                "expected": 4,
                "is_hidden": False,
                "explanation": "2, 3, 5, 7 are the 4 primes < 10"
            },
            {
                "input": [
                    0
                ],
                "expected": 0,
                "is_hidden": False,
                "explanation": "No primes < 0"
            },
            {
                "input": [
                    1
                ],
                "expected": 0,
                "is_hidden": False,
                "explanation": "No primes < 1"
            },
            {
                "input": [
                    2
                ],
                "expected": 0,
                "is_hidden": True,
                "explanation": "Smallest prime is 2, so strictly less than 2 has 0"
            },
            {
                "input": [
                    20
                ],
                "expected": 8,
                "is_hidden": True,
                "explanation": "Primes: 2, 3, 5, 7, 11, 13, 17, 19"
            },
            {
                "input": [
                    100
                ],
                "expected": 25,
                "is_hidden": True,
                "explanation": "25 primes below 100"
            }
        ],
        "solution_approach": "Create boolean array is_prime of size n. Mark 0 and 1 as False. For p from 2 to int(n**0.5) + 1, if is_prime[p], mark multiples p*p to n as False. Return sum(is_prime).",
        "edge_cases": [
            {
                "name": "n <= 2",
                "input_example": "n=0, 1, 2",
                "why_important": "No primes strictly less than 2.",
                "what_could_go_wrong": "IndexError on small arrays."
            },
            {
                "name": "Square Boundaries",
                "input_example": "p*p optimization",
                "why_important": "Inner loop starting at p*p is standard Sieve optimization.",
                "what_could_go_wrong": "Off-by-one errors."
            }
        ],
        "hints": [
            "A prime is an integer greater than 1 divisible only by 1 and itself. Think about marking composite numbers.",
            "The Sieve of Eratosthenes creates an array is_prime = [True] * n. Set index 0 and 1 to False.",
            "For p from 2 up to sqrt(n), if is_prime[p] is True, mark all multiples p*p, p*p+p, ... as False. Finally return sum(is_prime)."
        ]
    },
    {
        "id": "p16_merge_dicts",
        "title": "Merge Dictionaries",
        "difficulty": "Intermediate",
        "category": "Dictionaries",
        "order_index": 16,
        "description": "### Problem Statement\nWrite a function `merge_dicts(d1, d2)` that merges two dictionaries into a **new** dictionary.\n\nIf a key exists in both dictionaries, the value from `d2` should overwrite the value from `d1`. Neither input dictionary should be modified.\n\n### Arguments\n* `d1` (dict): First dictionary.\n* `d2` (dict): Second dictionary.\n\n### Returns\n* `dict`: New merged dictionary.\n\n### Examples\n```python\nmerge_dicts({\"a\": 1, \"b\": 2}, {\"b\": 3, \"c\": 4})\n# Returns {\"a\": 1, \"b\": 3, \"c\": 4}\n\nmerge_dicts({}, {\"a\": 1}) # Returns {\"a\": 1}\n```",
        "learning_objective": "Practice dictionary unpacking (`{**d1, **d2}`), copying, and non-destructive data updates in Python.",
        "starter_code": "def merge_dicts(d1, d2):\n    # Merge d1 and d2 into a new dictionary without mutating originals\n    pass\n",
        "function_name": "merge_dicts",
        "test_cases": [
            {
                "input": [
                    {
                        "a": 1,
                        "b": 2
                    },
                    {
                        "b": 3,
                        "c": 4
                    }
                ],
                "expected": {
                    "a": 1,
                    "b": 3,
                    "c": 4
                },
                "is_hidden": False,
                "explanation": "Key 'b' overwritten by d2"
            },
            {
                "input": [
                    {},
                    {
                        "a": 1
                    }
                ],
                "expected": {
                    "a": 1
                },
                "is_hidden": False,
                "explanation": "Empty d1"
            },
            {
                "input": [
                    {
                        "a": 1
                    },
                    {}
                ],
                "expected": {
                    "a": 1
                },
                "is_hidden": False,
                "explanation": "Empty d2"
            },
            {
                "input": [
                    {},
                    {}
                ],
                "expected": {},
                "is_hidden": True,
                "explanation": "Both empty"
            }
        ],
        "solution_approach": "Return {**d1, **d2} or create result = d1.copy() then result.update(d2) and return result.",
        "edge_cases": [
            {
                "name": "Mutation Prevention",
                "input_example": "Calling d1.update(d2) directly",
                "why_important": "Must return a new dictionary without mutating d1 or d2.",
                "what_could_go_wrong": "Accidental side-effect modifying d1."
            },
            {
                "name": "Empty Inputs",
                "input_example": "d1={}, d2={}",
                "why_important": "Returns clean empty dictionary.",
                "what_could_go_wrong": "NoneType errors."
            }
        ],
        "hints": [
            "How do you combine two dictionaries in Python while ensuring you don't mutate either original input?",
            "Look at Python's dictionary unpacking syntax `{**d1, **d2}` or `d1.copy()`.",
            "Create a copy of d1 using `result = dict(d1)`, then call `result.update(d2)` and return `result`."
        ]
    },
    {
        "id": "p17_longest_valid_parens",
        "title": "Longest Valid Parentheses",
        "difficulty": "Intermediate",
        "category": "Data Structures",
        "order_index": 17,
        "description": "### Problem Statement\nWrite a function `longest_valid_parens(s)` that takes a string containing only `'('` and `')'`, and finds the length of the longest valid (well-formed) parentheses substring.\n\n### Arguments\n* `s` (str): String containing only `'('` and `')'`.\n\n### Returns\n* `int`: Length of the longest valid substring.\n\n### Examples\n```python\nlongest_valid_parens(\"(()\")    # Returns 2 (\"()\")\nlongest_valid_parens(\")()())\") # Returns 4 (\"()()\")\nlongest_valid_parens(\"\")       # Returns 0\n```",
        "learning_objective": "Utilize a stack storing boundary indices to measure contiguous matching intervals in $O(n)$ time.",
        "starter_code": "def longest_valid_parens(s):\n    # Find the length of the longest well-formed parentheses substring\n    pass\n",
        "function_name": "longest_valid_parens",
        "test_cases": [
            {
                "input": [
                    "(()"
                ],
                "expected": 2,
                "is_hidden": False,
                "explanation": "'()' has length 2"
            },
            {
                "input": [
                    ")()())"
                ],
                "expected": 4,
                "is_hidden": False,
                "explanation": "'()()' has length 4"
            },
            {
                "input": [
                    ""
                ],
                "expected": 0,
                "is_hidden": False,
                "explanation": "Empty string yields 0"
            },
            {
                "input": [
                    "()"
                ],
                "expected": 2,
                "is_hidden": True,
                "explanation": "Exact pair"
            },
            {
                "input": [
                    "(())"
                ],
                "expected": 4,
                "is_hidden": True,
                "explanation": "Nested pair"
            },
            {
                "input": [
                    ")("
                ],
                "expected": 0,
                "is_hidden": True,
                "explanation": "Inverted pair"
            }
        ],
        "solution_approach": "Initialize stack = [-1] as boundary. For index i, char in s: if char == '(': stack.append(i). Else: stack.pop(); if not stack: stack.append(i); else: max_len = max(max_len, i - stack[-1]).",
        "edge_cases": [
            {
                "name": "Closing Bracket First",
                "input_example": "')'",
                "why_important": "Stack pops base -1; must reset base to index 0.",
                "what_could_go_wrong": "IndexError on empty stack."
            },
            {
                "name": "No Valid Pairs",
                "input_example": "'((('",
                "why_important": "Stack only grows; max_len remains 0.",
                "what_could_go_wrong": "False positive lengths."
            }
        ],
        "hints": [
            "Think about using a stack that tracks INDICES of parentheses rather than just the characters.",
            "Initialize your stack with `[-1]` as a starting reference point for calculating substring lengths.",
            "When seeing '(', push its index i. When seeing ')', pop. If stack is now empty, push i as the new base; otherwise, update max_len with `i - stack[-1]`."
        ]
    },
    {
        "id": "p18_two_sum",
        "title": "Two Sum",
        "difficulty": "Intermediate",
        "category": "Dictionaries",
        "order_index": 18,
        "description": "### Problem Statement\nWrite a function `two_sum(nums, target)` that returns the indices of the two numbers in `nums` such that they add up to `target`.\n\nAssume that each input has exactly one solution, and you may not use the same element twice. Return the indices sorted in ascending order `[i, j]`.\n\n### Arguments\n* `nums` (list of int): A list of integers.\n* `target` (int): Target sum.\n\n### Returns\n* `list of int`: Sorted pair of indices `[i, j]`.\n\n### Examples\n```python\ntwo_sum([2, 7, 11, 15], 9) # Returns [0, 1]\ntwo_sum([3, 2, 4], 6)       # Returns [1, 2]\ntwo_sum([3, 3], 6)          # Returns [0, 1]\n```",
        "learning_objective": "Achieve $O(n)$ time complexity using a hash map lookup instead of brute force $O(n^2)$ nested loops.",
        "starter_code": "def two_sum(nums, target):\n    # Return sorted indices [i, j] of elements summing to target\n    pass\n",
        "function_name": "two_sum",
        "test_cases": [
            {
                "input": [
                    [
                        2,
                        7,
                        11,
                        15
                    ],
                    9
                ],
                "expected": [
                    0,
                    1
                ],
                "is_hidden": False,
                "explanation": "nums[0] + nums[1] = 9"
            },
            {
                "input": [
                    [
                        3,
                        2,
                        4
                    ],
                    6
                ],
                "expected": [
                    1,
                    2
                ],
                "is_hidden": False,
                "explanation": "nums[1] + nums[2] = 6"
            },
            {
                "input": [
                    [
                        3,
                        3
                    ],
                    6
                ],
                "expected": [
                    0,
                    1
                ],
                "is_hidden": False,
                "explanation": "nums[0] + nums[1] = 6"
            },
            {
                "input": [
                    [
                        1,
                        2,
                        3,
                        4
                    ],
                    7
                ],
                "expected": [
                    2,
                    3
                ],
                "is_hidden": True,
                "explanation": "nums[2] + nums[3] = 7"
            }
        ],
        "solution_approach": "Use a dict seen = {} to store value -> index. For index i, num in enumerate(nums): complement = target - num. If complement in seen: return sorted([seen[complement], i]). Else: seen[num] = i.",
        "edge_cases": [
            {
                "name": "Duplicate Values",
                "input_example": "nums=[3,3], target=6",
                "why_important": "Complement is checked before inserting current value to prevent using the same index twice.",
                "what_could_go_wrong": "Overwriting index before checking."
            },
            {
                "name": "Negative Target/Values",
                "input_example": "nums=[-1, -2, -3], target=-5",
                "why_important": "Subtraction math holds for negative values.",
                "what_could_go_wrong": "Absolute value mistakes."
            }
        ],
        "hints": [
            "A brute-force double loop is O(n^2). Can you do this in a single pass O(n) using extra memory?",
            "For each number x at index i, the required partner is target - x. Have you seen target - x previously?",
            "Store numbers and their indices in a dictionary as you iterate: if `target - num` is already in seen, return `sorted([seen[target - num], i])`."
        ]
    },
    {
        "id": "p19_matrix_transpose",
        "title": "Matrix Transpose",
        "difficulty": "Intermediate",
        "category": "Lists & Indexing",
        "order_index": 19,
        "description": "### Problem Statement\nWrite a function `transpose(matrix)` that computes and returns the transpose of a 2D matrix (represented as a list of lists).\n\nTransposing flips a matrix over its diagonal, switching its row and column indices.\n\n### Arguments\n* `matrix` (list of lists): A 2D list of dimensions M x N.\n\n### Returns\n* `list of lists`: The transposed matrix of dimensions N x M.\n\n### Examples\n```python\ntranspose([[1, 2, 3], [4, 5, 6]])\n# Returns [[1, 4], [2, 5], [3, 6]]\n\ntranspose([[1]]) # Returns [[1]]\ntranspose([])    # Returns []\n```",
        "learning_objective": "Work with multi-dimensional lists, grid index transformations `(i, j) -> (j, i)`, and `zip(*matrix)`.",
        "starter_code": "def transpose(matrix):\n    # Return the transposed 2D matrix\n    pass\n",
        "function_name": "transpose",
        "test_cases": [
            {
                "input": [
                    [
                        [
                            1,
                            2,
                            3
                        ],
                        [
                            4,
                            5,
                            6
                        ]
                    ]
                ],
                "expected": [
                    [
                        1,
                        4
                    ],
                    [
                        2,
                        5
                    ],
                    [
                        3,
                        6
                    ]
                ],
                "is_hidden": False,
                "explanation": "2x3 becomes 3x2"
            },
            {
                "input": [
                    [
                        [
                            1
                        ]
                    ]
                ],
                "expected": [
                    [
                        1
                    ]
                ],
                "is_hidden": False,
                "explanation": "1x1 matrix"
            },
            {
                "input": [
                    []
                ],
                "expected": [],
                "is_hidden": False,
                "explanation": "Empty matrix"
            },
            {
                "input": [
                    [
                        [
                            1,
                            2
                        ],
                        [
                            3,
                            4
                        ]
                    ]
                ],
                "expected": [
                    [
                        1,
                        3
                    ],
                    [
                        2,
                        4
                    ]
                ],
                "is_hidden": True,
                "explanation": "2x2 square matrix"
            }
        ],
        "solution_approach": "If not matrix or not matrix[0]: return []. Return [list(row) for row in zip(*matrix)].",
        "edge_cases": [
            {
                "name": "Empty Matrix",
                "input_example": "[]",
                "why_important": "Guard against accessing matrix[0].",
                "what_could_go_wrong": "IndexError on matrix[0]."
            },
            {
                "name": "Single Row / Single Column",
                "input_example": "[[1,2,3]]",
                "why_important": "Converts 1x3 into 3x1 [[1],[2],[3]].",
                "what_could_go_wrong": "Flattening instead of nesting."
            }
        ],
        "hints": [
            "Transposing swaps row and column indices: the element at row i, col j moves to row j, col i.",
            "In Python, unpacking rows with `zip(*matrix)` groups columns together automatically.",
            "Check for empty matrix: if not matrix: return []. Then return `[list(col) for col in zip(*matrix)]`."
        ]
    },
    {
        "id": "p20_string_compression",
        "title": "String Compression",
        "difficulty": "Intermediate",
        "category": "Strings",
        "order_index": 20,
        "description": "### Problem Statement\nWrite a function `compress(s)` that performs basic string compression using the counts of repeated characters (run-length encoding).\n\nFor example, `\"aaabbc\"` becomes `\"a3b2c1\"`.\nIf the \"compressed\" string would not become strictly shorter than the original string, your function should return the original string.\n\n### Arguments\n* `s` (str): Input string.\n\n### Returns\n* `str`: Compressed string if shorter, otherwise `s`.\n\n### Examples\n```python\ncompress(\"aaabbc\") # Returns \"a3b2c1\" (len 6 vs 6, so wait: len(\"a3b2c1\")==6 not strictly shorter -> returns \"aaabbc\")\ncompress(\"aaaa\")   # Returns \"a4\" (len 2 < 4)\ncompress(\"abcd\")   # Returns \"abcd\"\n```",
        "learning_objective": "Iterate across runs of consecutive equal characters, track counts, and compare result lengths.",
        "starter_code": "def compress(s):\n    # Perform run-length compression; return original if not strictly shorter\n    pass\n",
        "function_name": "compress",
        "test_cases": [
            {
                "input": [
                    "aaaa"
                ],
                "expected": "a4",
                "is_hidden": False,
                "explanation": "'a4' is length 2, shorter than 4"
            },
            {
                "input": [
                    "abcd"
                ],
                "expected": "abcd",
                "is_hidden": False,
                "explanation": "'a1b1c1d1' is longer than 4, return original"
            },
            {
                "input": [
                    ""
                ],
                "expected": "",
                "is_hidden": False,
                "explanation": "Empty string returns empty"
            },
            {
                "input": [
                    "aabb"
                ],
                "expected": "aabb",
                "is_hidden": True,
                "explanation": "'a2b2' is length 4, not strictly shorter"
            },
            {
                "input": [
                    "aaaaaaaaaa"
                ],
                "expected": "a10",
                "is_hidden": True,
                "explanation": "'a10' is length 3, strictly shorter than 10"
            }
        ],
        "solution_approach": "Iterate through s, counting consecutive occurrences of the current character. Append char + str(count) to a parts list. Compare len(compressed) < len(s).",
        "edge_cases": [
            {
                "name": "Equal Length",
                "input_example": "'aabb' -> 'a2b2'",
                "why_important": "The rule requires strictly shorter; 'a2b2' is not shorter than 'aabb'.",
                "what_could_go_wrong": "Returning 'a2b2' instead of 'aabb'."
            },
            {
                "name": "Empty String",
                "input_example": "''",
                "why_important": "Guard against index errors on empty input.",
                "what_could_go_wrong": "IndexError accessing s[0]."
            }
        ],
        "hints": [
            "Scan the string character by character while keeping track of the current character and how many consecutive times it has appeared.",
            "When the character changes, append `current_char + str(count)` to your result and reset count to 1.",
            "After the loop, don't forget the last run! Finally, return the compressed string only if `len(compressed) < len(s)`, else return `s`."
        ]
    },
    {
        "id": "p21_lru_cache_sim",
        "title": "LRU Cache Simulation",
        "difficulty": "Advanced",
        "category": "Data Structures",
        "order_index": 21,
        "description": "### Problem Statement\nWrite a function `lru_cache_simulation(capacity, operations)` that simulates a Least Recently Used (LRU) Cache.\n\nOperations is a list of tuples/lists:\n* `[\"put\", key, value]`: Inserts or updates the value of the key. If the cache reaches capacity, evict the least recently used key.\n* `[\"get\", key]`: Returns the value of the key if it exists, otherwise `-1`. Marks the key as recently used.\n\n### Arguments\n* `capacity` (int): Positive integer maximum capacity.\n* `operations` (list): Sequence of get and put commands.\n\n### Returns\n* `list`: The list of integer results returned by every `get` operation in sequence.\n\n### Examples\n```python\nops = [[\"put\", 1, 1], [\"put\", 2, 2], [\"get\", 1], [\"put\", 3, 3], [\"get\", 2], [\"get\", 3]]\nlru_cache_simulation(2, ops) # Returns [1, -1, 3]\n```",
        "learning_objective": "Implement an LRU eviction policy using `collections.OrderedDict` for O(1) get/put operations.",
        "starter_code": "from collections import OrderedDict\n\ndef lru_cache_simulation(capacity, operations):\n    # Simulate LRU Cache with given capacity and sequence of operations\n    pass\n",
        "function_name": "lru_cache_simulation",
        "test_cases": [
            {
                "input": [
                    2,
                    [
                        [
                            "put",
                            1,
                            1
                        ],
                        [
                            "put",
                            2,
                            2
                        ],
                        [
                            "get",
                            1
                        ],
                        [
                            "put",
                            3,
                            3
                        ],
                        [
                            "get",
                            2
                        ],
                        [
                            "get",
                            3
                        ]
                    ]
                ],
                "expected": [
                    1,
                    -1,
                    3
                ],
                "is_hidden": False,
                "explanation": "Key 2 was evicted because 1 was accessed before 3 was inserted"
            },
            {
                "input": [
                    1,
                    [
                        [
                            "put",
                            1,
                            1
                        ],
                        [
                            "get",
                            1
                        ],
                        [
                            "put",
                            2,
                            2
                        ],
                        [
                            "get",
                            1
                        ],
                        [
                            "get",
                            2
                        ]
                    ]
                ],
                "expected": [
                    1,
                    -1,
                    2
                ],
                "is_hidden": False,
                "explanation": "Capacity 1 evicts on every new put"
            }
        ],
        "solution_approach": "Use collections.OrderedDict. For 'get': if key in cache, move_to_end(key) and append value, else append -1. For 'put': if key in cache, move_to_end(key), update value; else if at capacity, popitem(last=False); insert key.",
        "edge_cases": [
            {
                "name": "Capacity 1",
                "input_example": "capacity=1",
                "why_important": "Any second key immediately evicts the first.",
                "what_could_go_wrong": "Failure to evict before adding."
            },
            {
                "name": "Updating Existing Key",
                "input_example": "put(1, 1) then put(1, 2)",
                "why_important": "Should NOT evict an item since the key already exists; just update value and mark recent.",
                "what_could_go_wrong": "Unnecessary eviction of another key."
            }
        ],
        "hints": [
            "An LRU cache requires tracking both key-value pairs and the order of recent usage.",
            "Python's `collections.OrderedDict` provides `move_to_end(key)` and `popitem(last=False)`.",
            "On 'get', if key exists, move_to_end and append value to results, else append -1. On 'put', update existing or insert, evicting the oldest if over capacity."
        ]
    },
    {
        "id": "p22_word_ladder",
        "title": "Word Ladder Length",
        "difficulty": "Advanced",
        "category": "Algorithms",
        "order_index": 22,
        "description": "### Problem Statement\nWrite a function `word_ladder_length(begin_word, end_word, word_list)` that returns the number of words in the shortest transformation sequence from `begin_word` to `end_word`.\n\nRules:\n* Only one letter can be changed at a time.\n* Each transformed word must exist in `word_list`.\n* Return `0` if no transformation sequence is possible.\n\n### Arguments\n* `begin_word` (str): Starting word.\n* `end_word` (str): Target ending word.\n* `word_list` (list of str): Available dictionary words.\n\n### Returns\n* `int`: Number of words in the shortest path, or `0`.\n\n### Examples\n```python\nword_ladder_length(\"hit\", \"cog\", [\"hot\", \"dot\", \"dog\", \"lot\", \"log\", \"cog\"]) # Returns 5 (hit -> hot -> dot -> dog -> cog)\nword_ladder_length(\"hit\", \"cog\", [\"hot\", \"dot\", \"dog\", \"lot\", \"log\"])        # Returns 0 (cog not in list)\n```",
        "learning_objective": "Model state spaces as unweighted graphs and compute shortest path lengths via Breadth-First Search (BFS).",
        "starter_code": "from collections import deque\n\ndef word_ladder_length(begin_word, end_word, word_list):\n    # Find shortest transformation sequence length using BFS\n    pass\n",
        "function_name": "word_ladder_length",
        "test_cases": [
            {
                "input": [
                    "hit",
                    "cog",
                    [
                        "hot",
                        "dot",
                        "dog",
                        "lot",
                        "log",
                        "cog"
                    ]
                ],
                "expected": 5,
                "is_hidden": False,
                "explanation": "hit -> hot -> dot -> dog -> cog (5 words)"
            },
            {
                "input": [
                    "hit",
                    "cog",
                    [
                        "hot",
                        "dot",
                        "dog",
                        "lot",
                        "log"
                    ]
                ],
                "expected": 0,
                "is_hidden": False,
                "explanation": "end_word not in list"
            },
            {
                "input": [
                    "a",
                    "c",
                    [
                        "a",
                        "b",
                        "c"
                    ]
                ],
                "expected": 2,
                "is_hidden": True,
                "explanation": "a -> c (2 words)"
            }
        ],
        "solution_approach": "Convert word_list to a set. If end_word not in words: return 0. Use BFS queue with (word, length). For each char pos and each letter a-z, generate neighbor. If neighbor in words, remove from set and queue.",
        "edge_cases": [
            {
                "name": "end_word not in dictionary",
                "input_example": "end_word='cog', word_list=['hot']",
                "why_important": "No path possible; early return 0.",
                "what_could_go_wrong": "Infinite loop or exhausted search."
            },
            {
                "name": "No reachable path",
                "input_example": "Disjoint words",
                "why_important": "Queue empties; return 0.",
                "what_could_go_wrong": "Returning -1 instead of 0."
            }
        ],
        "hints": [
            "This is a shortest-path problem in an unweighted graph. Which graph traversal algorithm finds shortest paths? (BFS)",
            "Store word_list in a set for O(1) membership checks. Use a queue containing tuples of `(current_word, current_distance)`.",
            "Pop from queue: if word == end_word, return distance. Otherwise generate all 1-letter substitutions; if in word_set, remove from word_set and add to queue with distance + 1."
        ]
    },
    {
        "id": "p23_number_of_islands",
        "title": "Number of Islands",
        "difficulty": "Advanced",
        "category": "Algorithms",
        "order_index": 23,
        "description": "### Problem Statement\nWrite a function `num_islands(grid)` that counts the number of islands in a 2D grid.\n\nAn island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are surrounded by water. `'1'` represents land and `'0'` represents water.\n\n### Arguments\n* `grid` (list of lists of str): 2D grid of `'1'`s and `'0'`s.\n\n### Returns\n* `int`: Total number of connected islands.\n\n### Examples\n```python\ngrid = [\n  [\"1\",\"1\",\"1\",\"1\",\"0\"],\n  [\"1\",\"1\",\"0\",\"1\",\"0\"],\n  [\"1\",\"1\",\"0\",\"0\",\"0\"],\n  [\"0\",\"0\",\"0\",\"0\",\"0\"]\n]\nnum_islands(grid) # Returns 1\n```",
        "learning_objective": "Implement Depth-First Search (DFS) or Breadth-First Search (BFS) grid traversals with in-place mutation or visited sets.",
        "starter_code": "def num_islands(grid):\n    # Count the number of islands using DFS or BFS\n    pass\n",
        "function_name": "num_islands",
        "test_cases": [
            {
                "input": [
                    [
                        [
                            "1",
                            "1",
                            "1",
                            "1",
                            "0"
                        ],
                        [
                            "1",
                            "1",
                            "0",
                            "1",
                            "0"
                        ],
                        [
                            "1",
                            "1",
                            "0",
                            "0",
                            "0"
                        ],
                        [
                            "0",
                            "0",
                            "0",
                            "0",
                            "0"
                        ]
                    ]
                ],
                "expected": 1,
                "is_hidden": False,
                "explanation": "Single connected island"
            },
            {
                "input": [
                    [
                        [
                            "1",
                            "1",
                            "0",
                            "0",
                            "0"
                        ],
                        [
                            "1",
                            "1",
                            "0",
                            "0",
                            "0"
                        ],
                        [
                            "0",
                            "0",
                            "1",
                            "0",
                            "0"
                        ],
                        [
                            "0",
                            "0",
                            "0",
                            "1",
                            "1"
                        ]
                    ]
                ],
                "expected": 3,
                "is_hidden": False,
                "explanation": "Three disconnected islands"
            },
            {
                "input": [
                    []
                ],
                "expected": 0,
                "is_hidden": True,
                "explanation": "Empty grid"
            }
        ],
        "solution_approach": "Iterate through each cell. When a '1' is found, increment count and execute a DFS helper to sink connected '1's to '0'.",
        "edge_cases": [
            {
                "name": "Empty Grid",
                "input_example": "[]",
                "why_important": "Handle empty inputs gracefully.",
                "what_could_go_wrong": "IndexError accessing grid[0]."
            },
            {
                "name": "All Water / All Land",
                "input_example": "Grid of all '0's or all '1's",
                "why_important": "Boundary conditions return 0 or 1.",
                "what_could_go_wrong": "Overcounting or recursion overflow."
            }
        ],
        "hints": [
            "When you find a '1', how do you mark all horizontally and vertically connected '1's so you don't recount them?",
            "Use DFS recursion or a BFS queue to visit all 4-directionally adjacent '1's, changing each visited '1' to '0'.",
            "Loop through all rows and cols: if grid[r][c] == '1', increment island_count and call dfs(r, c) to flood-fill the island."
        ]
    },
    {
        "id": "p24_coin_change",
        "title": "Coin Change (Fewest Coins)",
        "difficulty": "Advanced",
        "category": "Dynamic Programming",
        "order_index": 24,
        "description": "### Problem Statement\nWrite a function `coin_change(coins, amount)` that computes the **fewest number of coins** that you need to make up that amount.\n\nIf that amount of money cannot be made up by any combination of the coins, return `-1`.\nYou may assume that you have an infinite number of each kind of coin.\n\n### Arguments\n* `coins` (list of int): Coin denominations.\n* `amount` (int): Total amount to make.\n\n### Returns\n* `int`: Minimum number of coins, or `-1`.\n\n### Examples\n```python\ncoin_change([1, 2, 5], 11) # Returns 3 (5 + 5 + 1)\ncoin_change([2], 3)        # Returns -1\ncoin_change([1], 0)        # Returns 0\n```",
        "learning_objective": "Master bottom-up 1D Dynamic Programming, state transitions `dp[i] = min(dp[i], dp[i-c] + 1)`, and unreachable state sentinel values.",
        "starter_code": "def coin_change(coins, amount):\n    # Compute minimum coins to make amount, or return -1\n    pass\n",
        "function_name": "coin_change",
        "test_cases": [
            {
                "input": [
                    [
                        1,
                        2,
                        5
                    ],
                    11
                ],
                "expected": 3,
                "is_hidden": False,
                "explanation": "5 + 5 + 1 = 3 coins"
            },
            {
                "input": [
                    [
                        2
                    ],
                    3
                ],
                "expected": -1,
                "is_hidden": False,
                "explanation": "Cannot make 3 with coin 2"
            },
            {
                "input": [
                    [
                        1
                    ],
                    0
                ],
                "expected": 0,
                "is_hidden": False,
                "explanation": "0 amount takes 0 coins"
            },
            {
                "input": [
                    [
                        1,
                        5,
                        11
                    ],
                    15
                ],
                "expected": 3,
                "is_hidden": True,
                "explanation": "5 + 5 + 5 = 3 coins (greedy 11+1+1+1+1=5 is sub-optimal)"
            }
        ],
        "solution_approach": "dp = [float('inf')] * (amount + 1); dp[0] = 0. For coin in coins: for i in range(coin, amount + 1): dp[i] = min(dp[i], dp[i - coin] + 1). Return dp[amount] if not inf else -1.",
        "edge_cases": [
            {
                "name": "Greedy Trap",
                "input_example": "coins=[1, 5, 11], amount=15",
                "why_important": "Greedy chooses 11+1+1+1+1 (5 coins), but DP finds 5+5+5 (3 coins).",
                "what_could_go_wrong": "Greedy approach fails optimality."
            },
            {
                "name": "Amount 0",
                "input_example": "amount=0",
                "why_important": "Requires 0 coins.",
                "what_could_go_wrong": "Returning -1 instead of 0."
            }
        ],
        "hints": [
            "Why doesn't a greedy approach (picking the largest coin first) always work?",
            "Use dynamic programming: define dp[i] as the minimum coins needed to make amount i.",
            "Initialize dp = [float('inf')] * (amount + 1) with dp[0] = 0. For each coin, update dp[i] = min(dp[i], dp[i - coin] + 1). Return dp[amount] if finite else -1."
        ]
    },
    {
        "id": "p25_longest_increasing_subsequence",
        "title": "Longest Increasing Subsequence",
        "difficulty": "Advanced",
        "category": "Dynamic Programming",
        "order_index": 25,
        "description": "### Problem Statement\nWrite a function `length_of_lis(nums)` that returns the length of the longest strictly increasing subsequence in an integer list.\n\nA subsequence is derived by deleting some or no elements without changing the order of the remaining elements.\n\n### Arguments\n* `nums` (list of int): List of integers.\n\n### Returns\n* `int`: Length of the longest strictly increasing subsequence.\n\n### Examples\n```python\nlength_of_lis([10, 9, 2, 5, 3, 7, 101, 18]) # Returns 4 ([2, 3, 7, 101])\nlength_of_lis([0, 1, 0, 3, 2, 3])           # Returns 4 ([0, 1, 2, 3])\nlength_of_lis([7, 7, 7, 7, 7])               # Returns 1\nlength_of_lis([])                            # Returns 0\n```",
        "learning_objective": "Implement the classic $O(n^2)$ Dynamic Programming solution for LIS and understand recurrence relations.",
        "starter_code": "def length_of_lis(nums):\n    # Find length of longest strictly increasing subsequence\n    pass\n",
        "function_name": "length_of_lis",
        "test_cases": [
            {
                "input": [
                    [
                        10,
                        9,
                        2,
                        5,
                        3,
                        7,
                        101,
                        18
                    ]
                ],
                "expected": 4,
                "is_hidden": False,
                "explanation": "[2, 3, 7, 101]"
            },
            {
                "input": [
                    [
                        0,
                        1,
                        0,
                        3,
                        2,
                        3
                    ]
                ],
                "expected": 4,
                "is_hidden": False,
                "explanation": "[0, 1, 2, 3]"
            },
            {
                "input": [
                    [
                        7,
                        7,
                        7,
                        7,
                        7
                    ]
                ],
                "expected": 1,
                "is_hidden": False,
                "explanation": "Strictly increasing requires distinct values"
            },
            {
                "input": [
                    []
                ],
                "expected": 0,
                "is_hidden": True,
                "explanation": "Empty list has LIS 0"
            },
            {
                "input": [
                    [
                        1,
                        2,
                        3,
                        4,
                        5
                    ]
                ],
                "expected": 5,
                "is_hidden": True,
                "explanation": "Already sorted strictly increasing"
            }
        ],
        "solution_approach": "If not nums: return 0. dp = [1] * len(nums). For i in range(len(nums)): for j in range(i): if nums[j] < nums[i]: dp[i] = max(dp[i], dp[j] + 1). Return max(dp).",
        "edge_cases": [
            {
                "name": "All Identical Elements",
                "input_example": "[5, 5, 5]",
                "why_important": "Strictly increasing means length is 1, not len(nums).",
                "what_could_go_wrong": "Checking <= instead of <."
            },
            {
                "name": "Empty List",
                "input_example": "[]",
                "why_important": "Guard against calling max() on empty list.",
                "what_could_go_wrong": "ValueError: max() arg is an empty sequence."
            }
        ],
        "hints": [
            "A subsequence does not need to be contiguous. What does dp[i] represent in relation to nums[i]?",
            "Define dp[i] as the length of the longest increasing subsequence ending at index i. Base case: dp[i] = 1 for all i.",
            "For each i, check all previous indices j < i. If nums[j] < nums[i], update dp[i] = max(dp[i], dp[j] + 1). Finally return max(dp)."
        ]
    },
    {
        "id": "p26_valid_sudoku",
        "title": "Validate Sudoku Board",
        "difficulty": "Advanced",
        "category": "Data Structures",
        "order_index": 26,
        "description": "### Problem Statement\nWrite a function `is_valid_sudoku(board)` that determines if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:\n\n1. Each row must contain the digits `1-9` without repetition.\n2. Each column must contain the digits `1-9` without repetition.\n3. Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without repetition.\n\nEmpty cells are marked with the character `'.'`.\n\n### Arguments\n* `board` (list of lists of str): 9x9 board containing `'1'`-`'9'` or `'.'`.\n\n### Returns\n* `bool`: `True` if valid, `False` otherwise.\n",
        "learning_objective": "Manage multidimensional constraints, coordinate mapping to 3x3 subgrids `(r // 3, c // 3)`, and hashing.",
        "starter_code": "def is_valid_sudoku(board):\n    # Validate rows, columns, and 3x3 sub-boxes without duplicates\n    pass\n",
        "function_name": "is_valid_sudoku",
        "test_cases": [
            {
                "input": [
                    [
                        [
                            "5",
                            "3",
                            ".",
                            ".",
                            "7",
                            ".",
                            ".",
                            ".",
                            "."
                        ],
                        [
                            "6",
                            ".",
                            ".",
                            "1",
                            "9",
                            "5",
                            ".",
                            ".",
                            "."
                        ],
                        [
                            ".",
                            "9",
                            "8",
                            ".",
                            ".",
                            ".",
                            ".",
                            "6",
                            "."
                        ],
                        [
                            "8",
                            ".",
                            ".",
                            ".",
                            "6",
                            ".",
                            ".",
                            ".",
                            "3"
                        ],
                        [
                            "4",
                            ".",
                            ".",
                            "8",
                            ".",
                            "3",
                            ".",
                            ".",
                            "1"
                        ],
                        [
                            "7",
                            ".",
                            ".",
                            ".",
                            "2",
                            ".",
                            ".",
                            ".",
                            "6"
                        ],
                        [
                            ".",
                            "6",
                            ".",
                            ".",
                            ".",
                            ".",
                            "2",
                            "8",
                            "."
                        ],
                        [
                            ".",
                            ".",
                            ".",
                            "4",
                            "1",
                            "9",
                            ".",
                            ".",
                            "5"
                        ],
                        [
                            ".",
                            ".",
                            ".",
                            ".",
                            "8",
                            ".",
                            ".",
                            "7",
                            "9"
                        ]
                    ]
                ],
                "expected": True,
                "is_hidden": False,
                "explanation": "Valid board"
            },
            {
                "input": [
                    [
                        [
                            "8",
                            "3",
                            ".",
                            ".",
                            "7",
                            ".",
                            ".",
                            ".",
                            "."
                        ],
                        [
                            "6",
                            ".",
                            ".",
                            "1",
                            "9",
                            "5",
                            ".",
                            ".",
                            "."
                        ],
                        [
                            ".",
                            "9",
                            "8",
                            ".",
                            ".",
                            ".",
                            ".",
                            "6",
                            "."
                        ],
                        [
                            "8",
                            ".",
                            ".",
                            ".",
                            "6",
                            ".",
                            ".",
                            ".",
                            "3"
                        ],
                        [
                            "4",
                            ".",
                            ".",
                            "8",
                            ".",
                            "3",
                            ".",
                            ".",
                            "1"
                        ],
                        [
                            "7",
                            ".",
                            ".",
                            ".",
                            "2",
                            ".",
                            ".",
                            ".",
                            "6"
                        ],
                        [
                            ".",
                            "6",
                            ".",
                            ".",
                            ".",
                            ".",
                            "2",
                            "8",
                            "."
                        ],
                        [
                            ".",
                            ".",
                            ".",
                            "4",
                            "1",
                            "9",
                            ".",
                            ".",
                            "5"
                        ],
                        [
                            ".",
                            ".",
                            ".",
                            ".",
                            "8",
                            ".",
                            ".",
                            "7",
                            "9"
                        ]
                    ]
                ],
                "expected": False,
                "is_hidden": False,
                "explanation": "Duplicate 8 in first column"
            }
        ],
        "solution_approach": "Use sets for rows, cols, and boxes. Box key: (r // 3, c // 3). For each cell, if not '.', check if digit in row/col/box set; if so return False, else add.",
        "edge_cases": [
            {
                "name": "Sub-box Duplicate",
                "input_example": "Same digit in 3x3 box but different rows and columns",
                "why_important": "Validates box formula (r // 3, c // 3).",
                "what_could_go_wrong": "Forgetting to validate the 3x3 sub-boxes."
            },
            {
                "name": "Empty Board",
                "input_example": "All '.'",
                "why_important": "Valid board with no constraints violated.",
                "what_could_go_wrong": "Expecting filled cells."
            }
        ],
        "hints": [
            "You need to check three constraints: no duplicates in any row, any column, or any 3x3 sub-box.",
            "How can you index which 3x3 box a cell (r, c) belongs to? Notice that `r // 3` and `c // 3` identify the box.",
            "Maintain sets or dictionaries: `rows[r]`, `cols[c]`, `boxes[(r//3, c//3)]`. Skip '.' cells. If a digit already exists in any of the three, return False."
        ]
    },
    {
        "id": "p27_min_path_sum",
        "title": "Minimum Path Sum in Grid",
        "difficulty": "Advanced",
        "category": "Dynamic Programming",
        "order_index": 27,
        "description": "### Problem Statement\nWrite a function `min_path_sum(grid)` that finds a path from top left to bottom right of an `M x N` grid which **minimizes the sum of all numbers along its path**.\n\nYou can only move either down or right at any point in time.\n\n### Arguments\n* `grid` (list of lists of int): 2D grid of non-negative integers.\n\n### Returns\n* `int`: Minimum path sum.\n\n### Examples\n```python\ngrid = [\n  [1, 3, 1],\n  [1, 5, 1],\n  [4, 2, 1]\n]\nmin_path_sum(grid) # Returns 7 (1 -> 3 -> 1 -> 1 -> 1)\n```",
        "learning_objective": "Formulate 2D grid Dynamic Programming recurrences `dp[r][c] = grid[r][c] + min(dp[r-1][c], dp[r][c-1])`.",
        "starter_code": "def min_path_sum(grid):\n    # Find minimum path sum from top-left to bottom-right moving only right and down\n    pass\n",
        "function_name": "min_path_sum",
        "test_cases": [
            {
                "input": [
                    [
                        [
                            1,
                            3,
                            1
                        ],
                        [
                            1,
                            5,
                            1
                        ],
                        [
                            4,
                            2,
                            1
                        ]
                    ]
                ],
                "expected": 7,
                "is_hidden": False,
                "explanation": "1+3+1+1+1 = 7"
            },
            {
                "input": [
                    [
                        [
                            1,
                            2
                        ],
                        [
                            1,
                            1
                        ]
                    ]
                ],
                "expected": 3,
                "is_hidden": False,
                "explanation": "1+1+1 = 3"
            },
            {
                "input": [
                    [
                        [
                            1
                        ]
                    ]
                ],
                "expected": 1,
                "is_hidden": True,
                "explanation": "1x1 grid"
            },
            {
                "input": [
                    [
                        [
                            1,
                            2,
                            3
                        ]
                    ]
                ],
                "expected": 6,
                "is_hidden": True,
                "explanation": "Single row"
            }
        ],
        "solution_approach": "Initialize dp table of same dimensions. Fill dp[0][0] = grid[0][0]. Fill first row and column accumulatively. For remaining cells, dp[r][c] = grid[r][c] + min(dp[r-1][c], dp[r][c-1]). Return dp[-1][-1].",
        "edge_cases": [
            {
                "name": "Single Cell",
                "input_example": "[[5]]",
                "why_important": "No moves needed; returns grid[0][0].",
                "what_could_go_wrong": "IndexError when filling boundaries."
            },
            {
                "name": "Single Row or Column",
                "input_example": "[[1, 2, 3]]",
                "why_important": "Only one path possible.",
                "what_could_go_wrong": "Looking above on row 0."
            }
        ],
        "hints": [
            "Since you can only move right or down, the minimum sum to reach (r, c) depends solely on cells (r-1, c) and (r, c-1).",
            "This is a classic 2D Dynamic Programming problem. What are the base cases for the first row and first column?",
            "Fill the first row accumulatively (can only come from left) and first column (can only come from above). For all other cells: dp[r][c] = grid[r][c] + min(dp[r-1][c], dp[r][c-1])."
        ]
    },
    {
        "id": "p28_decode_ways",
        "title": "Decode Ways",
        "difficulty": "Advanced",
        "category": "Dynamic Programming",
        "order_index": 28,
        "description": "### Problem Statement\nA message containing letters from `A-Z` can be encoded into numbers using the mapping:\n`'A' -> \"1\"`, `'B' -> \"2\"`, ..., `'Z' -> \"26\"`.\n\nWrite a function `num_decodings(s)` that returns the **number of ways** to decode a given string of digits `s`.\n\nFor example, `\"12\"` could be decoded as `\"AB\"` (1 2) or `\"L\"` (12), so the answer is `2`. Any grouping with leading zero like `\"06\"` is invalid.\n\n### Arguments\n* `s` (str): A string containing only digits.\n\n### Returns\n* `int`: Total number of valid decodings.\n\n### Examples\n```python\nnum_decodings(\"12\")  # Returns 2 (\"AB\" or \"L\")\nnum_decodings(\"226\") # Returns 3 (\"BZ\", \"VF\", or \"BBF\")\nnum_decodings(\"06\")  # Returns 0 (leading zero is invalid)\nnum_decodings(\"0\")   # Returns 0\n```",
        "learning_objective": "Solve constrained Fibonacci-like state transitions handling zero-cases and multi-digit windows.",
        "starter_code": "def num_decodings(s):\n    # Return number of ways to decode digit string s\n    pass\n",
        "function_name": "num_decodings",
        "test_cases": [
            {
                "input": [
                    "12"
                ],
                "expected": 2,
                "is_hidden": False,
                "explanation": "'AB' (1, 2) or 'L' (12)"
            },
            {
                "input": [
                    "226"
                ],
                "expected": 3,
                "is_hidden": False,
                "explanation": "'BZ' (2, 26), 'VF' (22, 6), 'BBF' (2, 2, 6)"
            },
            {
                "input": [
                    "06"
                ],
                "expected": 0,
                "is_hidden": False,
                "explanation": "Leading zero cannot be decoded"
            },
            {
                "input": [
                    "0"
                ],
                "expected": 0,
                "is_hidden": True,
                "explanation": "'0' has no mapping"
            },
            {
                "input": [
                    "1"
                ],
                "expected": 1,
                "is_hidden": True,
                "explanation": "'A'"
            }
        ],
        "solution_approach": "If not s or s[0] == '0': return 0. dp = [0] * (len(s) + 1); dp[0] = 1; dp[1] = 1. For i in range(2, len(s) + 1): if s[i-1] != '0': dp[i] += dp[i-1]. If 10 <= int(s[i-2:i]) <= 26: dp[i] += dp[i-2]. Return dp[-1].",
        "edge_cases": [
            {
                "name": "Leading Zero",
                "input_example": "'0' or '06'",
                "why_important": "No encoding maps to 0.",
                "what_could_go_wrong": "Counting 0 as a valid single digit."
            },
            {
                "name": "Valid vs Invalid Two-digit",
                "input_example": "'27' vs '26'",
                "why_important": "26 is 'Z', but 27 is out of range.",
                "what_could_go_wrong": "Checking <= 30 instead of <= 26."
            }
        ],
        "hints": [
            "Think of this like climbing stairs: at each digit, you can either take 1 digit or 2 digits if they form a number from 10 to 26.",
            "Careful with '0': '0' by itself is never valid, but '10' and '20' are valid two-digit tokens.",
            "Use dp where dp[i] is ways to decode s[:i]. If single digit s[i-1] != '0', add dp[i-1]. If two digits '10' <= s[i-2:i] <= '26', add dp[i-2]."
        ]
    },
    {
        "id": "p29_task_scheduler",
        "title": "Task Scheduler",
        "difficulty": "Advanced",
        "category": "Algorithms",
        "order_index": 29,
        "description": "### Problem Statement\nGiven a list of characters `tasks` representing CPU tasks, and an integer cooldown `n`, write a function `least_interval(tasks, n)` that calculates the minimum number of units of time that the CPU will take to finish all the given tasks.\n\nEach task takes 1 unit of time. For each interval, the CPU could finish one task or be idle. However, there must be at least `n` units of time between any two identical tasks.\n\n### Arguments\n* `tasks` (list of str): List of uppercase letters representing tasks.\n* `n` (int): Cooldown interval between identical tasks.\n\n### Returns\n* `int`: Minimum time units required.\n\n### Examples\n```python\nleast_interval([\"A\",\"A\",\"A\",\"B\",\"B\",\"B\"], 2) # Returns 8 (A -> B -> idle -> A -> B -> idle -> A -> B)\nleast_interval([\"A\",\"A\",\"A\",\"B\",\"B\",\"B\"], 0) # Returns 6\n```",
        "learning_objective": "Analyze greedy arrangements and mathematical bottleneck framing `max((max_freq - 1) * (n + 1) + max_count, len(tasks))`.",
        "starter_code": "from collections import Counter\n\ndef least_interval(tasks, n):\n    # Compute minimum CPU intervals needed with cooldown n\n    pass\n",
        "function_name": "least_interval",
        "test_cases": [
            {
                "input": [
                    [
                        "A",
                        "A",
                        "A",
                        "B",
                        "B",
                        "B"
                    ],
                    2
                ],
                "expected": 8,
                "is_hidden": False,
                "explanation": "A B idle A B idle A B = 8 units"
            },
            {
                "input": [
                    [
                        "A",
                        "A",
                        "A",
                        "B",
                        "B",
                        "B"
                    ],
                    0
                ],
                "expected": 6,
                "is_hidden": False,
                "explanation": "No cooldown, 6 tasks take 6 units"
            },
            {
                "input": [
                    [
                        "A",
                        "A",
                        "A",
                        "A",
                        "A",
                        "A",
                        "B",
                        "C",
                        "D",
                        "E",
                        "F",
                        "G"
                    ],
                    2
                ],
                "expected": 16,
                "is_hidden": True,
                "explanation": "A is bottleneck"
            }
        ],
        "solution_approach": "Count frequencies. Max frequency f determines structure: (f - 1) chunks of size (n + 1), plus the number of tasks sharing max frequency. Answer is max(formula, len(tasks)).",
        "edge_cases": [
            {
                "name": "Cooldown 0",
                "input_example": "n=0",
                "why_important": "No idles ever required; answer is simply len(tasks).",
                "what_could_go_wrong": "Overcalculating intervals."
            },
            {
                "name": "More Distinct Tasks Than Cooldown",
                "input_example": "Cooldown is small, tasks fill all slots without any idles.",
                "what_could_go_wrong": "Formula yielding less than len(tasks)."
            }
        ],
        "hints": [
            "Which task creates the biggest scheduling bottleneck? The task with the highest frequency.",
            "If the highest frequency is f, there are (f - 1) full cycles of length (n + 1).",
            "Calculate (max_freq - 1) * (n + 1) + count_of_tasks_with_max_freq. The final answer is `max(calculated, len(tasks))`."
        ]
    },
    {
        "id": "p30_regex_matching",
        "title": "Regular Expression Matching",
        "difficulty": "Advanced",
        "category": "Dynamic Programming",
        "order_index": 30,
        "description": "### Problem Statement\nWrite a function `is_match(s, p)` that implements regular expression matching with support for `'.'` and `'*'`.\n\n* `'.'` Matches any single character.\n* `'*'` Matches zero or more of the preceding element.\n\nThe matching should cover the **entire** input string `s` (not partial).\n\n### Arguments\n* `s` (str): Input text string.\n* `p` (str): Pattern string.\n\n### Returns\n* `bool`: `True` if pattern matches string, `False` otherwise.\n\n### Examples\n```python\nis_match(\"aa\", \"a\")    # Returns False\nis_match(\"aa\", \"a*\")   # Returns True\nis_match(\"ab\", \".*\")   # Returns True\nis_match(\"aab\", \"c*a*b\") # Returns True\n```",
        "learning_objective": "Model non-deterministic finite automaton transitions in 2D Dynamic Programming.",
        "starter_code": "def is_match(s, p):\n    # Implement regex matching supporting '.' and '*'\n    pass\n",
        "function_name": "is_match",
        "test_cases": [
            {
                "input": [
                    "aa",
                    "a"
                ],
                "expected": False,
                "is_hidden": False,
                "explanation": "Pattern 'a' does not match full string 'aa'"
            },
            {
                "input": [
                    "aa",
                    "a*"
                ],
                "expected": True,
                "is_hidden": False,
                "explanation": "'*' matches two 'a's"
            },
            {
                "input": [
                    "ab",
                    ".*"
                ],
                "expected": True,
                "is_hidden": False,
                "explanation": "'.*' matches any string"
            },
            {
                "input": [
                    "aab",
                    "c*a*b"
                ],
                "expected": True,
                "is_hidden": True,
                "explanation": "'c*' matches 0 'c's, 'a*' matches two 'a's, followed by 'b'"
            },
            {
                "input": [
                    "",
                    ""
                ],
                "expected": True,
                "is_hidden": True,
                "explanation": "Empty matches empty"
            },
            {
                "input": [
                    "",
                    "a*"
                ],
                "expected": True,
                "is_hidden": True,
                "explanation": "'a*' matches zero occurrences"
            }
        ],
        "solution_approach": "2D DP table dp[i][j] where s[:i] matches p[:j]. Base case dp[0][0] = True. For '*' patterns, check 0 occurrences dp[i][j-2] or 1+ occurrences if preceding char matches.",
        "edge_cases": [
            {
                "name": "Zero Occurrences with *",
                "input_example": "s='', p='a*b*'",
                "why_important": "Empty string matches patterns where all tokens have *.",
                "what_could_go_wrong": "Failing base case setup."
            },
            {
                "name": "Dot-Star (.*)",
                "input_example": "s='anything', p='.*'",
                "why_important": "Matches any sequence.",
                "what_could_go_wrong": "Handling dot without star."
            }
        ],
        "hints": [
            "Use a 2D boolean DP table where dp[i][j] indicates whether s[:i] matches pattern p[:j].",
            "What is the base case? dp[0][0] = True. For empty string s, pattern 'a*' or 'a*b*' can match if dp[0][j-2] is True.",
            "If p[j-1] == '*': dp[i][j] is True if 0 occurrences (dp[i][j-2]) OR (preceding char matches and dp[i-1][j]). Else if chars match or p[j-1]=='.': dp[i][j] = dp[i-1][j-1]."
        ]
    }
]
