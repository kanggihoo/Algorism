N = int(input())
values = []
for _ in range(N):
    S,B = map(int, input().split())
    values.append((S,B))
ans = 1e10
for i in range(1,2**N):
    s,b = 1,0
    for j in range(N):
        if i & (1<<j):
            s *=values[j][0]
            b += values[j][1]
    ans = min(ans , abs(s-b))
print(ans)