# ATM기기앞에 1~N명이 줄서있음.
# i번 사람이 인출하는데 걸리는 시간 P_i분
# 



N = int(input())
time = list(map(int , input().split()))


# 기다리는 시간이 최소가 되려면 오름차순으로 정렬 하고 누적합을 구한다.

time.sort()

for i in range(1,N):
    time[i] += time[i-1]
print(sum(time))