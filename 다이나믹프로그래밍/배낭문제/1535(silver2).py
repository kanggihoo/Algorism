'''
N명의 사람 (1~N)
i번 사람에게 인사하면 체력을 읽고L  기쁨을 얻는다J.(중복 안됨)
주어진 체력내에서 최대한의 기쁨을 느끼는 것(체력이 0 이나 음수가 되면 더이상 기쁨 못느낌)
처음 체력은 100, 기쁨은 0

'''
N = int(input())
L = list(map(int , input().split()))
J = list(map(int , input().split()))

D = [[0]*101 for _ in range(N+1)]

for idx in range(N):
    for h in range(1,100+1):
        if L[idx] > h:
            D[idx][h] = D[idx-1][h]
        else:
            D[idx][h] = max(D[idx-1][h] , D[idx][h-L[idx]]+J[idx])
print(D[N-1][100])