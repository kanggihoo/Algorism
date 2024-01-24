'''
3kg, 5kg 추가하는 2가지 경우만 존재하며
이때 D[i-3] == -1 또는 D[i-5] 경우에는 존재할 수없으므로 
-1이 되는지 확인해야 한다.
이때 둘 중에 하나만 -1이면 min(D[i-3] , D[i-5]) = 무조건 -1이므로 주의
'''

N = int(input())
D = [-1 for _ in range(5000+1)]
D[3] = 1
D[5] = 1



for i in range(3,N+1):
    if D[i-3] == -1 and D[i-5] == -1:
        continue
    elif D[i-3] == -1:
        D[i] = D[i-5]+1
    elif D[i-5] == -1:
        D[i] = D[i-3]+1
    else:
        D[i] = min(D[i-3] , D[i-5]) +1
print(D[N])

    
        