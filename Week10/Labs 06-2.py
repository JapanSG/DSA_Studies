'''Labs 06.02 - ProbHash Hashing'''

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

class ProbHash:
    def __init__(self,size : int):
        self.size : int = size
        self.hash_table = [None for i in range(size)]
        self.inserted = 0

    def hash(self, key : int, new_key : int) -> int:
        '''return hash of the key'''
        if key != new_key and key%self.size == new_key%self.size:
            return 0
        index = new_key%self.size
        if self.hash_table[index] and self.hash_table[index].get_std_id() != key:
            # print(key, "!=", self.hash_table[index].get_std_id())
            return self.rehash(key, new_key)
        return index

    def rehash(self, key : int, new_key : int) -> int:
        '''rehash the key in case of collision'''
        return self.hash(key,new_key+1)

    def insert_data(self, std : Student):
        '''Insert data'''
        if self.is_full():
            print(f"The list is full. {std.get_std_id()} could not be inserted.")
            return
        index = self.hash(std.get_std_id(),std.get_std_id())
        self.hash_table[index] = std
        print(f"Insert {std.get_std_id()} at index {index}")
        self.inserted += 1

    def search_data(self,std_id : int):
        # '''Search Data'''
        # for i, std in enumerate(self.hash_table):
        #     if std and std.get_std_id() == std_id:
        #         print(f"Found {std_id} at index {i}")
        #         return std
        # print(f"{std_id} does not exist.")
        # return None
        index = self.hash(std_id,std_id)
        if self.hash_table[index] and self.hash_table[index].get_std_id() == std_id:
            print(f"Found {std_id} at index {index}")
            return self.hash_table[index]
        print(f"{std_id} does not exist.")
        return None

    def is_full(self):
        '''Return true if full'''
        if None in self.hash_table:
            return False
        return True

def main():
    import json
    size = int(input())
    hashtable = ProbHash(size)
    while True:
        finish = input()
        if finish == "Done":
            break
        condition, data = finish.split(" = ")
        if condition == "I":
            std_in = json.loads(data)
            std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
            hashtable.insert_data(std)
        elif condition == "S":
            print("------")
            student = hashtable.search_data(int(data))
            if student is not None:
                student.print_details()
            print("------")
        else:
            print("Invalid Condition!")
main()
