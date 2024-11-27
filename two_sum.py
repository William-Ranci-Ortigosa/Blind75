class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        previous_nums = {} 

        for index, num in enumerate(nums):
            complimenting_num = target - num                # Determine the num you want to look for by substracting the current num from the target
            if complimenting_num in previous_nums:          # Look for this number inside a set containing the previous nums in the list
                return [previous_values[complimenting_value], index]
            previous_values[value] = index                  # Keep adding to dict upon each iteration if match not found 

solution = Solution()
print(solution.two_sum([2, 5, 9, 7], 9))

"""
Time: O(n)
    For loop through list is linear operation
    Searching through hashmap is constant time operation
    Adding to hashmap is constant time operation

Space: O(n)
    Hashmap can be as big as list

Why does this work? 
Subtracting the current num from the target allows us to search for a specific number
Keeping memory of past nums is what we search in to find that number
"""
