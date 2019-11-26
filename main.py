import codeTokenizer as ctok
import cyk
import sys

# Load Chomsky Normal Form
if len(sys.argv) > 1:
    modelPath = str(sys.argv[1])
else:
	modelPath = 'out.txt'
	
cyk.LoadCNF(modelPath)

# Tokenize
tokenizedCode = ctok.tokenizeInput("input.txt")

print(tokenizedCode)

# CYK
table = cyk.cyk(tokenizedCode)

for x in table:
    print(x)

print(cyk.checkValidity(table, "PRINT"))