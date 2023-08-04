## Lexical Analyzer for Python Code

The Lexical Analyzer is a Python script that performs lexical analysis on Python source code. It tokenizes the input code into various types such as variables, keywords, numbers, strings, operators, and more, helping to identify and process individual elements of the source code.

## Features

- Tokenizes Python source code into different types, including variables, keywords, numbers, strings, operators, etc.
- Supports error handling for invalid tokens and provides detailed error messages with line and column numbers.
- Easily customizable token patterns to fit different programming languages or specific use cases.
- Detects Python keywords and disallows their use as variable names.
- Provides an option to detect number types (integer or float) for numeric literals.
- Works with Python 3.x and above.

## Usage

Clone the repository:

   ```bash
   git clone https://github.com/your_username/lexical_analyzer.git
  ```


1. Run the lexical analyzer on your Python code:
   ```bash
   python lexical_analyzer.py path_to_your_python_file.py
   ```
    Replace path_to_your_python_file.py with the path to the Python file you want to analyze.
   

2. The lexical analyzer will tokenize the input Python code and print the results in a tabular format, showing token type, value, row, and column.

Sample Output:
```bash
Type       Value                Row   Column
=============================================
FUNCTION   def                  1     0
VARIABLE   factorial            1     4
SEPARATOR  (                    1     13
VARIABLE   n                    1     14
SEPARATOR  )                    1     15
SEPARATOR  :                    1     16
KEYWORD    if                   2     4
VARIABLE   n                    2     7
OPERATOR   ==                   2     9
NUMBER     0                    2     12
SEPARATOR  :                    2     13
KEYWORD    return               3     8
NUMBER     1                    3     15
KEYWORD    else                 4     4
KEYWORD    return               5     8
VARIABLE   n                    5     15
OPERATOR   *                    5     17
FUNCTION   factorial            5     19
SEPARATOR  (                    5     28
VARIABLE   n                    5     29
OPERATOR   -                    5     30
NUMBER     1                    5     31
SEPARATOR  )                    5     32
EOF                              6     0
```

## Customization
The lexical analyzer's behavior can be customized by modifying the regular expressions in the regex_patterns dictionary in the lexical_analyzer.py file. You can adapt the token patterns to fit different programming languages or specific lexical requirements.

## Contributions
Contributions to this project are welcome. Feel free to open issues and pull requests to suggest improvements or report bugs.
