# pyhon/.py
from collections import Counter

# 과제 1. 학생들의 이름과 점수 정보를 리스트로 관리하는 코드 구현
# 학생 추가: 이름과 점수를 입력 받아 목록에 추가
def add_students(students:list):
    new_students_list = []
    while True:
        name = input(f"이름을 입력하세요: ")
        score = int(input(f"점수를 입력하세요: "))
        names = check_student_name
        if names :
            if name in names: 
                print(f"* 해당 이름({name}) 중복입니다. 자동으로 뒤에 인덱스가 붙습니다.")
            
        if score <= 100 and score >= 0:
            new_students_list.append([name, score])
        else:
            print("0~100 사이의 점수를 입력해주세요.")
        if input(f"계속 입력하시겠습니까? (y/n) : ") == "y":
            continue
        else:
            print(f"처리를 종료합니다.")
            print(f"입력내용: {new_students_list}")
            break
    return new_students_list

# 학생 삭제: 이름을 입력 받아 해당 학생 정보 삭제
def delete_student(students:list):
    name = input(f"삭제할 학생의 이름을 입력하세요: ")
    new_students_list = students
    if not check_student_name(name, students) : 
        return students
    for student in new_students_list:
        if student[0] == name:
            new_students_list.remove(student)
            print(f"학생 {name}을 삭제했습니다.")
    return new_students_list

# 성적 수정: 이름을 입력 받아 해당 학생의 점수 수정
def modify_student(students:list):
    name = input(f"점수를 수정할 학생의 이름을 입력하세요: ")
    if not check_student_name(name, students) : 
        return students
    new_score = int(input(f"점수를 몇점으로 수정하시겠습니까? : "))
    new_students_list = students
    for student in new_students_list:
        if student[0] == name:
            new_students_list[new_students_list.index(student)][1] = new_score
            print(f"학생 {name}의 점수를 수정했습니다.")
    return new_students_list

# 전체 목록 출력: 모든 학생의 이름과 점수 출력
def print_student_list(students:list):
    for student in students :
        print(f"----{students.index(student) + 1} 번째 학생----")
        print(f"이름: {student[0]}")
        print(f"점수: {student[1]}")
    return

# 통계 출력: 최고 점수, 최저 점수, 평균 점수 계산 및 출력
def print_stats(students:list):
    print("<<<<< 통계 출력 >>>>>")
    scores = [int(student[1]) for student in students]
    print(f"최고 점수 : {max(scores)}")
    print(f"최저 점수 : {min(scores)}")
    print(f"평균 점수 : {sum(scores) / len(scores)}")
    return

# 학생 확인: 이름을 입력 받아 해당 학생의 정보가 존재하는지 확인
def check_student_name(name, students_list:list):
    student_names = [student[0] for student in students_list]
    if name not in student_names : 
        print(f"!!! 해당하는 학생이 없습니다 : {name}")
        return False
    return student_names

students_list = [["김철수", 85], ["이영희", 99]]
while(True):
    print("----------학사 정보 시스템----------")
    print(" 1: 학생 추가 \n 2: 학생 삭제\n 3: 성적 수정 \n 4: 목록 출력 \n 5: 통계 출력\n 기타: 종료")
    choice = input(f"작업을 입력하세요: ")
    if choice == "1" :
        students_list.extend(add_students(students_list))
    elif choice == "2" :
        students_list = delete_student(students_list)
    elif choice == "3" :
        students_list = modify_student(students_list)
    elif choice == "4" :
        print_student_list(students_list)
    elif choice == "5" :
        print_stats(students_list)
    else : break