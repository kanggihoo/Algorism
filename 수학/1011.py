'''
이전에 k광년 이동시 -> k-1 , k , k+1 광년 다시 이동
맨 처음에는 1광년 이동 => 그 다음에는 0,1,2 광년 이동 => (1,2,3) 가능

x -> y 지점이동시 최소한의 작동 횟수로 이동 (y지점 독차전에는 반드시 y-1을 지나야함)
x < y 무조건 만족 

참고 : https://phil-baek.tistory.com/entry/%EB%B0%B1%EC%A4%80-1011-Fly-me-to-the-Alpha-Centauri-%ED%92%80%EC%9D%B4-C
'''
import sys 
input = sys.stdin.readline
T = int(input())
result = []
for _ in range(T):
    x , y = map(int , input().split())
    n = 1
    distance = y-x
    min_value = 1
    while 1:
        step_value = min_value
        if n**2 <= distance <= (n+1)**2:
            mid = (n**2+(n+1)**2)//2
            if distance == n**2:
                print(step_value)
            elif distance <= mid:
                print(step_value+1)
            else:
                print(step_value+2)
            break
        else:
            n+=1
            min_value += 2
