name = "철수"
age = 12

# 기본 변수 삽입
print(f"이름: {name}, 나이: {age}")  # 이름: 철수, 나이: 12

# 수학 연산
a, b = 5, 3
print(f"{a} + {b} = {a + b}")       # 5 + 3 = 8

# 함수 호출
def greet():
    return "안녕하세요"
print(f"{greet()}!")                # 안녕하세요!

# 딕셔너리 키 접근
user = {"name": "영희", "age": 10}
print(f"이름: {user['name']}, 나이: {user['age']}")  # 이름: 영희, 나이: 10


# 소수점 둘째 자리까지
pi = 3.141592
print(f"원주율: {pi:.2f}")  # 원주율: 3.14

# 천 단위 구분 기호
number = 1000000
print(f"금액: {number:,}원")  # 금액: 1,000,000원

# 날짜 형식
from datetime import datetime
now = datetime.now()
print(f"현재 시간: {now:%Y-%m-%d %H:%M:%S}")  # 현재 시간: 2024-07-22 15:30:00

# 진법 변환
num = 255
print(f"16진수: {num:#x}")   # 16진수: 0xff
print(f"2진수: {num:b}")     # 2진수: 11111111

# 정렬 및 공백 채우기
text = "Python"
print(f"왼쪽 정렬: {text:<10}!")  # 왼쪽 정렬: Python    !
print(f"오른쪽 정렬: {text:>10}!") # 오른쪽 정렬:     Python!
print(f"가운데 정렬: {text:^10}!") # 가운데 정렬:  Python  !
