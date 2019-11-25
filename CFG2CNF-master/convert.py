released = {
		"bA" : ["S"],
		"aB" : ["S"],
		"bAA" : ['A'],
		"aS" : ['A'],
        "a" : ['A','C'],
        "aBB" : ['B'],
        "bS" : ['B'],
        "b" : ['B']
	}

for key in released:
    for i in range(len(released[key])):
        print(released[key][i],"->", key)

def IsUseless (c):
    count = 1
    result = true
    for key in released:
        for char in key:
            if (count > 1):

        count += 1

print()
check = True
# Elimination Useless Production
for key in released:
    for char in key:
        print(char)
        check = IsUseless(char)
        if (check):
            print("Unique")
        else:
            print("None")