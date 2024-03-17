import sys
input = sys.stdin.readline
N , M = map(int , input().split())
T = [0]*(N+1)
for _ in range(M):
    command = list(map(int , input().split()))
    if len(command) == 3:
        c , n ,idx= command
        if c == 1:
            T[n] |= (1<<idx)
        elif c == 2:
            T[n] &= ~(1<<idx)
    else:
        c , n = command
        if c == 3:
            T[n] = T[n]<<1
            T[n] &= ~(1<<21)
        elif c == 4:
            T[n] = T[n]>>1
            T[n] &= ~(1<<0)
print(len(set(T[1:])))