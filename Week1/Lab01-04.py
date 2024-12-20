'''Lab 01.04 - Student Class (No Class)'''
def bundle_student():
    '''bundle all student info into a list and return the list'''
    student = []
    for _ in range(5):
        student.append(input())
    return student

def print_student(student : list):
    '''print student'''
    honorific = "Mr"
    if student[1] == "Female":
        honorific = "Miss"
    print(f"{honorific} {student[0]} ({student[2]}) ID: {student[3]} GPA {float(student[4]):.2f}")

def main():
    '''Driver Code'''
    students = []
    for _ in range(3):
        students.append(bundle_student())
    stu_id = input()
    for student in students:
        if stu_id == student[3]:
            print_student(student)
            return
    print("Student not found")

if __name__ == "__main__":
    main()
