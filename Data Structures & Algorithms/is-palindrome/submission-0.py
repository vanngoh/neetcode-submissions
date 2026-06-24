class Solution:
    def isPalindrome(self, s: str) -> bool:
        regex = r'[a-zA-Z0-9]'
        chars = []
        for char in s:
            if not re.match(regex, char):
                continue
            chars.append(char.lower())
        
        chars_str = "".join(chars)
        chars.reverse()     # reverse() returns None
        return chars_str == "".join(chars)