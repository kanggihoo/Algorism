# N명의 참가자, 0~N-1번의 번호이며, 일부사람은 친구이다.
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N , M = map(int , input().split())
graph = [[] for i in range(N)]
for _ in range(M):
    n1,n2 = map(int , input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)


def DFS(S , depth):
    if depth==4:
        return True
    else:
        visited[S] = True
        for i in graph[S]:
            if not visited[i]:
                # depth = 4를 찍어서 True가 반환된 경우 계속 True를 반환한다. 
                if(DFS(i , depth+1)):
                    return True
        # DFS로 탐색했을 때 depth 가 4가 안된 경우는 방문한 노드를 False로 초기화 해야 다음 탐색에 영향을 미치지 않는다. 
        visited[S] = False
                
        

enable_flag = False
visited = [ False for i in range(N)]
for i in range(0,N):
    
    if DFS(i,0):
        enable_flag = True
        break
if enable_flag:
    print(1)
else:
    print(0)
    