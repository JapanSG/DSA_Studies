'''Exercise 03.01 - Indexing'''
class DataNode:
    '''DataNode class'''
    def __init__(self, data = None):
        '''Constructor'''
        self.data = data
        self.next : DataNode = None

class SinglyLinkedList:
    '''SinglyLinkedList class'''
    def __init__(self):
        '''Constructor'''
        self.count = 0
        self.head : DataNode = None

    def insert_last(self, data) -> None:
        '''insert data node at the tail of the linkedlist'''
        self.count += 1
        pointer = self.head
        if not pointer:
            self.head = DataNode(data)
            return
        while pointer.next:
            pointer = pointer.next
        pointer.next = DataNode(data)

    def insert_front(self, data) -> None:
        '''insert data node at the head of the linkedlist'''
        self.count += 1
        temp = DataNode(data)
        temp.next = self.head
        self.head = temp

    def insert_before(self, node, data) -> None:
        '''insert data node before a node which have the specified data'''
        if not self.count:
            print("Cannot insert, "+ str(node) +" does not exist.")
            return
        if self.head.data == node:
            self.insert_front(data)
            return
        pointer = self.head
        while pointer.next:
            if pointer.next.data == node:
                temp = DataNode(data)
                temp.next = pointer.next
                pointer.next = temp
                self.count += 1
                return
            pointer = pointer.next
        print("Cannot insert, "+ str(node) +" does not exist.")

    def delete(self, data) -> None:
        '''Delete the first occurence node that have the specified data'''
        if not self.head:
            print("Cannot delete, "+ str(data) +" does not exist.")
            return
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
            self.count -= 1
            return
        pointer = self.head
        while pointer.next:
            if pointer.next.data == data:
                pointer.next = pointer.next.next
                self.count -= 1
                return
            pointer = pointer.next
        print("Cannot delete, "+ str(data) +" does not exist.")

    def traverse(self) -> None:
        '''traverse and print datanode in linked list'''
        if not self.count:
            print("This is an empty list.")
            return
        print(self.head.data, end = "")
        pointer = self.head.next
        while pointer is not None:
            print(" -> " + str(pointer.data), end = "")
            pointer = pointer.next
        print("")

    def get_at(self, i : int):
        '''get date at index'''
        if i < 0:
            i = self.count + i
        if i+1 > self.count or i < 0:
            return "Error"
        pointer = self.head
        for _ in range(i):
            pointer = pointer.next
        return pointer.data


def main():
    '''Driver Code'''
    students = SinglyLinkedList()
    scores = SinglyLinkedList()
    length = int(input())
    for _ in range(length):
        student, score =  input().split()
        students.insert_last(student)
        scores.insert_last(score)
    total = 0
    for i in range(length):
        total += float(scores.get_at(i))
    avg = total/length
    max_stu = ""
    max_score = -1
    for i in range(length):
        temp_score = float(scores.get_at(i))
        if temp_score <= avg and temp_score > max_score:
            max_stu = students.get_at(i)
            max_score = temp_score
    print(max_stu, max_score, sep="\t")

main()
