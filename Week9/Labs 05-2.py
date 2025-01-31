'''Labs 05.01 - Summation (แบบที่ 1)'''
import time
def type1(n):
    '''
    Time Complexity(O(n))

    TestResult :
    n < 10000 : 0.000 s
    100000      : 0.002 s
    1000000     : 0.023 s
    10000000    : 0.229 s
    100000000   : 2.356 s
    1000000000  : 23.20 s
    '''
    ans = 0
    for i in range(1,n+1):
        ans += i
    return ans

def type2(n):
    # Time Complexity(O(1))
    return (n*(n+1))/2

def main():
    analyze_func(type1,int(input()))

def analyze_func(func, n : int):
    start = time.time()
    ans = func(n)
    end = time.time()
    print(f"ans : {ans}")
    print(f"Time Taken : {end-start}")
main()
