# 거의 소수 구하기
# 소수의 N제곱이 N>=2 이 A~B사이에 몇개 존재하는지 출력
# A,B의 범위가 10^14

# 소수 구하기
import math
A , B = map(int , input().split())
arr = [1]*(int(math.sqrt(B))+1)
arr[0] =0
arr[1] = 0


# 소수 찾기
for i in range(2,int(math.sqrt(B))+1):
    if arr[i] == 0:
        continue
    
    for j in range(i+i , len(arr) , i):
        arr[j] = 0
    

result = 0

# 소수의 N 제곱이 A,B사이인지 확인
for idx , i in enumerate(arr):
    if i !=0:
        tmp = idx*idx
        if tmp > B:
            break
        
        while(tmp <= B):
            if tmp >= A:
                result += 1
            tmp *= idx

print(result)

            
