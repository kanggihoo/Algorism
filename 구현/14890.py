'''
NxN 지도, 각 칸은 높이
2n개의 길
지나갈러면 길에 속한 모든 칸의 높이가 모두 같아야 한다. 
길이란 한 행 또는 한 열 전부를 나타내며, 한쪽 끝에서 다른쪽 끝까지 지나가는 것이다.
또는 경사로를 놓아서 길을 만들 수도 있음(경사로 높이는 항상1, 길이 L, 개수는 무제한)
경사로는 낮은 칸과 높은 칸을 연결

경사로 
'''
N , L  = map(int , input().split())
maps = []
for _ in range(N):
    maps.append(list(map(int , input().split())))


def check_row(y,x):
    slide_road  = [False]*N
    while x+1 < N:
        # 높이가 같은 경우 
        if maps[y][x] == maps[y][x+1]:
            x+=1
        # 높이가 다른경우
        elif abs(maps[y][x] - maps[y][x+1]) == 1:
            if maps[y][x] > maps[y][x+1]:
                # 경사로 놓을 칸이보장되어야 함.
                # x보다 L만큼 떨어진 높이가 모두 동일해야 함.
                if x+L < N and  all(maps[y][x+1+i] == maps[y][x+1] and not slide_road[x+1+i] for i in range(L)):
                    for i in range(L):
                        slide_road[x+1+i] =True
                    x+=L # L만큼 이동
                else:
                    return False
            elif maps[y][x] < maps[y][x+1]:
                # 경사로 높을 칸이 보장되어야 함
                if x-L+1 >=0 and all(maps[y][x] == maps[y][x-i] and not slide_road[x-i] for i in range(L)):
                    for i in range(L):
                        slide_road[x-i] =True
                    x+=1 # 다음칸 확인
                    
                else:
                    return False
        else:
            return False    
    return True

def check_col(y,x):
    slide_road  = [False]*N
    while y+1 < N:
        # 높이가 같은 경우 
        if maps[y][x] == maps[y+1][x]:
            y+=1
        # 높이가 다른경우
        elif abs(maps[y][x] - maps[y+1][x]) == 1:
            if maps[y][x] > maps[y+1][x]:
                # 경사로 놓을 칸이보장되어야 함.
                # x보다 L만큼 떨어진 높이가 모두 동일해야 함.
                if y+L < N and  all(maps[y+1+i][x] == maps[y+1][x] and not slide_road[y+1+i]for i in range(L)):
                    for i in range(L):
                        slide_road[y+1+i] =True
                    y+=L # L만큼 이동
                else:
                    return False
            elif maps[y][x] < maps[y+1][x]:
                # 경사로 높을 칸이 보장되어야 함
                if y-L+1 >=0 and all(maps[y][x] == maps[y-i][x] and not slide_road[y-i] for i in range(L)):
                    for i in range(L):
                        slide_road[y-i] =True
                    y+=1 # 다음칸 확인
                else:
                    return False
        else:
            return False    
    return True
    
        
    

# 모든 행 조사 
result = 0 
for i in range(N):
    if check_row(i,0):
        result +=1
        # print(f"{i},{0} , 행방향")
    if check_col(0,i):
        result +=1
        # print(f"{i},{0} , 열방향")
print(result)


         