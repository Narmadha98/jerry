from itertools import permutations
s=input()
p=permutations(s)
for i in list(p):
    print(''.join(i))
#permutation
