'''
N - Queen
N개의 퀸을 서로 공격하지 못하게 놓는 방법수 구하기



'''
N = int(input())
maps = [[]]
result = 0

def dfs(y , width , D1 , D2):
    if y ==N:
        global result
        result+=1
        return
    # 가능한 x 위치 찾기
    for i in range(N):
        if not width[i] and not D1[i+y] and not D2[y-i+N]:
            width[i] = D1[i+y] = D2[y-i+N] = True
            dfs(y+1 , width , D1 , D2)
            width[i] = D1[i+y] = D2[y-i+N] = False
            
dfs(0,[False]*N , [False]*2*N , [False]*2*N)
print(result)