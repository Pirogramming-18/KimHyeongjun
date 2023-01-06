#함수 이름은 변경 가능합니다.

##############  menu 1
def Menu1(name, score1, score2) :
    #사전에 학생 정보 저장하는 코딩
    global student_name
    global student_score1
    global student_score2
    student_name.append(name)
    student_score1.append(score1)
    student_score2.append(score2)

     

##############  menu 2
def Menu2() :
    #학점 부여 하는 코딩
    global student_score1
    global student_score2
    global student_final_score
    last = len(student_score1)
    middle = len(student_final_score)
    for i in range(middle, last):
        score = (student_score1[i] + student_score2[i]) / 2
        final = ""
        if score >= 90:
            final = "A"
        elif score >= 80:
            final = "B"
        elif score >= 70:
            final = "C"
        else:
            final = "D"
        student_final_score.append(final)

##############  menu 3
def Menu3():
    #출력 코딩
    global student_name
    global student_score1
    global student_score2
    global student_final_score
    print('-------------------------------')
    print('name   mid   final  grade')
    print('-------------------------------')
    for i in range(len(student_name)):
        print(student_name[i], student_score1[i], student_score2[i], student_final_score[i])

##############  menu 4
def Menu4(name):
    #학생 정보 삭제하는 코딩
    global student_name
    global student_score1
    global student_score2
    global student_final_score
    ind = student_name.index(name)
    student_name.remove(name)
    student_score1.pop(ind)
    student_score2.pop(ind)
    if(len(student_final_score) > ind):
        student_final_score.pop(ind)

student_name = []
student_score1 = []
student_score2 = []
student_final_score = []
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        try:
            a, b, c = input('Enter name mid-score final-score : ').split(' ')
            if '.' in b or '.' in c or '-' in b or '-' in c:
                raise Exception('Score is not positive integer!')
            for i in range(len(student_name)):
                if student_name[i] == a:
                    raise Exception('Already exist name!')
        except ValueError:
            print("Num of data is not 3!")
        #예외사항이 아닌 입력인 경우 1번 함수 호출 
        else:
            b = int(b)
            c = int(c)
            Menu1(a, b, c)
        #학생 정보 입력받기
        #예외사항 처리(데이터 입력 갯수, 이미 존재하는 이름, 입력 점수 값이 양의 정수인지)
        #예외사항이 아닌 입력인 경우 1번 함수 호출 

    elif choice == "2" :
        if len(student_name) == 0:
            print('No student data!')
        else:
            Menu2()
            print('Grading to all students.')
        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우 2번 함수 호출
        #"Grading to all students." 출력

    elif choice == "3" :
        if len(student_name) == 0:
            print('No student data!')
        elif len(student_name) == len(student_final_score):
            Menu3()
        else:
            print("There is a student who didn't get grade.")
        #예외사항 처리(저장된 학생 정보의 유무, 저장되어 있는 학생들의 학점이 모두 부여되어 있는지)
        #예외사항이 아닌 경우 3번 함수 호출

    elif choice == "4" :
        if len(student_name) == 0:
            print('No student data!')
        else:
            student = input('Enter the name to delete : ')
            find_st = False
            for i in range(len(student_name)):
                if student_name[i] == student:
                    Menu4(student)
                    print(student, 'student information is deleted.') 
                    find_st = True
                    break
            if not find_st:
                print('Not exist name!')
        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
        #입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
        #있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력

    elif choice == "5" :
        #프로그램 종료 메세지 출력
        #반복문 종료

        print('Exit Program!')
        break
        
    else :
        #"Wrong number. Choose again." 출력
        print('Wrong number. Choose again.')