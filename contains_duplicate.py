class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_nums = set()
        for num in nums:
            if num in unique_nums:
                return True
            unique_nums.add(num)
        
        return False

"""
Time: O(n)
    For loop through list is linear operation
    Searching through hashmap is constant time operation
    Adding to hashmap is constant time operation

Space: O(n)
    Hashmap can be as big as list

Why does this work? 
Keeping a set of previous items alows us to search that set on each iteration to see if the current num in the list is a duplicate
"""
