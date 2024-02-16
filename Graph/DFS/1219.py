'''

1219번
맨 뒤에 A이면 제거 후 다음 동작 또는 맨 앞에 B이면 B제거 후 뒤집은 후 
다음동작 
처음 길이와 동일할때 둘이 같으면 1, 다르면 0
'''

def dfs(S,target):
    if len(target) == len(S):
        if target == S:
            return 1
        else:
            return 0
    result = 0
    if S[-1] =="A":
        result += dfs(S[:-1],target)
    if S[0] =="B":
        result += dfs(S[1:][::-1] , target)

    return result
T = input().strip()
S = input().strip()
if dfs(S , T):
    print(1)
else:
    print(0)