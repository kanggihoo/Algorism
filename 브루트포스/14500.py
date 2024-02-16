N,M = map(int ,input().split())
maps = [] 
for _ in range(N):
    maps.append(list(map(int , input().split())))
max_score = 0
def shape1(N,M):# 1x4 모양
    max_score = 0
    x , y = 0,0
    while y+3 < N:
        while x +3< M :
        # 가로모양인경우
            max_score = max(max_score , sum(maps[y][i+x] for i in range(4)))
            x +=1
            print(x,y)
        x=0
        y+=1
        
    return max_score
print(shape1(N,M))
        
    