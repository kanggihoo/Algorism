'''
영어 소문자만 기록 편집기 
커서는 문장 맨앞, 맨뒤, 문장 임의의 중간 위치 가능
L : 왼쪽이동(맨 앞이면 무시)
D : 오른쪽(맨 뒤면 무시)
B : 커서 왼쪽 문자 삭제(맨 앞으면 무시)
P $ : $문자를 커서 왼쪽에 추가
문자열 ㅈ어지고, 명령어가 주어졌을 때 최종 편집기의 문자열 구하라
초기에 커서는 문장의 맨 뒤에 위치
'''
'''
리스트의 pop() , insert()로 계산하면 시간초과 발생
따라서 cursor를 기준으로 left는 리스트, right는 deque()로 선언하여
매 명령마다 left, right 자료구조를 append , pop 연산을 통해 동작후
맨 마지막에 left와 right를 합친다.
'''
import sys
from collections import deque
input = sys.stdin.readline
string = list(input().rstrip())
M = int(input())
commands = []
for _ in range(M):
    commands.append(input())
left = string.copy()
right = deque()

for C in commands:
    if C[0] == "L":
        if len(left):
            right.appendleft(left.pop())
    elif C[0] == "D":
        if len(right):
            left.append(right.popleft())
    elif C[0] =="B":  
        if len(left):
            left.pop()
    elif C[0] =="P":
        c = C.split()[1]
        left.append(c)

while len(right):
    left.append(right.popleft())
print("".join(left))

        
    
    
