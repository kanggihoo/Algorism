'''
가장 멀리 떨어져 있는 것은 맨 마지막에 처리 
= > 책 자리에 놓고 다시 0으로 복귀하지 않아도 되서


'''
N , M = map(int , input().split())
B = list(map(int , input().split()))
plus = [i for i in B if i > 0]
mius = [i for i in B if i < 0]
result = 0

if abs(min(B)) < abs(max(B)):
    # 왼쪽에서 부터 오른쪽
    if len(mius):
        mius.sort(reverse=True)
        if len(mius) > M:
            while len(mius) > M: 
                result +=abs(mius.pop())*2
                for _ in range(M-1):
                    mius.pop()
        if len(plus):            
            result += abs(mius[-1])*2
        else:
            result += abs(mius[-1])
    if len(plus):
        plus.sort()
        if len(plus) <= M:
            result += plus[-1]
        else:
            # 미리 마지막에 처리할 책 빼놓고
            result += plus.pop()
            for _ in range(M-1):
                plus.pop()
            
            if len(plus) > M:
                while len(plus) > M:
                    result += plus.pop()*2
                    for _ in range(M-1):
                        plus.pop()
            result += plus[-1]*2
else:
    # 오른쪽부터 시작 후 왼쪽을 마지막에 
    if len(plus):
        plus.sort()
        if len(plus) > M:
            while len(plus) > M:
                result += plus.pop()*2
                for _ in range(M-1):
                    plus.pop()
        if len(mius):
            result += plus[-1]*2
        else:
            result += plus[-1]
    if len(mius):
        mius.sort(reverse=True)
        if len(mius) <= M:
            result += abs(mius[-1])
        else:
            # 미리 책 빼놓기
            result += abs(mius.pop())
            for _ in range(M-1):
                mius.pop()
            if len(mius) > M:
                while len(mius) > M:
                    result += abs(mius.pop())*2
                    for _ in range(M-1):
                        mius.pop()
            result += abs(mius[-1])*2
print(result)
