'''Labs 05.04 - Calculator'''
import math
def cal(n : int):
    total = 1
    if n == 1:
        return 1
    for i in range(2,n+1):
        total += len(str(i)) + 1
    return total+1
def main():
    '''main'''
    print(cal(int(input())))
main()
