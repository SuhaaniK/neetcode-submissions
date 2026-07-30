class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #using hash set
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False 

        # time and space complexity = O(n)

        """
        Alternative approach:
        sort first

        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True 
        return False 

        complexity: time: O(n log n), space: O(n) or O(1)
        """

        
