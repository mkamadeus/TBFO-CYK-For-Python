# global terminal
# terminal = ['a','b']

global CNF
CNF = {}
# released = {
#         "aA" : ["S"],
# 		"AA" : ["S"],
# 		"AB" : ["A"],
# 		"EA" : ['B'],
#         "a" : ['A'],
#         "b" : ['E'],
# }

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
            value = CNF.get(C[j])
            if (value == None):
                print(C[j])
                CNF.update({C[j] : [A]})
            else :
                print(A)
                print(C[j])
                CNF[C[j]].append(A)
    print(CNF)

# global CNF
# CNF = {}
# if len(sys.argv) > 1:
#     modelPath = str(sys.argv[1])
# else:
# 	modelPath = 'out.txt'
# LoadCNF()
# Program CYK

# print(released)
# for key in released:
#     for i in range(len(released[key])):
#         print(released[key][i],"->", key)

# def IsTerminal (c):
#     if (c in terminal):
#         return True
#     else:
#         return False

# def IsTwoNonTerminal (key):
#     result1 = ((ord(key[0]) >= 65) and (ord(key[0]) <= 90))
#     result2 = ((ord(key[1]) >= 65) and (ord(key[1]) <= 90))
#     return (result1 and result2)

# print()
# check = True

# # Elimination Unit Production
# heg = 90
# for key in released:
#     if ((IsTwoNonTerminal(key)) and (len(key) == 2)):
#         CNF.update({key : released[key]})
#         heg = heg - 1
#     else:
#         if ((IsTerminal(key)) and (len(key) == 1)):
#             CNF.update({key : released[key]})
#         else:
#             counter = 0
#             s = ''
#             print("wow",s)
#             for char in key:
#                 print(char,key)
#                 if (IsTerminal(char)):
#                     s = s + chr(heg)
#                     CNF.update({char : chr(heg)})
#                     heg = heg - 1
#                     print(s)
#                 else :
#                     s = s + released[key][counter-1]
#                     print(s)
#                 counter = counter + 1
#             CNF.update({s : released[key]})

# print("Grammar CFG") 
# for key in released:
#     for i in range(len(released[key])):
#         print(released[key][i],"->", key)
# print("Grammar CNF") 
# for key in CNF:
#     for i in range(len(CNF[key])):
#         print(CNF[key][i],"->", key)