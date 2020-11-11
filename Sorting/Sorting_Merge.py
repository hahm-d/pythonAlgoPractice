# classic example of a divide-and-conquer category of algorithms.
# O(n log n)
#An initial array is divided into two roughly equal parts. If the array has an odd number of elements, one of those "halves" is by one element larger than the other.
#The subarrays are divided over and over again into halves until you end up with arrays that have only one element each.
#Then you combine the pairs of one-element arrays into two-element arrays, sorting them in the process. Then these sorted pairs are merged into four-element arrays, and so on until you end up with the initial array sorted

def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2 # floor division - round down
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        # recursion
        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)
