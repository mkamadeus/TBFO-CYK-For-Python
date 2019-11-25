# S -> AB
# A -> CD | CF
# B -> c | EB
# C -> a
# D -> b
# E -> c
# F -> AD

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

dict = {
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

# def IsUseless (c):
#     count = 0
#     for key in released:
#         for char in key:
#             if (c == char):
#                 count += 1
#     if (count == 1):
#         return False
#     else:
#         return True

# print()
# check = True
# # Elimination Useless Production
# for key in released:
#     for char in key:
#         print(char)
#         check = IsUseless(char)
#         if (check):
#             print("Unique")
#         else:
#             print("None")