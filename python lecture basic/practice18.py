# with open("study.txt","w",encoding = "utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어오.")

# with open("study.txt","r",encoding = "utf8") as study_file:
#     print(study_file.read())

#quiz4
for i in range(1,51):
    with open(str(i) + " 주차.txt","w",encoding = "utf8") as report:
        report.write("- "+str(i) +" 주차 주간보고 -\n")
        report.write("부서 : \n")
        report.write("이름 : \n")
        report.write("업무 요약 : \n")