'''heaps'''
class MaxHeap:
    '''MaxHeap Class'''
    def __init__(self):
        '''Constructor'''
        self.arr = []
        self.count = 0

    def insert(self, data):
        '''Insert data to heap'''
        self.arr.append(data)
        self.count += 1
        self.reheap_up()

    @staticmethod
    def get_parent(index):
        '''Get parent index'''
        if not index % 2:
            return (index-2)//2
        return (index-1)//2

    @staticmethod
    def get_left_child(index):
        '''Get left child index'''
        return 2*index+1

    @staticmethod
    def get_right_child(index):
        '''Get right child index'''
        return 2*index+2

    def swap(self, i, j):
        '''Swap data between index'''
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def reheap_up(self):
        '''reheap from bottom to top'''
        child = self.count -1
        parent = MaxHeap.get_parent(child)
        while child:
            if self.arr[child] > self.arr[parent]:
                self.swap(child, parent)
                child = parent
                parent = MaxHeap.get_parent(child)
            else:
                break

    def delete(self):
        '''Delete in heap'''
        if not self.count:
            print("Empty heap")
            return
        arr = self.arr
        data = self.arr.pop()
        arr[0] = data
        self.count -= 1
        i = 0
        while MaxHeap.get_right_child(i) < self.count:
            left_child = MaxHeap.get_left_child(i)
            right_child = MaxHeap.get_right_child(i)
            if arr[left_child] > arr[i] and arr[right_child] > arr[i]:
                if arr[left_child] > arr[right_child]:
                    self.swap(left_child, i)
                    i = left_child
                else:
                    self.swap(right_child, i)
                    i = right_child
            elif arr[left_child] > arr[i]:
                self.swap(left_child, i)
                i = left_child
            elif arr[right_child] > arr[i]:
                self.swap(right_child, i)
                i = right_child
            else:
                break

    def __str__(self):
        '''__str__'''
        return f"{self.arr}"

    def __len__(self):
        return self.count
