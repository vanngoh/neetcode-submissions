class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # for current in range(len(nums)):
        #     for i in range(current+1, len(nums)):
        #         if nums[current] == nums[i]:
        #             return True
                
        # return False

        dup_map = {}
        for current in range(len(nums)):
            if dup_map.get(nums[current], None) is None:
                dup_map[nums[current]] = 1
                continue
            else:
                return True
        return False