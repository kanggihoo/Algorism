from itertools import combinations
S = list(input())
stack = []
comb = []
for idx in reversed(range(len(S))):
    if S[idx] == ")":
        stack.append(idx)
    elif S[idx] == "(":
        comb.append((idx,stack.pop()))
result = set()
# /print(comb)
for i in range(1,len(comb)+1):
    C = combinations(comb , i)
    for c in C:
        index = set()
        for i1,i2 in c:
            index.add(i1)
            index.add(i2)
        answer = [s for idx , s in enumerate(S) if idx not in index]
        result.add("".join(answer))
result = sorted(list(result))
for i in result:
    print(i)
    

        
   
    