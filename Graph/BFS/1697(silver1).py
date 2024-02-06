'''
숨박꼭질
N에서 출발하여 다음 위치로 N-1 , N+1 , N*2로 이동가능
이때 각 이동하는데 걸리는 시간은 1이며 K까지 도착하는데
걸리는 최소 시간 구하시오

'''


from collections import deque
N , M = map(int , input().split())
Q = deque()
Q.append((N,0))
distance = [1e6]*(100001)
distance[N] = 0
while Q:
    
    cur , time = Q.popleft()
    if cur == M:
        print(time)
        break
    next_P = [ cur*2, cur +1 , cur-1]
    for i in next_P:
        if i >=0 and i<=100000 and distance[i] == 1e6:
            distance[i] = time+1
            Q.append((i,time+1))
        