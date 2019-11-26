import pprint as pp

released = {
        "AB" : ["S"],
        "CD" : ["A"],
        "CF" : ["A"],
        "c" : ["B","E"],
        "EB" : ["B"],
        "a" : ["C"],
        "b" : ["D"],
        "AD" : ["F"]
}


file = open("input.txt", "r")
contents = file.read()

print(len(contents))

cykTable = [[[] for j in range(i)] for i in range(len(contents),0,-1)]
pp.PrettyPrinter(indent=4).pprint(cykTable)

# Initialize
for i in range(len(contents)):
    print(contents[i])
    cykTable[0][i].extend(released[contents[i]])

pp.PrettyPrinter(indent=4).pprint(cykTable)

# Iterative
for i in range(1,len(contents)):
    for j in range(len(contents)-i):
        for k in range(i):
            # Test for combinations
            for production1 in cykTable[i-k-1][j]:
                for production2 in cykTable[k][j+i-k]:
                    try:
                        cykTable[i][j]=released[production1+production2]
                        print(i,j,cykTable[i][j])
                    except KeyError:
                        continue
                
            pp.PrettyPrinter(indent=4).pprint(cykTable)
            # print(cykTable[i-k-1][j],cykTable[k][j+i-k])

# for i in range(len(contents)):
#     for j in range(i+1):
#         cykTable[i][j]=released[contents[j]]