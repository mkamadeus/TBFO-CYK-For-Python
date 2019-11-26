import re
import numpy as np

# Read from file
f = open("input.txt", "r")
contents = f.read()
contents = contents.split('\n')
f.close()

result = contents
print(result)
result = [string.strip(chr(32)) for string in result]

operators = ['=', '<', '>', '>=', '<=', '==', '!=', r'\+', '-', r'\*', '/', r'\*\*', r'\(', r'\)',r'\'\'\'', r'\'', r'\"']

# For each operator..
for operator in operators:
    temporaryResult = []
    # For each statement..
    for statement in result:
        format = r"[A..z]*(" + operator +r")[A..z]*"
        x = re.split(format, statement)
        
        # Append 
        for splitStatement in x:
            temporaryResult.append(splitStatement) 
    result = temporaryResult

# Strip space
temporaryResult = []
for statement in result:
    stripped = statement.split()
    for splitStatement in stripped: 
        temporaryResult.append(splitStatement)

result = temporaryResult

# Strip empty string
result = [string for string in result if string!='']

print(result)