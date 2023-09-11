#binary search which searches an item in sorted list . function should return index of element to be searched in list.

def binary_search(lst, item):
    low = 0
    high = len(lst)-1
    while low<=high:
        mid = round((high+low)/2)
        if lst[mid] == item:
            return mid
        elif lst[mid]>item:
            high = mid -1
        else:
            low = mid + 1
    return  None

lst =[1,3,5,7,9]
print(binary_search(lst,1))
