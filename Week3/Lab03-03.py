'''Lab 03.03 - Singly Linked List (Insert Front)'''
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

    def traverse(self) -> None:
        '''traverse and print datanode in linked list'''
        if not self.count:
            print("This is an empty list.")
            return
        print(self.head.data, end = "")
        pointer = self.head.next
        while pointer is not None:
            print(" -> " + pointer.data, end = "")
            pointer = pointer.next

def main():
    '''Driver Code'''
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        text = input()
        condition, data = text.split(": ")
        if condition == "F":
            mylist.insert_front(data)
        elif condition == "L":
            mylist.insert_last(data)
        # elif condition == "B":
        #     mylist.insert_before(*data.split(", "))
        # elif condition == "D":
        #     mylist.delete(data)
        else:
            print("Invalid Condition!")
    mylist.traverse()

main()
