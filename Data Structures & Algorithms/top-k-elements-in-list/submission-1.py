class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ints = {}
        for n in nums:
            if n in ints.keys():
                ints[n] += 1
            else:
                ints[n] = 1
        sorted_ints = sorted(ints.items(), key=lambda x: x[1], reverse=True)
    
        return [num for num, count in sorted_ints[:k]]