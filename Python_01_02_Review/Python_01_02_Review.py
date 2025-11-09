# _02_datatype 
# 01_number.ipynb

import math

# 실습문제 (2025/10/30)
"""
1. 주어진 실수 3.6을 올림한 결과를 출력하세요.
2. 주어진 실수 4.2를 내림한 결과를 출력하세요.
3. 주어진 실수 5.5를 반올림한 결과를 출력하세요.
4. 주어진 실수 -2.8을 올림한 결과를 출력하세요.
5. 주어진 실수 -3.9를 내림한 결과를 출력하세요.
6. 주어진 실수 -6.5를 반올림한 결과를 출력하세요.
7. 실수 3.14159를 소수점 둘째 자리까지 반올림한 결과를 출력하세요.
8. 실수 7.25를 올림해서 소수점 첫번째 자리까지 결과를 출력하세요.
9. 실수 -7.999를 버림한 결과를 출력하세요
10. 실수 123.456789를 소수점 셋째 자리까지 반올림한 결과를 출력하세요.
"""

# round(): 가장 가까운 정수로 반올림 합니다. # 반올림
# math.ceil(): 주어진 수보다 크거나 같은 가장 작은 정수로 올림합니다. # 올림
# math.floor(): 주어진 수보다 작거나 같은 가장 큰 정수를 반환합니다. # 내림
# math.trunc(): 소수점 이하를 버림(truncate) 합니다. (즉, 0쪽으로 버림) # 소수점 버림

# 1. 
print("주어진 실수 3.6을 올림한 결과를 출력하세요.")
print(math.ceil(3.6))

# 2. 
print("주어진 실수 4.2를 내림한 결과를 출력하세요.")
print(math.floor(4.2))

# 3. 
print("주어진 실수 5.5를 반올림한 결과를 출력하세요.")
print(round(5.5))

# 4. 
print("주어진 실수 -2.8을 올림한 결과를 출력하세요.")
print(math.ceil(-2.8))

# 5. 
print("주어진 실수 -3.9를 내림한 결과를 출력하세요.")
print(math.floor(-3.9))

# 6. 
print("주어진 실수 -6.5를 반올림한 결과를 출력하세요.")
print(round(-6.5))

# 7. 
print("실수 3.14159를 소수점 둘째 자리까지 반올림한 결과를 출력하세요.")
print(round(3.14159,2))

# 8. 
print("실수 7.25를 올림해서 소수점 첫번째 자리까지 결과를 출력하세요.")
print(math.ceil(7.25),1)

# 9. 
print("실수 -7.999를 버림한 결과를 출력하세요")
print(math.trunc(-7.999))

# 10. 
print("실수 123.456789를 소수점 셋째 자리까지 반올림한 결과를 출력하세요.")
print(round(123.456789,3))


# 04_str.ipynb

# str.replace(): 문자열 안에서 특정 문자를 다른 문자로 바꾸는 함수예요.
# str.strip(): 문자열의 양쪽 끝 공백이나 특정 문자를 제거합니다.

"""
upper(): 모든 알파벳을 대문자로 바꿈
lower(): 모든 알파벳을 소문자로 바꿈
capitalize(): 문장의 첫 글자만 대문자로 바꿈
swapcase(): 대문자는 소문자로, 소문자는 대문자로 바꿈
title(): 단어의 첫 글자만 대문자
"""

# 05_list.ipynb

# str.split(구분자): 문자열을 구분자 기준으로 나누어 리스트로 반환합니다.
# list.index(): 리스트에서 특정 값의 위치(인덱스) 를 반환합니다.
# list.count(value): 리스트 안에서 특정 값이 몇 번 등장하는지 세어줍니다.
# list.sort(): 리스트를 정렬(오름차순/내림차순) 합니다.
"""
리스트.sort(reverse=False)
reverse=False → 오름차순 (기본값)

reverse=True → 내림차순
"""
# (built-in) sorted(): 정렬된 새 리스트를 반환합니다. (원본은 그대로 유지)


# 07_dict.ipynb

# value = dict1.pop('a') # 요소꺼내기 (pop())
# zip(): 두개 이상의 리스트의 요소를 묶어서 처리

# 실습문제 (2025/10/31)
import math

# 01.  
"""
어떤 실수가 주어졌을 때, 이 수를  
- 첫째 자리에서 반올림한 정수  
- 올림한 정수  
- 버림한 정수  
를 출력하는 프로그램을 작성하시오.  
```python
# 예시 입력: 3.14  
# 예시 출력: 3 (반올림), 4 (올림), 3 (버림)
"""

x1 = float(input("실수 입력:" ))
print(round(x1)) 
print(math.ceil(x1))
print(math.floor(x1))

# 02.
"""
사용자로부터 두 개의 숫자를 입력받아, 두 숫자가 같은지 비교하고 결과를 출력하시오.  
```python
# 예시 입력: 5, 5  
# 예시 출력: True
```
"""

x2 = int(input("정수1 입력: "))
x3 = int(input("정수2 입력: "))

print(x2 == x3)

# 03. 
"""
정수 x가 10 이상이고 100 이하인지 판단하여 `True` 또는 `False`를 출력하시오.  
힌트: and 연산자 사용

---
"""

x4 = int(input("정수 입력: "))
print(10<=x4 and x4<=100)

# 04. 
"""
0 에서 1 사이의 실수 하나를 입력받아, 소수점 이하가 0.5 이상이면 True를, 그렇지 않으면 False를 출력하시오.  
힌트: `round()`, 비교연산자 사용
"""

x5 = float(input("0에서 1사이의 실수 입력: "))
print((round(x5)) >= 0.5)

# 05.
"""
사용자로부터 실수 하나를 입력받아 다음 조건을 모두 만족하는지 확인하라:  
- 소수점 첫째자리에서 올림한 값이 10보다 작다.  
- 소수점 이하를 버린 값이 5 이상이다.  
```python
# 위 두 조건을 and 연산자로 판단
"""

f1 = float(input("실수1 입력: "))

condition = (math.ceil(f1) < 10 and (math.floor(f1) >= 5))
print(condition)

# 06. 
"""
숫자 a와 b를 입력받아 다음 조건 중 하나라도 만족하면 `True`, 아니면 `False`를 출력하시오:  
- a가 b보다 크다  
- a를 반올림한 값이 b의 버림값보다 크다  
힌트: `or`, `round()`, `math.floor()`
"""

a = float(input("숫자1 입력: "))
b = float(input("숫자2 입력: "))

condition2 = (a>b) or (round(a) > math.floor(b))
print(condition2)

# 07.
"""
임의의 실수 `x`가 주어졌을 때,  
- x의 올림값이 짝수이고  
- x의 반올림값이 10보다 작을 경우  
`True`를 출력하시오. 아니면 `False`.  
힌트: `math.ceil(x) % 2 == 0`, `round(x) < 10`
"""
x6= float(input("실수 입력: "))
condition3 = (math.ceil(x6) % 2 == 0) and (round(x6) < 10)
print(condition3)

# 08. 
"""
실수 `x`가 주어졌을 때, `버림값`, `반올림값`, `올림값`을 각각 구한 후 이 중 가장 큰 값을 출력하시오.
"""

x7 = float(input("실수 입력: "))

values = [(math.floor(x7)), (round(x7)), (math.ceil(x7))]
print(max(values))

# 09. 
"""
사용자로부터 실수 하나를 입력받고, 다음 조건 중 하나라도 만족하면 "조건 만족", 아니면 "조건 불만족"을 출력하시오:  
- 반올림한 값이 5의 배수이다.  
- 올림한 값이 짝수이다.
"""
f2 = float(input("실수 입력: "))
if round(f2) % 5 == 0 or math.ceil(f2) % 2 ==0:
    print("조건 만족!!!")
else:
    print("조건 불만족 ㅜㅜ")


# 10.
"""
실수 두 개 `a`, `b`를 입력받고 다음 조건을 만족하는지 판별하시오:  
- a를 반올림한 값이 b를 반올림한 값보다 작거나 같고  
- a를 올림한 값이 b를 버림한 값보다 크다
"""
a2 = float(input("실수1 입력: "))
b2 = float(input("실수2 입력: "))

condition4 = (round(a2) <= round(b2)) and (math.ceil(a2) > math.floor(b2))
print(condition4)



# 11.
"""
```python
numbers = [5, 2, 9, 1, 7]

```

이 리스트에 다음 작업을 순서대로 수행해보자.

1. 리스트에 숫자 `3`을 추가한다.
2. 리스트를 오름차순으로 정렬한다.
3. 가장 큰 값을 제거한다.
4. 마지막 두 값을 제외한 나머지만 출력한다.

```python
# TODO: 위 내용을 코드로 작성해보자
numbers = [5, 2, 9, 1, 7]

# 1. 값 추가: append()
# 2. 정렬: sort()
# 3. 최대값 제거: remove()
# 4. 슬라이싱 후 출력 

```
"""

numbers = [5,2,9,1,7]
numbers.append(3) # 값을 추가
numbers.sort() # 값을 정렬
numbers.remove(max(numbers)) # 최댓값 제거

print(numbers[:-2]) # 마지막 두 값 제외 후 출력



# 12. 
"""
```python
info = ("Alice", 25, "Engineer")

```

이 튜플에서 이름과 나이를 꺼내어 다음 형식으로 출력해보자.

```
이름은 Alice이고, 나이는 25살이다.

```

*힌트:* 튜플의 인덱싱을 사용하자.

---
"""
info = ("Alice", 25, "Engineer")
print(f"이름은 {info[0]} 이고, 나이는 {info[1]}살이다. 나는 {info[2]}야~")



# 13. 
"""
```python
scores = {"Tom": 87, "Jane": 92, "Mike": 78}

```

1. "Mike"의 점수를 82로 수정하고,
2. "Lucy"의 점수를 95로 추가한 후,
3. 모든 학생의 평균 점수를 출력해보자.

*힌트:* `values()`와 `sum()` 사용 가능.
"""

scores = {"Tom": 87, "Jane": 92, "Mike": 78}

"""
이미 존재하는 키면 수정,
존재하지 않는 키면 추가로 동작
하는 거예요.
"""
scores["Mike"] = 82 # 수정
scores["Lucy"] = 95 # 추가

# 평균 점수 출력
average = sum(scores.values()) / len(scores)
print("평균 점수: ", round(average, 2))