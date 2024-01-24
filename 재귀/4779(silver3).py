'''
칸토어 집합 : 0~1사이 실수 집합, [0,1] 구간을 3등분하여 가운데 구간을 제외
1. "-"가 3^N개 존재 (N:0~12)
2. 3등분 후 가운데 문자열 공백
3. 남은 - 부분을 다시 3등분 , 모든 선의 길이가 1일때까지
'''
# 문자열로 다루지 말고 1이면 - , 0이면 공백으로 생각하고
# 최종출력에서 - 출력되도록
import sys
sys.setrecursionlimit(100000)
def Kantor(string):
    # 중단
    if len(string) == 1:
        return string
    
    idx = len(string)//3
    S1 = string[:idx]
    S2 = string[idx:idx*2].replace("-" , " ")
    S3 = string[idx*2:]
    S1_ = Kantor(S1)
    S3_ = Kantor(S3)
    return S1_+S2+S3_
while 1:
    try:
        N = int(input())
        start = 0
        end = 3**N-1
        string = "-"*(3**N)
        print(Kantor(string))
    except:
        sys.exit()
        

    
    
    
    

