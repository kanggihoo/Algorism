# 유클리드 호제
import sys 
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    A,B = map(int , input().split())
    A_cp , B_cp = A,B
    GCD = 0
    while(A_cp%B_cp !=0):
        A_cp , B_cp = B_cp , A_cp%B_cp
    GCD = B_cp
    print((A//GCD) * (B//GCD) * GCD)
    