'''algorithms'''
import json
def insertion_sort(lis : list, last : int):
    '''insertion Sort'''
    com = 0
    for i, val in enumerate(lis):
        if i == last+1:
            break
        if i == 0:
            continue
        j = i - 1
        while j > -1 :
            com += 1
            if lis[j] > val:
                lis[j],lis[j+1] = lis[j+1],lis[j]
                j -= 1
            else:
                break
        # print(f"com = {com}")
        # if j+1 == i:
        #     print(f"pass {i+1:>3d} = {lis} | key = {val:>2d} | Didn't insert")
        #     continue
        # print(f"pass {i+1:>3d} = {lis} | key = {val:>2d} | insert key at index {j+1:2d}")
        print(lis)
    print(f"Comparison times: {com}")

def selection_sort(lis : list, last : int):
    '''selection sort'''
    com = 0
    for i in range(last):
        lowest = i
        for j in range(i+1,last+1):
            com += 1
            if lis[j] < lis[lowest]:
                lowest = j
        lis[i],lis[lowest] = lis[lowest],lis[i]
        print(lis)
    print(f"Comparison times: {com}")

def bubble_sort(lis : list, last: int):
    '''bubble sort'''
    com = 0
    for i in range(last+1):
        swapped = False
        for j in range(last, i, -1):
            com += 1
            if lis[j] < lis[j-1]:
                lis[j],lis[j-1] = lis[j-1],lis[j]
                swapped = True
        print(lis)
        if not swapped:
            break
    print(f"Comparison times: {com}")

def main():
    '''main'''
    sort = insertion_sort
    lis = json.loads(input())
    last = int(input())
    sort(lis,last)
if __name__ == "__main__":
    main()
