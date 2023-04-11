class Solution:
    def isPalindrome(self, x: int) -> bool:
        # cast to string and check if it's a palindrome?
        word = str(x)
        return (word == word[::-1])
