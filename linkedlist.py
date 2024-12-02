'''LinkedList'''
class Node:
    '''Node Class'''
    def __init__(self, val):
        '''Constructor'''
        self.val  = val
        self.next : Node = None

    def __repr__(self):
        return f"{self.val}"

class LinkedList:
    '''LinkedList Class'''
    def __init__(self, *val) -> None:
        '''Constructor'''
        self._head = Node(val[0])
        pointer = self._head
        self._pointer = self._head
        for i in range(1 ,len(val)):
            pointer.next = Node(val[i])
            pointer = pointer.next

    def __str__(self) -> str:
        '''__str__'''
        string = "["
        pointer = self._head
        while pointer:
            string += f" {pointer.val}"
            pointer = pointer.next
        string += " ]"
        return string

    def __len__(self) -> int:
        '''Return lenght of LinkeList'''
        length = 0
        pointer = self._head
        while pointer:
            pointer = pointer.next
            length += 1
        return length

    def __add__(self, lis):
        '''Add Function'''
        new1 = self.clone()
        new2 = lis.clone()
        pointer = new1._head
        while pointer.next:
            pointer = pointer.next
        pointer.next = new2._head
        return new1

    def __getitem__(self, index : int):
        '''Get val from Node at index'''
        if index < 0:
            index += len(self)
        i = 0
        pointer = self._head
        while i != index:
            pointer = pointer.next
            i += 1
        return pointer.val

    def __setitem__(self, index : int, val):
        '''Set val in Node at index'''
        i = 0
        pointer = self._head
        while i != index:
            pointer = pointer.next
            i += 1
        pointer.val = val

    def __iter__(self):
        '''Return iterator of self'''
        self._pointer = self._head
        return self

    def __next__(self):
        '''Logic for iterator'''
        if self._pointer:
            val = self._pointer.val
            self._pointer = self._pointer.next
            return val
        raise StopIteration

    def clone(self):
        '''Return a clone of LinkedList'''
        if not self._head:
            return None
        new = LinkedList(self._head.val)
        pointer = self._head.next
        while pointer:
            new.append(pointer.val)
            pointer = pointer.next
        return new

    def append(self, val) -> None:
        '''Append Node'''
        pointer = self._head
        while pointer.next:
            pointer = pointer.next
        pointer.next = Node(val)

    def pop(self):
        '''Remove last Node'''
        pointer = self._head
        if not pointer:
            raise ValueError("Can't pop an Empty List")
        if not pointer.next:
            val = self._head.val
            self._head = None
            return val
        while pointer.next.next:
            pointer = pointer.next
        val = pointer.next.val
        pointer.next = None
        return val

def main():
    '''Driver Code'''
    lis = LinkedList(10,20,30,40,50)
    lis1 = LinkedList(60,70,80)
    lis2 = lis +lis1
    print(lis2)
if __name__ == "__main__":
    main()
