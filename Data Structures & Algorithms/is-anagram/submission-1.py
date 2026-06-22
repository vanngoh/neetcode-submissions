class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # After submission I checked the answer,
        # it's better to have a length check to 
        # prevent unnecessary computation.
        if len(s) != len(t):
            return False
            
        return sorted(t) == sorted(s)
