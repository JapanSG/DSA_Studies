'''infix -> postfix'''
from stack import Stack
def infix_to_postfix(expression : str, ans : str = "") -> str:
    '''Parse infix to postfix'''
    stack = Stack()
    length = len(expression)
    i = 0
    while i < length:
        print(f"{expression[i:]:<30s} | {str(stack):<30s} | {ans}")
        char = expression[i]
        if char == ')':
            while not stack.is_empty():
                ans += stack.pop()
            return ans
        elif char == '(':
            paren = Stack()
            paren.push('(')
            i += 1
            ans = infix_to_postfix(expression[i:],ans)
            while not paren.is_empty():
                if expression[i] == ')':
                    paren.pop()
                elif expression[i] == "(":
                    paren.push('(')
                i += 1
            while not stack.is_empty():
                ans += stack.pop()
            continue
        elif char in '+-':
            if not stack.is_empty() and stack.peek() in '*/':
                while not stack.is_empty():
                    ans += stack.pop()
            stack.push(char)
        elif char in '*/':
            stack.push(char)
        else:
            ans += char
        i += 1
    while not stack.is_empty():
        ans += stack.pop()
    print(f"{expression[i:]:<30s} | {str(stack):<30s} | {ans}")
    return ans

def main():
    '''Driver Code'''
    # expression = "A*((B+C)/D)-E/F"
    expression = input("Input expression (Ex. A+B*C) -> ")
    print(infix_to_postfix(expression))
if __name__ == "__main__":
    main()
