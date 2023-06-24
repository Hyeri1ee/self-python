#사전(key, value)

cabinet ={3:"유재석",100:"김태호"}
# print(cabinet)
# print(cabinet[100]) #key로 값 가져오기1
# print(cabinet.get(3)) #key로 값 가져오기2
# print(cabinet.get(5,"사용 가능")) #key가 존재하지 않는 경우 "사용가능" 출력

# print(3 in cabinet)
# print(5 in cabinet)

# cabinet[43] = "이성경" #값 추가
# print(cabinet)

# del cabinet[3] #값 지우기
# print(cabinet)

print(cabinet.keys()) #key값만 출력
print(cabinet.values()) #value만 출력
print(cabinet.items())#둘 다 출력

cabinet.clear()
print(cabinet)