'''
N개의 단어(대문자)
각 알파벳을 0~9 숫자로 변경 후 모두 더하는 문제
 - 같은 알파벳은 같은 숫자로
 - 알파벳 다르면 다른 숫자로 매핑

N개의 단어가 주어질때 그 수의 합을 최대로 
'''


'''
맨 앞자리 숫자가 커야 하고 

매핑 테이블만 올바르게 만들면 계산은 쉬운데

1. 알파벳 갯수 확인
2. 문자 개수 길이가 긴 순으로 정렬
3. 그리고 다음 긴 문자와 길이가 같아질때까지 문자에 대해 숫자 배정
4. 길이가 같아지면 같은것끼리 순서대로 숫자 배정 
'''