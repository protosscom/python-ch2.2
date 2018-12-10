# 한 줄 문자열 정의
s = ""
str1 = 'Hello World'
str2 = "Hello World"

print(type(s), type(str1), type(str2))
print(isinstance(str2, str))

# 여러줄 문자열 정의
str3 = """ABCDEFG
abcdef
가나다라마
123456789"""
print(str3)

# escape
print("hello\nworld\nI say \"Hello World\"")

# 문자열 연산
str1 = "First String"
str2 = "Second String"

# 1. 인덱싱
print(str1[0], str1[2], str1[4])

# 2. 슬라이싱
str3 = str2[2:5]
print(str3)
#print(str[2:])

# 3. 연결 +는 생략도 가능하다(단 리터럴 일때)
print(str1 + " " + str2)
print("First String" " " "Second String")

# 문자열 객체와 정수형 객체는 + 연결을 할 수 없다.
name = "길동"
age = 40
print("->1")
#print(name + 40)
print(name + str(40))
print("......")

# 4. 반복(*)
print(str1*3)

# 5. 길이 len()
print(len(str2))

# 6. in, not in
print("S" in str2)
print("S" not in str2)

# 문자열 객체는 변경할 수 없다(immutable)
#str1[0] = "F"


# 서식(formatting) - format() 함수
print("name : " + name + ", age : " + format(age, "d"))
print("name : " + format(name, "s") + ", age : " + format(age, "d"))

# 튜플을 이용한 서식
print("name:%s, age:%d")
print("name:%s, age:%d" % ('길동', 40))

#cf C 스타일
#printf("name : %s , age : %d", name, age);


# 딕셔너리를 이용한 서식
print("name:%(name)s, age:%(age)d" % {"name" : "둘리", "age" : 30})


