import re
import keyword

# Token types
VARIABLE = 'VARIABLE'
INSTANCE = 'INSTANCE'
FUNCTION = 'FUNCTION'
METHOD = 'METHOD'
KEYWORD = 'KEYWORD'
NUMBER = 'NUMBER'
STRING = 'STRING'
COMMENT = 'COMMENT'
SEPARATOR = 'SEPARATOR'
OPERATOR = 'OPERATOR'
ERROR = 'ERROR'
EOF = 'EOF'

# Regular expressions for token recognition
regex_patterns = {
    INSTANCE: r'^self(?:\.[a-zA-Z_][a-zA-Z0-9_]*)?(?=\()?',
    FUNCTION: r'^[a-zA-Z_][a-zA-Z0-9_]*\s*(?=\()',
    METHOD: r'^[a-zA-Z_][a-zA-Z0-9_]*\.[a-zA-Z_][a-zA-Z0-9_]*\s*(?=\()',
    KEYWORD: r'^(if|else|while|for|return|def|class)\b',
    VARIABLE: r'^[a-zA-Z_][a-zA-Z0-9_]*\b',
    NUMBER: r'^\d+$|^\d+\.\d+',
    STRING: r'^"((\\"|[^"])*)"',
    COMMENT: r'^#.*',
    SEPARATOR: r'^[(),.;:]',
    OPERATOR: r'^[+\-*/><=!]=|^[+\-*/><=!]',
}

def lex_line(line, line_number, detect_number_type=False):
    tokens = []
    idx = 0
    while idx < len(line):
        match = None
        for token_type, pattern in regex_patterns.items():
            match = re.match(pattern, line[idx:])
            if match:
                token_value = match.group(1) if token_type == STRING else match.group(0)
                if detect_number_type and token_type == NUMBER:
                    if "." in token_value:
                        token_type = 'FLOAT'
                    else:
                        token_type = 'INT'
                tokens.append((token_type, token_value.strip(), line_number, idx + match.start()))
                idx += match.end()
                break
        if not match:
            # If no match is found, it means there's an error
            tokens.append((ERROR, line[idx], line_number, idx))
            idx += 1
    return tokens

def lex(code, detect_number_type=False):
    lines = code.strip().split('\n')
    all_tokens = []
    for line_number, line in enumerate(lines, 1):
        line_tokens = lex_line(line, line_number, detect_number_type)
        all_tokens.extend(line_tokens)
    # Add an EOF token to indicate the end of input
    all_tokens.append((EOF, '', len(lines), len(lines[-1])))
    return all_tokens

if __name__ == "__main__":
    file_path = "input_code.py"  # Replace with your input code file path
    with open(file_path, 'r') as file:
        code_to_analyze = file.read()

    tokens = lex(code_to_analyze, detect_number_type=True)

    # Define the table headers
    headers = ["Type", "Value", "Row", "Column"]

    # Print the formatted output
    print("{:<10} {:<20} {:<5} {:<5}".format(*headers))
    print("=" * 47)
    for token_type, token_value, row, col in tokens:
        if token_type != ERROR:
            print("{:<10} {:<20} {:<5} {:<5}".format(token_type, token_value, row, col))
