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
        print([f"{data[0]}{data[1]}" for data in lis])
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
        print([f"{data[0]}{data[1]}" for data in lis])
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
        print([f"{data[0]}{data[1]}" for data in lis])
        if not swapped:
            break
    print(f"Comparison times: {com}")

def main():
    '''main'''
    sort = bubble_sort
    lis = json.loads(input())
    last = int(input())
    new_lis = [(seat[0], int(seat[1:])) for seat in lis]
    sort(new_lis,last)
if __name__ == "__main__":
    main()
