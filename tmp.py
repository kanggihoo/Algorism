'''
수강신청
S에 시작 T에 끝나는 N개의 수업
최소의 강의실 사용해서 모든 수업 가능하게
(수업 끝나고 바로 수업 가능)

# 종료-시작 값이 가장 작고, 시작시간이 가장 작은 순으로 정려 후 판단
# '''
# import sys
# input= sys.stdin.readline
# N = int(input())
# studies = []
# for _ in range(N):
#     S, T = map(int , input().split())
#     studies.append((S,T))


# # print(sorted(studies ,key = lambda x : x[0]))
# studies.sort(key = lambda x : x[1])
# result = 0
# S , E = 0,0
# for study in studies:
#     if E <=study[0]:
#         E =study[1]
#         result +=1
#         # print(study)
# print(result)

    
    
'''
0~N 까지의 정수 K개를 더해서 그 합이 N이 되는 경우 구하기
덧셈의 순서 바뀐 경우 다른 경우 
한개 숫자 중복 가능
'''


#######################################################################
# N , K = map(int , input().split())

# D = [[0]*(K+1) for _ in range(N+1)] # D[N][K]
# # K = 1일때는 항상 1
# for i in range(0,N+1):
#     D[i][1] = 1
# # N = 1일때는 K의 값의 상관없이 1
# for i in range(1,K+1):
#     D[1][i] = i

# for i in range(2,N+1):
#     for j in range(2,K+1):
#         for a in range(i+1):
#             D[i][j] += D[i-a][j-1]

# # print(D)
# print(D[N][K]%1000000000)


# n, k = map(int,input().split())
# dp = [[0] * (k+1) for _ in range(n+1)]
# dp[0][0] = 1
# for i in range(0, n+1):
#     for j in range(1, k+1):
#             dp[i][j] = dp[i-1][j] + dp[i][j-1]
# print(dp[n][k] % 1000000000)
#######################################################################


#
# 1644 연속된 소수의 합
# import math
# N = int(input())
# check = [True for _ in range(N+1)] 
# count = 0
# for i in range(2,int(math.sqrt(N))+1):
#     for j in range(i+i, N+1, i):
#         if not check[i]:
#             break
#         check[j] = False

# prime = []
# for i in range(2,N+1):
#     if check[i]:
#         prime.append(i)
# if not len(prime):
#     print(0)
# else:
#     result = 0 
#     acc_sum = prime[0]
#     L , R = 0,0
#     # print(prime)
#     while L <= R:
#         # 2 3 5 7
#         if acc_sum < N:
#             R +=1
#             if R < len(prime):
#                 acc_sum += prime[R]
#             else:
#                 break
#         elif acc_sum > N:
#             acc_sum -= prime[L]
#             L +=1
#         else:
#             result +=1
#             acc_sum -= prime[L]
#             L +=1
#     print(result)
        
#1963
'''
4자리 소수 A,B 주어질때 A->B변경시 항상 4자리 소수 유지하면서 몇단계 거쳐야 하는지 찾기(0039이런거 안됨)
불가능한 경우 Impossible 출력

'''
# import math
# from collections import deque
# T = int(input())
# N = 10000
# # 4자리 소수 찾기
# check = [True for _ in range(10000)]
# for i in range(2,int(math.sqrt(N))+1):
#     for j in range(i+i , N , i):
#         if not check[i]:
#             break
#         check[j] = False
# # 4자리 소수만 따로 저장
# prime = []
# for i in range(1001,N):
#     if check[i]:
#         prime.append(i)
# # 주어진 두 수가 1자리만 다른지 확인
# def enable(adj , cur):
#     adj = list(str(adj))
#     cur = list(str(cur))
#     cnt = 0
#     for i in range(4):
#         if adj[i] == cur[i]:
#             cnt +=1
#     return True if cnt ==3 else False
# def bfs(A,B):
#     Q = deque()
#     Q.append((A,0))
#     check = [True for _ in range(10000)]
#     check[A] = False
#     while Q:
#         cur_prime , cur_depth = Q.popleft()
#         if cur_prime == B:
#             print(cur_depth)
#             return True
#         for adj in prime:
#             if check[adj] and enable(adj,cur_prime):
#                 check[adj] = False
#                 Q.append((adj,cur_depth+1))
#         # print(Q)
#     return False
# # Test case 마다 확인
# for _ in range(T):
#     A , B = map(int , input().split())  
#     if bfs(A,B):
#         pass
#     else:
#         print("Impossible")
    
def bfs(y,n, width , diagnal1 , diagnal2):
        ans = 0
        if y==n:
            ans+=1
        else:
            for i in range(n):
                try:
                    if width[i] or diagnal1[y+i] or diagnal2[y-i+n-1]:
                        continue
                    # 말 놓기
                    width[i] = diagnal1[y+i] = diagnal2[y-i+n-1] = True
                except Exception as e:
                    print((y,i , y+i , y-i+n) , width , diagnal1 , diagnal2)

                ans += bfs(y+1 , n , width , diagnal1 , diagnal2)
                # 백 트래킹
                width[i] = diagnal1[y+i] = diagnal2[y-i+n-1] = False
        return ans
    
def solution(n):
            
    ans = bfs(0,n,[False]*n , [False]*(2*n-1) , [False]*(2*n-1))
    return ans
print(solution(1))

            

    
    
    



        
        