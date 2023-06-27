#함수
def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money): #입금
    print("입금이 완료되었습니다. 잔액은 {0}입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money): #출금
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}입니다.".format(balance-money))
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}입니다.".format(balance))
def withdraw_night(balance, money): #저녁에 출금
    commission = 100
    return commission, balance-money-commission #튜플 형식 반환
balance = 0
balance = deposit(balance , 1000)
commssion, balance = withdraw_night(balance,500)
print("수수료 = {0} , 잔액 = {1} 원 입니다.".format(commssion,balance))
balance = deposit(balance,5000)
balance = deposit(balance,400)
print("잔액은 {0}원 입니다.".format(balance))