import math
from typing import List
# BIG O 
# worst O(log(n))   best O(1)
#sorted array 
def binarySearch(arr: List[int], elem:int) -> None:
    start =0
    end = len(arr) - 1
    mid = math.floor((start + end) / 2) # will round down
    while arr[mid] != elem and start <= end:
        #print(arr[start], arr[mid], arr[end])
        if elem < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
        mid = math.floor((start + end) / 2)
    #print(arr[start], arr[mid], arr[end])
    if arr[mid] == elem:
        return mid
    return -1

listA = [2,3,4,5,6,9,10,11,13,15,16,18,20,21,24,28]
#print(binarySearch(listA,15))
#print(binarySearch(listA,-11))


