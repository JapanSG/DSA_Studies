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
            print("max")
            return
        self.__head.val += 1
        top = Node(val)
        top.next = self.__head.next
        self.__head.next = top

    def pop(self):
        '''Pop'''
        if not self.__head.val:
            print("Empty Stack")
            return
        self.__head.val -= 1
        temp = self.__head.next.val
        self.__head.next = self.__head.next.next
        return temp

    def stack_top(self):
        '''Return __top of the stack'''
        return self.__head.next.val

def main():
    '''Driver Code'''
    s1 = Stack(5)
    s1.push(5)
    s1.push(5)
    s1.push(20)
    s1.push(20)
    print(s1.stack_top())
    print(s1.pop())
    print(s1.pop())
    print(s1.pop())
if __name__ == "__main__":
    main()
