'''
N개의 높이가 다른 탑을 세우고 꼭대기에 송신기 설치
송신기는 레이저 신호를 왼쪽 방향으로 발사,
탑의 기둥에는 레이저 신호 수신 장치 존재.
해당 레이저는 먼저 만나는 탑에서만 수신 가능 


N개 탑의 높이가 주어질 때 각 탑에서 발사한 
신호를 어느 탑에서 수신하는지 구하기
(1번 ~N번 탑 )
수신 하는 탑이 없음면 0을 출력
'''
import sys 
input = sys.stdin.readline
N = int(input())
tops = list(map(int , input().split()))
stack = []
result = [0 for _ in range(N)]

for i in range(N):
    while stack:
        if tops[i] < stack[-1][0]:
            result[i] = stack[-1][1] +1
            break
        else:
            stack.pop()
    stack.append((tops[i] , i))
# print(" ".join(list(map(str , result))))
print(*result)
        
    