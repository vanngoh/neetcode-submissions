class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # # Initial idea: CANNOT HANDLE CASE nums=[0,0,0]
        #
        # # Split the list into positive and negative
        # positives, negatives = [], []
        # ans = set()
        # for num in nums:
        #     if num >= 0:
        #         positives.append(num)
        #     else:
        #         negatives.append(num)

        # positives.sort()
        # negatives.sort()

        # for positive in positives:
        #     # Use two-pointers approach in negatives
        #     left, right = 0, len(negatives) - 1
        #     while left < right:
        #         if negatives[left] + negatives[right] == -positive:
        #             ans.add((negatives[left], negatives[right], positive))
        #             left += 1
        #             right -= 1
        #             continue
        #         if negatives[left] + negatives[right] < -positive:
        #             left += 1
        #             continue
        #         if negatives[left] + negatives[right] > -positive:
        #             right -= 1
        #             continue

        # for negative in negatives:
        #     # Use two-pointers approach in positives
        #     left, right = 0, len(positives) - 1
        #     while left < right:
        #         if positives[left] + positives[right] == -negative:
        #             ans.add((positives[left], positives[right], negative))
        #             left += 1
        #             right -= 1
        #             continue
        #         if positives[left] + positives[right] < -negative:
        #             left += 1
        #             continue
        #         if positives[left] + positives[right] > -negative:
        #             right -= 1
        #             continue

        # # Convert the set of tuples to list of lists
        # ans = [list(t) for t in ans]
        # return ans


        # Sort the input
        nums.sort()
        ans = set()
        # Let's simply it by fixing the num as target
        # then do the two-sums with 2-pointers approach
        for i, target in enumerate(nums):
            left, right = i+1, len(nums)-1
            while left < right:
                if target + nums[left] + nums[right] > 0:
                    right -= 1
                    continue
                if target + nums[left] + nums[right] < 0:
                    left += 1
                    continue
                if target + nums[left] + nums[right] == 0:
                    ans.add((target, nums[left], nums[right]))
                    left += 1
                    right -= 1
                    continue
        
        # Convert set of tuples into list of lists
        ans = [list(t) for t in ans]
        return ans


