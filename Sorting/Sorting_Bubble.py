from typing import List
# not commonly used since time complexity worst case O(n^2)
def bubbleSort(arr:List[int]):
    has_swapped = True
    num_of_iterations = 0

    while(has_swapped):
        has_swapped = False
        for i in range(len(arr) - num_of_iterations - 1):
            if arr[i] > arr[i+1]:
                # Swap
                arr[i], arr[i+1] = arr[i+1], arr[i]
                has_swapped = True
        num_of_iterations += 1


arr = [64, 34, 25, 12, 22, 11, 90] 
bubbleSort(arr)
print(arr)