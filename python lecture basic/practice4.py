#문자열
# sentence = """
# 나는 소년이고,
#   ㅁㄴㅇㄹㅁㄴ"""
# print(sentence)

#문자열 슬라이싱
# jumin = "990120-1234567"
# print("성별 : "+jumin[7])
# print("연 : "+jumin[0:2])
# print("월 : "+jumin[2:4])
# print("일 : "+jumin[4:6])
# print("생년월일 : "+jumin[:6])
# print("뒤 7자리 : "+jumin[7:])
# print("뒤 7자리(뒤에서부터) : "+jumin[-7:])

#문자열 처리 방식
# python = "Python Is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python","java"))

# index = python.index("n")
# print(index)
# index = python.index("n",index+1)
# print(index)

# print(python.find("java"))
# #print(python.index("java"))
# print("hi")

# print(python.count("n"))

#문자열 포맷
# print("a"+"b")
# print("a","b")

#문자열 포맷 방법1
# print("나는 %d살입니다."%20)
# print("나는 %s를 좋아해요."%"파이썬")
# print("Apple 은 %c로 시작해요."%'A')
# print("나는 %s색과 %s색을 좋아해요."%("파란","빨간"))

#문자열 포맷 방법2
# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아효".format("파란","노란"))
#print("나는 {1}색과 {0}색을 좋아효".format("퍼란","노란"))

#문자열 포맷 방법3
#print("나는 {age}살이며, {color}색을 좋아해요".format(age=20,color = "빨간"))

#문자열 포맷 방법4
# age = 24
# color = "핑크색"
# print(f"나는 {age}살이며, {color}을 좋아해요")