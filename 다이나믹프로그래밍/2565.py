'''
전봇대 A와 B사이에 전깃줄을 추가 => 교차하는 전깃줄을 업고자함

전깃줄의 개수와 전깃줄들이 두 전봇대에 연결되는 위치의 번호가 주어질 때,
모든 전깃줄이 교차하지 않게 없애야 하는 전깃줄의 최소 개수 구하기

무조건 감소하거나 증가하는 형식 또는 - 자로 연결
'''
N = int(input())
CON = []
for _ in range(N):
    CON.append(list(map(int , input().split())))

CON.sort(key= lambda x :x[0]  )
D = [1 for _ in range(N)]
for i in range(1,N):
    for k in range(i):
        if CON[i][1] > CON[k][1]:
            D[i] = max(D[i] , D[k]+1)
print(N-max(D))