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

operators = ['=', '<', '>', '>=', '<=', '==', '!=', r'\+', '-', r'\*', '/', r'\*\*', r'\(', r'\)']

# For each operator..
for operator in operators:
    print(operator)
    temporaryResult = []
    # For each statement..
    for statement in result:
        format = "[A..z]*(" + operator +")[A..z]*"
        x = re.split(format, statement)
        
        # Append 
        for splitStatement in x:
            temporaryResult.append(splitStatement) 
    result = temporaryResult
    print(result)
        

