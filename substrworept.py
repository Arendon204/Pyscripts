class Solution(object):
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        charSet = set()

        l = 0

        res = 0 

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res    
        
        """
        :type s: str
        :rtype: int
        """
        
        #In this LeetCode challenge we’re asked to find the length of the 
        # longest string of characters in a provided string that does not 
        # contain repeating characters. In other words, in the string hello 
        # the longest substring without repeating characters is hel (with a length of 3).
        
        #https://www.youtube.com/watch?v=wiGpQwVHdE0

