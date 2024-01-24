# import sys
# sys.setrecursionlimit(100000)
# N , M = map(int , input().split())
# arr= list(map(int , input().split()))
# arr.sort()
# visit = [False for _ in range(N)]

# def dfs(depth , result,visit,SET):

#     if depth == M:
#         print(" ".join(map(str , result)))
#         return 
    
#     before = None
#     for idx , j in enumerate(arr):
#         if not visit[idx] and before != j:
#             result.append(j)
#             before= j
#             visit[idx] = True
#             dfs(depth+1, result, visit,SET)
#             result.pop()
#             visit[idx] = False



# dfs(0, [],visit,set())

