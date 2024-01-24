'''
s지점에서 출발 => 최단거리로 이동
g와 h 교차로 사이에 있는 도로를 지나갔다는 정보를 알때
목적지가 어디인지 유추

'''


'''
문자열이 폭발 문자열 포함하는 경우 해당 문자열 폭발
남은 문자열을 순서대로 이어 붙여 새로운 문자열 만듬
더이상 폭발하지 않을때까지 최종 남은 문자열 출력
만약 남은 문자열이 없으면 "FRULA" 출력

처음에 문자열 주어지고
두번째에 폭발 문자열 주어짐(1보다 큼)
주어지는 문자열은 소문자, 대문자 숫자로만 이루어짐

'''
from collections import deque
S = list(input())
B = input().strip()
L = []
R = deque(S)
candidate = []


while R:
    if R[0] == B[0]:
        # 폭발 문자열인지 확인
        for i in range(len(B)):
            if len(R) and R[0] != B[i]: # R이 존재하지만, 다른 글자 발견한 경우
                # 현재 글자 추가 후 L에 붙힌뒤 후보 리스트 초기화 후 종료
                L+=candidate
                candidate.clear()
                break  
            else:
                if len(R): # R이 존재하고 계속 문자열이 일치하는경우
                    candidate.append(R.popleft())        
                else:
                    # R이 빈 경우, 폭발 문자열이 아니므로 그동안의 후보군 L에 더하고 초기화
                    L += candidate
                    candidate.clear()
                    break
        
        # 문자열 제거후 더 제거할 수 있는지 확인
        if len(candidate): # 폭발 문자열이 들어있음. => L의 맨 마지막 R로 이동
            candidate.clear()
            for _ in range(len(B)):
                if len(L):
                    R.appendleft(L.pop())
    else:
        L.append(R.popleft())
result = "".join(L)   
print(result) if len(result) else print("FRULA")
