'''Labs 05.01 - Summation (แบบที่ 1)'''
def type1(n):
    # Time Complexity(O(n))
    ans = 0
    for i in range(1,n+1):
        ans += i
    return ans

# def type2(int n):
#     # Time Complexity(O(1))
#     return (n*(n+1))/2

def main():
    print(type1(int(input())))

main()
