# 1. 간단한 if-else문 - 성인/미성년자 구분
input_age = input("나이를 입력하세요: ")
if int(input_age) >= 20:
    print("성인입니다.")
else:
    print("미성년자입니다.")

# 2. if-elif-else문 - 학점 계산
input_score = input("점수를 입력하세요: ")
if int(input_score) >= 90:
    print("A 학점")
elif int(input_score) >= 80:
    print("B 학점")
elif int(input_score) >= 70:
    print("C 학점")
else:
    print("F 학점")

# 3. 중첩 if문 - 숫자 양수/음수/0 구분
input_number = input("숫자를 입력하세요: ")
if int(input_number) != 0:
    if int(input_number) > 0:
        print("양수입니다.")
    else:
        print("음수입니다.")
else:
    print("0입니다.")

# 4. and/or 연산자를 사용한 if문
input_age = input("나이를 입력하세요: ")
input_has_id = input("신분증이 있나요? (True/False): ")

if int(input_age) >= 20 and input_has_id == "True":
    print("술을 구매할 수 있습니다.")
else:
    print("술을 구매할 수 없습니다.")