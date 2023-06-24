#escape sequence : \n , \" , \' , \\ , \r
# print("저는 \"나도코딩\" 입니다.")
# print("Red Apple\rPine")
# print("Red\bapple")
# print("red\tapple")
#quiz
#사이트별로 비밀번호를 만들어 주는 프로그램 작성
# s = "http://naver.com"
# s = s[7:]
# s = s[:-4]
# a = len(s)
# b = s.count("e")
# s = s[:3]
# s += str(a)
# s+=str(b)
# s +="!"
# print(s)

#solution
url = "http://google.com"
my_str = url.replace("http://","")
my_str = my_str[:my_str.index(".")]
password = my_str[:3]+str(len(my_str))+str(my_str.count("e"))+"!"
print("{0}의 비밀번호는 {1}입니다.".format(url,password))