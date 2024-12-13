'''stack'''
from linkedlist import Node
class Stack:
    '''Stack Class'''
    def __init__(self, maxi = float('inf')):
        '''Constructor'''
        self.__max = maxi
        self.__head = Node(0)

    def push(self, val):
        '''Add Node to __top of stack'''
        if self.__head.val >= self.__max:
            print("Full Stack")
            return
        self.__head.val += 1
        top = Node(val)
        top.next = self.__head.next
        self.__head.next = top

    def pop(self):
        '''Pop'''
        if not self.__head.val:
            print("Empty Stack")
            return None
        self.__head.val -= 1
        temp = self.__head.next.val
        self.__head.next = self.__head.next.next
        return temp

    def peek(self):
        '''Return __top of the stack'''
        return self.__head.next.val

    def is_empty(self):
        '''Check if stack is empty'''
        return not bool(self.__head.val)

    def copy(self):
        '''Return a copy of stack'''
        s2 = Stack(self.__max)
        temp = Stack(self.__max)
        while not self.is_empty():
            x = self.pop()
            temp.push(x)
        while not temp.is_empty():
            val = temp.pop()
            self.push(val)
            s2.push(val)
        return s2

    def __repr__ (self):
        return f"|{self.__head.next}|"

    def __str__(self):
        return f"{self.__head.next}"
def main():
    '''Driver Code'''
    s1 = Stack(5)
    s1.push(5)
    s1.push(5)
    s1.push(20)
    s1.push(20)
    s2 = s1.copy()
    print(s2.peek())
    print(s1.peek())
    print(s1)
if __name__ == "__main__":
    main()
