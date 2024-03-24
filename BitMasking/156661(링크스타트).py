import sys
input = sys.stdin.readline

'''
N명 , 스타트팀, 링크팀 분리(최소 1명이상, 달라도됨)
1~N번호, 능력치 S

'''

N = int(input())
S = []
Total = 0
for _ in range(N):
    nums = list(map(int , input().split()))
    S.append(nums)
    Total+=nums

def cal(team):
    tsum = 0
    for i in team:
        for j in team:
            tsum += S[i][j]
    return tsum

min_v = 100*20
for i in range(1,(1<<N-1)+1):
    team1 = []
    team0 = []
    for j in range(N):
        if i&(1<<j): # 1팀
            team1.append(j)
        else: # 0팀
            team0.append(j)
    
    # 능력치 계산
    t1 = cal(team1)
    t0 = cal(team0)
    min_v = min(abs(t1-t0) , min_v)


print(min_v)
    
    



