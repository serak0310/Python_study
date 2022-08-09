# 리스트 자료형

# 1. 리스트 만들기
a = [1,2,3,4,5,6]
print(a)

print(a[4])

# 빈 리스트 생성
a =list()
print(a)

a = []
print(a)

# 크기가 N이고 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0]*n
print(a)


# 2. 인덱싱 & 슬라이싱
a = [1,2,3,4,5,6]
print(a[-1])    # 뒤에서 첫 번째 원소 출력
print(a[-3])    # 뒤에서 세 번째 원소 출력

print(a[1:4])   # 두 번째 원소부터 네 번재 원소까지


# 3. 컴프리헨션(리스트 초기화)
# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]
print(array)

# == 
array = []
for i in range(20):
    if i % 2 == 1:
        array.append(i)
print(array)

# 1부터 9까지의 수의 제곱 값을 포함하는 리스트
array = [i*i for i in range(1,10)]
print(array)

# N X M 크기의 2차원 리스트 초기화
n = 3
m = 4
array = [[0]*m for _ in range(n)]
print(array)

# N X M 크기의 2차원 리스트 초기화(잘못된 방법)
# 내부적으로 포홤된 3개의 리스트가 모두 동일한 객체에 대한 3개의 레퍼런스로 인식되기 때문.
n = 3
m = 4
array = [[0]*m]*n
print(array)

array[1][1] = 5
print(array)


# 4. 기타 메소드
a = [1,4,3]
print("기본 리스트: ", a)

# 리스트에 원소 삽입
a.append(2)
print("삽입: ", a)

# 오름차순 정렬
a.sort()
print("오름차순 정렬: ", a)

# 내림차순 정렬
a.sort(reverse=True)
print("내림차순 정렬: ", a)

# 리스트 원소 뒤집기
a.reverse
print("원소 뒤집기: ", a)

# 특정 인덱스에 데이터 추가
a.insert(2,3)
print("인덱스 2에 3 추가: ", a)

# 특정 값인 데이터 개수 세기
print("값이 3인 데이터 개수: ", a.count(3))

# 특정 값 데이터 삭제
a.remove(1)
print("값이 1인 데이터 삭제: ", a)

# 시간 복잡도를 고려한 remove
a = [1,2,3,4,5,5,5]
remove_set={3,5}

# remove_set에 포함되지 않은 값만을 저장
result = [i for i in a if i not in remove_set]
print(result)