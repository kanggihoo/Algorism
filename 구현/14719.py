'''
세로 : H , 가로 : W
블록이 쌓인 높이 0~H가 맨 왼쪽위치부터 차례때로 W개 주어짐 

'''

H, W = map(int , input().split())
B = list(map(int , input().split()))

# 물이 고이기위해서는 특정 지점의 왼,오른쪽 블록 보다 작은경우
result = 0
for i in range(1,len(B)-1):
    left_max = max(B[:i])
    right_max = max(B[i+1:])
    
    if left_max > B[i] and B[i] < right_max:
        min_value = min(left_max , right_max)
        result += min_value-B[i]
print(result)
    
        
            
        
            
