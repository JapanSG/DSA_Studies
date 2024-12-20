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
        return self.size

    def print_stack(self):
        '''Print the ArrayStack'''
        print(self.data)
def is_parentheses_matching(expression : str) -> bool:
    '''check if input have matching parentheses'''
    matching = True
    paren = ArrayStack()
    for char in expression:
        if char == "(":
            paren.push(char)
        if char == ")":
            val = paren.pop()
            if val is None:
                matching = False
    if paren.is_empty() and matching:
        print("Parentheses in", expression, "are matched")
        return True
    print("Parentheses in", expression, "are unmatched")
    return False
def main():
    ''''Driver Code'''
    print(is_parentheses_matching(input()))

main()
