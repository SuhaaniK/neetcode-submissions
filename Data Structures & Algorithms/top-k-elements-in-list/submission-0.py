from typing import List 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # count occurrences in a dictionary 
        for i in nums:
            count[i] = count.get(i,0) + 1
        
        # sort the unique nos based on freq 
        # reverse = True makes it sort descending (highest freq first)
        sorted_nums = sorted(count.keys(), key=lambda x: count[x], reverse=True)

        # return the first k elements using python list slicing 
        return sorted_nums[:k]

