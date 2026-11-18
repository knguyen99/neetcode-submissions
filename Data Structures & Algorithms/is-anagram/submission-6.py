class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_counts = [0] * 26

        for char in s:
            char_counts[ord(char) - ord("a")] += 1
    
        for char in t:
            char_counts[ord(char) - ord("a")] -= 1
        
        return all(count == 0 for count in char_counts)