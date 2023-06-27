#quiz
# from random import *
# count = 0
# for i in range(50):
#     x = randrange(5,51)
#     if (x > 5 and x <15):
#         print("[0] "+str(i+1)+"번째 손님 (소요시간 : "+str(x)+"분)")
#         count += 1
#     else:
#          print("[ ] "+str(i+1)+"번째 손님 (소요시간 : "+str(x)+"분)")

# print("\n총 탑승 승객 : "+str(count)+" 분")

#모범답안
from random import *
cnt = 0
for i in range(1,51):
    time = randrange(5,51)
    if 5<= time <= 15:
        print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i,time))
        cnt +=1
    else:
         print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i,time))
print("총 탑승 승객 : {}분".format(cnt))