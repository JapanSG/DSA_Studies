'''Lab 06.03 - Binary Search'''
import json
class Student:
    ''''''
def binary_search(data : list, name):
    '''Return true if there's name in lis otherwise return False'''
    lis = [std["name"] for std in data]
    # print(lis)
    left = 0
    right = len(lis)-1
    com = 0
    while left <= right:
        mid = (right+left)//2
        com += 1
        if name == lis[mid]:
            print(f"Found {name} at index {mid}")
            print_std(data[mid])
            print(f"Comparisons times: {com}")
            return mid
        elif name < lis[mid]:
            right = mid-1
        else:
            left = mid+1
    print(f"{name} does not exists.")
    print(f"Comparisons times: {com}")
    return -1

def print_std(std :dict):
    idd = std["id"]
    name = std["name"]
    gpa = float(std["gpa"])
    print(f"ID: {idd}")
    print(f"Name: {name}")
    print(f"GPA: {gpa:.2f}")

def main():
    data = json.loads(input())
    name = input()
    binary_search(data,name)
main()
