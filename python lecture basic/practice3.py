#숫자 처리 함수
# print(abs(-123123))
# print(pow(4,2))
# print(max(102,2445))
# print(min(234,-123))
# print(round(3.14))
# print(round(4.99))

# from math import *
# print(floor(4.99))
# print(ceil(3.1544))
# print(sqrt(16))

# #랜덤 함수
# from random import *
# # print(random()) #0.0~1.0 미만의 임의의 값
# # print(round(random() * 10))
# # print(int(random()*10)) #0~10미만

# print(int(random()*45)+1) #1~45이하의 임의의 값
# print(randrange(1,46)) #1~45이하의 임의의 값
# print(randint(1,45)) #1~45이하의 임의의 값

#quiz2
from random import *
x = randrange(4,29)
print("오프라인 스터디 모임 날짜는 매월 "+str(x)+"일로 선정되었습니다.")