'''
수빈이 위치 :  N = 0~100,000
동생 위치 : K  = 0~100,000


'''
import heapq
N , K = map(int , input().split())
maxD = 100001
distance = [maxD for _ in range(100000+1)]
visited = [False  for _ in range(100000+1)]

def min_distance(S):
    hq = []
    distance[S]= 0
    heapq.heappush(hq , (0 , S))


    while hq:
        dist , cur = heapq.heappop(hq)
        if visited[cur]:
            continue
        visited[cur] = True
        if cur*2 <= 100000 :
            if distance[cur*2] > dist:
                distance[cur*2] = dist
                heapq.heappush(hq , (distance[cur*2] , cur*2))
            
        for next in [cur+1 , cur-1]:
            if next >=0 and next <= 100000:
                tmp = dist+1
                if distance[next] > tmp:
                    distance[next] = tmp
                    heapq.heappush(hq , (distance[next] , next))
min_distance(N)  
print(distance[K])
    
    

