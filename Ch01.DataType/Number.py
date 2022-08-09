# 수 자료형

# 1. 정수형
a = 1000 # 양의 정수
print(a)

a = -7 # 음의 정수
print(a)

# 0
a = 0
print(a)


# 2. 실수형
a = 157.93  # 양의 실수
print(a)

a = -189.2  # 음의 실수
print(a)

a = 5.  # 소수부가 0일 때 0을 생략
print(a)

a = -.7 # 정수부가 0일 때 0을 생략
print(a)


# 3. 지수 표현방식
a = 1e9 # 10억의 지수 표현 방식
print(a)

a = 75.25e1 #752.5
print(a)

a = 3954e-3 # 3.954
print(a)


# 4. 컴퓨터의 실수 표현 한계
a = 0.3 + 0.6
print(a)

if a==0.9:
    print(True)
else:
    print(False)


# 5. round()
a = 0.3 + 0.6
print(round(a,4))

if round(a,4)==0.9:
    print(True)
else:
    print(False)

# 6. 수 자료형 연산
a = 7
b = 3

# 나누기
print(a/b)  # 2.33333

# 나머지
print(a%b)  # 1

# 몫
print(a//b) # 2

# 거듭제곱
print(a**b) # 343