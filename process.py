import re

def splittingProduction(OldProduction):
    # Kamus Lokal
    result = []
    removeline = OldProduction.replace('\n','').split(';')
    # Algoritma
    for rule in removeline:
        symbol = rule.split(' -> ')[0].replace(' ','')
        resproduction = rule.split(' -> ')[1].split(' | ')
        for res in resproduction:
            result.append((symbol, res.split(' ')))
    return result