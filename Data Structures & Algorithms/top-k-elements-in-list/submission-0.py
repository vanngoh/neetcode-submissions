class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ref = {}
        for num in nums:
            if ref.get(num, None) is None:
                ref[num] = 1
                continue
            ref[num] += 1
        
        # Sort the dict into list of tuple
        desc_ref = sorted(ref.items(), key=lambda item: item[1], reverse=True)
        res = []
        for i in range(k):
            res.append(desc_ref[i][0])
        return res