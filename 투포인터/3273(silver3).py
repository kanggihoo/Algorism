'''
서로 다른 양의 정수 n개의 수열에서 
자연수 x가 주어지면 a_i + a_j = x인 모든 쌍의 수를 구하라
이때 i < j 만족

'''

N = int(input())
arr = list(map(int , input().split()))
X = int(input())
result = 0
start = 0 
end = len(arr)-1
arr.sort()


while start < end:
    tmp = arr[start] + arr[end]
    
    if tmp < X:
        start +=1
    elif tmp > X:
        end -=1
    # elif tmp == X:
    else:

        start += 1
        end -=1   
        result+=1

print(result)
    
        
        

