'''Lab 01.02 - Max…Min…Avg'''

import json

def least(lis : list) -> int:
    '''Find least in list'''
    ans = lis[0]
    for i in lis:
        if i < ans:
            ans = i
    return ans

def most(lis : list) -> int:
    '''Find most in list'''
    ans = lis[0]
    for i in lis:
        if i > ans:
            ans = i
    return ans

def avg(lis : list) -> float:
    '''Find average of list'''
    return round(sum(lis)/len(lis), 2)

def main():
    '''Driver Code'''
    lis = json.loads(input())
    print(f"{most(lis), least(lis), avg(lis)}")

if __name__ == "__main__":
    main()
