# 1개의 회의실에서 N개의 회의실  사용표 만들기
# 각 회의 시작 , 끝 시간 주어질 때 겹치지 않으면서 최대 몇번 회의 가능한지 
# (회의 중간에 중단 못하고, 끝내는 동시에 바로 회의 시작 가능)

# 첫번째줄에 회의의 수 
# 회의시작, 종료 시간 공백으로

import sys
from queue import PriorityQueue
input = sys.stdin.readline
N = int(input())
Q = PriorityQueue()
END = None
result = 0
for _ in range(N):
    start , end = map(int , input().split())
    Q.put((end,(start,end)))
## end를 기준으로 우선순위 큐값을 가져온다.
start , end = Q.get()[1] # 종료 시간이 가장 작은 값을 빼옴
# print((start , end))
END = end
result +=1
while(not Q.empty()):
    start , end = Q.get()[1]
    if start >= END:
        END = end
        result +=1
        # print((start , end))
print(result)

    
            
            
            


