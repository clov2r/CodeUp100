"""
6043:: 실수 2개(f1, f2)를 입력받아 f1 을 f2 로 나눈 값을 출력해보자.
소숫점 넷째자리에서 반올림하여 무조건 소숫점 셋째 자리까지 출력한다.
"""
f1=float(input())
f2=float(input())
result=f1/f2
print("%.3f"%result)
