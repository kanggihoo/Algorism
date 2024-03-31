import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N, M = map(int , input().split())
parents = [i for i in range(N+1)]

def findset(x):
    if parents[x] != x:
        parents[x] = findset(parents[x])
    return parents[x]
def union(x,y):
    p_x = findset(x)
    p_y = findset(y)
    if p_x > p_y:
        parents[p_x] = p_y
    else:
        parents[p_y] = p_x
        


for _ in range(M):
    Q , n1 , n2 = map(int , input().split())
    if Q == 0:
        if findset(n1) != findset(n2):
            union(n1,n2)
    elif Q==1:
        if findset(n1) == findset(n2):
            print("YES")
        else:
            print("NO")
