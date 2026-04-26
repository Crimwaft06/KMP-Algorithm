from lexer import lexer

print("Mini Lexer using KMP")
print("Example: while x == 10 ;")

text = input("Enter source code: ")
print("\nTokens:\n")

lexer(text)