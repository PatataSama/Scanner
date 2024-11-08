import re

source_code = []
with open('input.txt', 'r') as f:
    source_code = f.readlines()


# List of C programming keywords
c_keywords = [
    "auto", "break", "case", "char", "const", "continue",
    "default", "do", "double", "else", "enum", "extern",
    "float", "for", "goto", "if", "inline", "int",
    "long", "register", "restrict", "return", "short",
    "signed", "sizeof", "static", "struct", "switch",
    "typedef", "union", "unsigned", "void", "volatile", "while",
    "NULL"

]

# List of C operators
c_operators = [
    '+', '-', '*', '/', '%', # Arithmetic Operators
    '==', '!=', '>', '<', '>=', '<=', # Relational Operators
    '&&', '||', '!', # Logical Operators
    '&', '|', '^', '~', '<<', '>>', # Bitwise Operators
    '=', '+=', '-=', '*=', '/=', '%=', '&=', '|=', '^=', '<<=', '>>=', # Assignment Operators
    'sizeof', '*' # Other Operators
]

# List of special characters used in C programming
special_characters = [
    '#', '$', "'", '(', ')', 
    ',', '.', ':', ';', '?', 
    '@', '[', '\\', ']', '_', '{', '}', 
    '\"', '`'
]

identifier_pattern = r'[a-zA-Z_][a-zA-Z0-9_]*'
numeric_constants_pattern = r'\d+(\.\d+)? | [-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?'
non_numeric_constants_pattern = r'\w+(\.\w+)+(\.\w+)+'
comment_pattern = r'(//.*)'
multi_comment_pattern = r'(/\*.*?\*/)'
string_pattern = r'\"(.*?)\"'

source_code_without_onelinecomment = []
for line in source_code:
    match_comment = re.search(comment_pattern , line)
    if match_comment:
        print(f"{match_comment.group()} is a comment in c programming language")
        line = line[:line.index("//")]

    source_code_without_onelinecomment.append(line)

source_code_without_onelinecomment = ' '.join(source_code_without_onelinecomment)
multiline_comment_pattern = re.compile(multi_comment_pattern, re.DOTALL)
comments = multiline_comment_pattern.findall(source_code_without_onelinecomment)
cleaned_code = source_code_without_onelinecomment
if comments:
    print("Multi-line comments found:")
    for comment in comments:
        print(f"{comment} is a multiple line comment in c programming language")
    cleaned_code = multiline_comment_pattern.sub('', source_code_without_onelinecomment)

string_pattern = re.compile(string_pattern, re.DOTALL)
match_strings = string_pattern.findall(cleaned_code)
if match_strings:
    for string in match_strings:
        print(f"{string} is a string in c programming language")
    cleaned_code = string_pattern.sub('', cleaned_code)


for word in cleaned_code.split():
    
    if word.lower() in c_keywords or word == "NULL":
        print(f"{word} is a keyword in C programming language")
    
    match_non_numeric = re.search(non_numeric_constants_pattern, word)
    if match_non_numeric:
        if match_non_numeric.group() not in c_keywords:
            parts = match_non_numeric.group().split(".")
            for i, part in enumerate(parts):
                matched_word = re.search(identifier_pattern, part)
                if matched_word:
                    if matched_word.group() not in c_keywords:
                        print(f"{matched_word.group()} is an identifier in c programming language")
                        if i != len(parts)-1:
                            print(". is a special character in c programming language")
                        continue
                matched_numeric = re.search(numeric_constants_pattern, part)
                if matched_numeric:
                    if matched_numeric.group() not in c_keywords:
                        print(f"{matched_numeric.group()} is an numeric constant in c programming language")
                if i != len(parts)-1:
                    print(". is a special character in c programming language")
        
        continue

    matched_numeric = re.search(numeric_constants_pattern, word)
    if matched_numeric:
        if matched_numeric.group() not in c_keywords:
            print(f"{matched_numeric.group()} is an numeric constant in c programming language")
            cleaned_code = re.sub(matched_numeric.group(), " " , cleaned_code)
            word = re.sub(matched_numeric.group(), " " , word)

    for char in word:
        if char in c_operators:
            print(f"{char} is an operator in c programming language")
            word.replace(char , " ")
        if char in special_characters:
            print(f"{char} is a special character in c programming language")
            word.replace(char , " ")

    matched_words = re.findall(identifier_pattern, word)
    for matched_word in matched_words:
        if matched_word not in c_keywords:
            print(f"{matched_word} is an identifier in c programming language")
            continue