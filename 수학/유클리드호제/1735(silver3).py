import math

num1_T , num1_B = map(int , input().split())
num2_T , num2_B = map(int , input().split())
sum_B = None
sum_T = None

if num1_B == num2_B:
    sum_B = num1_B
    sum_T = num1_T + num2_T 
else:
    sum_T = num1_T*num2_B + num2_T*num1_B
    sum_B = num2_B*num1_B
    
gcd = math.gcd(sum_B , sum_T)
print(sum_T//gcd , sum_B//gcd)



