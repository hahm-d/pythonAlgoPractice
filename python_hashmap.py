from typing import List
from collections import Counter
# 287. Find the duplicate number
def findDuplicate(nums:List[int]) -> int:
    find = Counter(nums)
    print(find)
    for key,value in find.items():
        if value > 1:
            return key

#print(findDuplicate([1,3,4,5,6,7,8,1]))

# 242. Valid Anagram
def isAnagram(s:str, t:str) -> bool:
    find = Counter(s)
    for n in t:
        if n in find.keys():
            find[n] -= 1
        else:
            return False
    for val in find.values():
        if val!=0:
            return False
    return True

s1 = "anagram"
t1 = "nagaram"
print(isAnagram(s1,t1))


# design a hashmap
# 771. Jewels and Stones
class MyHashMap:
    def __init__(self):
        self.cap = 100
        self.internal_map = [[] for i in range(self.cap)]
    def hash_function(self, key):
        return key % self.cap
    def put(self, key:int, value:int) -> None:
        hash_key = self.hash_function(key)
        bucket = self.internal_map[hash_key]
        found = False
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket[i][0] = value
                found = True
                break
        if not found:
            bucket.append([key, value])
    def get(self, key:int) -> None:
        hash_key = self.hash_function(key)
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                return bucket[i][1]
        return -1
    def remove(self, key: int) -> None:
        hash_key = self.hash_function(key)
        bucket = self.internal_map[hash_key]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                temp = bucket[i]
                bucket[i] = bucket[0]
                bucket[0] = temp
                bucket.pop(0)
                break

# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


class Solution:
    def numJewelsInStone(self, J: str, S:str) -> int:
        my_dict = dict()
        num = 0
        for i in range(len(J)):
            # populate the dictionary with each J 
            my_dict[J[i]] = J[i] 
        for letter in S:
            try:
                print(my_dict)
                my_dict[letter]
            except KeyError:
                print("Error")
                continue
            else:
                print("count up!")
                num += 1
        return num

solution = Solution()
#print(solution.numJewelsInStone("aA","aAAbbb"))