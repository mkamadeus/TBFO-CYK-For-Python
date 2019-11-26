string = """As -> ABD
G -> D | A | F
A -> S"""
res = {}
st = string.split('\n')
for s in st:
    left = s.split(' -> ')[0]
    right = s.split(' -> ')[1].split(' | ')
    for i in range(len(right)):
        res.update({right[i] : left})

print(res)
