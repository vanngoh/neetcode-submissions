class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            if i == 0:
                hashmap[target-num] = i
                continue

            if hashmap.get(num, None) is not None:
                return [hashmap.get(num), i]
            
            hashmap[target-num] = i


        # My initial approach would be
        # substract the target in nums
        # to get a new goals: List[int].
        # Find is there any goal inside
        # the nums then we could get the
        # i & j. But it will fail the case
        # nums=[5,5], target=10

        # goals = [target - goal for goal in nums]
        # goals_set = set(goals)
        # return [idx for idx, val in enumerate(nums) if val in goals_set and val != goals[idx]]
