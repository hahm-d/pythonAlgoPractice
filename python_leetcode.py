from typing import List 
class Solution:
    def intersect(self, nums1:List[int], nums2:List[int]) -> List[int]:
        i = 0
        j = 0
        res = []
        nums1.sort()
        nums2.sort()
        while( i < len(nums1) and j < len(nums2) ):
            if nums1[i] < nums2[j]:
                i += 1
                continue
            if nums1[i] > nums2[j]:
                j += 1
                continue
            res.append(nums1[i])
            i += 1
            j += 1
        return res

test = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]

#print(test.intersect(nums1, nums2))


# 15 3Sum
# given array nums = [-1, 0, 1, 2 -1, 4]
# return sets that equal 0
# solution: [ [-1, 0, 1], [-1, -1, 2]]
 
def threeSum(nums:List[int]) -> None:
   # Sorting the array to make the pointer movement choice obvious
    nums.sort()
    # Final result goes here
    res = []
    
    # Go through each element as a candidate
    for i in range(len(nums)):
        
        # Skip away the repeats, prevent duplicates (based on sorted list)
        if i != 0 and nums[i] == nums[i-1]: 
            continue
        # Reducing question to 2Sum - set target value to negative
        target = -nums[i]
        # Basic 2 pointer approach to find all the elemnts possible
        l, r = i+1, len(nums)-1
        while l < r:
            print("nums[l]: {}".format(nums[l]), "nums[r]: {}".format(nums[r]))
            if nums[l] + nums[r] == target:
                
                # You found 1, add it
                res.append([nums[i], nums[l], nums[r]])
                print("added!")
                # additional dups logic for both r and l (skip over value)
                while l < r and nums[l] == nums[l+1]: 
                    print("duplicate skip i++")
                    l += 1
                while l < r and nums[r] == nums[r-1]: 
                    print("duplicate skip r--")
                    r -= 1
                    
                # Mandatory obvious movement
                l += 1
                r -= 1
            
            # Selective movements
            
            #below target value
            elif nums[l] + nums[r] < target: 
                print("behind target, move pointer l") 
                l += 1
                
            #above target value
            else:
                print("over target, move pointer r")
                r -= 1
    return res


nums3 = [-2,0,1,1,2]
#print(threeSum(nums3))


# 3Sum using hashmap

def threeSumHash(nums:List[int]) -> List[List[int]]:
    nums.sort()
    lookup = {} #set
    res = set() #create a set for results

    # NOTE: last index for each elements in nums  
    # IMPORTANT! use enumerate for both counter and value!
    # add values to lookup
    print(nums)

    for i,each in enumerate(nums):
        lookup[each] = i
        print(lookup)
 
    for i,a in enumerate(nums):
        # duplicate value, skip
        if i != 0 and nums[i]==nums[i-1]:
            continue
        
        for j,b in enumerate(nums[i+1:]):
            target = -a-b #basically if -(valueA + valueB) result should be value we need to make 0
            print("target: {}".format(target)) #target is then looking for the value 2 
            print(i,j,1)
            # if target exists in lookup (additionally - duplicate logic: j+i+1?)
            if target in lookup and lookup[target] > j+i+1:
                print("lookup: {}".format(lookup[target]))
                print("added: {}".format([a,b,target]))
                res.add((a,b,target))

    return list(res)

#print(threeSumHash(nums3))



# 53 Maximum subarray
num4= [-2,1,-3,4,-1,2,1,-5,4]
# dynamic programming solution 
def maxSubArray(nums: List[int]) -> int:
    # DP (keep track of max sum)
    dp = [0]*len(nums) # created empty array with place holders which will help avoid some if/else conditions
    for i,num in enumerate(nums):
        dp[i] = max(dp[i-1] + num, num) # at i=0 this will check dp[-1] which is 0 since we prepopulated dp list 
        #print("max = {}".format(dp[i])) # check highest value between previous dp value + current vs. current value
    return max(dp)

#print(maxSubArray(num4))



