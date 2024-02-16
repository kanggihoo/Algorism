'''
하루에 1개 과제 끝내기 가능
과제를 끝낼때마다 점수 얻음
마감일이 지나면 못얻음
가장 점수 많이 받도록 과제

N 개 입력
d , w : d는 과제 마감일까지 남은 일수 , w는 과제 점수

=> 가장 큰 보상을 가진것을 해당 날자에 마무리 하도록 하고
만약 해당 날짜에 하기로 한 일이 정해져 있다면 -1씩 감소하여
가능한 위치를 찾는다. 이때 없다면 해당 과제는 할 수 없는 경우 


'''
import sys
import heapq

input = sys.stdin.readline
N = int(input()) 
works = []
max_day = 0
for _ in range(N):
    d , w = map(int , input().split())
    if max_day < d:
        max_day = d
    works.append((d,w))

works.sort(key = lambda x : (-x[1],x[0]) ) # 보상이 큰 것별로 내림차순 정렬
visited = [False]*(max_day+1) # 방문 여부 확인
reward = 0
for w in works: 
    d , r = w
    if not visited[d]: 
        visited[d] = True
        reward += r
    else:
        i = d
        while i > 0 and visited[i]: # 자리가 차 있는 경우 1씩 감소
            i-=1
        # i ==0 인 경우는 빈자리 못찾은 경우 
        if i ==0:
            continue
        else:
            visited[i] = True
            reward +=r
print(reward)

