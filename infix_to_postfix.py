'''infix -> postfix'''
from stack import Stack

def empty_stack(stack : Stack, string : str) -> str:
    '''Empty the stack and concatat it with a string'''

    while not stack.is_empty():
        string += stack.pop()
    return string

def infix_to_postfix(expression : str) -> str:
    '''Parse infix to postfix'''
    print('-'*100)
    print(f"{'infix':^40s} | {'stack':^30s} | postfix")
    print('-'*100)
    return recursion(expression)

def stack_to_string(stack :Stack) -> None:
    '''print_stack logic'''
    if stack.is_empty():
        return str(stack)
    return f"{str(stack)[:-8]}"

def recursion(expression : str, ans : str = "", count = 1) -> str:
    '''Parse infix to postfix'''
    stack = Stack()
    length = len(expression)
    i = 0
    while i < length:
        print(f"{count:>3d}. {expression[i:]:<35s} | {stack_to_string(stack):<30s} | {ans}")
        count += 1
        char = expression[i]
        if char == ')':
            ans = empty_stack(stack, ans)
            return ans
        elif char == '(':
            paren = Stack()
            paren.push('(')
            i += 1
            ans = recursion(expression[i:], ans, count)
            while not paren.is_empty():
                if expression[i] == ')':
                    paren.pop()
                elif expression[i] == "(":
                    paren.push('(')
                i += 1
                count += 1
            ans = empty_stack(stack, ans)
            continue
        elif char in '+-':
            if not stack.is_empty():
                ans = empty_stack(stack, ans)
            stack.push(char)
        elif char in '*/':
            if not stack.is_empty() and stack.peek() in '/*':
                ans = empty_stack(stack, ans)
            stack.push(char)
        else:
            ans += char
        i += 1
    ans = empty_stack(stack,ans)
    print(f"{count:>3d}. {expression[i:]:<35s} | {stack_to_string(stack):<30s} | {ans}")
    count += 1
    print('-'*100)
    return ans

def main():
    '''Driver Code'''
    # expression = "A*((B+C)/D)-E/F"
    expression = input("Input expression Ex. A+B*C -> ")
    print(f"Final answer = {infix_to_postfix(expression)}")
if __name__ == "__main__":
    main()
