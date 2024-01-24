import sys
input = sys.stdin.readline
T = int(input())
for t in range(T):
    N = int(input())
    coins = list(map(int , input().split()))
    M = int(input())

    D = [0 for _ in range(10000+1)]

    for coin in coins:
        D[coin] +=1
        for m in range(1,M+1):
            if coin <= m:
                D[m]  += D[m-coin]
    print(D[M])
        