# 집합 자료형
# 리스트 or 문자열 이용해 만듦

# 집합 특징
# 1. 중복을 허용하지 않음
# 2. 순서가 없음 (리스트or튜플은 순서 있음)

# 1-1. 초기화 방법1
data = set([1,1,2,3,4,4,5])
print(data)

# 1-2. 초기화 방법2
data = {1,1,2,3,4,4,5}
print(data)


# 2. 집합 자료형의 연산
# 합집합(|), 교집합(&), 차집합(-)
a = set([1,2,3,4,5])
b = set([3,4,5,6,7])

print(a|b)  # 합집합
print(a&b)  # 교집합
print(a-b)  # 차집합


# 3. 집합 자료형 관련 함수
data = set([1,2,3])
print(data)

#새로운 원소 추가
data.add(4)
print(data)

#새로운 우너소 여러 개 추가
data.update([5,6])
print(data)

# 특정한 값을 갖는 원소 삭제
data.remove(3)
print(data)