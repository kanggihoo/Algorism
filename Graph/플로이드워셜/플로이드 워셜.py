INF = int(1e9)

# 노드 , 간선의 개수 입력받기
# N , M = map(int , input().split())
N = int(input())
M = int(input())

# 2차원 리스트(그래프 만들고), 모든 값을 무한으로 초기화(nxn)
graph = [[INF]*(N+1) for _ in range(N+1)]

# graph에서 ixi (i=0~N)인 원소값은 0으로 초기화
for i in range(N+1):
    graph[i][i] = 0

# 간선에 대한 정보 입력받고, 그 값으로 최기화
for _ in range(M):
    n1 , n2 , cost  = map(int , input().split())
    graph[n1][n2] = cost

# 점화식으로 플로이드 워셜 알고리즘 수행
for i in range(1,N+1):
    for j in range(1,N+1):
        for k in range(1,N+1):
            if not(i !=j and i !=j and j != k):
                continue
            graph[j][k] = min(graph[j][k] , graph[j][i] + graph[i][k])
            
# 결과 출력
for i in range(1,N+1):
    for j in range(1,N+1):
        if graph[i][j] == INF:
            print("0" , end = ' ')
        else:
            print(graph[i][j] , end = ' ')
    print()

'''
입력예시
4 7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
'''

'''
출력:
0 4 8 6 
3 0 7 9
5 9 0 4
7 11 2 0
'''
