# 삼항 연산자
"""
print('참' if True else '거짓')
print('참' if False else '거짓')
"""
# 사용자로 부터 두 개의 정수를 입력 받고, 큰수/작은수를 구분해 출력
a = int(input("정수 입력: "))
b = int(input("정수 입력: "))

big = a if a > b else b
small = a if a < b else b

print(
    f"""
큰수: {big}
작은수: {small}
"""
)

# if문

# 점수에 따른 학점 부여
# - 90점 이상 A
# - 80점 이상 B
# - 70점 이상 C
# - 60점 이상 D
# - 60점 미만 F

score = int(input("점수를 입력해 주세요: "))
if 90 <= score <= 100:
    print("A학점 입니다.")
elif 80 <= score < 90:
    print("B학점 입니다.")
elif 70 <= score < 80:
    print("C학점 입니다.")
elif 60 <= score < 70:
    print("D학점 입니다.")
elif 0 <= score < 60:
    print("F학점 입니다.")
else:
    print("점수를 잘못 입력하셨습니다. 0~100점 사이의 점수를 입력해 주세")

# for..in 문
name = "홍길동"
for ch in name:
    print(ch)

for char in "apple":
    print(char)

# range 객체
# - range(start, end, step)
# 반복횟수와 범위

range(1, 11)

for n in range(1, 11):
    print(n)

print()

# 1~100 사이의 숫자 중 짝수만 출력

for g in range(2, 101, 2):
    print(g, end="")

print()

for k in range(2, 101):
    if k % 2 == 0:
        print(k, end=" ")

print()

# match..case 문
# 사용자로부터 두 정수와 연산자를 입력받고 결과를 출력하세요.
# 10 3 입력시 13 출력
a = int(input("정수1 입력: "))
b = int(input("정수2 입력: "))
operand = input("연산자 입력 (+ - * / // %): ")

match operand:
    case "+":
        result = a + b
    case "-":
        result = a - b
    case "*":
        result = a * b
    case "/":
        result = a / b
    case "//":
        result = a // b
    case "%":
        result = a % b
    case _:
        raise ValueError("잘못된 연산자를 입력하셨습니다.")

print(f"{a} {operand} {b} = {result}")

# raise 함수(정확히는 키워드)는 Python에서 예외(Exception)를 발생시키는 데 사용됩니다.
# 즉, 프로그램이 특정 조건에서 “이건 오류 상황이야!”라고 명시적으로 알려주고 싶을 때 쓰는 문법이에요.

# while 문

i = 0  # 초기식

while i < 10:  # 조건식
    print("🐯")
    i += 1  # 증감식

j = 0
while True:
    print("🍡")
    j += 1

    if j >= 3:
        break  # 현재 반복문을 즉시 중지

# 메뉴 선택 예제

menu = """
--------------------------------------
SK Network 구내식당
--------------------------------------
1. 된장찌개---8000원
2. 김치찌개---8500원
3. 청국장---9000원
0. 종료
--------------------------------------
"""
# hint:
"""
1. 사용자가 고른 메뉴 이름을 리스트로 저장
2. 지금까지 선택한 메뉴의 총 금액을 누적
3. 무한 반복문
4. 메뉴 출력 및 사용자 입력
5. match-case 문
6. 반복 종료 후 결과 출력
"""

# # 1. 사용자가 고른 메뉴 이름을 리스트로 저장
# menu = []

# # 2. 지금까지 선택한 메뉴의 총 금액을 누적
# total_price = 0

# # 3. 무한 반복문
# while True:

# # 4. 메뉴 출력 및 사용자 입력
#     print(menu)
#     choice = input('선택하세요: ')
#     print(choice)

# # 5. match-case 문
# match choice:
#     case '1':
#         menus.append('된장찌개')
#         total_price += 8000
#     case '2':
#         menus.append('김치찌개')
#         total_price += 8500
#     case '3':
#         menus.append('청국장')
#         total_price += 9000
#     case '0':
#         break
#     case _:
#         print('잘못 입력하셨습니다.')

# # 6. 반복 종료 후 결과 출력
# print(f'{menus =}')
# print(f'결제할 금액은 {total_price}원 입니다.')

# menus = []
# total_price = 0

while True:
    print(menu)
    choice = input("선택하세요: ")
    print(choice)

    match choice:
        case "1":
            menus.append("된장찌개")
            total_price += 8000
        case "2":
            menus.append("김치찌개")
            total_price += 8500
        case "3":
            menus.append("청국장")
            total_price += 9000
        case "0":
            break
        case _:
            print("잘못 입력하셨습니다.")

print(f"{menus = }")
print(f"결제할 금액은 {total_price}원 입니다.")

# 컴프리헨션(내포)부분은 다시 한번 봐야 함

# 실습 문제
# 1번 문제
""" 
두 학생이 수강한 과목이 다음과 같을 때,

```python
student1 = {"Python", "Math", "English"}
student2 = {"Python", "Biology", "English"}

```

1. 두 학생이 모두 듣는 과목은?
2. 두 학생 중 한 명만 듣는 과목은?
3. 두 학생이 듣는 전체 과목 목록은?

*힌트:* `intersection()`, `symmetric_difference()`, `union()` 메서드를 사용해보자.
"""

# 1번 문제 hint:
"""
print(f'합집합: {a.union(b)}')
print(f'교집합: {a.intersection(b)}')
print(f'차집합(a-b): {a.difference(b)}')
print(f'차집합(b-a): {b.difference(a)}')
print(f'대칭차집합: {a.symmetric_difference(b)}') # 합집합 - 교집합
"""
student1 = {"Python", "Math", "English"}
student2 = {"Python", "Biology", "English"}

# 1.
print(f"두 학생이 모두 듣는 과목은? {student1.intersection(student2)}")

# 2.
print(f"두 학생 중 한 명만 듣는 과목: {student1.difference(student2)}")

# 3.
print(f"두 학생이 듣는 전체 과목 목록: {student1.union(student2)}")

# 2번 문제
"""
- 요구사항 :
    - 키(cm)와 몸무게(kg)을 입력 받고, BMI(체질량지수)를 계산하여 계산된 값에 따라
        - 저체중(18.5미만),
        - 정상체중(18.5이상 23미만),
        - 과체중(23이상 25미만),
        - 비만(25이상 30미만),
        - 고도비만(30이상)을 출력하세요.
    
    <aside>
    💡 BMI 계산식 = 체중(kg) / (신장(m) * 신장(m) )
    
    </aside>
    
- 출력예시
    
    ```
    체중입력(kg) : 67
    신장입력(cm) : 172
    --------------------------
    BMI 지수 : 22.64
    정상체중입니다.
    ```
"""
# 체중과 키 입력
weight = float(input("체중입력(kg): "))
height = float(input("신장입력(cm): "))

# cm -> m 단위로 변환
height_m = height / 100

# BMI 계산
bmi = weight / (height_m**2)

print("-----------------------------")
print(f"BMI 지수: {bmi: .2f}")

# BMI 기준에 따른 결과 출력
if bmi < 18.8:
    print("저체중입니다.")
elif bmi < 23:
    print("정상체중입니다.")
elif bmi < 25:
    print("과체중입니다.")
elif bmi < 30:
    print("비만입니다.")
else:
    print("고도비만입니다.")


# 3번 문제 나중에 다시 풀 것!
