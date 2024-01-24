import sys
input = sys.stdin.readline

N, K = map(int , input().split())
coins = []
for _ in range(N):
    coin = int(input())
    if coin <=K:
        coins.append(coin)

D = [0 for _ in range(10000+1)] 
    
for coin in coins:
    D[coin] += 1
    for k in range(1,K+1):
        if coin > k:
            continue
        else:
            D[k] += D[k-coin]
print(D[K])