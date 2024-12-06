'''Lab 01.01 - Is_Even'''
def is_even(num : int) -> bool:
    '''Return True if num is even else return False'''
    return not bool(num & 1)

def main():
    '''Driver Code'''
    num = int(input())
    print(is_even(num))

if __name__ == "__main__":
    main()
