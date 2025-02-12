'''Labs 06.01 - Student Class'''

class Student:
    '''Student class'''
    def __init__(self,std_id : int, name : str, gpa : float):
        '''Constructor'''
        self.std_id : int = std_id
        self.name :str = name
        self.gpa : float = gpa

    def get_std_id(self) -> int:
        '''return std_di'''
        return self.std_id

    def get_name(self) -> str:
        '''return name'''
        return self.name
    def get_gpa(self) -> float:
        '''return gpa'''
        return self.gpa

    def print_details(self):
        '''print student details'''
        print(f"ID: {self.std_id}")
        print(f"Name: {self.name}")
        print(f"GPA: {self.gpa:.2f}")

def main(text_in):
    '''Driver Code'''
    import json
    std_in = json.loads(text_in)
    std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
    std.print_details()

main(input())
