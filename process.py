import re

white_space = ' '
'''
def cleaningProduction(OldProduction):
    for key in OldProduction:
        for i in range(len(OldProduction[key])):
            if(len(re.findall("BOOL",key)) == 0):
                print(OldProduction[key][i],'->',key)
            else:
                for subkey in OldProduction:
                    for j in range(len(OldProduction[subkey])):
                        if(len(re.findall("BOOL",subkey)) == 0):
                            print(OldProduction[key][i],'->',key.replace("BOOL",subkey))
'''
'''
def cleaningProduction(OldProduction):
    variable = 1
    for key in OldProduction:
        lexeme = ''
        FirstProduction = ''
        NewProduction = {}
        count = 0
        for char in key:
            if char == white_space:
                count+=1
                if(count>1):
                    NewProduction.update(lexeme)
                lexeme = ''
            else:
                if(count < 1):
                    FirstProduction+=char
                lexeme+=char
        NewProduction.append(lexeme)
        for i in range(len(OldProduction[key])):
            if(count <= 1):
                print(OldProduction[key][i],'->',key)
            else:
                for j in range(count-1):
                    print(OldProduction[key][i],'->',FirstProduction,'U'+str(variable))
                    print('U'+str(variable),'->',NewProduction)
                    variable+=1
'''           

dictionary = {
            # Boolean
            'True':['BOOL'],
            'False':['BOOL'],
            'BOOL AND BOOL':['BOOL'],
            'and':['AND'],
            'BOOL OR BOOL':['BOOL'],
            'or':['OR'],
            'not BOOL':['BOOL']
            }
cleaningProduction(dictionary)