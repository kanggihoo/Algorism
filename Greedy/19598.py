'''
N개의 회의 를 모두 진행할 수 있는 최소 회의실 개수
한 회의실에서 동시에 두개 이상의 회의 진행못함
한번 시작시 중간에 중단못함.
끝나는 동시에 다음 회의 가능 


'''
import heapq
N = int(input())
R = []
for _ in range(N):
    s,e = map(int , input().split())
    R.append((s,e))
R.sort(key = lambda x : (x[0],x[1]) )
hq = []
heapq.heappush(hq , R.pop(0)[1])
for r in R:
    s ,e = r
    if hq[0] <= s:
        heapq.heappop(hq)
    heapq.heappush(hq , e)

print(len(hq))
    