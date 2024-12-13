'''queue_adt'''
from linkedlist import Node
class Queue:
    '''Queue class'''
    def __init__(self, limit = float('inf')):
        '''Constructor'''
        self.front : Node = None
        self.rear : Node = None
        self.limit = limit
        self.count = 0

    def __repr__ (self):
        return f"|{self.front}|"

    def __str__(self):
        return f"{self.front}"

    def enqueue(self, val):
        '''Add a Node at the rear of the queue'''
        if self.count > self.limit:
            print("Overflowed")
            return
        if self.is_empty():
            self.front = Node(val)
            self.rear = self.front
        else:
            self.rear.next = Node(val)
            self.rear = self.rear.next
        self.count += 1

    def dequeue(self):
        '''Delete a Node at the front of the queue'''
        if self.is_empty():
            print("Underflowed")
            return
        self.front = self.front.next
        self.count -= 1

    def queue_front(self):
        '''View Node val at the front'''
        if self.is_empty():
            print("Empty queue")
        return self.front.val

    def queue_rear(self):
        '''View Node val at the rear'''
        if self.is_empty():
            print("Empty queue")
        return self.rear.val

    def is_empty(self):
        '''Return True if empty else return False'''
        return not bool(self.count)

    def concat_queue(self, q2):
        '''Concat a queue to self'''
        q2 : Queue = q2
        temp = Queue()
        while not q2.is_empty():
            x = q2.queue_front()
            q2.dequeue()
            temp.enqueue(x)
        while not temp.is_empty():
            x = temp.queue_front()
            temp.dequeue()
            self.enqueue(x)
            q2.enqueue(x)

def main():
    '''Driver Code'''
    q1 = Queue()
    q2 = Queue()
    for i in range(10,50,10):
        q1.enqueue(i)
    q2.enqueue(45)
    q2.enqueue(25)
    print(q1)
    print(q2)
    q1.concat_queue(q2)
    print(q1)
    print(q2)
    print("-"*100)
    #______________________
    q = Queue()
    data = (9, 72, 1, 43, 29, 0, 34, 62, 3, 56, 0, 34)
    for num in data:
        if num > 5:
            q.enqueue(num)
        else:
            x = q.queue_rear()
            q.enqueue(x)
    print(q)
if __name__ == "__main__":
    main()
