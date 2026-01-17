class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        substring = set()
        max_len = 0
        for right in range(len(s)):
            while s[right] in substring:
                substring.remove(s[left])
                left +=1
            substring.add(s[right])
            max_len = max(max_len,len(substring))
        return max_len