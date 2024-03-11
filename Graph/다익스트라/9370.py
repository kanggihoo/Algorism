'''
예술가 추적
- S에서 출발 , 우리의 후모들 중 하나가 최종 목적지(이들은 최단거리로 이동)
그들이 g ,h 교차로 사이에 있는 도로를 지나감
이때 이들은 어디를 가는 걸까?

테스트 케이스 마다, 주어진 후보들 중 불가능한 경우들을 제외한 목적지들을 공백으로 분리 후 오름차순


'''
import sys
input = sys.stdin.readline
test = int(input())
for _ in range(test):
    N,M,T = map(int , input().split()) # T:목적지 후보 갯수(서로 다르며 S과 다르다.)
    S,G,H = map(int , input().split())
    graph = [[] for _ in range(N+1)]
    g2h = None
    for _ in range(M):
        n1,n2,c = map(int , input().split())
        graph[n1].append((n2,c))
        graph[n2].append((n1,c))
        if n1 == G and n2 ==H or n1 == H and n2 ==G:
            g2h = c
    candidate = []
    for _ in range(T):
        candidate.append(int(input()))
    import heapq
    def dijkstra(S):
        hq = []
        INF = float("inf")
        distance = [INF]*(N+1)
        distance[S] = 0
        heapq.heappush(hq, (0,S))
        while hq:
            dist , cn = heapq.heappop(hq)
            if distance[cn] == INF:
                continue
            for nn ,cost in graph[cn]:
                if distance[nn] > cost+dist:
                    distance[nn] = cost+dist
                    heapq.heappush(hq , (cost+dist , nn))
        return distance
    # S=>g S=>h , g->h = graph[]
    distance_s = dijkstra(S)
    distance_g = dijkstra(G)
    distance_h = dijkstra(H)
    result = []
    for c in candidate:
        s2c = distance_s[c]
        if s2c == float("inf"):
            continue
        # S->G->H->C
        case1 = distance_s[G] + g2h + distance_h[c]
        # S->H->G->C
        case2 = distance_s[H] + g2h + distance_g[c]
        
        if s2c >= min(case1,case2):
            result.append(c) 
    result.sort()
    print(" ".join(list(map(str , result))))
        

    