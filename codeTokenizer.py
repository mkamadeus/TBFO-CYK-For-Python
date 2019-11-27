import re

def tokenizeInput(inputFilename):
    # Read from file
    f = open(inputFilename, "r")
    contents = f.read()
    contents = contents.split()
    f.close()

    result = contents

    operators = [':', ',', '=', '<', '>', '>=', '<=', '==', '!=', r'\+', '-', r'\*', '/', r'\*\*', r'\(', r'\)',r'\'\'\'', r'\'', r'\"']

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

    return result