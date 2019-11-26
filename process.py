import re

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
white_space = ' '

def IsKataSama(str1,str2):
    # Melakukan cek apakah str1 == str2
    # Kamus Lokal
    b = True
    # Algoritma
    if(len(str1) != len(str2)):
        b = False
    else:
        i = 1
        while(b and i < len(str1)):
            if(str1[i] != str2[i]):
                b = False
            else:
                i+=1
    return b

def JumlahKata(str1):
    # Melakukan perhitungan jumlah kata
    # Input tidak diakhiri blank
    # Kamus lokal
    sum = 1
    i = 0
    # Algoritma
    # IgnoreBlank
    while(str1[i] == white_space):
        i+=1
    while(i < len(str1)):
        if(str1[i] == white_space):
            sum+=1
        i+=1
    return sum

def CKata(str1):
    # Kamus lokal
    i = 0
    lexeme = ''
    # Algoritma
    # IgnoreBlank
    while(str1[i] == white_space):
        i+=1
    while(i < len(str1) and str1[i] != white_space):
        lexeme+=str1[i]
        i+=1
    return lexeme
  
def CleaningUnitRules(OldDict, NewDict):
    # Melakukan pembersihan unit rules
    for key in OldDict:
        for i in range(len(OldDict[key])):
            pass

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