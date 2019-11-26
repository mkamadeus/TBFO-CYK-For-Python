import cyk
# Load CNF File

def LoadCNF(modelPath):
    file = open("out.txt").read()
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
                print(C[j])
                chomskyGrammar.update({C[j] : [A]})
            else :
                print(A)
                print(C[j])
                chomskyGrammar[C[j]].append(A)
    print(chomskyGrammar)