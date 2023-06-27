#표준 입출력

# import sys
# # print("python","java","javascript",sep = " , ", end="? ")
# # print("무엇이 재밌을까요?")
# print("python","java",file = sys.stdout) #표준출력
# print("python","java",file = sys.stderr) #표준에러

#정렬
# scores = {"수학" : 0, "영어" : 50, "코딩" : 100}
# for subject,score in scores.items():
#     #print(subject , score)
#     print(subject.ljust(8), str(score).rjust(4),sep = " : ")

#은행 대기순번표
# for num in range(1,21):
#     print("대기번호 : "+str(num).zfill(3))

# answer = input("아무 값을 입력하세요 : ")
# print("입력하신 값은 {}입니다.".format(answer))

#빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간 확보
print("{0: >10}".format(500))
print("{0: >10}".format(-500))
#양수일땐 + 표시, 음수일땐 -표시
print("{0: >+10}".format(+500))
print("{0: >+10}".format(-500))
#왼쪽 정렬하고, 빈찬 _로 채움
print("{0:_<+10}".format(500))
print("{0:_<+10}".format(-500))
#3자리마다 콤마 찍어주기
print("{0:,}".format(10000000000000000))
#3자리마다 콤마 찍어주기 , +- 부호 붙이기
print("{0:+,}".format(10000000000000000))
print("{0:+,}".format(-10000000000000000))
#3자리마다 콤마 찍어주기 , +- 부호 붙이고, 자릿수 확보
#빈자리 ^ 채우기
print("{0:^<+30,}".format(101020030120301203012))
#소수점 출력
print("{0:f}".format(5/3))
#소수점 특정 자리수까지만 표시 (소수점 3째 자리에서 반올림)
print("{0:.2f}".format(5/3))

