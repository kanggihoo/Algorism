# 유클리드 호제법

# 최대공약수 GCD(greatest common divisor)를 빠르게 구하는 방법
# 재귀 반복문으로 구현 가능

def GCD_recur(a,b):
    if a%b ==0:
        return b
    return GCD_recur(b,a%b)

def GCD_loop(a,b):

    while(a%b !=0):
        a,b = b,a%b

    return b

print(GCD_loop(270 , 192))

