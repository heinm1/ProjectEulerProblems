
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return False if x < 0 else x == int(str(x)[::-1])


s = Solution()
print(s.isPalindrome(3223))