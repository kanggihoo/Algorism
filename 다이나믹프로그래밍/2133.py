# https://yabmoons.tistory.com/536/
N = int(input())
D = [1 if i %2 ==0 else 0 for i in range(30+1)]
D[2] = 3
for i in range(4,30+1):
    
    idx = i-4
    tmp = 0
    while idx >=0:
        tmp += (D[idx]*2)
        idx -=2
    D[i] = D[i-2]*D[2] +tmp
print(D[N])