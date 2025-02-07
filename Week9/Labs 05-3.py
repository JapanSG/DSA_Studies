'''Labs 05.03 - isIntersect(A, B, C)'''
import json

def is_intersect(a : list, b : list, c :list):
    '''Check if 3 list have atleast one common member.'''
    for mem_a in a:
        if binary_search(b,mem_a) and binary_search(c,mem_a):
            return True
    return False

def binary_search(lis : list, num : int):
    '''Return true if there's num in lis otherwise return False'''
    left = 0
    right = len(lis)-1
    while left < right-1:
        mid = (right+left)//2
        # print(left,right)
        if num == lis[mid] or num == lis[left] or num == lis[right]:
            return True
        elif num < lis[mid]:
            right = mid
        else:
            left = mid
    return False

def bin_search_re(lis : list, num : int):
    '''Return true if there's num in lis otherwise return False'''
    def re(left : int, right : int):
        '''recursion '''
        mid = (right+left)//2
        if lis[mid] == num or lis[left] == num or lis[right] == num:
            return True
        if right == left or left == right-1:
            return False
        if num < lis[mid]:
            return re(left,mid)
        else:
            return re(mid,right)
    return re(0,len(lis)-1)

def main():
    '''Main'''
    a = json.loads(input())
    b = json.loads(input())
    c = json.loads(input())
    a.sort()
    b.sort()
    c.sort()
    print(is_intersect(a,b,c))
if __name__ == "__main__":
    a = [10,30,50,70,80,90,100]
    for i in range(5,105,5):
        print(f" i = {i}", end = " ")
        print(bin_search_re(a,i))
