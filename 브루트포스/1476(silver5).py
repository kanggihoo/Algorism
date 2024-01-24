# 3개의 수를 이용해서 연도 표현(지구, 태양 ,달)

# (1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19)
# 해당 범위 넘어가면 초기화

total = 1
E, S, M = map(int , input().split())
e,s,m = (1,1,1)
while(not(e==E and s ==S and m==M)):
    e+=1
    s+=1
    m+=1
    total+=1
    if e > 15:
        e = 1
    if s > 28:
        s = 1
    if m > 19:
        m = 1
print(total)