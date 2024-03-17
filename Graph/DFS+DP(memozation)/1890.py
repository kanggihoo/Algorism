'''
NxN
'''
N = int(input())
MAP = []
for _ in range(N):
    MAP.append(list(map(int , input().split())))
D = [[0]*N for _ in range(N)]


def dfs(x,y):
    
    if y == N-1 and x == N-1:
        global ans 
        ans +=1
        return 1
    elif MAP[y][x] ==0:
        return 0
    
    if D[y][x] !=0:
        return D[y][x]
    
    value = MAP[y][x]
    for nx , ny in [(x+value , y) , (x,y+value)]:
        if ny < N and nx <N:
            D[y][x] +=dfs(nx,ny)
    return D[y][x]

    
ans = 0
# print(dfs(0,0))
print(ans)
# for i in range(N):
#     for j in range(N):
#         print(D[i][j] , end=" ")
#     print()    