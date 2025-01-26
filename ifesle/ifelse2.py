# 1. 비밀번호 유효성 검사
def validate_password(password):
    if len(password) < 8:
        return "비밀번호는 최소 8자 이상이어야 합니다."
    
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in "!@#$%^&*" for char in password)
    
    if not (has_upper and has_lower and has_digit and has_special):
        return "비밀번호는 대문자, 소문자, 숫자, 특수문자를 모두 포함해야 합니다."
    
    return "유효한 비밀번호입니다."

# 2. 계절 판별 프로그램
def get_season(month, day):
    if not (1 <= month <= 12 and 1 <= day <= 31):
        return "잘못된 날짜입니다."
    
    if (month == 3 and day >= 21) or (month == 4) or (month == 5) or (month == 6 and day < 21):
        return "봄"
    elif (month == 6 and day >= 21) or (month == 7) or (month == 8) or (month == 9 and day < 23):
        return "여름"
    elif (month == 9 and day >= 23) or (month == 10) or (month == 11) or (month == 12 and day < 21):
        return "가을"
    else:
        return "겨울"

# 3. 할인율 계산 프로그램
def calculate_discount(price, membership_level, is_birthday):
    discount = 0
    
    if membership_level == "VIP":
        discount = 0.2  # 20% 할인
    elif membership_level == "GOLD":
        discount = 0.15  # 15% 할인
    elif membership_level == "SILVER":
        discount = 0.1  # 10% 할인
    
    if is_birthday:
        # 생일인 경우 추가 10% 할인
        remaining_price = price * (1 - discount)
        birthday_discount = remaining_price * 0.1
        total_discount = (price * discount) + birthday_discount
    else:
        total_discount = price * discount
    
    final_price = price - total_discount
    return final_price

# 4. 파일 확장자에 따른 파일 종류 분류
def get_file_type(filename):
    if not isinstance(filename, str) or '.' not in filename:
        return "잘못된 파일명입니다."
    
    extension = filename.lower().split('.')[-1]
    
    if extension in ['jpg', 'jpeg', 'png', 'gif']:
        return "이미지 파일"
    elif extension in ['mp3', 'wav', 'flac']:
        return "음악 파일"
    elif extension in ['mp4', 'avi', 'mkv']:
        return "비디오 파일"
    elif extension in ['doc', 'docx', 'pdf', 'txt']:
        return "문서 파일"
    else:
        return "기타 파일"

# 예제 실행
if __name__ == "__main__":
    # 비밀번호 검사 예제
    print("\n1. 비밀번호 검사")
    test_password = input("비밀번호를 입력하세요: ")
    print(validate_password(test_password))
    
    # 계절 판별 예제
    print("\n2. 계절 판별")
    month = int(input("월을 입력하세요 (1-12): "))
    day = int(input("일을 입력하세요 (1-31): "))
    print(f"{month}월 {day}일은 {get_season(month, day)}입니다.")
    
    # 할인 계산 예제
    print("\n3. 할인 계산")
    price = float(input("가격을 입력하세요: "))
    membership = input("멤버십 등급을 입력하세요 (VIP/GOLD/SILVER): ").upper()
    is_birthday = input("생일인가요? (yes/no): ").lower() == 'yes'
    final_price = calculate_discount(price, membership, is_birthday)
    print(f"최종 가격: {final_price:,.0f}원")
    
    # 파일 종류 분류 예제
    print("\n4. 파일 종류 분류")
    filename = input("파일명을 입력하세요: ")
    print(f"파일 종류: {get_file_type(filename)}")
