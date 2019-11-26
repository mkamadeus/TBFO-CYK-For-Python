import codeTokenizer as ctok
import cyk

# Tokenize
tokenizedCode = ctok.tokenizeInput("input.txt")

print(tokenizedCode)

# CYK
table = cyk.cyk(tokenizedCode)

for x in table:
    print(x)

print(cyk.checkValidity(table, "PRINT"))