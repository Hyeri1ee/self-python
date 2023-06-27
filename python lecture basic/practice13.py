# def profile(name ,  age =17, main_lang = "파이썬"):
#     print("이름 : {0}\t나이 : {1}\t주 사용언어 : {2}"\
#           .format(name, age, main_lang))
# profile("유재석","20","자바")
# profile("김태호")

# def profile(name, age, main):
#     print(name, age, main)

# profile(name = "유재석",main = "파이썬",age = 40)

# def profile(name,age,lang1,lang2,lang3,lang4,lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name,age),end =" ")
#     print(lang1,lang2,lang3,lang4,lang5)

# profile("유재석",20,"python","java","c","c++","swift")

# def profile(name,age,*language):
#     print("이름 : {0}\t나이 : {1}\t".format(name,age),end =" ")
#     for lang in language:
#         print(lang, end = " ")
#     print()

# profile("유재석",30,"파이썬","자바","c")
# profile("김태호",40,"파이썬","자바","c","swift","kotlin","c++","r")

gun =10

def checkpoint(soldiers):
    global gun #전역 공간의 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun,soldiers):
    gun = gun - soldiers
    print("[함수 내]남은 총 : {0}".format(gun))
    return gun

print("전체 총수 : {0}".format(gun))
#checkpoint(2)
gun = checkpoint_ret(gun,2)
print("남은 총수 : {0}".format(gun))