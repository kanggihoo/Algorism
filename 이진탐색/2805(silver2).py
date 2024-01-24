N , M = map(int , input().split())
Trees = list(map(int , input().split()))



def getTree(num):
    total =0
    for i in Trees:
        if i <=num:
            continue
        total +=(i-num)
    return total
        
start = 0
end = max(Trees)
mid = int((start+end)/2)
max_lenght = 0
while start <= end:
    mid = int((start+end)/2)
    gets = getTree(mid)
    if gets >= M:
        start = mid +1
    elif gets < M:
        end = mid -1
print(end)
    
    
    
        

    
        
    
    