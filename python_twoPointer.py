from typing import List
# 283 Move Zeroes (explorer and anchor)
# 344. Reverse String
# 345. Reverse Vowels of a String
# 88. Merge Sorted Array
class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 
        start = 0
        end = 1
        while end < len(nums):
            if nums[start] == 0 and nums[end] != 0:
                nums[end], nums[start] = nums[start], nums[end]
                start += 1 
                end += 1
            elif nums[end] == 0 and nums[start]== 0:
                end += 1 
            else:
                start += 1
                end += 1
        return nums
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        a = len(s) - 1 #dec from max
        b = 0 # inc
        while b < a:
            s[a], s[b] = s[b], s[a]
            print(b, a, s)
            a -= 1
            b += 1
        return s
    def reverseVowels(self, s: str) -> str:
        a = len(s) - 1
        b =  0
        arr = list(s)
        vowels =['a','e','i','o','u','A','E','I','O','U']
        while b < a:
            # case when both a and b are vowels
            if arr[a] in vowels and arr[b] in vowels:
                arr[a], arr[b] = arr[b], arr[a]
                a -= 1
                b += 1
            # only if b is a vowel but a is not
            elif arr[b] in vowels:
                a -= 1
            # only if a is a vowel but a is not
            elif arr[a] in vowels:
                b += 1
            else:
                a -= 1
                b += 1
        return ''.join(arr)
    def merge(self, nums1:List[int], m:int, nums2:List[int], n:int) -> None:
        nums1[m:] = nums2
        nums1.sort()
        return nums1



nums = [0,-1,0,1,3,0,4,0,8,0]

s  = ["H","a","n","n","a","h"]

stringR = "leetcode"

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

solution = Solution()
#print(solution.moveZeroes(nums))
#print(solution.reverseString(s))
#print(solution.reverseVowels(stringR))
print(solution.merge(nums1, m, nums2, n))
