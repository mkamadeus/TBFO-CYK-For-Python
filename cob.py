string = """As -> ABD
G -> D | A | F
A -> S"""
res = {}
st = string.split('\n')
for s in st:
    left = s.split(' -> ')[0]
    right = s.split(' -> ')[1].split(' | ')
    res.update(left,right)

print(res)
