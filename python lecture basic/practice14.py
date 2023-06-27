x = int(input("키 값을 입력하세요 :"))
y = input("성별을 입력하세요(여/남) : ")

def std_weight(k,s):
    if(s == "여"):
        return ((k / 100)*(k/100) )* 21
    else:
        return ((k/100)*(k/100) )* 22

print("키 {0}cm {1}자의 표준 체중은 {2: .2f}kg 입니다.".format(str(x),str(y),std_weight(x,y)))