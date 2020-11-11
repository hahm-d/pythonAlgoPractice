# Quicksort is a representative of three types of sorting algorithms: divide and conquer, in-place, and unstable.
# O(n*logn) 
# divide and conquer: splits thearrayinto smallerarrays until empty array/ only has one element. 
# in-place: stack memory for all the recursive calls
# stable: A stable algorithm is one in which elements with the same value appear in the same relative order.
# un-stable: Doesnt guarantee relative order in sorted array.

# This is something that becomes important when you sort objects instead of primitive types. 
# For example, imagine you have several Person objects that have the same age, 
# i.e. Dave aged 21 and Mike aged 21. 
# If you were to use Quicksort on a collection that contains both Dave and Mike, sorted by age.
# There is no guarantee that Dave will come before Mike every time you run the algorithm, and vice versa.

# process:
# Divide the collection in two (roughly) equal parts by taking a pseudo-random element and using it as a pivot.
# Elements smaller than the pivot get moved to the left of the pivot, and elements larger than the pivot to the right of it.
# This process is repeated for the collection to the left of the pivot, as well as for the array of elements to the right of the pivot until the whole array is sorted.

def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and array[high] >= pivot:
            high = high - 1

        # Opposite process of the one above
        while low <= high and array[low] <= pivot:
            low = low + 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            array[low], array[high] = array[high], array[low]
            # The loop continues
        else:
            # We exit out of the loop
            break

    array[start], array[high] = array[high], array[start]

    return high

def quick_sort(array, start, end):
    if start >= end:
        return
    
    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)

array = [29,99,27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21,44]

quick_sort(array, 0, len(array) - 1)
print(array)