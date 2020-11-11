from typing import List
from collections import Counter
# Number of minimum subarrays that equal sum amount num
def minSubArrayLength(arr: List[int],num:int) -> int:
    #anchor and explorer 
    anc,exp,count = 0,1,0 
    total = arr[anc] + arr[exp]
    while exp < len(arr):
        if total == num:
            total -= arr[anc]    
            count += 1
            anc +=1
            print(anc, exp, total)
        elif total > num:
            total -= arr[anc]
            anc +=1
        else:
            total += arr[exp]
            exp += 1
            print(anc, exp, total)
    return count
arr1 = [2,3,1,2,4,3]
num1 = 7
#print(minSubArrayLength(arr1, num1))


# 53 Maximum subarray
def maxSubArraySlide(nums) -> None:
    maxSum, curSum = nums[0], 0
    print(nums)
    for n in nums:
        if curSum < 0: #only adding postive values since we want to return the maximum value. thus setting curr to zero.
            curSum = 0
        curSum += n 
        print(n)
        print("current Sum: {}".format(curSum))
        print("max Sum: {}".format(maxSum))
        maxSum = max(maxSum, curSum) # new maxSub, take the highest value
    return maxSum  

num1= [-2,1,-3,4,-1,2,1,-5,4]
#print(maxSubArraySlide(num1))



# 1004 Max Consecutive Ones III 
def longestOnes(A:List[int], K:int) -> int:
    start = end = max_length = 0

    while end < len(A):
        if A[end] == 1: #expand right of window by one since end value is a 1
            end += 1
        elif A[end] == 0 and K > 0: # expand right even if 0 only if K is greater than 0
            K -= 1
            end += 1
        else: # ran out of K's and A[end] is 0... 
            max_length = max(end-start, max_length) #calc max
            if A[start] == 0: # if left boundry has a zero, inc K to be used later
                K += 1
            start += 1 # move left boundary
        print(A)
        print("window: start={}, end={}, K={}, MAX={}".format(start,end,K, max_length))

    return max(max_length, end-start)

A = [1,1,1,0,0,0,1,1,1,1,0]
K = 2

#print(longestOnes(A,K))


# 76 Minimum Window Substring
def minWindow(s:str, t:str) -> str:
    # create dictionary (from collections import Counter)
    need = Counter(t)
    print(need)
    #initialize sliding window characters
    l,r,i,j,missing = 0,0,0,0, len(t) 
    # start sliding window
    while r < len(s):
        if need[s[r]] >0: #if letter exists (positive)
            missing -=1 
        need[s[r]]-=1 #dictionary value becomes neg
        r+=1
        print("start={}, end={}, missing={}".format(l,r,missing))    
        while missing == 0: # no more missing values
            if j==0 or r-l < j-i: # compare for shortest length, update i and j only if r and l is smaller (since we want the shortest length)
                i,j=l,r
                print(i,j)
            need[s[l]]+=1 # regardless of t value, add letter to dictionary ++value
            print("added to needs:{}".format(s[l])) 
            if need[s[l]]>0: #check if start value exists in map. Only if exists add back 1 to missing
                print("start contains need value, missing++")
                missing +=1
            l += 1
            print(need)
            print("shift start")
            print("i ={}, j={}".format(i,j))
    return s[i:j]

s = "ADOBECODEBANC"
t = "ABC"
#print(minWindow(s,t))