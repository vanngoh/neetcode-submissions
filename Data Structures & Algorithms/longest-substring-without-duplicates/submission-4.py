class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        q = []
        max_len = 0

        for char in s:
            if char not in q:
                q.append(char)
            else:
                i = q.index(char)
                q = q[i+1:]
                q.append(char)
            
            if len(q) > max_len:
                max_len = len(q)

        return max_len
