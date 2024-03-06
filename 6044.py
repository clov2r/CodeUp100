"""
6044::정수 2개 입력받아 자동 계산하기
정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산해보자.
단, b는 0이 아니다.
"""
a = int(input())
b = int(input())
result= a+b
result1= a-b
result2= a*b
result3= a//b
result4= a%b
print(result, result1, result2, result3, result4)

# 나눈 값을 구하는 방법
# result5 = a/b
