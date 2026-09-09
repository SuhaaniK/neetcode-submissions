from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for s in strs:
            count = [0]*26

            for char in s:
                #ord() gets the ASCII integer valure of the character 
                count[ord(char)-ord('a')]+=1

            # lists are mutable and cannot be dictionary keys, so we can cast to a tuple 
            anagram_map[tuple(count)].append(s)

        return list(anagram_map.values())

