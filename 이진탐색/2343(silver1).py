'''
블루레이에는 총 N개의 강의 몇 녹화 순서 변경안됨
블루레이의 개수는 최대한 줄이기
M개의 블루레이 제작(이때 블루레이 크기는 최소지만 M개의 블루레이는 모두 같은 크기)
각 강의는 분단위(자연수), 가능한 블루레이 크기 중 최소
'''


# N개의 강의 , M개의 블루레이

N , M = map(int , input().split())
lecture_lenght = list(map(int , input().split()))
start = max(lecture_lenght)
end = sum(lecture_lenght)
result = end


        
        
def is_vaild(x , lecture_lenght):
    record = 0
    acc_sum = 0
    for i in lecture_lenght:
        if acc_sum+i > x:
             acc_sum = 0
             record +=1
        acc_sum +=i
        if record >= M and acc_sum > 0:
            return False
    return True
        

while start <= end:
    mid = (start+end)//2
    
    if is_vaild(mid,lecture_lenght):
        end = mid -1
        result = mid
    else:
        start = mid+1
print(start , end ,mid , result)

    
            
        
    
