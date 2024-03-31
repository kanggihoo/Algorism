import sys
input = sys.stdin.readline

N , M = map(int , input().split())
# G = [[] for _ in range(N+1)]
E = []
for _ in range(M):
    A,B,C = map(int , input().split())
    E.append((A,B,C))
parents = [i for i in range(N+1)]

def find_p(n):
    if parents[n] !=n:
        parents[n] = find_p(parents[n])
    return parents[n]

def merge(a,b):
    p_a , p_b = find_p(a) , find_p(b)
    if p_a < p_b:
        parents[p_b] = p_a
    else:
        parents[p_b] = p_a

max_cost = 0
tcost = 0
E.sort(key= lambda x : -x[2])
while E:
    a,b,c = E.pop()
    pa , pb = find_p(a) , find_p(b)
    if pa != pb:
        merge(a,b)
        max_cost = max(max_cost , c)
        tcost += c
        # print(f"a:{a} , b:{b} , cost : {c}")
print(tcost - max_cost)