'''
2개의 파일을 합쳐 하나의 파일 만들고 계속 합쳐나가면서
최종 하나의 파일로 만듬.
두개 파일 합칠때 비용은 두 파일 크기의 합일때 ,최종 한개 파일 완성하는데
필요한 총 비용 계산

하나의 파일로 합칠 때 필요한 최소비용 계산
'''

T = int(input())
import heapq 
for _ in range(T):
    K = int(input())
    B = list(map(int , input().split()))
    hq = []
    for b in B:
        heapq.heappush(hq , b)
    result = 0
    while len(hq) >1:
        b1 = heapq.heappop(hq)
        b2 = heapq.heappop(hq)
        result += b1+b2
        heapq.heappush(hq , b1+b2)
    print(result)
