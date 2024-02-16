'''
n개의 대학에서 강연 , d일 안에 와서 강연을 하면 p만큼의 보상
가장 많은 돈을 벌 수 있도록 순회강연
하루에 한 곳에서만 강연 가능



'''
N = int(input())
lectures = []
for _ in range(N):
    p , d = map(int , input().split())
    lectures.append((p,d))
# 정렬
# lectures.sort(key = lambda x : (x[0] , x[1]) , reverse = True)
# visited = [False]*(10000+1)
# result = 0
# for l in lectures:
#     p , d = l
#     if not visited[d]:
#         visited[d] = True
#         result += p
#     else:
#         while d >=0 and visited[d]:
#             d -=1
#         if d !=0:
#             visited[d] = True
#             result +=p
# print(result)

# 우선순위 큐를 사용한 방법 (day를 기준으로 오름차순정렬)
# 이 방법이 위의 방법보다 훨씬 빠름
import heapq
lectures.sort(key=lambda x : x[1])
hq = []
for l in lectures:
    p , d = l
    heapq.heappush(hq , p)
    if len(hq) > d: # 힙에 저장된 원소 개수가 현재 제한일수 보다 큰 경우(가장 작은 가치를 가지는거 삭제)
        heapq.heappop(hq)
print(sum(hq))
            
            
    