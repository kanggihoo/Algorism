

# 첫번째 줄에 N 
# N줄에 덜쳐서 숫자 카드 묶음의 크기가 주어지고 최소 비교횟수 출력

import heapq
import sys
input = sys.stdin.readline
N = int(input())
cards = []
for _ in range(N):
    cards.append(int(input()))
#최소힙으로 만들기
heapq.heapify(cards)

#가장 작은 카드 2개 제거 후 더한뒤 다시 headp에 넣기
result =0
while len(cards) >=2:
    n1 = heapq.heappop(cards)
    n2 = heapq.heappop(cards)
    result +=(n1+n2)
    heapq.heappush(cards , n1+n2)
# 힙에 1개 원소만 남음
print(result)
    
    
    
        
    
