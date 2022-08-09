# 문자열 자료형

# 1. 문자열 초기화
data = 'Hello World'
print(data)

data = '안녕"이라고 말하지마"'
print(data)

data = "민정이가 '뭐라하맨'"
print(data)

data = '혹시 그거 아니 \'파이썬\''
print(data)


# 2. 문자열 연산
a = "Hello"
b = "Wrold"
print(a+b)

a = "String"
print(a*3)

# 파이썬 문자열 = 내부적으로 리스트와 같이 처리
a = "ABCDEF"
print(a[2:4])