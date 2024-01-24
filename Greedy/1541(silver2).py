# 양수와 + , - , ()를 이용하여 만든 식에서 ()를 모두 지움
# 그리고 다시 괄호를 적절히 쳐서 최소가 되도록 만드는 프로그램

# 첫째줄에 식은 0~9 , + , - (가장 처음 마지막은 숫자 , 연속해서 연산자 나오지 않고, 수는 0으로 시작 가능)


EQ = input()
result = 0
start = 0
end = 0

while(start <= len(EQ)-1):
    if EQ[start] !='+' and EQ[start] !='-' : 
        while(EQ[end] !='+' and EQ[end] !='-' and end < len(EQ)-1):
            end +=1
        num = int(EQ[start:end])
        start = end+1
        end +=1
        print(num)
        
    


# for idx , char in enumerate(EQ):
#     if char =='-' or char =='+':
#         num = int(EQ[])
#         if char =='-':
#             if first_sub_sign==False:
#                 first_sub_sign = True
#             else:
#                 fisrt_sub_sign = False
#                 ## 지금까지 수 모두 더하기
        
#         elif char == '+':
#             if fisrt_sub_sign == True:
#                 pass
                
#     else:
#         start +=1
            
        
        
        


    
