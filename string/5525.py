import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
S = input().strip()
idx = 0
cnt = 0
while idx < M:
    if idx + 2*N >= M:
        break
    if S[idx] == "I":
        subs = 1
        R = 0
        while idx+R+1 < M:
            R+=1
            if R %2==0 and S[R+idx] == "I":
                subs += 1
            elif R %2==1 and S[R+idx] == "O":
                subs += 1
            else:
                break
        # print(R,idx,subs)
        if subs >= 2*N+1:
            cnt += ((subs-(2*N+1)) //2 +1)
        idx += R          
    else:
        idx+=1
print(cnt)