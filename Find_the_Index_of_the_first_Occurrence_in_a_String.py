# Solution 1: Traversal







class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Assuming the length of the string "haystack" is n  and the length of the string needle is m, the time complexity is O((n - m) * m), and the space complexity is O(1).
        n, m = len(haystack), len(needle)
        for  i in range(n - m + 1):
            # We compare the string needle with each character of the string haystack as the starting point. If we find a matching index, we return it directly.
            if haystack[i : i + m] == needle:
                return i 
        return -1
