import re
import pprint as pp

# Regex List
regexList = [r'[A..z]*']

# Maps regex into valid key
regexMap = {
    r'[A..z]*' : ["thisisastring", "thisisavar"]
}

# Grammar in CNF form
# "PREDCON":["PRINT"],
# "print":["PRED"],
# "DUCKFUDGE":["CON"],
# "DUCKGORILLA":["CON"],
# "EGGFUDGE":["GORILLA"],
# "(":["DUCK"],
# "string":["EGG"],
# ")":["FUDGE"],


# Load CNF File
global chomskyGrammar
chomskyGrammar = {}

def LoadCNF(modelPath):
    file = open(modelPath).read()
    rawRules = file.split('\n')
    print(len(rawRules))
    for i in range (len(rawRules)-1):
        A = rawRules[i].split(' -> ')[0]
        B = rawRules[i].split(' -> ')[1]
        B = B.replace(" ","")
        C = B.split('|')
        for j in range (len(C)):
            value = chomskyGrammar.get(C[j])
            if (value == None):
                print(A, "->", C[j])
                chomskyGrammar.update({C[j] : [A]})
            else :
                print(A, "->", C[j])
                chomskyGrammar[C[j]].append(A)
    # print(chomskyGrammar)

# Returns CYK table from tokenized input
def cyk(tokenizedInput):

    # Initialize CYK Table
    cykTable = [[[] for j in range(i)] for i in range(len(tokenizedInput),0,-1)]

    # Initialize first row (Bottom-Up DP base case)
    for i in range(len(tokenizedInput)):
        print(cykTable)
        # If key valid..
        try:
            cykTable[0][i].extend(chomskyGrammar[tokenizedInput[i]])
        # If key invalid..
        except KeyError:
            for pattern in regexList:
                # x = re.match(pattern, tokenizedInput[i])
                # print(x)
                if(re.match(pattern, tokenizedInput[i])):
                    for regexType in regexMap[pattern]:
                        try:
                            cykTable[0][i].extend(chomskyGrammar[regexType])
                        except KeyError:
                            continue
                    break

                
    # Iterate DP Bottom Up
    for i in range(1,len(tokenizedInput)):
        for j in range(len(tokenizedInput)-i):
            for k in range(i):
                # Test for combinations
                for production1 in cykTable[i-k-1][j]:
                    for production2 in cykTable[k][j+i-k]:
                        try:
                            cykTable[i][j]=chomskyGrammar[production1+production2]
                        except KeyError:
                            continue
                    
    return cykTable

# Check if table valid
def checkValidity(table, wanted):
    return wanted in table[-1][-1]