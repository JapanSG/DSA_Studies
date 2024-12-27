'''LinkedList'''
class Node:
    '''Node Class'''
    def __init__(self, val):
        '''Constructor'''
        self.val  = val
        self.next : Node = None

    def __repr__(self):
        mem = []
        pointer = self
        string = ""
        while pointer not in mem:

            if pointer is None:
                return string + "None"

            if pointer in mem:
                return string + f"jump to index {mem.index(pointer)}"

            mem.append(pointer)
            string += f"[{pointer.val}] -> "
            pointer = pointer.next

    def __str__(self):
        return f"{self.__repr__()}"

class LinkedList:
    '''LinkedList Class'''
    def __init__(self, *val) -> None:
        '''Constructor'''
        if not val:
            self.__head = None
            self.__pointer = self.__head
            return
        self.__head = Node(val[0])
        pointer = self.__head
        for i in range(1 ,len(val)):
            pointer.next = Node(val[i])
            pointer = pointer.next

    def __str__(self) -> str:
        '''__str__'''
        return f"{self.__head}"

    def __len__(self) -> int:
        '''Return lenght of LinkeList'''
        length = 0
        pointer = self.__head
        while pointer:
            pointer = pointer.next
            length += 1
        return length

    def __add__(self, lis):
        '''Add Function'''
        new = self.clone()
        for i in lis:
            new.append(i)
        return new

    def __getitem__(self, index : int):
        '''Get val from Node at index'''
        if index < 0:
            index += len(self)
        i = 0
        pointer = self.__head
        while i != index:
            pointer = pointer.next
            i += 1
        return pointer.val

    def __setitem__(self, index : int, val):
        '''Set val in Node at index'''
        i = 0
        pointer = self.__head
        while i != index:
            pointer = pointer.next
            i += 1
        pointer.val = val

    def __iter__(self):
        '''Return iterator of self'''
        self.__pointer = self.__head
        return self

    def __next__(self):
        '''Logic for iterator'''
        if self.__pointer:
            val = self.__pointer.val
            self.__pointer = self.__pointer.next
            return val
        raise StopIteration

    def clone(self):
        '''Return a clone of LinkedList'''
        if not self.__head:
            return None
        new = LinkedList(self.__head.val)
        pointer = self.__head.next
        while pointer:
            new.append(pointer.val)
            pointer = pointer.next
        return new

    def append(self, val) -> None:
        '''Append Node'''
        if not self.__head:
            self.__head = Node(val)
            return
        pointer = self.__head
        while pointer.next:
            pointer = pointer.next
        pointer.next = Node(val)

    def pop(self):
        '''Remove last Node'''
        pointer = self.__head
        if not pointer:
            raise ValueError("Can't pop an Empty List")
        if not pointer.next:
            val = self.__head.val
            self.__head = None
            return val
        while pointer.next.next:
            pointer = pointer.next
        temp = pointer.next
        val = pointer.next.val
        pointer.next = None
        del temp
        return val

    def insert(self, val, index):
        '''insert Node of val at index'''
        if not index:
            new = Node(val)
            new.next = self.__head
            self.__head = new
            return
        pointer = self.__head.next
        prev = self.__head
        count = 1
        while count != index:
            count += 1
            prev = pointer
            pointer = pointer.next
        prev.next = Node(val)
        prev.next.next = pointer

def main():
    '''Driver Code'''
    lis = LinkedList(10,20,30,40)
    print(lis)
    lis.insert(5,4)
    print(lis)
    lis.pop()
    print(lis)
if __name__ == "__main__":
    main()
