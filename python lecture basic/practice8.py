#튜플 (속도가 list보다 빠름)

# menu = ("돈까스","치즈까스")
# print(menu[0])
# print(menu[1])

#튜플 값 추가 못함
#대신

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name,age,hobby)

#튜플
# (name, age, hobby) = ("김종국" , 20, "코딩")
# print(name, age, hobby)

#set (집합)
#중복안됨, 순서없음
# set = {1,2,3,3,3}
# print(set)

java = {"유재석","김태호","양세호"}
python = set(["유재석", "박명수"])

# #교집합
# print(java & python)
# print(java.intersection(python))

# #합집합
# print(java | python)
# print(java.union(python))

# #차집합
# print(java - python)
# print(java.difference(python))

python.add("김태호")
print(python)

java.remove("김태호")
print(java)