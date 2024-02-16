'''
문제는 N개의 단어로 구성(알파벳 대문자)
알파벳 => 0~9 숫자로 변환 후 N개의 수 합 구하기
같은 알파벳은 같은 숫자 , 모두 고유한 숫자로
'''
N = int(input())
Q = []
for _ in range(N):
    Q.append(list(input().strip()))

word_dict = { chr(i):0 for i in range(ord("A") , ord("Z")+1)}
num = 9
for q in Q:
    for i in range(len(q)):
        word_dict[q[i]] += 10**(len(q)-i-1)
# 각 자리숫 별로 점수 매긴 것의 내림차순 정렬
priority = sorted(word_dict , key=lambda x : word_dict[x] , reverse=True)
alpha2num = {}
for i in priority:
    alpha2num[i] = num
    num -=1

# 계산
result = 0
for q in Q:
    s=""
    for ch in q:
        s+=str(alpha2num[ch])
    result += int(s)
    
print(result)
        
