class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        count = [0] * 26 # count is a list of size 26 each with frequency of one letter 
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        # increase the count for s[i] and decrease the count for t[i] => if strings are anagrams, all counts will end up back at 0
        for num in count:
            if num != 0:
                return False 
        return True 

