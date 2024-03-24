'''
nxx, 학생수 n*2, 1번 부터번호, 
학생 순서, 좋아하는 학생 4명
인접 거리가 1

행의번호 작고, 열의 번호 작은 칸 

최종적으로 학생 만족도, => 자리배치 종료 시 구함
인접한 칸에 앉은 학생수, 
'''
import sys
input = sys.stdin.readline
N = int(input())
MAP = [[0]*N for _ in range(N)]
orders = []
for _ in range(N*N):
    orders.append(list(map(int , input().split())))
S_list = [None]*(N*N)
from collections import defaultdict

def case1(num,favorit):
    cnt = defaultdict(int)
    for f in favorit:
        if S_list[f-1] is not None:
            y,x = S_list[f-1] 
            for ny,nx in [(y-1,x),(y+1,x) , (y,x-1) , (y,x+1)]:
                if 0<=ny < N and 0<=nx<N and MAP[ny][nx] ==0:
                    cnt[ny*N+nx]+=1
    # print(cnt)
    if len(cnt):
        if len(cnt) ==1:
            
            p = int(list(cnt.keys())[0])
            y,x = p//N , p%N
            return (y,x) , True
        cnt = sorted(cnt.items() , key = lambda x :-x[1])
        if cnt[0][1] != cnt[1][1]:
            p = int(cnt[0][0])
            return (p//N , p%N) , True
        else:
            max_cnt = max(cnt , key=lambda x:x[1])[1]
            return [(int(k)//N,int(k)%N) for k ,v in cnt if v == max_cnt] , False
    else:
        return [None] , False
    
    
def case2(P):
    cnt = defaultdict(int)
    if P[0] is None: # 모든 자리 빈자리 확인
        for i in range(N):
            for j in range(N):
                if MAP[i][j] == 0:
                    cnt[i*N+j] =0
                    for ny , nx in [(i-1,j),(i+1,j) , (i,j-1) , (i,j+1)]:
                        if 0<=ny < N and 0<=nx <N and MAP[ny][nx] ==0:
                            cnt[i*N+j]+=1
    else: # case1에서의 후보군만 확인
        for y,x in P:
            cnt[y*N+x] =0
            for ny , nx in [(y-1,x),(y+1,x) , (y,x-1) , (y,x+1)]:
                if 0<=ny < N and 0<=nx <N and MAP[ny][nx] ==0:
                    cnt[y*N+x]+=1
    
    cnt = sorted(cnt.items() , key = lambda x : (-x[1],int(x[0])//N ,int(x[0])%N) )
    return int(cnt[0][0])
        
            

for order in orders:
    num , *F = order
    C1 = case1(num,F)
    # print(num , C1)
    if C1[1]:
        y,x = C1[0]
        MAP[y][x] = num
        S_list[num-1] = (y,x)
    else:
        # print("c1 :",C1[0])
        k= case2(C1[0])
        y,x = k//N,k%N
        MAP[y][x] = num
        S_list[num-1] = (y,x)
    # print(k)
    # if num == 5:
    #     print(S_list)
    #     break
def cal():
    total= 0
    for order in orders:
        num , *F = order
        y,x = S_list[num-1]
        cnt = 0
        for ny,nx in [(y-1,x),(y+1,x),(y,x-1),(y,x+1)]:
            if 0<=ny <N and 0<=nx<N:
                if MAP[ny][nx] in F:
                    cnt +=1
        if cnt ==0:
            continue
        total += 10**(cnt-1)
        # print(num, 10**cnt)
    return total
            
# for i in range(N):
#     for j in range(N):
#         print(MAP[i][j] , end =" ")
#     print()

print(cal())
                
        
        
        
        
    
    