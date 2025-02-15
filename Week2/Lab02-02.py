'''Lab 02.01 – Stack (Create Stack)'''
class ArrayStack:
    '''Array Stack class made from list '''
    def __init__(self):
        '''Constructor'''
        self.size  = 0
        self.data = list()

    def push(self, input_data):
        '''Push input_data to top of the ArrayStack'''
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(input_data)
            self.size += 1

    def pop(self):
        '''Return and remove data at the top of ArrayStack'''
        if not self.size:
            print("Underflow: Cannot pop data from an empty list")
            return None
        self.size -= 1
        return self.data.pop()

    def is_empty(self):
        '''Return true if self.size is 0 else return false'''
        return not bool(self.data)

    def get_stack_top(self):
        '''Return data at the top of the ArrayStack'''
        if not self.size:
            print("Underflow: Cannot get stack top from an empty list")
            return None
        top_data = self.pop()
        self.push(top_data)
        return top_data

    def get_size(self):
        '''Return the size of ArrayStack'''
        size = 0
        for _ in self.data:
            size += 1
        return size

    def print_stack(self):
        '''Print the ArrayStack'''
        print(self.data)

def main():
    '''Driver Code'''
    students = ArrayStack()
    groups = ArrayStack()
    group_num = int(input())
    student_num = int(input())
    for _ in range(group_num):
        groups.push(ArrayStack())
    for _ in range(student_num):
        students.push(input())
    while not students.is_empty():
        temp = ArrayStack()
        while not groups.is_empty() and not students.is_empty():
            group = groups.pop()
            group.push(students.pop())
            temp.push(group)
        while not temp.is_empty():
            groups.push(temp.pop())
    i = 1
    while not groups.is_empty():
        print_group(groups.pop(), i)
        i += 1
def print_group(group : ArrayStack, i : int):
    '''print Group'''
    print(f"Group {i}: ", end="")
    print(*group.data, sep = ", ")
main()
