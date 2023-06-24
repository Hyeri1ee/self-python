#자료구조 변경
# menu = {"커피","우유","주스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))

# from random import *
# coffee = set() #coffee = {} 은 dict 형태 초기화 선언임.
# while(len(coffee)<4):
#     x = randint(1,21)
#     coffee.add(x)
# coffee = list(coffee) #set 자료형은 인덱스로 접근 못하므로 list로 전환
# print("--당첨자 발표--")
# print("치킨 당첨자 : "+str(coffee[0]))
# del coffee[0]
# coffee = list(coffee)
# print("커피 당첨자 : "+str(coffee))
# print("--축하합니다--")

from random import *
users = range(1,21)
users = list(users)
shuffle(users)
#print(users)
winners = sample(users,4)
#print(type(winners))
print("--당첨자 발표--")
print("치킨 당첨자 : {}".format(winners[0]))
print("커피 당첨자 : {}".format(winners[1:]))
print("--축하합니다--")