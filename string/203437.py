from collections import defaultdict
T = int(input())
for _ in range(T):
    cnt = defaultdict(int)
    S = input().strip()
    K = int(input())
    L, R = 0,0
    min_len = len(S)
    while R < len(S):
        cur_max= max(cnt.values()) if len(cnt)  else 0 
        if cur_max < K:
            cnt[S[R]] +=1
            R+=1
        elif cur_max == K:
            min_len = min(min_len , R-L)
            cnt[S[L]]-=1
            L+=1
    
    print(min_len)
        
            