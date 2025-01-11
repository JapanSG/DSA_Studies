'''music_box'''
class Song:
    '''Song class'''
    def __init__(self, name : str, genre : str, duration : int):
        '''Constructor'''
        self.name = name
        self.genre = genre
        self.duration = int(duration)

    def show_info(self) -> str:
        '''Show info'''
        message = f"{self.name} <|> {self.genre} <|> {self.duration//60}.{self.duration%60:02d}"
        return message

class Node:
    def __init__(self, val : Song):
        self.val = val
        self.next : Node = None
class Queue:

    def __init__(self):
        self.head :Node = None
        self.count = 0
        self.prev = None
    def enqueue(self, item : Song):
        self.prev = self.clone()
        if self.isEmpty():
            self.head = Node(item)
        else:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(item)
        self.count += 1

    def dequeue(self) -> Song:
        self.prev = self.clone()
        if self.isEmpty():
            print("Underflow! Dequeue from an empty queue")
            return
        val = self.head.val
        self.head = self.head.next
        self.count -= 1
        return val

    def peek(self):
        if self.isEmpty():
            print("Underflow! peek from an empty queue")
            return
        return self.head.val

    def isEmpty(self):
        return not bool(self.count)

    def show_Queue(self):
        if self.isEmpty():
            print("Queue is empty!")
            return
        pointer = self.head
        num = 1
        while pointer:
            print(f"Queue#{num} {pointer.val.show_info()}")
            pointer = pointer.next
            num += 1

    def lastSong(self, time : int):
        if self.isEmpty():
            print("Nothing here! Please add some song")
            return
        num = 1
        pointer = self.head
        while True:
            if not pointer:
                pointer = self.head
                num = 1
            time -= pointer.val.duration
            if time <= 0:
                print(f"Queue#{num} {pointer.val.show_info()}")
                return
            pointer = pointer.next
            num += 1
        
    def removeSong(self, name : str):
        self.prev = self.clone()
        if self.head and self.head.val.name == name:
            self.head = self.head.next
            self.count -= 1
            return
        pointer = self.head
        while pointer and pointer.next:
            if pointer.next.val.name == name:
                pointer.next = pointer.next.next
                self.count -= 1
                return
            pointer = pointer.next
        print(f"Can not Delete! {name} is not exist")

    def groupSong(self):

        def printall(q : Queue):
            if not q.isEmpty():
                print(f"{q.dequeue().name} ", end = "")
            while not q.isEmpty():
                print(f"| {q.dequeue().name} ", end = "")
            print()

        jpop = Queue()
        kpop = Queue()
        rb = Queue()
        pointer = self.head
        while pointer:
            genere = pointer.val.genre
            if genere == "JPOP":
                jpop.enqueue(pointer.val)
            elif genere == "KPOP":
                kpop.enqueue(pointer.val)
            else:
                rb.enqueue(pointer.val)
            pointer = pointer.next
        print("JPOP: ", end = "")
        printall(jpop)
        print("KPOP: ", end = "")
        printall(kpop)
        print("R&B: ", end = "")
        printall(rb)

    def undo(self):
        self.head = self.prev.head
        self.prev = self.prev.prev
    def rev_queue(self):
        pass

    def clone(self):
        new = Queue()
        pointer = self.head
        while pointer:
            new.enqueue(pointer.val)
            pointer = pointer.next
        new.prev = self.prev
        return new

def main():
    """this is main function"""
    q = Queue()
    while (choice := input()) != "End":
        command, data = choice.split(": ")
        match command:
            case "enqueue":
                q.enqueue(Song(*data.split("|")))
            case "dequeue":
                temp = q.dequeue()
                if temp:
                    message = f"Dequeue item: {temp.show_info()}"
                    print(message)
            case "peek":
                temp= q.peek()
                if temp:
                    temp.show_info()
            case "isEmpty":
                print(q.isEmpty())
            case "showQueue":
                q.show_Queue()
            case "lastSong":
                q.lastSong(int(data))
            case "removeSong":
                q.removeSong(data)
            case "groupSong":
                q.groupSong()
            case "undo":
                q.undo()
            case "rev":
                q.rev_queue()
    q.show_Queue()
main()
