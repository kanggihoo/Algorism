'''
사무실이 NxM 
총 K개의 CCTV (CCTV는 5종류 존재)
1. 한쪽 방향 감지 => 4방향 조절 가능
2. 양쪽 방향감지(방향 반대) => 2방향 조절
3. 양쪽 방향 감지(방향 수직) => 4방향
4. 3방향 감지  => 4방향
5. 4방향 감지
CCTV는 보는 방향의 전체 영역 탐지 가능(벽통과 못함)
CCTV 90도 회전만 가능, CCTV는 CCTV통과 가능
0: 빈칸 , 6:벽 1~5: CCTV 종류

CCTV 방향을 적절히 정해서 사각 지대의 최소 크기 계산
'''

# N , M = map(int , input().split())
# maps = []
# for _ in range(N):
#     maps.append(list(map(int , input().split())))
H , M = map(int , input().split())
if M >= 45:
    print(f"{H} {M-45}")
else:
    if H >=1:
        print(f"{H-1} {M-45+60}")
    else:
        print(f"{23} {M-45+60}")
