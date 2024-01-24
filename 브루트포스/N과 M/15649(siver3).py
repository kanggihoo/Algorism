
N , M = map(int , input().split())

def dfs(n , depth ,arr):
    if depth == M:
        print(" ".join(map(str , arr)))
        return
    for j in range(1,N+1):
        if j not in arr:
            arr.append(j)
            dfs(j+1 , depth+1, arr)
            arr.pop()
    
for i in range(1,N+1):
    arr = []
    arr.append(i)
    dfs(i+1,1 , arr)
    