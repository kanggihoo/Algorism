# 조약돌 N개 , 색상 1~M 
# K개 봅을 때 뽑은 조약돌이 모두 같은 색깔일 확률

# 1<=M<=50
# 1~조약돌 개수~50
# 1~K<=N
import sys
input = sys.stdin.readline
M = int(input())
color_by_stone = list(map(int , input().split()))
total_stone = sum(color_by_stone)
K = int(input())



    
    