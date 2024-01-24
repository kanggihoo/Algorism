N , M = map(int , input().split())

arr = []
def dfs(i, depth):
    if depth == M:
        
        print(" ".join(map(str , arr)))
        return

    
    for j in range(i,N+1):
        arr.append(j)
        dfs(j,depth+1)
        arr.pop()


for i in range(1, N+1):
    arr.append(i)
    dfs(i , 1)
    arr.pop()