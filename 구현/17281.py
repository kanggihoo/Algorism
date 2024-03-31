import sys
input = sys.stdin.readline


'''
9명, 공격,수비 교대, 1이닝: 공격과 수비로 구성 총 N번
3아웃시 종료(공수교대)
시작전 타순 정하고, 경기 중 변경못함 1->9->1로 순환 
타순은 이닝 변경되어도 유지 

타자는 안타,2,3,홈런,아웃 중 하나 
1~9번, 중 1번선수는 항상 4번 타자 

'''
from itertools import permutations
N = int(input()) 
A = []
for _ in range(N):
    A.append(list(map(int , input().split())))
case = permutations(range(2,9+1), 8)


max_score = 0
p1,p2,p3 =0,0,0
for c in case:
    x = list(c)
    orders = x[:3] + [1] + x[3:]
    tscore = 0
    idx = 0 
    for i in range(N):
        cnt = 0
        p1,p2,p3 = 0, 0,0
        while cnt < 3:
            hit = A[i][orders[idx]-1]
            if hit == 0:
                cnt+=1
            else:
                if hit == 1:
                    tscore += p3
                    p1,p2,p3 = 1, p1,p2
                elif hit == 2:
                    tscore += p2+p3
                    p1,p2,p3 = 0, 1,p1
                    
                elif hit == 3:
                    tscore += (p1+p2+p3)
                    p1,p2,p3 = 0, 0,1
                else:
                    tscore += p1+p2+p3+1
                    p1,p2,p3 = 0, 0,0
            idx = (idx +1)%9
        
    max_score = max(max_score , tscore)
print(max_score)