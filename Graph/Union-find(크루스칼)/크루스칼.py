'''
1. 엣지 비용에 따라 오름차순 정렬
2. 정렬된 것을 차례대로 집합에 추가하되 안전간선에 대해서만 추가(사이클 발생 안됨)

'''
# makeset : 부모 노드가 자기 자신으로 초기화
def makeset(parents):
    for i in range(1,V+1):
        parents[i] = i

def union(x,y,parents):
    p_x = findset(x,parents)
    p_y = findset(y,parents)
    if p_x > p_y:
        parents[p_x] = p_y
    else:
        parents[p_y] = p_x
        
    

# def findset(x , parents):  
#     '''
#     노드 x가 속한 집합의 대표값 반환
#     '''
#     if parents[x] != x: # 자기 자신이 대표가 아닌 경우
#         return findset(parents[x] , parents)
#     return x

def findset(x , parents):
    if parents[x] != x: # 자기 자신이 대표가 아닌 경우
        parents[x] = findset(parents[x] , parents)
    return parents[x]
    
     

# 노드 개수, 간선 개수 입력받기
V , E = map(int , input().split())
parents = [0]*(V+1)
MST = set()
result = 0 # MST 최종 비용
# 간선 정보 입력받기
edges = []
for _ in range(E):
    n1,n2,cost = map(int , input().split())
    edges.append((n1,n2,cost))

# 간선 비용에 따라 오름차순 정렬
edges.sort(key=lambda x : x[2])

# makeset
makeset(parents)

# 모든 간선 하나씩 확인
for edge in edges:
    n1 , n2 , cost = edge
    if findset(n1,parents) != findset(n2,parents):
        # 합치기(union)
        union(n1, n2,parents)
        print(n1,n2)
        MST.add(n1)
        MST.add(n2)
        result += cost
print(parents)   
print(MST)
print(result)


'''
예제 입력
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
'''
    
    
    
    




    
    
