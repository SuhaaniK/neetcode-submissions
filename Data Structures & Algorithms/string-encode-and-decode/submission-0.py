from typing import List 

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res+= str(len(s)) + "#" + s
        return res 

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 # Our main pointer to read through the string
        while i < len(s):
            j = i 
            # Move j forward until we find the "#" delimiter
            while j < len(s) and s[j] != "#":
                j += 1
            # The number before the "#" is our length
            length = int(s[i:j])
            # Extract the actual word using string slicing
            # Start right after the "#" (j + 1) and read 'length' characters
            word = s[j+1:j+1+length]
            res.append(word)
            # Move our main pointer i to the start of the next encoded word
            i = j + 1+ length

        return res 
