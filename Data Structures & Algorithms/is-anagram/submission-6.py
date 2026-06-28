class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        for char in s:
            if char not in counts:
                counts[char] = 0
            counts[char] += 1
        for char in t:
            if char not in counts:
                return False
            counts[char] -= 1 

        for x in counts.values():
            if x != 0:
                return False
        return True