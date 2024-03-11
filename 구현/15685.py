'''
세가지 속성
x축은 ->
y축은 아래방향
1. 시작점
2. 시작방향
3. 세대 

0세대는 길이가 1인 선분 
1세대는 0세대의 끝점을 기준으로 시계방향 90도 회전 후 0세대
2세대는 1세대를 90도 회전 후 이어붙인거 

크기 100x100 격자 위 커브가 N개 있음.
1x1 정사각형 네 꼭짓점이 모두 커브의 일부인 정사각형 개수 구하라

입력으로 주어진 커브는 격자를 벗어나지 않는다. 
커브의 개수 N
x,y,d,g 정보 : (x,y) 커브 시작점 , d : 시작 방향 , g: 세대
0: 오 , 1: 위쪽 , 2: 왼 , 3: 아래
3
3 3 0 1
4 2 1 3
4 2 2 1
'''

N = int(input())
curves = []
for _ in range(N):
    x,y,d,g = map(int , input().split())
    curves.append((x,y,d,g))
maps = [[0]*101 for _ in range(101)]
def new_p(x,y,d):
    if d == 0: # 위쪽방향 리턴
        return (x,y-1,1)
    elif d==1: # 왼쪽방향 리턴
        return (x-1 , y , 2)
    elif d==2: # 아래방향 리턴
        return (x,y+1 , 3)
    elif d==3: # 오른 리턴
        return (x+1 , y , 0)
        

def dragon_curve(x,y,d,g):
    # 시작점과 방향정보로  0세대 만들기
    element = [(x,y,d)]
    end = (x+1,y,d) if d == 0 else (x,y-1,d) if d==1 else (x-1,y,d) if d==2 else (x,y+1,d)
    element.append(end)
    # g세대 좌표 구하기
    for i in range(g):
        for idx in reversed(range(1,len(element))):
            d = element[idx][-1]
            end = element[-1][:2]
            element.append(new_p(*end,d))
            
    return element
            
            
            
# 0: 오 , 1: 위쪽 , 2: 왼 , 3: 아래
for curve in curves:
    element = dragon_curve(*curve)
    # print(element)
    for e in element:
        x,y = e[:2]
        maps[y][x] = 1

def check():
    result = 0 
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            count = 0
            if maps[i][j] == 1:
               for dy,dx in zip([0,0,1,1],[0,1,0,1]):
                   ny , nx = i+dy , j+dx
                   if ny <= 100 and nx <=100 and maps[ny][nx] ==1:
                       count +=1 
                   else:
                       break
            if count ==4 :
                result +=1
    return result
print(check())
                
                
    

