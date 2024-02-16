'''
4개의 기호를 이용해 만들어지는 괄호 열 중 올바른 괄호열
() [] 

올바른 괄호열 x에 대해 그 괄오형의 값을 아래와 같이 정의
‘()’ 인 괄호열의 값은 2이다.
‘[]’ 인 괄호열의 값은 3이다.
‘(X)’ 의 괄호값은 2×값(X) 으로 계산된다.
‘[X]’ 의 괄호값은 3×값(X) 으로 계산된다.
올바른 괄호열 X와 Y가 결합된 XY의 괄호값은 값(XY)= 값(X)+값(Y) 로 계산된다.

올바르지 못한 괄호열은 0을 출력
'''

S= input().strip()
# 일단
result = 0
value = 1
stack = []
isAns = True
for idx , s in enumerate(S):
    if s =="(" or s=="[":
        stack.append(s)
        value = value*3 if s =="[" else value*2
    else:
        if not len(stack):
            isAns = False
            break
        elif len(stack) :
            if s ==")" and stack[-1] =="(": 
                if S[idx-1] == "(":
                    result += value  
                stack.pop()
                value //=2
            elif s =="]" and stack[-1] == "[":
                if S[idx-1] == "[":
                    result += value  
                stack.pop()
                value //=3    
            else:
                isAns = False
                break
            
if len(stack) == 0 and isAns:
    print(result)
else:
    print(0)        