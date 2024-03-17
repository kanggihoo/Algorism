'''
그자체로 회문인지(0), 한 문자 삭제하면 회문인지(1), 둘다 아닌지(2)

'''
def check(S,cnt=0):
    L,R = 0,len(S)-1
    while L < R:
        if S[L] == S[R]:
            L+=1
            R-=1
        else:
            if cnt ==0:
                cnt +=1
                tmp = []
                if S[L+1] == S[R]:
                    case1 = check(S[L+1:R+1] , cnt)
                    tmp.append(case1)
                if S[L] == S[R-1]:
                    case2 = check(S[L:R] , cnt)
                    tmp.append(case2)
                if tmp:
                    return 1 if min(tmp) == 1 else 2 
                else:
                    return 2
            else:
                return 2
    return 0 if cnt == 0 else 1

                
        
T = int(input())
for _ in range(T):
    S = input().strip()
    ans = check(S)
    print(ans)
   
    