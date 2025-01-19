'''Exercise 02.03 - SPÄM'''
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

def correct_paren(string : str) -> bool:
    '''Check if string as correct paren'''
    paren = ArrayStack()
    brack = ArrayStack()
    wing = ArrayStack()
    is_correct = True
    for char in string:
        if char == '(':
            paren.push('(')
        elif char == '[':
            brack.push('[')
        elif char == '{':
            wing.push('{')
        elif char == ')':
            if not paren.pop():
                is_correct = False
        elif char == ']':
            if not brack.pop():
                is_correct = False
        elif char == '}':
            if not wing.pop():
                is_correct = False
    return paren.is_empty() and brack.is_empty() and wing.is_empty() and is_correct

def main():
    '''Driver Code'''
    string = input()
    print(correct_paren(string))

main()
