'''Lab 01.05 - Student Class (Class)'''
class Student:
    '''Student class'''
    def __init__(self):
        '''Constructor'''
        self.name = input()
        self.gender = input()
        self.age = input()
        self.iden = input()
        self.gpa = float(input())

    def __str__(self) -> str:
        '''__str__'''
        if self.gender == "Male":
            return f"Mr {self.name} ({self.age}) ID: {self.iden} GPA {self.gpa:.2f}"
        else:
            return f"Miss {self.name} ({self.age}) ID: {self.iden} GPA {self.gpa:.2f}"
def main():
    '''Driver Code'''
    students = [Student(), Student(), Student()]
    stu_id = input()
    for student in students:
        if student.iden == stu_id:
            print(student)
            return
    print("Student not found")

if __name__ == "__main__":
    main()
