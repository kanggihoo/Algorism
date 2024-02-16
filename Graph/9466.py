'''
사이클 발생 여부 확인
1. 방문한적없는 노드이면 방문한적 있는 노드를 만날때 까지 dfs 진행
2. 다음으로 이동할 노드가 방문한 적이있는 경우
    2.1 다음 노드가 우리의 사이클에 포함되어 있으면 사이클이 완성됨
        따라서 다음 노드가 사이클의 어디에 포함되어 있는지 확인 후
        사이클처리
    2.2 다음 노드가 우리의 사이클에 포함되지 않은 경우 =>
        다음 노드는 방문한적이 있기 때문에 다음 노드는 이미 누군가의
        사이클에 포함된 경우 이므로 이때는 동작 중단
'''
import sys
sys.setrecursionlimit(10**8)
def dfs(i ,cycle , done):
    visited[i] = True
    cycle.append(i)
    ni = S[i]
    if not visited[ni]: # 방문하지 않은 노드는 dfs
        dfs(ni,cycle,done)
    else: # 방문한 노드 (실제 cycle 에 있는 경우는 중단하고 없는 경우는 dfs)
        if not done[ni]: # 현재 노드가사이클에 포함된 경우
            # 다음 노드가현재 사이클에서 언제 발생되었는지 확인후 결과 반영
            global result
            # print(cycle , ni)
            result += len(cycle[cycle.index(ni):]) # ni가 등장하고 나서부터 cycle의 원소 개수
            # print("사이클 발견" , cycle)
    # dfs 종료 후 처음으로 돌아가면서 done 값을 업데이트 
    done[i] = True
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    S = [0]+list(map(int , input().split()))

    visited = [False]*(N+1)
    done = [False]*(N+1) # 이미 사이클이 발생하여 더이상 진행하지 않아도 되는지 확인
    result = 0
            
    for i in range(1,N+1):
        if not visited[i]:
            cycle = []
            dfs(i,cycle,done)
    print(N - result)
# result = 0
# for i in range(1,N+1):
#     if not visited[i]:
#         result+=1
# print(result)
