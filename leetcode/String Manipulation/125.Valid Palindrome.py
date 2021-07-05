class Solution:
    def isPalindrome(self, s: str) -> bool:
        pp_string = [ch.lower() for ch in s if ch.isalnum()]
        pp_string = ''.join(pp_string)
        if pp_string == pp_string[::-1]:
            return True
        return False
