# 조건문
# 실행될 소스코드가 한 줄인 경우, 굳이 줄 바꿈 없이 표현 가능

x = 15
if x>=10:
    print(x)

score = 85
if score >= 90:
    print("학점: A")
elif score >= 80:
    print("학점: B")
elif score >= 70:
    print("학점: c")
else:
    print("학점: F")