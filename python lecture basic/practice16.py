# score_file = open("score.txt","w",encoding ="utf8")
# print("수학 : 0",file = score_file)
# print("영어 : 50",file = score_file)
# score_file.close()

# score_file = open("score.txt","a",encoding = "utf8") #append
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt","r",encoding = "utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt","r",encoding = "utf8")
# print(score_file.readline(),end= "") #줄별로 읽고 커서 다음줄로 이동
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# score_file = open("score.txt","r",encoding = "utf8")
# while True:
#     line=  score_file.readline()
#     if not line:
#         break
#     print(line, end = "")
# score_file.close()