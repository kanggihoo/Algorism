'''


'''
import sys
input = sys.stdin.readline
N , K = map(int , input().split())
coins = []
for _ in range(N):
    coin = int(input())
    if coin <= K :
        coins.append(coin)
coins.sort()
# D[N][K] => K원을 넣
if len(coins):
    D = [10001]*(K+1)
    for c in coins:
        D[c] = 1
    for i in range(1,K+1):
        for c in coins:
            if i > c and D[i-c] !=10001:
                D[i] = min(D[i] , D[i-c]+1)
    if D[K] >= 10001:
        print(-1)
    else:        
        print(D[K])
    
else:
    print(-1)
  
