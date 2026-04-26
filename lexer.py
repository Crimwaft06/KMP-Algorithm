from kmp import kmp_search

keywords = ["if", "while", "return", "for", "int", "float"]

operators = ["==", "!=", "<=", ">=", "+", "-", "*", "/", "=", "<", ">"]

symbols = ["(", ")", "{", "}", ";", ","]


def is_keyword(word):
    for key in keywords:
        if kmp_search(word, key) and len(word) == len(key):
            return True
    return False


def lexer(text):
    tokens = text.split()

    for token in tokens:

        if is_keyword(token):
            print("KEYWORD    :", token)

        elif token in operators:
            print("OPERATOR   :", token)

        elif token in symbols:
            print("SYMBOL     :", token)

        elif token.replace('.', '', 1).isdigit():
            print("NUMBER     :", token)

        elif token[0].isalpha() or token[0] == "_":
            print("IDENTIFIER :", token)

        else:
            print("UNKNOWN    :", token)