'''
두명의 플레이어가 돌아가며 게임 진행(선공 : 홀수 , 후공 : 짝수)
고유번호 0~n-1인 n개의 평면 상의 점(어느 세 점도 일직선상에 없음)
매턴 마다 두 점 선택해서 연결하는 직선을 긋는다.
처음으로 사이클을 완성하는 순간 게임종료
=> 몇번째에 사이클이 완성되었는지, 아직 완성되지 않았는지 판단하는 프로그램 작성


'''
import sys
input = sys.stdin.readline
N , M = map(int , input().split())
parents = [i for i in range(N)]

def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x,y):
    p1 = find(x)
    p2 = find(y)
    if p1 > p2:
        parents[p1] = p2
    else:
        parents[p2] = p1
def solution():
    for idx in range(M):
        n1, n2 = map(int , input().split())
        if find(n1) == find(n2):
            return idx+1
        else:
            union(n1 , n2)
    return 0

print(solution())
             