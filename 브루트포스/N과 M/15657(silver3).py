import sys
sys.setrecursionlimit(100000)
N , M = map(int , input().split())
arr= list(map(int , input().split()))
arr.sort()

def dfs(S , depth , result):
    if depth == M:
        print(" ".join(map(str , result)))
        return
    
    for j in arr:
        if j >= result[depth-1]:
            result.append(j)
            dfs(j , depth+1, result)
            result.pop()
        
for i in arr:
    dfs(i , 1, [i])
        
    