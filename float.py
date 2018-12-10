a = 1.2
print(a, type(a))
print(isinstance(a, float))

b = 2.00000
print(b, type(b))

# 객체 함수 is_integer()는 값이 정수인지 실수인지 확인하는 함수
# 타입이 실수인지 정수인지는 모름.
print(b.is_integer())


# 다른 언어와 마찬가지로 e, E를 사용한 부동소수점 표기가 가능.
b = 2e3
c = 0.2e-4

print(b, c)