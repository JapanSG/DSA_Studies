'''infix -> postfix'''
# 
from stack import Stack

def empty_stack(stack : Stack, string : str) -> str:
    '''Empty the stack and concatenate it with a string'''
    while not stack.is_empty():
        string += stack.pop()
    return string

def stack_to_string(stack :Stack) -> None:
    '''print_stack logic'''
    if stack.is_empty():
        return str(stack)
    return f"{str(stack)[:-8]}"

def infix_to_postfix(expression : str) -> str:
    '''v2'''
    length = len(expression)
    print('-'*100)
    print(f"{'infix':^{length+5}s} | {'stack':^30s} | postfix")
    print('-'*100)
    ans = ''
    count = 1
    stack = Stack()
    i = 0
    while i < length:
        print(f"{count:>3d}. {expression[i:]:<{length}s} | {stack_to_string(stack):<30s} | {ans}")
        count += 1
        char = expression[i]
        if char == ')':
            while stack.peek() != '(':
                ans += stack.pop()
            stack.pop()
        elif char == '(':
            stack.push('(')
        elif char in '+-':
            if not stack.is_empty() and stack.peek() in '+-*/':
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
    print(f"{count:>3d}. {expression[i:]:<{length}s} | {stack_to_string(stack):<30s} | {ans}")
    count += 1
    print('-'*100)
    return ans

def main():
    '''Driver Code'''
    # expression = "A*((B+C)/D)-E/F"
    # expression = "A*(B+C)-D*F-E"
    expression = input("Input expression Ex. A+B*C -> ")
    print(f"Final answer = {infix_to_postfix(expression)}\n")
if __name__ == "__main__":
    main()
