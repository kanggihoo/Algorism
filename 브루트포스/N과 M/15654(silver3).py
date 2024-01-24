N , M = map(int , input().split())
N_arr = list(map(int , input().split()))
N_arr.sort()
arr = []
def dfs(i, depth):
    if depth == M:
        
        print(" ".join(map(str , arr)))
        return
    for j in N_arr:
        if not j in arr:
            arr.append(j)
            dfs(j,depth+1)
            arr.pop()


for i in N_arr:
    arr.append(i)
    dfs(i , 1)
    arr.pop()